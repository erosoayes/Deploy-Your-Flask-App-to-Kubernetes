from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Hello, World from Flask!\n'



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)



# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTk5MTkwOTksIm5iZiI6MTY1ODcwOTQ5OSwiZW1haWwiOiJlcm9zb2F5ZXNAZ21haWwuY29tIn0.VbJXnMkEj8E5ZINaGTyyPm9vZfH97MQHZ8n22Z_rjgg