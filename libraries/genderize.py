from collections import Counter
import requests
requests.packages.urllib3.disable_warnings()

class Genderize():
    def __init__(self):
        pass

    def get_gender_of_name(self, name):
        response = requests.get('https://api.genderize.io/', params={'name': name, 'country_id': 'US'}, verify = False)
        return response.json()["gender"]

    def male_and_female_name_count(self, name_count: Counter):
        female_name_count = 0
        for name in name_count:
            if self.get_gender_of_name(name) == 'female' : female_name_count += name_count[name]
        total_count = sum(name_count.values())

        return (total_count - female_name_count, female_name_count)
