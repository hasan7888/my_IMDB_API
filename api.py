# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, json, request
import csv
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

def movie(genre):
    genre=genre.capitalize()
    #print(genre)
    result=[]
    filename="./imdb-movie-data.csv" 
    with open(filename) as csvfile:
       csv1=csv.DictReader(csvfile) 
       for line in csv1:
           #print(line)
           genres=line["Genre"].split(",")
           
           if genre in genres:
                result.append(line)
    return result

@app.route('/')
def home():
         genre=request.args.get('genre')
         
         movies=movie(genre)
         return json.dumps(movies)


@app.route('/<genre>')
def list_movies(genre):
    movies=movie(genre)
    return json.dumps(movies)


# driver function
if __name__ == '__main__':

    app.run("0.0.0.0", port=8080)
