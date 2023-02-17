
from utils.dropbox_toolkit import DropboxToolkit

f = open ('dropbox_credentials.json', "r")  
credentials = json.loads(f.read())
dbx = DropboxToolkit(credentials)
# do whatever you want to do
