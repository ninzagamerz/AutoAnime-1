import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', '28776072')) #API ID
API_HASH = environ.get('API_HASH', 'b3a786dce1f4e7d56674b7cadfde3c9d') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '7377357282:AAER1lGRQKTgCpg1PG3r4V91_dK6xJ_N9OY') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://ftm:ftm@cluster0.rhh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', '7042535787')) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', '-1002209201816'))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', '-1002209201816'))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', '-1002209201816')) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
