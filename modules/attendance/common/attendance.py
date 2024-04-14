
def check_duplicate_attendance(data):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        select_query = f"Select * from tb_attendance where employee_id = '{data['employee_id']}' and date(attendance_date) = '{data['attendance_date']}'"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount > 0:
            response['status'] = True
            response['message'] = "Attendance already marked ..."
            return response
        return response
    except Exception as e:
        print(str(e))
        return response