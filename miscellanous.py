from datetime import datetime
import pickle
def convert_to_datetime(t):
    year = int(t[:4])
    month = int(t[5:7])
    day = int(t[8:10])
    hour = int(t[11:13])
    minute = int(t[14:16])
    seconds = int(t[-2:])
    return datetime(year,month,day,hour,minute,seconds)
def save_file(data,path):
    with open(path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
def load_file(path):
    with open(path, 'rb') as handle:
        b = pickle.load(handle)
    return b

def extract_necessary_info(trip):
    from_c =trip["waypoints"][0]["place"]["city"],
    from_t =convert_to_datetime(trip["waypoints"][0]["date_time"])
    to_c = trip["waypoints"][1]["place"]["city"]
    to_t = convert_to_datetime(trip["waypoints"][1]["date_time"])
    price = trip["price"]["amount"]
    return from_c,from_t,to_c,to_t,price
    
def display(trip):
    print("From",trip["waypoints"][0]["place"]["city"],end="")
    print("(",trip["waypoints"][0]["date_time"][8:10],trip["waypoints"][0]["date_time"][11:16],")",end="")
    print(" to",trip["waypoints"][1]["place"]["city"],end="")
    print("(",trip["waypoints"][1]["date_time"][8:10],trip["waypoints"][1]["date_time"][11:16],")")