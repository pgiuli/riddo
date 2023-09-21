#Yes, i know a utils file is not always the best, but cPanel has a great way of running this.

def create_db():
    import sqlite3

    # Create a connection to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("links.db")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table if it doesn't exist to store the redirects
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS redirects (
            CODE TEXT PRIMARY KEY,
            URL TEXT
        )
    """)
    
    # Commit the changes and close the connection when done
    conn.commit()
    conn.close()

#create_db()