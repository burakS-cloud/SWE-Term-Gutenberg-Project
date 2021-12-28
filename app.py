from flask import *
import requests
import urllib.request

app = Flask('mars_discovery')


@app.route('/')
def index():
    books = []
    if 'book' in request.args:
        search_word = request.args.get('book')
        response = requests.get("http://gutendex.com/books/?search=" + search_word)
        data = json.loads(response.content)
        tempbooks = data['results']
        for book in tempbooks:
            if book['media_type'] == "Text":
                books.append(book)

    return render_template('home.html', books=books)


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()


app.run(debug=True)
