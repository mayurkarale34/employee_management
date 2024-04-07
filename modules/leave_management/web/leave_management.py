
# leave management
@app.route('/leave_management')
def leave_management():
    try:
        employee_list = get_all_employees()['data']
        return render_template('leave_management.html', employee_list = employee_list)
    except Exception as e:
        print("Exception in leave_management() : ", str(e))
        return redirect('/home')
    
     
    # add leave
@app.route('/apply_for_leave', methods=['POST'])
def apply_for_leave():
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        request_data = dict(request.form)
        data = {
            "employee_id" : request_data['employee_id'],
            "leave_type" : request_data['leave_type'],
            "from_date" : request_data['from_date'],
            "to_date" : request_data['to_date'],
            "status" : "New",
            "applied_by" : session['logged_user_name'],
            "applied_on" : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        duplicate_response = check_duplicate_leave(data)
        print(duplicate_response)
        if duplicate_response['status']:
            return redirect('/leave_management')
        
        apply_leave_response = add_to_database(data, "tb_leave_applications", connection)
        transaction.commit()
        connection.close()
        return redirect('/leave_management')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/leave_management')

@app.route('/retrive_leave_applications', methods=['GET'])
def retrive_leave_applications():
    response = {
        "rows" : [],
        "total" : 0,
        "message" : ""
    }
    try:
        select_query = f"Select tla.employee_id, concat(tei.first_name, ' ', if(tei.middle_name is null, '', concat(tei.middle_name, ' ')), tei.last_name) as employee_name, tla.leave_type, date_format(tla.from_date, '%d-%m-%Y') as from_date, date_format(tla.to_date, '%d-%m-%Y') as to_date, status, tla.applied_by, date_format(tla.applied_on, '%d-%m-%Y %H:%i:%s') as applied_on from tb_leave_applications tla left join tb_employee_info tei on(tla.employee_id=tei.employee_id)"
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