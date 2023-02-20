from dropbox_toolkit.dbx_toolkit import DropboxToolkit
import json


f = open ('dropbox_credentials/credentials.json', "r")  
credentials = json.loads(f.read())
dbx = DropboxToolkit(credentials)
