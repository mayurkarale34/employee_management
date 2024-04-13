
# common get overallleave
def check_duplicate_overall_leave_master(data):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        
        select_query =f"Select * from tb_overallleave where employee_id = '{data['employee_id']}';"
        result = app._engine.connect().execute(text(select_query))
        
        if result.rowcount > 0:
            response['status'] = True
            response['message'] = "Found duplicate record"
            return response
        return response
    except Exception as e:
        print(str(e))
        return response
