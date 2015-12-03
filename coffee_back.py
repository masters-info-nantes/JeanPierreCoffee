from flask import Flask, redirect, url_for
import requests
app = Flask(__name__)

AUTH_SERVER = "http://blank.org/"
token = ""

@app.route("/hello")
def hello():
	#get request on authentication server
	token = requests.get(AUTH_SERVER).content
	print(token)
	return ""

@app.route("/buyCoffee")
def buyCoffee():
	return 

if __name__ == "__main__":
    app.run(debug=True)
