
# Common function to generate employee id
def generate_employee_id(first_name, last_name):
    # Extracting first character of first_name and last_name
    first_char_first_name = first_name[0].upper()
    first_char_last_name = last_name[0].upper()
    
    # Generating two random characters
    random_chars = ''.join(random.choices(string.ascii_letters, k=2)).upper()
    
    # Generating four random digits
    random_digits = ''.join(random.choices(string.digits, k=4))
    
    # Constructing the employee ID
    employee_id = f"{first_char_first_name}{first_char_last_name}{random_chars}{random_digits}"
    
    return employee_id

# Get all employee  
def get_all_employees():
    response = {
        "data" : [],
        "message" : ""
    }
    try:
        select_query = f"Select employee_id, concat(first_name, ' ', if(middle_name is null, '', concat(middle_name, ' ')), last_name) as employee_name from tb_employee_info where employment_status = 'Active';"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount:
            columns = result.keys()
            for row in result:
                row_dict = dict(zip(columns, row))
                response['data'].append(row_dict)
            
        return response
    except Exception as e:
        print(str(e))
        return response
    
def check_duplicate_record(data):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        select_query = f"Select * from tb_employee_info where mobile_number = '{data['mobile_number']}'"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount > 0:
            response['status'] = True
            response['message'] = "Record already added ..."
            return response
        return response
    except Exception as e:
        print(str(e))
        return response