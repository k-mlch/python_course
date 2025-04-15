import sqlite3

class DatabaseManager:
    def __init__(self, db_name="news_feed.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def insert_news(self, news_text, city, date):
        #add news record, checking for duplicates
        try:
            self.cursor.execute("INSERT INTO News (news_text, city, date) VALUES (?, ?, ?)",
                                (news_text, city, date))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Duplicate news record found, skipping insertion.")

    def insert_ad(self, ad_text, expiration_date, current_date):
        #add adds record, checking for duplicates
        try:
            self.cursor.execute("INSERT INTO PrivateAd (ad_text, expiration_date, current_date) VALUES (?, ?, ?)",
                                (ad_text, expiration_date, current_date))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Duplicate ad record found, skipping insertion.")

    def insert_quote(self, quote, author, rating):
        #add quotes record, checking for duplicates
        try:
            self.cursor.execute("INSERT INTO QuoteOfTheDay (quote, author, rating) VALUES (?, ?, ?)",
                                (quote, author, rating))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Duplicate quote record found, skipping insertion.")

    def _create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS News (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_text TEXT,
            city TEXT,
            date TEXT,
            UNIQUE(news_text, city, date)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS PrivateAd (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad_text TEXT,
            expiration_date TEXT,
            current_date TEXT,
            UNIQUE(ad_text, expiration_date)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS QuoteOfTheDay (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT,
            author TEXT,
            rating INTEGER,
            UNIQUE(quote, author)
        )
        """)

    def __enter__(self):
        self.connect()
        self._create_tables()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Error occurred: {exc_type} - {exc_val}")
        self.close()
