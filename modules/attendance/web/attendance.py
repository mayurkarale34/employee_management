
# Manage attendance_management routes
@app.route('/attendance')
def attendance():
    try:
        user_name = "Admin"
        return render_template('attendance.html', username = user_name)
    except Exception as e:
        print("Exception in attendance() : ", str(e))
        return redirect('/home')
    
# add attendance
@app.route('/add_attendance', methods=['POST'])
def add_attendance():
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        request_data = dict(request.form)
        # Getting the current date and time
        # current_datetime = datetime.now()

        data = {
            "employee_name" : request_data['employee_name'],
            "clock_in" : datetime.strptime(request_data['clock_in_time'], '%H:%M').strftime('%H:%M:%S'),
            "attendance_date" : datetime.strptime(request_data['attendance_date'], '%Y-%M-%d').strftime('%Y-%m-%d %H:%M:%S')
        }
        
        add_attendance_response = add_to_database(data, "tb_attendance", connection)
        transaction.commit()
        connection.close()
        return redirect('/attendance')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/attendance')
    
      
@app.route('/retrive_attendance', methods=['GET'])
def retrive_attendance():
    response = {
        "rows" : [],
        "total" : 0,
        "message" : ""
    }
    try:
        print('Hello')
        select_query = f"Select * from tb_attendance"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount:
            columns = result.keys()
            for row in result:
                row_dict = dict(zip(columns, row))
                response['rows'].append(row_dict)
            
            response['total'] = len(response['rows'])
        return jsonify(response)
    except Exception as e:
        print(str(e))
        return jsonify(response)