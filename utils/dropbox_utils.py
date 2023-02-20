import dropbox
import json
import tempfile
import os 


class DropboxToolkit:
    def __init__(self, credentials): 
        try:
            self.dbx = dropbox.Dropbox(
                app_key = credentials["app_key"],
                app_secret = credentials["app_secret"],
                oauth2_refresh_token = credentials["oauth2_refresh_token"])
            print("Sucessfully connected with dropbox")            
        except Exception as e:
            print('Error connecting to Dropbox with access token: ' + str(e))

    def download_file(self, dropbox_file_path, local_file_path):
        """Download a file from Dropbox to the local machine."""
        try:
            with open(local_file_path, 'wb') as f:
                metadata, result = dbx.files_download(path=dropbox_file_path)
                f.write(result.content)
        except Exception as e:
            print('Error downloading file from Dropbox: ' + str(e))

    def list_files(self, path):
        try:
            files = self.dbx.files_list_folder(path).entries
            files_list = []
            for file in files:
                if isinstance(file, dropbox.files.FileMetadata):
                    files_list.append(file.name)
            return files_list
        except Exception as e:
            print('Error getting list of files from Dropbox: ' + str(e))

    def list_folders(self, path):
        try:
            folders = self.dbx.files_list_folder(path).entries
            folders_list = []
            for folder in folders:
                folders_list.append(folder.name)
            return folders_list
        except Exception as e:
            print('Error getting list of folders from Dropbox: ' + str(e))
            
    def delete_file(self ,path):
        self.dbx.files_delete(path)
    
    def create_folder(self ,path):
        self.dbx.files_create_folder_v2(path)

    def download_to_tempfile(self, dropbox_file_path):
        """Download a file from Dropbox to the local machine."""
        try:
            fd, path = tempfile.mkstemp()
            with open(path, 'wb') as f:
                metadata, result = self.dbx.files_download(path=dropbox_file_path)
                f.write(result.content)
                return path
        except Exception as e:
            print('Error downloading file from Dropbox: ' + str(e))

    def upload_file(self, content, upload_path):
        self.dbx.files_upload(content, upload_path)
