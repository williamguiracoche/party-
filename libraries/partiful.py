from urllib import response
import requests
from termcolor import colored

class Partiful():
    def __init__(self, party_id):
        self.party_id = party_id

    # Data in response for brainstorming
    # 'id', 'status', 'count', 'rsvpDate', 'plusOneCount', 'user', 'userId', 'name', 'rsvpHistory'
    def get_guests(self):
        request_url = "https://us-central1-getpartiful.cloudfunctions.net/getGuests"
        json_data = {'data': {'eventId': self.party_id}}
        response = requests.post(request_url, json=json_data)
        response.raise_for_status()
        return response.json()

    def get_guests_first_names(self):
        first_names = []
        for guest_info in self.get_guests()['result']:
            first_names.append(guest_info['name'].split()[0].lower())
        return first_names

    def print_guest_list(self):
        for guest in self.get_guests()['result']:
            plus_one_str = ''
            if guest['plusOneCount'] > 0:
                plus_one_str = "(+{})".format(guest['plusOneCount'])
            print(
                colored(guest['name'], "white"),
                colored(plus_one_str, "cyan")
            )
        return
