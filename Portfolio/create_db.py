import sqlite3

def create_table():
    conn = sqlite3.connect('contact_form.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact_form_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
