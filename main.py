import pickle,requests
import datetime
from geopy.geocoders import Nominatim
import run_request,find_routes,miscellanous
import os

### Enter your variables
API_KEY = "YOUR_API_KEY" # you must request access to Blablacar for this
from_city = "Name of your starting city"
to_city = "Name of your destination"
intermediary_cities = ["Intermediate city 1","Intermediate city 2"]
start_date_local = "2024-03-04T12:00:00"
max_waiting_time = 60*3 ###in minutes
time_delta = 3 ### in days. This is the search window. Max is 3.
number_of_seats = 1
currency = "EUR"


##### Dont edit after this - clean this up later #####
RUN_REQUEST = True
locale = None
from_cursor = None
count = None
requested_seats = str(number_of_seats)
radius_in_meters = str(50000)
sort = None
path = "test.pickle"
coordinate_name = "coordinates.pickle"
if __name__=="__main__":
    if not os.path.isfile(coordinate_name):
        miscellanous.save_file({}, coordinate_name)
    run_request.run_all_requests(API_KEY,from_city,to_city,locale,currency,from_cursor,count,start_date_local,time_delta,
                requested_seats,radius_in_meters,sort,path,coordinate_name,intermediary_cities)
    find_routes.find_compatible_routes(path,from_city,to_city,intermediary_cities,max_waiting_time)
    
