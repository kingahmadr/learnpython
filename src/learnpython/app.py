import os

from dotenv import load_dotenv, dotenv_values
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/value')
def get_value():
    load_dotenv()

    result = os.getenv("HOST")
    return result


# main driver function
if __name__ == '__main__':
    app.run()