
# Manage attendance_management routes
@app.route('/Attendance_management')
def Attendance_management():
    try:
        user_name = "Admin"
        return render_template('Attendance_management.html', username = user_name)
    except Exception as e:
        print("Exception in Attendance_management() : ", str(e))
        return redirect('/home')