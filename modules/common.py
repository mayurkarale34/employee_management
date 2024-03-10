
def add_metadata_info(data):
    response = {
        "status" : False,
        "message" : ""
    }
    connection = app._engine.connect()
    transaction = connection.begin()
    try:
        insert_query = text(f"insert into tb_metadata(element, type) values('{data['element']}', '{data['type']}');")
        connection.execute(insert_query)

        transaction.commit()
        connection.close()
    except Exception as e:
        print(str(e))