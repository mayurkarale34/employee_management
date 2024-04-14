
def check_duplicate_metadata(data):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        select_query = f"Select * from tb_metadata where element = '{data['element']}' and date(type) = '{data['type']}'"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount > 0:
            response['status'] = True
            response['message'] = "Found duplicate"
            return response
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
 