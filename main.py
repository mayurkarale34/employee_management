import configparser

def integrate():
    try:
        fin = open("modules/app_init.py", "r")
        app_init = fin.read()
        fin.close()

        fin = open("modules/app_run.py", "r")
        app_run = fin.read()
        fin.close()
        


        fin = open("modules/web.py", "r")
        app_web = fin.read()
        fin.close()

        fin = open("modules/common.py", "r")
        app_common = fin.read()
        fin.close()

        fin = open("modules/employee_management/common/employee_management.py", "r")
        common_employee_management = fin.read()
        fin.close()

        fin = open("modules/employee_management/web/employee_management.py", "r")
        web_employee_management = fin.read()
        fin.close()

        fin = open("modules/attendance/common/attendance.py", "r")
        common_attendance = fin.read()
        fin.close()

        fin = open("modules/attendance/web/attendance.py", "r")
        web_attendance = fin.read()
        fin.close()
         
        fin = open("modules/overallleave_management/common/overallleave_management.py", "r")
        common_overallleave_management = fin.read()
        fin.close()

        fin = open("modules/overallleave_management/web/overallleave_management.py", "r")
        web_overallleave_management = fin.read()
        fin.close()

        fin = open("modules/leave_management/common/leave_management.py", "r")
        common_leave_management = fin.read()
        fin.close()

        fin = open("modules/leave_management/web/leave_management.py", "r")
        web_leave_management = fin.read()
        fin.close()
        combine_file_content = app_init + app_web + app_common + web_employee_management + common_employee_management + common_attendance + web_attendance +common_overallleave_management +web_overallleave_management + common_leave_management + web_leave_management+ app_run 
        
        fout = open("employee.py", "w")
        fout.write(combine_file_content)
        fout.close()


    except Exception as e:
        print(str(e))

try:
    config_object = configparser.ConfigParser()
    config_object.read('default_config.ini')
    with open('config.py', 'w') as f:
        for key in config_object['DEFAULT']:
            f.write(f"{key.upper()} = {config_object['DEFAULT'][key]}\n")
    integrate()
except Exception as e:
    print(f"Exception occured : " +str(e))
    
    
    
    

   