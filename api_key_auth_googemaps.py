class APIKEY:
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