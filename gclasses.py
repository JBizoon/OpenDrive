from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import smtplib, ssl
import os
import datetime
import argparse
import json
import re
import sys

class Gopen():
    # def __init__(self, drive,file,folderid,title):
    #     self.drive = drive
    #     self.file = file
    #     self.folderid = folderid
    #     self.title = title


    def auth(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        return drive

    def uploadfile(self,drive,file,folderid):
        file2 = drive.CreateFile({'parents': [{'id': folderid}]})
        file2.SetContentFile(file)
        file2.Upload()
        return True

    def mkdr(self,title,drive):
        folder_metadata = {'title' : title, 'mimeType' : 'application/vnd.google-apps.folder'}
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        folderid = folder['id']
        return folderid


class Actions():
    def __init__(self, arg):
        superActions, (self).__init__()
        self.arg = arg



class Sanitize():
                            # def __init__(self, arg):
                            #     super(sanitize, self).__init__()
                            #     self.arg = arg

    def check_mail(self,email):
        regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if(re.search(regex,email)):
            p1= email.split("@")
            if ((len(p1[0])) < 64) & ((len(p1[1])) < 255):
                return email
            else:
                print ("Invalid email")
                sys. exit()
    def check_path(self,path):
        if os.path.isdir(path):
            return path
        else:
            print ("Directory does not exist")
            sys. exit()
