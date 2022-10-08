# This script takes a party id as an argument and returns
# stats about the party.
from collections import Counter
from libraries.partiful import Partiful
import requests
import sys
requests.packages.urllib3.disable_warnings()

def main():
    party_id = sys.argv[1]
    partiful_service = Partiful(party_id)
    guest_first_names = partiful_service.get_guests_first_names()
    male_name_count, female_name_count = gender_count(Counter(guest_first_names))

    print("Party info:")
    print("Male name count: " + str(male_name_count))
    print("Female name count: " + str(female_name_count))

    print('Guest List:')
    partiful_service.print_guest_list()
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
