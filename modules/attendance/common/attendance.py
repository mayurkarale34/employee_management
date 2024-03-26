          
# common get attendance
def retrive_attendance_by_employee_name(employee_name):
    response = {
        "status" : False,
        "data" : [],
        "message" : ""
    }
    try:

        select_query = text(f"Select employee_name, clock_in_time, attendance_date from tb_attendance where employee_name = '{employee_name}';")

        # Executing the query with the provided connection
        result = app._engine.connect().execute(select_query)
        
        for row in result:
            response['data'].append({
                "employee_name" : row[0],
                "clock_in_time" : row[1],
                "attendance_date" :row[2]
            })
        response['status'] = True
        response['message'] = "Data retrived successfully..."
        return response
    except Exception as e:
        print(str(e))
        response['message'] = "Error while getting attendance, Please contact to admin"
        return response
