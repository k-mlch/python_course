import csv
import re


class LetterCounter:
    @staticmethod
    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r"[^a-z]", " ", text)
        return text

    @staticmethod
    def count_letters(text):
        letter_counts = {}
        for letter in text:
            if letter.isalpha():
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
        return letter_counts

    @staticmethod
    def count_uppercase(text):
        uppercase_counts = {}
        for letter in text:
            if letter.isupper():
                uppercase_counts[letter] = uppercase_counts.get(letter, 0) + 1
        return uppercase_counts

    @staticmethod
    def save_to_csv(letter_counts, uppercase_counts, total_letters, filename="letter_count.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])

            for letter in letter_counts:
                count_all = letter_counts.get(letter, 0)
                count_uppercase = uppercase_counts.get(letter.upper(), 0)
                percentage = (count_all / total_letters) * 100 if total_letters > 0 else 0
                writer.writerow([letter, count_all, count_uppercase, f"{percentage:.2f}"])

    @staticmethod
    def process_file(input_filename="news.txt", output_filename="letter_count.csv"):
        try:
            with open(input_filename, "r", encoding="utf-8") as file:
                text = file.read()

            uppercase_counts = LetterCounter.count_uppercase(text)

            text = LetterCounter.preprocess_text(text)
            letter_counts = LetterCounter.count_letters(text)
            total_letters = sum(letter_counts.values())

            LetterCounter.save_to_csv(letter_counts, uppercase_counts, total_letters, output_filename)
            print(f"Letter count CSV updated: {output_filename}")
        except Exception as e:
            print(f"Error processing file: {e}")


if __name__ == "__main__":
    LetterCounter.process_file()
