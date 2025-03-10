import task4_2
import task4_3
from pprint import pprint


def main():
    print("Task2:")
    print("Generate random dictionaries:")
    list_of_dicts = task4_2.generate_random_dicts()
    pprint(list_of_dicts)

    data_about_values = task4_2.collect_data_about_values(list_of_dicts)
    common_dict = data_about_values[0]
    key_count = data_about_values[1]
    final_dict = task4_2.generate_final_dictionary(common_dict, key_count)

    print("\nGenerated final dict:")
    pprint(final_dict)

    print("\nTask3:")
    task4_3.generate_final_text()

if __name__ == "__main__":
    main()