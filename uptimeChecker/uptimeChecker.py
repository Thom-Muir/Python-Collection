import requests
import json
import time
import pandas as pd

#Loads configuration
with open("sites.json", "r") as file:
    sites_list = json.load(file)


csv_file = "siteUptimes.csv"
fail_counter = {}
time_counter = {}

while True:
    #Sends get requests to websites on list
    for site in sites_list.get('sites', []):
        try:
            req = requests.get(site, timeout=5)
            #Tracks status code
            print(f"{site} responded {req.status_code}")
            #If 500+(server error) then track failure
            if req.status_code >= 500:
                fail_counter[site] = fail_counter.get(site, 0) + 1
            #Otherwise track uptime
            else:
                fail_counter[site] = 0
            if site not in time_counter:
                time_counter[site] = time.time()
            uptime = time.time()- time_counter[site]
            print(f"{site} has been up for {uptime:.2f} seconds")
            
            #Append to uptime CSV file
            try:
                df = pd.read_csv(csv_file)
            except FileNotFoundError:
                df = pd.DataFrame(columns=["Site", "Uptime (seconds)"])    
            df.loc[df["Site"] == site, "Uptime (seconds)"] = round(uptime, 2)
            if site not in df["Site"].values:
                df = pd.concat([df, pd.DataFrame([{"Site": site, "Uptime (seconds)": round(uptime, 2)}])], ignore_index=True)
            df.to_csv(csv_file, index=False)
        
        #If failed to connect to server, track failure        
        except requests.exceptions.ConnectionError:
            print(f"Connection error to {site}")
            fail_counter[site] = fail_counter.get(site, 0) + 1
        
        #If request timed out, track failure  
        except requests.exceptions.Timeout:
            print(f"Connection to {site} timed out")
            fail_counter[site] = fail_counter.get(site, 0) + 1
        
        #Catch all for any other error, track faliure
        except requests.exceptions.RequestException as error:
            print(f"Error: {error} for {site}")
            fail_counter[site] = fail_counter.get(site, 0) + 1
            
        #Displays alert if site fails +3 checks in a row
        if fail_counter.get(site, 0) >= 3:
            print(f"\n  -Alert: {site} has failed {fail_counter[site]} consecutive checks-  \n")

    #Rest for 3 minutes
    print("Sleeping for 3 minutes")
    print("\n") 
    time.sleep(180)    