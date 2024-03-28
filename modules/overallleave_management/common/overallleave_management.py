
# common get overallleave
def retrive_overallleave_by_employee_name(employee_name):
    response = {
        "status" : False,
        "data" : [],
        "message" : ""
    }
    try:
        
        select_query = text(f"Select employee_name, earn_leave, casual_leave, maternity_leave, paternity_leave from tb_overallleave where employee_name = '{employee_name}';")

        # Executing the query with the provided connection
        result = app._engine.connect().execute(select_query)
        
        for row in result:
            response['data'].append({
                "employee_name" : row[0],
                "earn_leave" : row[1],
                "casual_leave" :row[2],
                "maternity_leave" :row[3],
                "paternity_leave" :row[4]
            })
        response['status'] = True
        response['message'] = "Data retrived successfully..."
        return response
    except Exception as e:
        print(str(e))
        response['message'] = "Error while getting attendance, Please contact to admin"
        return response
