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