import miscellanous
import datetime



def trip_is_compatible(trip_1,trip_2,max_waiting_time):
    info1 = miscellanous.extract_necessary_info(trip_1)
    info2 = miscellanous.extract_necessary_info(trip_2)
    minutes = (info2[1]-info1[3] )/ datetime.timedelta(minutes=1)
    if minutes < max_waiting_time and minutes > -10:
        return True
    else :
        return False

def get_price(trip_list):
    s = 0
    for t in trip_list:
        s+= float(miscellanous.extract_necessary_info(t)[4])
    return s
    
def find_compatible_routes(path,from_city,to_city,inter_cities,max_waiting_time):
    requests = miscellanous.load_file(path)
    directs = requests["DIRECT"].json()
    for trip in directs["trips"]:
        print(" #####")
        print("Price : ",miscellanous.extract_necessary_info(trip)[4])
        miscellanous.display(trip)
        
    for c in inter_cities:
        trips1 = requests[from_city+c].json()
        trips2 = requests[c+to_city].json()
        for t1 in trips1["trips"]:
            for t2 in trips2["trips"]:
                if trip_is_compatible(t1, t2, max_waiting_time):
                    print(" #####")
                    print("Price : ",get_price([t1,t2]))
                    miscellanous.display(t1)
                    miscellanous.display(t2)