
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/validate_login', methods = ['POST'])
def validate_login():
    data = dict(request.form)
    user_name = data['username']
    password = data['password']
    if user_name.upper() == 'ADMIN' and password.upper()=='ADMIN':
        return jsonify({"status" : True})
    else:
        return jsonify({"status" : False})