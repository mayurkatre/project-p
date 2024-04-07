import sqlite3
import string
import random

# Function to generate a random alphanumeric code for short URL
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to create a SQLite database and table if they don't exist
def create_database():
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_code TEXT)''')
    conn.commit()
    conn.close()

# Function to shorten a URL and store it in the database
def shorten_url(original_url):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()

    # Check if the URL already exists in the database
    c.execute("SELECT short_code FROM urls WHERE original_url=?", (original_url,))
    row = c.fetchone()
    if row:
        conn.close()
        return row[0]

    # Generate a unique short code
    short_code = generate_short_code()

    # Insert the URL and short code into the database
    c.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
    conn.commit()
    conn.close()

    return short_code

# Function to retrieve the original URL from the short code
def get_original_url(short_code):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()

    c.execute("SELECT original_url FROM urls WHERE short_code=?", (short_code,))
    row = c.fetchone()
    conn.close()

    if row:
        return row[0]
    else:
        return None

# Example usage
if __name__ == "__main__":
    create_database()

    original_url = input("Enter the URL to shorten: ")
    short_code = shorten_url(original_url)
    print("Shortened URL:", f"example.com/{short_code}")

    # Retrieving original URL
    short_code = input("Enter the short code: ")
    original_url = get_original_url(short_code)
    if original_url:
        print("Original URL:", original_url)
    else:
        print("URL not found")
