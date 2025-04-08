import csv
import re

class WordCounter:
    @staticmethod
    def preprocess_text(text):
        # Convert text to lowercase
        text = text.lower()

        text = re.sub(r"^['‘’\"“]+|['‘’\"”]+$", "", text) #Remove single and double quotes around words or entire phrases
        text = re.sub(r"['‘’\"“]+(.*?)['‘’\"”]+", r"\1", text)  #Remove quotes from the start and end of the quote
        text = re.sub(r"[^a-z\s'-]", "", text)  #Keep letters, spaces, apostrophes, and hyphens
        text = re.sub(r"-+", " ", text)  #Remove lines of dashes

        return text

    @staticmethod
    def count_words(text):
        word_counts = {}
        words = text.split()
        for word in words:
            if word:
                word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    @staticmethod
    def save_to_csv(word_counts, filename="word_count.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for word, count in word_counts.items():
                writer.writerow([f"{word}-{count}"])

    @staticmethod
    def process_file(input_filename="news.txt", output_filename="word_count.csv"):
        try:
            with open(input_filename, "r", encoding="utf-8") as file:
                text = file.read()

            with open(output_filename, "w", newline="", encoding="utf-8") as file:
                pass

            processed_text = WordCounter.preprocess_text(text)
            word_counts = WordCounter.count_words(processed_text)
            WordCounter.save_to_csv(word_counts, output_filename)
            print(f"Word count CSV updated: {output_filename}")
        except Exception as e:
            print(f"Error processing file: {e}")

if __name__ == "__main__":
    WordCounter.process_file()
