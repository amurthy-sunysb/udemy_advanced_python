import requests
from selectorlib import Extractor



class Temperature:
    """Represents a temperature value extracted from the timeanddate.com/weather webpage"""

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    url_prefix = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        url_to_request = self.url_prefix + self.country.lower().replace(' ', '-') + '/' + self.city.lower().replace(' ', '-')

        r = requests.get(url_to_request, headers=self.headers)
        if (r.status_code == 200):
            c = r.text
            extractor = Extractor.from_yaml_file('temperature.yaml')
            raw_text = extractor.extract(c)
            
            try:
                temperature = float(raw_text['temp'].replace('°F', '').strip())
                return temperature
            except:
                print('Could not retreive valid temperature')
        else:
            print('Couldnt retrieve temperature')


if __name__ == "__main__":
    t = Temperature(country='USA', city = 'New York')
    print(t.get())



