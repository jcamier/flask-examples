# Get Python libraries/packages
from flask import Flask
import webbrowser as wb
from selenium import webdriver
import sys

# Variables
app_port = 5000
dev_url = 'http:127.0.0.1:' + str(app_port) + '/'
python_url = "http://www.python.org"
webapp_url = "http://yourapp.mobi"

# Functions
def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


def get_chrome_path():
    platform = get_platform()
    chrome_path = ''
    if platform == 'OS X':
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    elif platform =='Windows':
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    elif platform == 'Linux':
        chrome_path = '/usr/bin/google-chrome %s'
    else:
        print('Chrome path is indeterminable, script might need to be updated')
    return chrome_path


# Flask app


app = Flask(__name__)

@app.route('/')  # Home page
def home():
    return "Hello, world!"

# wb.get(get_chrome_path()).open_new(webapp_url)
wb.get(get_chrome_path()).open_new(dev_url)
app.run(port=app_port)


