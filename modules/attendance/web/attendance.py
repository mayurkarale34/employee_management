
# Manage attendance_management routes
@app.route('/attendance')
def attendance():
    try:
        user_name = "Admin"
        return render_template('attendance.html', username = user_name)
    except Exception as e:
        print("Exception in attendance() : ", str(e))
        return redirect('/home')