# Dropbox

## Installation
```
pip install dropbox
```
## Integration
```
from utils.dropbox_toolkit import DropboxToolkit

f = open ('dropbox_credentials.json', "r")  
credentials = json.loads(f.read())
dbx = DropboxToolkit(credentials)
```
* Note: Place your dropbox credentials in `dropbox_credentials.json` file.

## Credentials for dropbox 

#### Get Access Token
* Go to the [Dropbox App Console](https://www.dropbox.com/developers/apps) and log in (you need a Dropbox account to do this).
* Select Create App.
*  After the app is created, you will be taken to the App's settings page.
*  Goto Permissions , enable files.content.write, files.content.read
*  Scroll to the OAuth 2 section, find the Generated access token section and click on Generate.

* Note: Acess tocken from the above method is temporary(expired within 4 hours).

#### Make your Access Tocken permanent
* Just follow these [steps](https://stackoverflow.com/questions/70641660/how-do-you-get-and-use-a-refresh-token-for-the-dropbox-api-python-3-x) and get `refresh tocken`
