
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
            "employee_name" : request_data['employee_name'],
            "earn_leave" : request_data['earn_leave'],
            "casual_leave" : request_data['casual_leave'],
            "meternity_leave" : request_data['meternity_leave'],
            "peternity_leave" : request_data['peternity_leave'],
        }
        
        duplicate_response = check_duplicate_leave(data)
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
        print('Hello')
        select_query = f"Select employee_name, earn_leave, casual_leave, sick_leave, meternity_leave, peternity_leave from tb_overallleave;"
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