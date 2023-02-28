import time
import hashlib
from urllib.request import urlopen, Request

link = 'https://members.linkedin.com/en-in/student/linkedin-premium'

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
        print("e")


