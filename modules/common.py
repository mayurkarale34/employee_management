
def check_duplicate_metadata(data):
    response = {
        "status" : False,
        "message" : ""
    }
    try:
        select_query = f"Select * from tb_metadata where element = '{data['element']}' and date(type) = '{data['type']}'"
        result = app._engine.connect().execute(text(select_query))
        if result.rowcount > 0:
            response['status'] = True
            response['message'] = "Found duplicate"
            return response
        return response
    except Exception as e:
        print(str(e))
        return response