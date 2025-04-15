import os
import json
import task4_3
from news_entities import News, PrivateAd, QuoteOfTheDay
from database_manager import DatabaseManager


class JSONFileProcessor:
    def __init__(self, file_path="new_records.json"):
        self.file_path = file_path

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' not found.")
            return

        db = DatabaseManager()

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.process_record(data, db)
            elif isinstance(data, list):
                for record in data:
                    self.process_record(record, db)
            else:
                print(f"Invalid JSON structure in file: {self.file_path}")
                return

            os.remove(self.file_path)
            print(f"Successfully processed and removed '{self.file_path}'.")

        except Exception as e:
            print(f"Error occurred while processing the JSON file: {e}")

        finally:
            db.close()

    def process_record(self, record, db):
        record_type = record.get("type")
        text = record.get("text")
        additional = record.get("additional")

        if not all([record_type, text, additional]):
            print(f"Incomplete record: {record}")
            return

        text_normalized = task4_3.normalize_text(text)

        if record_type == "News":
            news = News(text_normalized, additional.strip())
            news.publish(db)

        elif record_type == "PrivateAd":
            ad = PrivateAd(text_normalized, additional.strip())
            ad.publish(db)

        elif record_type == "MotivationalQuote":
            quote = QuoteOfTheDay(text_normalized, additional.strip())
            quote.publish(db)

        else:
            print(f"Unknown record type: {record_type}")


if __name__ == "__main__":
    processor = JSONFileProcessor()
    processor.process_file()
