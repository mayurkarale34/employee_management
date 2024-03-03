
# Manage employee routes
@app.route('/manage_employee')
def manage_employee():
    try:
        user_name = "Admin"
        return render_template('manage_employee.html', username = user_name)
    except Exception as e:
        print("Exception in manage_employee() : ", str(e))
        return redirect('/home')