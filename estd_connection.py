def estd_connection():

    import psycopg2
    conn = psycopg2.connect(
        database="final_project",
        user="postgres",
        password="134679",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully!")
    cursor = conn.cursor()
    return cursor
