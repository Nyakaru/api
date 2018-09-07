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

#GET/orders
@app.route('/orders')
def get_orders():
	return jsonify({'orders':orders})

app.run(port=5000)