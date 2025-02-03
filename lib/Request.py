import requests
from requests import Response

class Request :

    def __init__( self , url : str , request : requests ) :

        self.url = url
        self.request = request
        self.has_fetched_data = False

    def fetch_data( self ) -> Response :

        try :
            response = self.request.get( self.url )
            self.has_fetched_data = True
            return response

        except requests.exceptions.ConnectionError :
            self.has_fetched_data = False
