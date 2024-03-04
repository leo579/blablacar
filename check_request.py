import pickle 
import miscellanous
path = "test.pickle"
def open_request(path):
    with open(path, 'rb') as handle:
        r = pickle.load(handle)
    return r
r = open_request(path)["DIRECT"].json()


def display(trip):
    print("From",trip["waypoints"][0]["place"]["city"],end="")
    print("(",trip["waypoints"][0]["date_time"][8:10],trip["waypoints"][0]["date_time"][11:16],")",end="")
    print(" to",trip["waypoints"][1]["place"]["city"],end="")
    print("(",trip["waypoints"][1]["date_time"][8:10],trip["waypoints"][1]["date_time"][11:16],")")

    
for trip in r["trips"]:
    display(trip)