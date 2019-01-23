# import necessary libraries
from flask import Flask, render_template
import pymongo
import datetime
import scrape_mars


# create instance of Flask app
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.mars_db

# Declare the collection
collection = db.mars_db


# Create route that renders index.html template
@app.route("/")
def echo():

    mars_data = collection.find_one()
    return render_template("index.html", mars_data=mars_data)


# Add a new route
@app.route("/scrape")
def scrape():
    mars_data = collection.mars_data
    mars_data_scrape = scrape_mars.scrape()
    mars_data.update({}, mars_data_scrape, upsert=True)
   


if __name__ == "__main__":
    app.run(debug=True)