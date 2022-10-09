# This script takes a party id as an argument and returns
# stats about the party.
from collections import Counter
from libraries.genderize import Genderize
from libraries.partiful import Partiful
import sys

def main():
    party_id = sys.argv[1]
    partiful_service = Partiful(party_id)
    guest_first_names = partiful_service.get_guests_first_names()
    genderize_service = Genderize()
    male_name_count, female_name_count = genderize_service.male_and_female_name_count(Counter(guest_first_names))

    print("Party info:")
    print("Male name count: " + str(male_name_count))
    print("Female name count: " + str(female_name_count))

    print('Guest List:')
    partiful_service.print_guest_list()
    return

if __name__ == "__main__":
   main()
