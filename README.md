# Bitly url shorterer
Shorten your link via bit.ly service with this simple command line utility. 


# How to Install
 
- Generate oauth token for bit.ly api in your bit.ly profile [here](https://app.bitly.com/Bj1l6E8H5vk/bitlinks/2SIukn9?actions=accountMain&actions=profile)
- Create .env file and place it in a folder with a script
- Specify your oauth token in .env file in format `TOKEN=oauth token`
- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

# Quickstart
Run it as a python script in your terminal with link to shorten as a required parameter
```bash
$ python3 short_me.py https://www.youtube.com/watch?v=sFrNsSnk8GM
http://bit.ly/2DOlc5Y
```
To see bit.ly link clicks statistics just provide it to the script the same way
```bash
$ python3 short_me.py http://bit.ly/2DOlc5Y
total bit.ly clicks: 1
```
All available parameters are:
```bash
usage: short_me.py [-h] link

optional arguments:
  -h, --help            show this help message and exit
```

# Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.