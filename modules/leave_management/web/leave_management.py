
# leave management
@app.route('/leave_management')
def leave_management():
    try:
        return render_template('leave_management.html')
    except Exception as e:
        print("Exception in leave_management() : ", str(e))
        return redirect('/home')
    
     
    # add leave
@app.route('/add_leave_management', methods=['POST'])
def add_leave_managenent():
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        request_data = dict(request.form)
        data = {
            "leave_type" : request_data['leave_type'],
            "start_date" : request_data['start_date'],
            "end_date" : request_data['end_date'],
            "duration" : request_data['duration'],
            "leave_status" : request_data['leave_status'],
           
        }
        
        add_metadata_response = add_to_database(data, "tb_leave", connection)
        transaction.commit()
        connection.close()
        return redirect('/leave_management')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/leave_management')