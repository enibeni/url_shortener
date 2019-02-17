import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def get_shortened_link(long_link, token):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    payload = {
        "long_url": long_link,
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        return response.json()["link"]


def get_link_summary(link, token):
    parsed_link = urlparse(link)
    link = parsed_link.netloc + parsed_link.path
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "unit": "month",
    }
    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        return response.json()["total_clicks"]


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    if token is None:
        exit("Please provide access token to bit.ly api in .env file")
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='link to short or see statistics')
    args = parser.parse_args()
    user_input_link = args.link
    summary = get_link_summary(user_input_link, token)
    if summary is not None:
        print(f"total bit.ly clicks: {summary}")
    else:
        bitlink = get_shortened_link(user_input_link, token)
        if bitlink is not None:
            print(bitlink)
        else:
            print("Something went wrong, make sure your link is correct")
