#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, jsonify
import json
import requests
app = Flask(__name__)

AUTH_SERVER = 'http://localhost:8080/ame-services-rest/service/token'
LOG_SERVER = ''

@app.route('/hello', methods=['GET'])
def hello():
	return jsonify({'url' : AUTH_SERVER})

@app.route("/buycoffee/<token>", methods=['GET'])
def buyCoffee(token, charset='utf-8'):
	print token

	logs = jsonify({
		'actionType' : "drink",
		'vendingMachineId' : "",
		'vendingMachineType' : "",
		'userType' : "",
		'userId' : "",
		'previousBalance' : 0.0,
		'currentBalance' : 0.0,
		'cost' : 0.0,
		'itemId' : "",
		'isoDate' : ""
	})

	headers = {'Api-Key': 'reQSFGgFSbgc54uyhjg35hgf23vJhg432JNkjH', 'Authorization': str(token), 'Content-Type': 'application/json;charset=UTF-8'}
	r = requests.get(AUTH_SERVER, headers=headers)
	print r	
	#print r.content
	#Send logs to log server
	#l = requests.post(LOG_SERVER, logs=logs)
	#print l.content
	return (r.text, r.status_code, r.headers.items())

if __name__ == "__main__":
    app.run(debug=True)
