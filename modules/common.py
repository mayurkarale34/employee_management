
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
