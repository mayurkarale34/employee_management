
# Manage employee routes
@app.route('/employee_management')
def manage_employee():
    try:
        user_name = "Admin"
        return render_template('manage_employee.html', username = user_name)
    except Exception as e:
        print("Exception in employee_management() : ", str(e))
        return redirect('/home')
    
# add employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        request_data = dict(request.form)
        

        data = {
            "employee_id" : request_data['employee_id'],
            "first_name" : request_data['fname'],
            "middle_name" : request_data['mname'],
            "last_name" : request_data['lname'],
            "mobile_number" : request_data['mobile_no'],
            "address" : request_data['address'],
            "date_of_birth" : request_data['dob'],
            "blood_group" : request_data['bloodgroup'],
            "gender" : request_data['gender'],
            "marital_status" : request_data['marital_status'],
            "highest_qualification_specialization" : request_data['qualification'],
            "percentage_cgpa" : request_data['percentage'],
            "year_of_passing" : request_data['yop'],
            "email" : request_data['email_id'],
            "date_of_joining" : request_data['doj'],
            "department" : request_data['department'],
            "job_title" : request_data['job_title'],
            "employment_type" : request_data['employment_type'],
            "employment_status" : request_data['status'],
            "salary" : request_data['salary'],
            "areas_for_improvement" : request_data['afi'],
            "achievements" : request_data['achievements'],
            "workshop_attended" : request_data['workshop'],
            "certifications" : request_data['certifications'],
            "skills_acquired" : request_data['skills']
            
        }
        
        add_employee_response = add_to_database(data, "tb_employee_info", connection)
        transaction.commit()
        connection.close()
        return redirect('/employee_management')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/employee_management')
    