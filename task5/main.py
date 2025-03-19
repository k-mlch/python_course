from news_entities import News, PrivateAd, QuoteOfTheDay

class NewsFeedManager:
    def __init__(self):
        print("Welcome to the News Manager!")

    def add_news(self):
        text = input("Enter news text: ")
        city = input("Enter city: ")
        news = News(text, city)
        news.publish()

    def add_private_ad(self):
        text = input("Enter ad text: ")
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
        ad = PrivateAd(text, expiration_date)
        ad.publish()

    def add_quote(self):
        quote = input("Enter quote of the day: ")
        author = input("Enter author: ")
        quote_entry = QuoteOfTheDay(quote, author)
        quote_entry.publish()

    def run(self):
        while True:
            print("\nSelect an option:")
            print("1. Add News")
            print("2. Add Private Ad")
            print("3. Add Quote")
            print("4. Exit \n")

            option = input("Enter your option: ")

            if option == "1":
                self.add_news()
            elif option == "2":
                self.add_private_ad()
            elif option == "3":
                self.add_quote()
            elif option == "4":
                print("Exiting the News Manager.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    manager = NewsFeedManager()
    manager.run()