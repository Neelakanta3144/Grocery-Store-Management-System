from flask import Flask,request,jsonify
import json
import products_dao
import orders_dao
from sql_connection import get_sql_connection
import uom_doa

app=Flask(__name__)

connection=get_sql_connection()

@app.route('/getproducts',methods=['GET'])
def get_products():
    products=products_dao.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteproduct',methods=['POST'])
def delete_products():
    return_id=products_dao.delete_product(connection,request.form['product_id'])
    response=jsonify({'product_id':return_id})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getuoms',methods=['GET'])
def get_uoms():
    response=uom_doa.get_uoms(connection)
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct',methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.add_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=='__main__':
    print("Starting Flask server for Groecry store management system")
    app.run()