from flask import Flask,jsonify,request,Response
import json

app = Flask(__name__)

orders = [
	{
		'name':'Ugali Kuku',
		'price':799,
		'order_id':1

	},

	{
		'name':'Fish Chips',
		'price':699,
		'order_id':2

	}
]



@app.route('/orders', methods=['POST'])
def add_order():
	request_data = request.get_json()
	response = Response("", 201, mimetype="application/json")
	return response 

app.run(port=5000)		