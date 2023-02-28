import time
import hashlib
from urllib.request import urlopen, Request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
     return render_template("index.html")

@app.route("/result")

def result():
    output = request.form.to_dict()
    link = output["name"]
    print(link)
    url = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    currentHash = hashlib.sha224(response).hexdigest()
    print('running...')
    time.sleep(10)
    while True:
            try: 
                response = urlopen(url).read()
                currentHash = hashlib.sha224(response).hexdigest()
                time.sleep(20)

                response = urlopen(url).read()
                newHash = hashlib.sha224(response).hexdigest()

                if newHash == currentHash:
                    continue
                else:
                    print('something changed')
                    response = urlopen(url).read()
                    currentHash = hashlib.sha224(response).hexdigest()
            except Exception as e:
                 print(e)
            return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True, port=5001)









