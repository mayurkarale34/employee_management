
# common add to database
def add_to_database(data, table, connection):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        # Constructing the INSERT query dynamically
        columns = ', '.join(data.keys())
        values = ""
        for val in data.values():
            if len(values):
                values = values + ', '+ "'" + val + "'"
            else:
                values = "'" + val + "'"
        insert_query = text(f"INSERT INTO {table} ({columns}) VALUES ({values});")

        # Executing the query with the provided connection
        connection.execute(insert_query)
        
        response['status'] = True
        return response
    except Exception as e:
        print(str(e))
        return response
    
# common get metadata
def retrive_metadata_by_type(type):
    response = {
        "status" : False,
        "data" : [],
        "message" : ""
    }
    try:

        select_query = text(f"Select id, element from tb_metadata where type = '{type}';")

        # Executing the query with the provided connection
        result = app._engine.connect().execute(select_query)
        
        for row in result:
            response['data'].append({
                "id" : row[0],
                "element" : row[1]
            })
        response['status'] = True
        response['message'] = "Data retrived successfully..."
        return response
    except Exception as e:
        print(str(e))
        response['message'] = "Error while getting metadata, Please contact to admin"
        return response
