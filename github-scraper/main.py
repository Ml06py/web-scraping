import requests
from bs4 import BeautifulSoup

# get the username
username = str(input("Enter your Username: "))

url = "https://github.com/{}"

# request for repo page
request = requests.get(url.format(username), params={"tab" : "repositories"})

if request.status_code == 200:
    response = BeautifulSoup(request.text, 'html.parser')

    # list of all repos
    all_repos = response.find("div", attrs={"id" : "user-repositories-list"})

    # single repos
    repos= all_repos.find_all("li", attrs={"class" : \
        "col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source"})

    for repo in repos:
        # name
        name = repo.find("a", attrs={"itemprop" : "name codeRepository"}).get_text(strip=True)
        # count stars
        star = repo.find("a", class_= "Link--muted mr-3")
        star = int(star.get_text(strip=True)) if star else 0
        # get the language
        language = repo.find("span", attrs={"itemprop" : "programmingLanguage"})
        language = language.get_text(strip=True) if language else "Unknown"
        # returm the result
        print(f"repo name: {name}, stars: {star}, language: {language}")

else:
    raise ValueError("User does not exist")