from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def fetchMail():
	
	mailID = []
	mailArray = {}
	scope = '''https://mail.google.com/'''
	cred_path = '''credentials.json'''
	stored_cred = file.Storage(cred_path)	
	creds = stored_cred.get()

	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets(cred_path,scope)
		creds = tools.run_flow(flow, stored_cred)
		
	svc  = build('gmail', 'v1', http=creds.authorize(Http()))
	results  = svc.users().messages().list(userId='me').execute()
	messages = results.get('messages', [])

	for msg in messages:
		mailID.append(msg['id'])

	for mgs in range(len(mailID)):
		sample = svc.users().messages().get(userId='me',id=mailID[mgs]).execute()
		mailArray[mailID[mgs]] =  sample['snippet']
	with open('gmailMessages.txt', 'wt') as mail:
		if mail.write(str(mailArray)):
			print("Gmail messages written sucessfully to file.")
			
if __name__ == '__main__':
    fetchMail()

#Reading Google Documentation and working with oauth2client libraries to access personal email data   11-11-18   El Arnold = si3mshady 
