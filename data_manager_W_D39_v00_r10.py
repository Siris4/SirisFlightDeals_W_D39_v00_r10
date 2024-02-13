import requests
import json, pprint

SHEETY_PRICES_URL_ENDPOINT = "https://api.sheety.co/cdae1a11efe5f92ecbe6d22972bba27d/sirisFlightDeals/prices"

#This class is responsible for talking to the Google Sheet.
class DataManager:
    # def __init__(self, JSON_data_in_PyDict_format):
    def __init__(self):
        self.destination_data = {}

    def get_request_for_getting_destination_data(self):
        # using the Sheety API to GET the data from that Google Sheet, and then print it out:
        sheety_API_GET_response = requests.get(url=SHEETY_PRICES_URL_ENDPOINT)  #  removed .json from end. no need for it!! it's not part of the endpoint. It goes on the next line:
        data = sheety_API_GET_response.json()
        self.destination_data = data["prices"]  # prices is the name of the sheet and also the List of Dictionaries
        # print(f"The sheety_API_GET_response: {sheety_API_GET_response.raise_for_status()}")

        # print("The pretty/formatted destination_data: ")
        # pprint.pprint(self.destination_data)
        return self.destination_data


    def update_destination_codes(self):   # remove: def destination_data(self): already used
        for city in self.destination_data:   #remove () after destination_data
            new_data = {
                "price": {      # singular form of the prices sheet name
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_URL_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

        # OR:
        #     }
        #     response = requests.put(
        #     url = f"{SHEETY_PRICES_URL_ENDPOINT}/{city['id']}",
        #     json = new_data
        # )
        # print(response.text)
