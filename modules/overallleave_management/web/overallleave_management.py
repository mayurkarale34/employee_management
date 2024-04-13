
# overall leave manage 
@app.route('/overallleave_management')
def overallleave_management():
    try:
        employee_list = get_all_employees()['data']
        return render_template('overallleave_management.html', employee_list = employee_list)
    except Exception as e:
        print("Exception in overallleave_management() : ", str(e))
        return redirect('/home')
    
# add overall leave
@app.route('/add_overallleave_managenent', methods=['POST'])
def add_overallleave_managenent():
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        request_data = dict(request.form)
        # Getting the current date and time
        # current_datetime = datetime.now()

        data = {
            "employee_id" : request_data['employee_id'],
            "earn_leave" : request_data['earn_leave'],
            "casual_leave" : request_data['casual_leave'],
            "meternity_leave" : request_data['meternity_leave'],
            "peternity_leave" : request_data['peternity_leave'],
        }
        
        duplicate_response = check_duplicate_overall_leave_master(data)
        print(duplicate_response)
        if duplicate_response['status']:
            return redirect('/overallleave_management')
        
        add_metadata_response = add_to_database(data, "tb_overallleave", connection)
        transaction.commit()
        connection.close()
        return redirect('/overallleave_management')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/overallleave_management')
    
@app.route('/retrive_overallleave_management', methods=['GET'])
def retrive_overallleave_management():
    response = {
        "rows" : [],
        "total" : 0,
        "message" : ""
    }
    try:

        select_query = f"Select tol.employee_id, concat(tei.first_name, ' ', if(tei.middle_name is null, '', concat(tei.middle_name, ' ')), tei.last_name) as employee_name, tol.earn_leave, tol.casual_leave, tol.sick_leave, tol.meternity_leave, tol.peternity_leave from tb_overallleave tol left join tb_employee_info tei on(tei.employee_id = tol.employee_id) order by tol.id desc;"
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