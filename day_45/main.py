from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
top_100 = soup.findAll(name='h3' ,class_="title")

movie_list = [movie.getText() for movie in top_100]

movies = movie_list[::-1]


with open("top_100_movies.txt", 'w', encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")