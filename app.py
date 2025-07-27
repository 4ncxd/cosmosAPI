from flask import Flask, render_template
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)
NASA_API_KEY = os.getenv("NASA_API_KEY")

@app.route('/')
def hello ():
    return "Hello world"

@app.route('/apod')
def inApod ():
    urlApod = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    resApod = requests.get(urlApod)
    dictApod = resApod.json()
    date = dictApod.get('date', 'inalid date req')
    explain = dictApod.get("explanation", "no explainitation available, sorry!")
    title = dictApod.get("title", "title invalid")
    imgURL = dictApod.get("url", "")
    return render_template(
        "apod.html",
        title=dictApod.get("title", "No Title"),
        date=dictApod.get("date", "Unknown Date"),
        explanation=dictApod.get("explanation", "No Explanation"),
        image_url=dictApod.get("url", "")
    )

app.run(debug=True)