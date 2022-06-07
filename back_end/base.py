import sqlite3


def create_db():
    """
    Create database
    :return:
    """
    conn = sqlite3.connect("longrich.db")
    # create a cusor
    curs = conn.cursor()
    # create a table
    curs.execute("""CREATE TABLE if not exists my_cart(name text, image text, category text)""")
    # commit change
    conn.commit()
    # close connection
    conn.close()


def insert_data(name: str, image: str, category: str):
    conn = sqlite3.connect("longrich.db")
    # create a cusor
    curs = conn.cursor()
    # add new data
    curs.execute("INSERT INTO my_cart VALUES (:name, :image, :category)",
                 {
                     'name': name,
                     'image': image,
                     'category': category
                 })
    # commit change
    conn.commit()
    # close connection
    conn.close()


def get_all_data() -> dict:
    """
    show all data
    :return:
    """
    conn = sqlite3.connect("longrich.db")
    # create a cusor
    curs = conn.cursor()
    # get all data
    curs.execute("SELECT * FROM my_cart")
    all_data = curs.fetchall()
    # commit change
    conn.commit()
    # close connection
    conn.close()
    return all_data


def get_by_name(name) -> dict:
    """
    show all data
    :return:
    """
    conn = sqlite3.connect("longrich.db")
    # create a cusor
    curs = conn.cursor()
    # get all data
    curs.execute("SELECT * FROM my_cart WHERE name=(:name)", {'name': name})
    all_data = curs.fetchone()
    # commit change
    conn.commit()
    # close connection
    conn.close()
    return all_data


def delete_by_name(name) -> dict:
    """
    show all data
    :return:
    """
    conn = sqlite3.connect("longrich.db")
    # create a cusor
    curs = conn.cursor()
    # get all data
    curs.execute("DELETE FROM my_cart WHERE name=(:name)", {'name': name})
    # commit change
    conn.commit()
    # close connection
    conn.close()
    data = get_all_data()
    return data
