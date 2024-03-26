
# leave management
@app.route('/leave_management')
def leave_management():
    try:
        return render_template('leave_management.html')
    except Exception as e:
        print("Exception in leave_management() : ", str(e))
        return redirect('/home')