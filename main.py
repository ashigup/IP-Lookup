#Author -- Ashish Kumar -aka- Lucifer07 
#Contact -- github.com/ashigup
import requests
import argparse
import json

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ipaddress",help="IP address to track")
    args=parser.parse_args()
    ip = args.ipaddress
    url="http://ip-api.com/json/" + ip
    response=requests.get(url)
    data=json.loads(response.content)
    #print(data)
    print("\t\t[+]query        \t\t\t:",data["query"])
    print("\t\t[+]status       \t\t\t:",data["status"])
    print("\t\t[+]country\     \t\t\t:",data["country"])
    print("\t\t[+]country code \t\t\t:",data["countryCode"])
    print("\t\t[+]region       \t\t\t:",data["region"])
    print("\t\t[+]regionName   \t\t\t:",data["regionName"])
    print("\t\t[+]city         \t\t\t:",data["city"])
    print("\t\t[+]zip          \t\t\t:",data["zip"])
    print("\t\t[+]lat          \t\t\t:",data["lat"])
    print("\t\t[+]long         \t\t\t:",data["lon"])
    print("\t\t[+]timezone     \t\t\t:",data["timezone"])
    print("\t\t[+]isp          \t\t\t:",data["isp"])
    print("\t\t[+]org          \t\t\t:",data["org"])
    print("\t\t[+]as           \t\t\t:",data["as"])
    