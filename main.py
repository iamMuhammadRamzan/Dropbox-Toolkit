from utils.dropbox_utils import DropboxToolkit
import json


f = open ('dropbox_credentials.json', "r")  
credentials = json.loads(f.read())
dbx = DropboxToolkit(credentials)
