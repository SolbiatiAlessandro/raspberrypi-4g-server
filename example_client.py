import requests
import os

if __name__ == "__main__":
    os.environ['LOCAL_PROXY'] = '127.0.0.1'
    r = requests.get('http://127.0.0.1:8000')
    print(r.text)
