
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    session.clear()
    with app.app_context():
        cache.clear()
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
        session['greatings'] = set_greetings()
        session['logged_user_name'] = 'Admin'
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

@app.route('/add_metadata', methods=['POST'])
def add_metadata():
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        request_data = dict(request.form)
        print(request_data)
        add_metadata_response = add_to_database(request_data, "tb_metadata", connection)
        transaction.commit()
        connection.close()
        return redirect('/manage_metadata')
    except Exception as e:
        transaction.rollback()
        connection.close()
        print(str(e))
        return redirect('/manage_metadata')
    
@app.route('/retrive_metadata', methods=['GET'])
def retrive_metadata():
    response = {
        "rows" : [],
        "total" : 0,
        "message" : ""
    }
    try:
        print('Hello')
        select_query = f"Select * from tb_metadata"
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