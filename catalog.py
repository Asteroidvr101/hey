import requests
from datetime import date
import json

# credits to czangilos 


def main():
    try:
        sessionTicket = input('Enter Session Ticket: ')

        response = requests.post(url="https://63FDD.playfabapi.com/Client/GetCatalogItems",
                                 headers={"Content-Type": "application/json",
                                          "X-Authorization": sessionTicket})
        if response.status_code != 200:
            print(f"[ERROR] Status Code Not 200! [StatusCode: {response.status_code}]")
            return

        rjson = response.json()

        del rjson['code']
        del rjson['status']

        catalog = rjson['data']['Catalog']
        del rjson['data']

        rjson['CatalogVersion'] = 'DLC'
        rjson['Catalog'] = catalog

        name = getFileName()

        with open(name, 'w') as file:  # Use a context manager to handle file opening/closing
            file.write(json.dumps(rjson))
        
        print(f"[INFO] DLC Saved To: {name}")

    except Exception as e:
        print(f"[ERROR] {e}")

def getFileName():
    return f"{date.today().strftime('%Y-%m-%d')}_DLC.json"  # Change double quotes to single quotes

if __name__ == '__main__':
    main()