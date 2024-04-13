
# Manage attendance_management routes
@app.route('/attendance')
def attendance():
    try:
        employee_list = get_all_employees()['data']
        return render_template('attendance.html', employee_list = employee_list)
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
            "employee_id" : request_data['employee_id'],
            "clock_in" : datetime.strptime(request_data['clock_in_time'], '%H:%M').strftime('%H:%M:%S'),
            "attendance_date" : datetime.strptime(request_data['attendance_date'], '%Y-%M-%d').strftime('%Y-%m-%d %H:%M:%S')
        }

        duplicate_response = check_duplicate_attendance(data)
        print(duplicate_response)
        if duplicate_response['status']:
            return redirect('/attendance')
        
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
        select_query = f"Select tla.employee_id, concat(tei.first_name, ' ', if(tei.middle_name is null, '', concat(tei.middle_name, ' ')), tei.last_name) as employee_name,date_format(tla.attendance_date, '%d-%m-%Y') as attendance_date, date_format(tla.clock_in, '%H:%i:%s') as clock_in from tb_attendance tla left join tb_employee_info tei on(tla.employee_id=tei.employee_id)"
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