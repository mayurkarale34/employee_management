
def check_duplicate_leave(data):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        select_query = f"Select * from tb_leave_applications where employee_id = '{data['employee_id']}' and from_date = '{data['from_date']}' and to_date = '{data['to_date']}'"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount > 0:
            response['status'] = True
            response['message'] = "Found duplicate record"
            return response
        return response
    except Exception as e:
        print(str(e))
        return response