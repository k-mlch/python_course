import os
import xml.etree.ElementTree as ET
from news_entities import News, PrivateAd, QuoteOfTheDay
from task4_3 import normalize_text
from database_manager import DatabaseManager


class XMLFileProcessor:
    def __init__(self, file_path="new_records.xml"):
        self.file_path = file_path

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"XML file '{self.file_path}' not found.")
            return

        db = DatabaseManager()

        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()

            for record in root.findall("record"):
                self.process_record(record, db)

            os.remove(self.file_path)
            print(f"Successfully processed and removed '{self.file_path}'.")

        except Exception as e:
            print(f"Error processing XML file: {e}")

        finally:
            db.close()

    def process_record(self, record, db):
        record_type = record.find("type").text
        text = normalize_text(record.find("text").text or "")
        additional = record.find("additional").text or ""

        if record_type == "News":
            news = News(text, additional)
            news.publish(db)

        elif record_type == "PrivateAd":
            ad = PrivateAd(text, additional)
            ad.publish(db)

        elif record_type == "MotivationalQuote":
            quote = QuoteOfTheDay(text, additional)
            quote.publish(db)

        else:
            print(f"Unknown record type in XML: {record_type}")


if __name__ == "__main__":
    processor = XMLFileProcessor()
    processor.process_file()
