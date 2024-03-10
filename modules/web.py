
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    user_name = "Admin"
    return render_template('home.html', username = user_name)


@app.route('/validate_login', methods = ['POST'])
def validate_login():
    data = dict(request.form)
    user_name = data['username']
    password = data['password']
    if user_name.upper() == 'ADMIN' and password.upper()=='ADMIN':
        return jsonify({"status" : True})
    else:
        return jsonify({"status" : False})
    
@app.route('/manage_metadata')
def metadata():
    user_name = "Admin"
    return render_template('metadata.html', username = user_name)

@app.route('/manage_reports')
def reports():
    user_name = "Admin"
    return render_template('reports.html', username = user_name)

@app.route('/add_employee')
def add_employee():
    user_name = "Admin"
    return render_template('add_employee.html', username = user_name)

@app.route('/add_metadata', methods=['POST'])
def add_metadata():
    try:
        request_data = dict(request.form)
        print(request_data)
        add_metadata_response = add_metadata_info(request_data)
        
        return redirect('/manage_metadata')
    except Exception as e:
        print(str(e))
        return redirect('/manage_metadata')