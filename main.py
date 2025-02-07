import re
import threading
import requests
from win10toast import ToastNotifier

from lib.Parser import Parser
from lib.Request import Request

url : str = 'https://www.karlancer.com/search?skillIds=1282,2915,1239,1369,2148'
request_object : Request = Request( url, requests )

def fetch_data() -> { str : str } :

    request = request_object.fetch_data()
    parser = Parser( request.text )
    return parser.get_all_data()[0]

def show_notification( data : dict ) :

    toast = ToastNotifier()
    toast.show_toast(
        data['title'],
        data['price'] ,
        duration = 10 ,
        icon_path = './karlancer-logo.ico'
    )
def start() -> { str : str } :

    thread = threading.Timer( 40 , start )
    thread.start()
    data = fetch_data()
    release_time =  data['release_time']

    if re.search( 'ثانیه' , release_time ) is not None :
        show_notification( data )
        for key in data:
            print(f'{key} : {data[key]}')

            
if __name__ == '__main__':

    start()
