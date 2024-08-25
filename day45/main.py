import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = soup.select("h3.title")
movies = [movie.getText() for movie in movies]
movies = movies[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
