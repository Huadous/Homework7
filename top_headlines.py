from flask import Flask, render_template
from secrets import api_key
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name/<nm>')  
def name_nm(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines_nm(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=xeFKNh4VSVnb3NXLeVacjQZaBM8GW5js'
    r = requests.get(url)
    topFive = json.loads(r.text)['results'][0:6]
    titles = []
    for ele in topFive:
        titles.append(ele['title'])
    return render_template('headlines.html', name=nm, titles=titles)

@app.route('/links/<nm>')
def links_nm(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=xeFKNh4VSVnb3NXLeVacjQZaBM8GW5js'
    r = requests.get(url)
    topFive = json.loads(r.text)['results'][0:6]
    titles = []
    urls = []
    for ele in topFive:
        titles.append(ele['title'])
        urls.append(ele['url'])
    return render_template('links.html', name=nm, titles=titles, urls=urls)

@app.route('/images/<nm>')
def images_nm(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=xeFKNh4VSVnb3NXLeVacjQZaBM8GW5js'
    r = requests.get(url)
    topFive = json.loads(r.text)['results'][0:6]
    titles = []
    urls = []
    imgs = []
    for ele in topFive:
        titles.append(ele['title'])
        urls.append(ele['url'])
        imgs.append(ele['multimedia'][0]['url'])
    return render_template('images.html', name=nm, titles=titles, urls=urls, imgs=imgs)

if __name__ == '__main__':
    print('starting Flask app', app.name)  
    app.run(debug=True)

