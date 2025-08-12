from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor=connection.cursor()

    query='''SELECT PRODUCTS.PRODUCT_ID,PRODUCTS.NAME,PRODUCTS.UNIT_ID,PRODUCTS.PRICE,UOM.UOM_NAME
                                            FROM PRODUCTS INNER JOIN UOM ON PRODUCTS.UNIT_ID=UOM.UOM_ID'''

    cursor.execute(query)

    response=[]

    for (product_id,name,unit_id,price,uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'name':name,
                'unit_id':unit_id,
                'price':price,
                'unit':uom_name
            }
        )

    return response

def add_new_product(connection,product):
    cursor=connection.cursor()

    query='''INSERT INTO PRODUCTS(NAME,UNIT_ID,PRICE) VALUES (%s,%s,%s)'''

    data=(product['name'],product['unit_id'],product['price'])

    cursor.execute(query,data)

    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor=connection.cursor()
    query='''DELETE FROM PRODUCTS WHERE PRODUCT_ID='''+str(product_id)
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection=get_sql_connection()
    print(get_all_products(connection))