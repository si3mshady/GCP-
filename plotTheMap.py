import urllib.request, json, gmplot

class Signs:
    def __init__(self,street_num,street,city,state):
        self.street_num = street_num
        self.street = street 
        self.city = city 
        self.state = state
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        self.key = self.get_apikey()
        self.master_url = "{0}{1}+{2},+{3},+{4}&key={5}".format(self.url,self.street_num,self.street,self.city,self.state,self.key)

    def get_apikey(self):
        self.apikey = open('apiKey').read().strip()
        return self.apikey

def greeting():
    print("Please enter an address to plot to Google Maps:",end='\n')        

def api_call(instance):
    response = urllib.request.urlopen(instance.master_url).read()  #authenticate to google geocode with api key 
    clean_response = json.loads(response)     
    extract_coordinates(clean_response)
      
def extract_coordinates(clean_response):   
    lat = clean_response['results'][0]['geometry']['bounds']['northeast']['lat']    #extract latitude coordinate  
    lng = clean_response['results'][0]['geometry']['bounds']['northeast']['lng']    #extract longitude coordinate 
    plot_thickens(lat,lng)

def plot_thickens(lat,lng):    
    plot = gmplot.GoogleMapPlotter(lat,lng,30)  #call gmplot to create google map object 
    filename = input('Save file as: ')
    plot.draw(filename + '.html')    
    print("Google Map object {} has been saved.".format(filename + '.html'))
    
def begin():    
    entries = ['Street Number: ','Street Name: ','City: ','State: ']    
    go = True 
    while go:
        greeting()
        address = []
        for entry in entries:
            response = input('Please enter: {}'.format(entry))
            address.append(response)
        s = Signs(address[0],address[1],address[2],address[3])
        api_call(s)        
        respuesta = input("Continue? 'y/n': ")
        if respuesta == 'n':
            go = False         
    print("GoodBye!")       

if __name__ == "__main__":  
    begin()

#diy quick api execrises on google cloud platform importing GMPLOT 12-5-19    Elliott Arnold / si3mshady 

       








       





