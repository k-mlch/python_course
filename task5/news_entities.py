from datetime import datetime
import random

class News:
    def __init__(self, news_text, city):
        self.news_text = news_text
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def publish(self):
        with open("news.txt", "a", encoding="utf-8") as file:
            file.write(f"News:\n{self.news_text}\n\n{self.city}, {self.date}\n\n{'-'*40}\n\n")
        print("Completed. News added to the output file.")

class PrivateAd:
    def __init__(self, ad_text, expiration_date):
        self.ad_text = ad_text
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.current_date = datetime.now()

    def calculate_days_left(self):
        if self.expiration_date < self.current_date:
            return 'Expired :('
        return (self.expiration_date - self.current_date).days

    def publish(self):
        with open("news.txt", "a", encoding="utf-8") as file:
            file.write(
                f"Private Ad:\n{self.ad_text}\n\nExpires on: {self.expiration_date.strftime('%Y-%m-%d')}\nDays left: {self.calculate_days_left()}\n\n{'-' * 40}\n\n")
        print("Completed. Ad published.")

class QuoteOfTheDay:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def generate_rating (self):
        return random.randint(1, 10)

    def publish(self):
        with open("news.txt", "a", encoding="utf-8") as file:
            file.write(f"Motivational Quote:\n'{self.quote}'\n\nAuthor: {self.author}\n\nRating: {self.generate_rating()}/10\n\n{'-'*40}\n\n")
        print("Completed. Quote of the day published.")