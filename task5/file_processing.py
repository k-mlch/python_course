import os
import task4_3
from news_entities import News, PrivateAd, QuoteOfTheDay
from database_manager import DatabaseManager

class FileProcessor:
    def __init__(self, file_path="new_records.txt"):
        self.file_path = file_path

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' not found.")
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            with DatabaseManager() as db:
                for line in lines:
                    self.process_line(line.strip(), db)

            os.remove(self.file_path)  #delete the file after processing
            print(f"Successfully processed and removed '{self.file_path}'.")

        except Exception as e:
            print(f"Error occurred while processing the file: {e}")

    def process_line(self, line, db):
        if not line:
            return  #skip empty lines

        parts = line.split(" | ")
        if len(parts) != 2:
            print(f"Incorrect format in line: {line}")
            return

        record_type, extra_data = parts
        text = record_type.split(":")[1].strip()  #Get the text after the colon
        text_normalized = task4_3.normalize_text(text) #Text normalization from Homework 4

        if record_type.startswith("News"):
            city = extra_data.strip()
            news = News(text_normalized, city)
            news.publish(db)

        elif record_type.startswith("PrivateAd"):
            expiration_date = extra_data.strip()
            ad = PrivateAd(text_normalized, expiration_date)
            ad.publish(db)

        elif record_type.startswith("MotivationalQuote"):
            author = extra_data.strip()
            quote = QuoteOfTheDay(text_normalized, author)
            quote.publish(db)

        else:
            print(f"Unknown record type: {record_type}")
