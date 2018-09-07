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

@app.route('/orders/<int:order_id>',methods=['PUT'])
def replace_order(order_id):
	request_data = request.get_json()
	new_order = {
			"name": request_data['name'],
			"price": request_data['price'],
			"order_id": order_id
		}
	i = 0;
	for order in orders:
		currentOrder_id = order['order_id']
		if currentOrder_id == new_order:
			orders[i] = new_order
		i += 1
	response = Response("", status=204)
	return response

app.run(port=5000)