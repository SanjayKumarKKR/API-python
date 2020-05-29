from flask import *
from flask import request
import requests

app = Flask(__name__)


@app.route('/')
def postJsonHandler():
    res =requests.get("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")
    content = res.json()
    print(content['paid'])
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run()