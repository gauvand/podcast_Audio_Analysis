#%% 
import pandas
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import urllib
import os

#%%
#G Drive authentication
#With credential file
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
drive=GoogleDrive(gauth)
#Without credential file
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# gauth.SaveCredentialsFile("mycredts.txt") # saves a credential file
# drive = GoogleDrive(gauth)

#%%
# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
#%%
folder = drive.ListFile({'q': 'title="podcast_audio" and trashed=false'}).GetList()[0] # get the folder we just created
#%%
# process mp3 file
example_link = "https://95bfm.com/sites/default/files/291117_Dear_Science.mp3"
dl = urllib.request.urlopen(example_link)
dl2= dl.read()
with open("testing.mp3","wb") as f:
    f.write(dl2)
mimetype = 'audio/mpeg'
title = "example_podcast1"
file1 = drive.CreateFile({'title':title,"mimetype":mimetype,"parents":[{'id':folder['id']}]})
file1.SetContentFile("testing.mp3")
file1.Upload()
os.remove("testing.mp3")
# %%
