
# over all leave manage 
@app.route('/overallleave_management')
def overallleave_management():
    try:
        user_name = "Admin"
        return render_template('overallleave_management.html', username = user_name)
    except Exception as e:
        print("Exception in overallleave_management() : ", str(e))
        return redirect('/home')
    
