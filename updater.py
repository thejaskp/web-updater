import time
import hashlib
from urllib.request import urlopen, Request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def checker():
    url = Request('https://members.linkedin.com/en-in/student/linkedin-premium', headers={'User-Agent': 'Mozilla/5.0'})
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
            print("e")
        return render_template("index.html")
        

if __name__ == '__main__':
    app.run(debug = True, port=5001)









