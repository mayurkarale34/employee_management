
# over all leave manage 
@app.route('/overallleave_management')
def overallleave_management():
    try:
        user_name = "Admin"
        return render_template('overallleave_management.html', username = user_name)
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
        data = {
            "employee_name" : request_data['employee_name'],
            "earn_leave" : request_data['earn_leave'],
            "casual_leave" : request_data['casual_leave'],
            "meternity_leave" : request_data['maternity_leave'],
            "peternity_leave" : request_data['paternity_leave'],
           
        }
        
        add_metadata_response = add_to_database(data, "tb_overallleave", connection)
        transaction.commit()
        connection.close()
        return redirect('/overallleave_management')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/overallleave_management')