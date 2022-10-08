# This script takes a party id as an argument and returns
# stats about the party.
from collections import Counter
import requests
import sys
requests.packages.urllib3.disable_warnings()

def main():
    request_url = "https://us-central1-getpartiful.cloudfunctions.net/getGuests"
    party_id = sys.argv[1]
    json_data = {'data': {'eventId': party_id}}
    guests_response = requests.post(request_url, json=json_data)
    # Data in response to brainstorm:
    # 'id', 'status', 'count', 'rsvpDate', 'plusOneCount', 'user', 'userId', 'name', 'rsvpHistory'

    # names used to display everyone going
    # first_names will be used for stats
    names = []
    first_names = []
    for guest in guests_response.json()['result']:
        name = guest['name']
        first_names.append(name.split()[0].lower())

        if guest['plusOneCount'] > 0:
            name = name + " (+ {})".format(guest['plusOneCount'])
        names.append(name)

    male_name_count, female_name_count = gender_count(Counter(first_names))
    print("Party info:")
    print
    print("Male name count: " + str(male_name_count))
    print("Female name count: " + str(female_name_count))
    return

def gender_count(name_count: Counter):
    female_name_count = 0
    for name in name_count:
        response = requests.get('https://api.genderize.io/', params={'name': name, 'country_id': 'US'}, verify = False)   
        if response.json()['gender'] == 'female' : female_name_count += name_count[name]
    total_count = sum(name_count.values())

    return (total_count - female_name_count, female_name_count)

if __name__ == "__main__":
   main()
