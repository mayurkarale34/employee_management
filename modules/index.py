
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
    
@app.route('/empmanagement')
def empmanagement():
    return render_template('empmanagement.html')