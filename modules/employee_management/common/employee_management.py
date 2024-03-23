
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