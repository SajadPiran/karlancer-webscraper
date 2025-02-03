import threading
import requests
from lib.Parser import Parser
from lib.Request import Request

url : str = 'https://www.karlancer.com/search?skillIds=1282,2915,1239,1369,2148'

if __name__ == '__main__':

    request_object = Request( url , requests )
    request = request_object.fetch_data()
    parser = Parser( request.text )


