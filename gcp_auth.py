from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as f
from oauth2client import client,tools

class MAKE_GCP_SVC:
    '''Creates a GCP authorization object which is the precursor to accessing personal GCP services'''
    def __init__(self,SCOPE,CLIENT_SECRET,SERVICE,VERSION):
        self.SCOPE = SCOPE
        self.SECRET = CLIENT_SECRET
        self.SERVICE = SERVICE 
        self.SVC = None 
        self.CACHED_CREDENTIALS = None  
        self.EVEN_FLOW = None 
        self.CRED = None         
        self.CACHED_CREDENTIALS = f.Storage('token.json')

        try:
            credentials = self.CACHED_CREDENTIALS.get()
            if not credentials or credentials == None:
                pass 
        except KeyError:
            pass 
        print("Initializing Oauth2 flow:\n")
        self.EVEN_FLOW = client.flow_from_clientsecrets(self.SECRET,self.SCOPE)
        if self.EVEN_FLOW:
            print("Pass: Flow from client secrets.\n")
            self.CRED = tools.run_flow(self.EVEN_FLOW,self.CACHED_CREDENTIALS )
        if self.CRED:
            print("Redirecting to browswer.\n")
            self.SVC = build(SERVICE,VERSION,http=self.CRED.authorize(Http()))
        print("Service {} is online and ready.".format(self.SERVICE))
