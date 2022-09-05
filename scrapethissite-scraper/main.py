import requests 
from bs4 import BeautifulSoup


url = "http://www.scrapethissite.com/pages/simple/"

request = requests.get(url)

response = BeautifulSoup(request.text, "html.parser")

if request.status_code == 200:

    # Get the main div of a country
    countries = response.find_all("div", class_="col-md-4 country")

    def get_text_and_strip(value):
        return value.get_text().strip()

    for country in countries:
        name = get_text_and_strip(country.find("h3", class_="country-name"))
        capital = get_text_and_strip(country.find("span", class_="country-capital"))
        population = get_text_and_strip(country.find("span", class_="country-population"))
        area = get_text_and_strip(country.find("span", class_="country-area"))

        with open("countris.txt", "a") as f:
            f.write(f"name:{name} | capital:{capital} | population: {population} | area: {area} \n")
    
    print("Data scraped successfully")
        
else:
    raise ValueError("page does not exist")


        


