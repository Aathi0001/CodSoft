import sqlite3
from sqlite3 import Error

# Function to create tables
def create_tables(connection):
    try:
        cursor = connection.cursor()

        # Create the "TechReviews" table
        create_tech_reviews_table = """
        CREATE TABLE TechReviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image BLOB NOT NULL,
            description TEXT NOT NULL
        );
        """
        cursor.execute(create_tech_reviews_table)

        # Create the "Comment" table with a foreign key reference to "TechReviews"
        create_comment_table = """
        CREATE TABLE Comment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            place_id INTEGER,
            FOREIGN KEY (place_id) REFERENCES TechReviews(id)
        );
        """
        cursor.execute(create_comment_table)

        # Create the "messages" table
        create_messages_table = """
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        );
        """
        cursor.execute(create_messages_table)

        connection.commit()

    except Error as e:
        print(f"Error: {e}")

# Connect to the SQLite database
try:
    connection = sqlite3.connect('tech_reviews.db')  # Creates or connects to an SQLite database

    create_tables(connection)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection:
        connection.close()
