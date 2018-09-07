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

@app.route('/orders/<int:order_id>')
def get_book_by_order_id(order_id):
 	return_value = {}
 	for order in orders:
 		if order["order_id"] == order_id:
 			return_value = {
 				'name':order["name"],
 				'price':order['price']
 			}
 	return jsonify(return_value)

app.run(port=5000)