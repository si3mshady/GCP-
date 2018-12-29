from gcp_auth import MAKE_GCP_SVC as mgs
import datetime 
global secret, scope, service, version 
scope = "https://www.googleapis.com/auth/calendar"
secret = "/Users/si3mshady/Documents/credentials.json"
service = 'calendar'
version = 'v3'
def create_calendar_bookend(mode=None):
    time_args = ['Year: ','Month as (1-12): ','Day of Month as (1-31): ','Hour (0-24): ','Minute (0-60): ','Seconds (0-60)']
    try:
        if mode.lower() == 'start' or mode.lower() == 'end':
            print('Please enter requested values to create {} date for event'.format(mode.lower()))
        elif mode.lower() == None:
            pass
    except:
        AttributeError
        pass
    user_response = []
    for arg in time_args:
        try:
            ans = int(input('Please Enter {}'.format(str(arg))))
            user_response.append(ans)
        except:
            ValueError
            print('Please enter time values as integers')
            continue
    
    return datetime.datetime(user_response[0],user_response[1],user_response[2],user_response[3],user_response[4],user_response[5]).isoformat()

def user_instructions():
    print("Please use the following script to add events to your Google Calendar.")

def main_event():
    user_instructions() 
    svc_gcp  = mgs(scope,secret,service,version)   
    while True:
        response = input('Please indicate any keyword to progress\n"Start","End","Description","Create","Quit":\n ')
        if response.lower() == 'start':
            start = create_calendar_bookend(response)
        elif response.lower() == 'end':
            end = create_calendar_bookend(response)
        elif response.lower() == 'description':
            description = input("Please submit a short description of the event.")
        elif response.lower() == 'create':
            event = {'description':description,'start':{'dateTime': start, 'timeZone': 'America/Chicago' },'end':{'dateTime': end, 'timeZone':'America/Chicago'}}
            event = svc_gcp.SVC.events().insert(calendarId='primary', body=event).execute()            
	     
        elif response.lower() == 'quit':
            break
        else:
            continue 
            
if __name__ == "__main__":
    main_event()

        


        

