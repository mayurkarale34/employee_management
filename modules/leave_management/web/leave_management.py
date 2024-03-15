
# leave management
@app.route('/leave_management')
def leave_management():
    try:
        user_name = "Admin"
        return render_template('leave_management.html', username = user_name)
    except Exception as e:
        print("Exception in leave_management() : ", str(e))
        return redirect('/home')