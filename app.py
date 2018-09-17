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

@app.route('/orders/<int:order_id>')
def get_order_by_order_id(order_id):
 	return_value = {}
 	for order in orders:
 		if order["order_id"] == order_id:
 			return_value = {
 				'name':order["name"],
 				'price':order['price']
 			}
 	return jsonify(return_value)


@app.route('/orders', methods=['POST'])
def add_order():
	request_data = request.get_json()
	response = Response("", 201, mimetype="application/json")
	return response 
	

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

@app.route('/orders/<int:order_id>',methods=['DELETE'])
def delete_order(order_id):
	i = 0;
	for order in orders:
		if order["order_id"] == order_id:
			orders.pop(i)
			response = Response("", status=204)
			return response

		i += 1
	invalidOrderObjectErrorMsg = {
			"error":"Order with order_id number was not found",
			
		}
	response = Response(json.dumps(invalidOrderObjectErrorMsg), status=404, mimetype="application/json")
	return response
		

app.run(port=5000)