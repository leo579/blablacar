import pickle,requests
import datetime
from geopy.geocoders import Nominatim
import miscellanous

def add_time_delta_to_start_date(start_date_local,time_delta):
    year = int(start_date_local[:4])
    month = int(start_date_local[5:7])
    day = int(start_date_local[8:10])
    s = datetime.date(year,month,day)
    delta = datetime.timedelta(days=time_delta)
    end = s+delta
    year = str(end.year)
    month = str(end.month)
    day = str(end.day)
    if len(month)==1:month="0"+month
    if len(day)==1:day="0"+day
    end = list(start_date_local)
    end[0:4] = list(year)
    end[5:7] =list(month)
    end[8:10]=list(day)
    end = "".join(end)
    return end

def get_coordinates(city_name,coordinate_name):
    coordinate_dic = miscellanous.load_file(coordinate_name)
    if city_name in coordinate_dic.keys():
        return coordinate_dic[city_name]
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city_name)
    coordinate_dic[city_name] = str(location.latitude)+","+str(location.longitude)
    miscellanous.save_file(coordinate_dic, coordinate_name)
    return str(location.latitude)+","+str(location.longitude)


def add_start_date_local(parameter):
    if parameter == None: return ""
    else :return "&start_date_local="+parameter
def add_end_date_local(parameter):
    if parameter == None: return ""
    else :return "&end_date_local="+parameter
def add_requested_seats(parameter):
    if parameter == None: return ""
    else :return "&requested_seats="+parameter
def add_radius_in_meters(parameter):
    if parameter == None: return ""
    else :return "&radius_in_meters="+parameter
def add_sort(parameter):
    if parameter == None: return ""
    else :return "&sort="+parameter 
def add_count(parameter):
    if parameter == None: return ""
    else :return "&count="+parameter
def add_from_cursor(parameter):
    if parameter == None: return ""
    else :return "&from_cursor="+parameter
def add_currency(parameter):
    if parameter == None: return ""
    else :return "&currency="+parameter
def add_locale(parameter):
    if parameter == None: return ""
    else :return "&locale="+parameter
def add_to_coordinate(parameter):
    if parameter == None: return ""
    else :return "&to_coordinate="+parameter
def add_from_coordinate(parameter):
    if parameter == None: return ""
    else :return "&from_coordinate="+parameter
def add_api_key(API_KEY):
    if API_KEY == None: return ""
    else :return "key="+API_KEY
def get_url(API_KEY,from_coordinate,to_coordinate,locale,currency,from_cursor,count,start_date_local,time_delta,
            requested_seats,radius_in_meters,sort):
    url = "https://public-api.blablacar.com/api/v3/trips?"
    end_date_local = add_time_delta_to_start_date(start_date_local,time_delta)
    url+=add_api_key(API_KEY)
    url+=add_from_coordinate(from_coordinate)
    url+=add_to_coordinate(to_coordinate)
    url+=add_locale(locale)
    url+=add_currency(currency)
    url+=add_from_cursor(from_cursor)
    url+=add_count(count)
    url+=add_sort(sort)
    url+=add_radius_in_meters(radius_in_meters)
    url+=add_requested_seats(requested_seats)
    url+=add_start_date_local(start_date_local)
    url+=add_end_date_local(end_date_local)
    return url
def run_request(url):
    return requests.get(url)
def save_requests(path,r):
    with open(path, 'wb') as handle:
        pickle.dump(r, handle, protocol=pickle.HIGHEST_PROTOCOL)

def run_all(API_KEY,from_city,to_city,locale,currency,from_cursor,count,start_date_local,time_delta,
            requested_seats,radius_in_meters,sort,path,coordinate_name,save=True):
    from_coordinate = get_coordinates(from_city,coordinate_name)
    to_coordinate = get_coordinates(to_city,coordinate_name)
    url = get_url(API_KEY,from_coordinate,to_coordinate,locale,currency,from_cursor,count,start_date_local,time_delta,
                requested_seats,radius_in_meters,sort)
    r = run_request(url)
    if save:
        save_requests(path, r)
    return r

def run_all_requests(API_KEY,from_city,to_city,locale,currency,from_cursor,count,start_date_local,time_delta,
            requested_seats,radius_in_meters,sort,path,coordinate_name,intermediary_cities):
    request_dic = {}
    request_dic["DIRECT"] = run_all(API_KEY,from_city,to_city,locale,currency,from_cursor,count,start_date_local,time_delta,
                requested_seats,radius_in_meters,sort,path,coordinate_name,save=False)
    for c in intermediary_cities:
        request_dic[from_city+c]=run_all(API_KEY,from_city,c,locale,currency,from_cursor,count,start_date_local,time_delta,
                    requested_seats,radius_in_meters,sort,path,coordinate_name,save=False)
        request_dic[c+to_city]=run_all(API_KEY,c,to_city,locale,currency,from_cursor,count,start_date_local,time_delta,
                    requested_seats,radius_in_meters,sort,path,coordinate_name,save=False)
    miscellanous.save_file(request_dic, path)