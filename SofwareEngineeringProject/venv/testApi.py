import flask
import json
import requests



search_word = "hyde"
books = []
response = requests.get("http://gutendex.com/books/?search=" + search_word)
data = json.loads(response.content)
books = data['results']
print(books[3])


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
