import sqlite3
import string
import random

#TODO: check url validity

def generate_random_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def shorten_url(url, code=None):
    # Generate a unique random code
    if code == None:
        code = generate_random_code()
    
    # Insert the URL and its associated code into the database
    conn = sqlite3.connect("links.db")
    cursor = conn.cursor()
    
    for i in range(3):
        try:
           cursor.execute("INSERT INTO redirects (CODE, URL) VALUES (?, ?)", (code, url))
           conn.commit()
        except sqlite3.IntegrityError:
            if __name__ == "__main__":
                break
            else:
                code = generate_random_code()
        else:
            break
    
    conn.close()
    
    return code


def retrieve_url(code):
    conn = sqlite3.connect("links.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT URL FROM redirects WHERE CODE=?", (code,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    else:
        return None


def delete_entry(code):
    conn = sqlite3.connect("links.db")
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM redirects WHERE CODE=?", (code,))
        conn.commit()
        deleted_count = cursor.rowcount
    except sqlite3.IntegrityError:
        deleted_count = 0

    conn.close()

    return deleted_count


def list_all_codes():
    conn = sqlite3.connect("links.db")
    cursor = conn.cursor()

    cursor.execute("SELECT CODE FROM redirects")
    codes = [row[0] for row in cursor.fetchall()]

    conn.close()

    return codes


if __name__ == "__main__":
    import sys
    print(len(sys.argv))
    # Check if the command line argument is provided
    if len(sys.argv) >2:

        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1, arg2)
        shorten_url(arg2, arg1)


#for i in list_all_codes():
#    delete_entry(i)

#shorten_url("https://github.com/pgiuli","github")
#shorten_url("https://instagram.com/pxxgl","instagram")
#shorten_url("https://blog.giuli.cat","blog")