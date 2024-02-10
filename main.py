import configparser

def integrate():
    try:
        fin = open("modules/app_init.py", "r")
        app_init = fin.read()
        fin.close()

        fin = open("modules/app_run.py", "r")
        app_run = fin.read()
        fin.close()
        


        fin = open("modules/index.py", "r")
        app_index = fin.read()
        fin.close()


        combine_file_content = app_init + app_index + app_run 
        
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
    
    
    
    

   