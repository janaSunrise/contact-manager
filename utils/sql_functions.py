import sqlite3


# Initialize the connection.
conn = sqlite3.connect("utils/contacts.db")

# Create the cursor for executing SQL commands.
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id integer PRIMARY KEY,
    name text NOT NULL,
    phone integer NOT NULL,
    address text,
    email text
)
""")


# Define the utility functions for SQL Queries
def insert_data(name: str, phone: int, address: str = None, email: str = None) -> None:
    sql = """
    INSERT INTO contacts(name, phone, address, email) values(?,?,?,?)
    """
    cur.execute(sql, (name, phone, address, email))
    conn.commit()


def update_data(id: int, name: str, phone: int, address: str = None, email: str = None) -> None:
    sql = ''' UPDATE contacts
              SET name = ?,
                  phone = ?,
                  address = ?,
                  email = ?
              WHERE id = ?'''
    cur.execute(sql, (name, phone, address, email, id))
    conn.commit()


def get_data(type=None, data=None) -> list:
    if type is None and data is None:
        sql = "SELECT * FROM contacts"
        cur.execute(sql)
        rows = cur.fetchall()

    else:
        if type == "name":
            sql = "SELECT * FROM contacts where name = ?"
            cur.execute(sql, (data,))

        elif type == "phone":
            sql = "SELECT * FROM contacts where phone = ?"
            cur.execute(sql, (data,))

        elif type == "address":
            sql = "SELECT * FROM contacts where address = ?"
            cur.execute(sql, (data,))

        elif type == "email":
            sql = "SELECT * FROM contacts where email = ?"
            cur.execute(sql, (data,))

        elif type == "id":
            sql = "SELECT * FROM contacts where id = ?"
            cur.execute(sql, (data,))

        rows = cur.fetchall()

    return rows


def delete_data(id) -> None:
    if id is None:
        sql = "DELETE FROM contacts"
        cur.execute(sql)
        conn.commit()
    else:
        sql = 'DELETE FROM contacts WHERE id=?'
        cur.execute(sql, (id,))
        conn.commit()
