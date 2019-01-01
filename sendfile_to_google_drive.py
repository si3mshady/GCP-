from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as f
from oauth2client import client,tools
from googleapiclient.http import MediaFileUpload as MFU
import os

scope = "https://www.googleapis.com/auth/drive"
secret = "/Users/user/client_secret.json"

def main():    
    cached_credentials = f.Storage('token.json')
    try:
        credentials = cached_credentials.get()
        print("Credentials Accepted.\n")
    except KeyError:
        print("Initializing Oauth2 flow:\n")
    even_flow = client.flow_from_clientsecrets(secret,scope)
    if even_flow:
        print("Pass: Flow from client secrets.\n")
    cred = tools.run_flow(even_flow,cached_credentials)
    if cred:
        print("Redirecting to browswer.\n")  
    global service
    service = build('drive','v3',http=cred.authorize(Http()))

    for FILE in os.listdir('/Users/user/Documents/blockchain'):
        if FILE.endswith('.py'):
            file_metadata = {FILE:FILE}
            media = MFU(FILE,mimetype='text/x-script.phyton')
            file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
            print('File ID: {}'.format(file.get('id')))       


if __name__ == '__main__':
    main()
    

