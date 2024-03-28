
# Manage employee routes
@app.route('/employee_management')
def manage_employee():
    try:
        cities = retrive_metadata_by_type('City')['data']
        departments = retrive_metadata_by_type('Department')['data']
        role = retrive_metadata_by_type('Role')['data']
        bloodgroup = retrive_metadata_by_type('BloodGroup')['data']
        return render_template('manage_employee.html', cities = cities, departments = departments, role = role, bloodgroup = bloodgroup)
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
            "employee_id" : generate_employee_id(request_data['fname'], request_data['lname']),
            "first_name" : request_data['fname'],
            "middle_name" : request_data['mname'],
            "last_name" : request_data['lname'],
            "mobile_number" : request_data['mobile_no'],
            "city" : request_data['city'],
            "date_of_birth" : '2023-03-23', #request_data['dob']
            "blood_group" : request_data['bloodgroup'],
            "gender" : request_data['gender'],
            "marital_status" : request_data['marital_status'],
            "highest_qualification_specialization" : request_data['qualification'],
            "percentage_cgpa" : request_data['percentage'],
            "year_of_passing" : request_data['yop'],
            "email" : request_data['email_id'],
            "date_of_joining" : '2023-03-23', #request_data['doj']
            "department" : request_data['department'],
            "job_title" : request_data['job_title'],
            "employment_type" : request_data['employment_type'],
            "employment_status" : "Active",
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
    

@app.route('/retrive_user_details', methods=['GET'])
def retrive_user_details():
    response = {
        "rows" : [],
        "total" : 0,
        "message" : ""
    }
    try:
        select_query = f"Select id, employee_id, first_name, middle_name, last_name, mobile_number, address, date_of_birth, blood_group, gender, marital_status, highest_qualification_specialization, percentage_cgpa, year_of_passing, email, city, date_of_joining, department, job_title, employment_type, employment_status, salary, areas_for_improvement, achievements, workshop_attended, certifications, skills_acquired from tb_employee_info;"
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