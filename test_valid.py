def validOrderObject(orderObject):
	if ("name" in orderObject
			and "price" in orderObject
				and "order_id" in orderObject):
		return True
	else:
		return False

valid_object = {
	'name':'Ugali Kuku',
		'price':799,
		'order_id':1
}

missing_name = {

	
	'price':799,
	'order_id':9
}

missing_price = {
	'name':'Green Eggs',
	'order_id':9
}

missing_order_id = {
	'name':'Green Eggs',
	'price':799
	
	
}

emptydictionary = {}