import random
import string
from pprint import pprint


def generate_random_dicts():
    list_of_dicts = []
    num_dicts = random.randint(2, 10)
    print("Number of dicts", num_dicts)

    for dictionary in range(num_dicts):
        number_of_keys = random.randint(2,10)
        keys = random.sample(string.ascii_lowercase, number_of_keys)  #generate random keys from letters

        random_dict = {}
        for key in keys:  #for every key generate random value from 0 to 100
            random_dict[key] = random.randint(0, 100)

        list_of_dicts.append(random_dict)
    return list_of_dicts


def collect_data_about_values(list_of_dicts):
    common_dict = {} #the maximum value and the dictionary index where it was found
    key_count = {}  #how many times a key appears across all dictionaries
    dict_index = 1

    for random_dict in list_of_dicts:
        for key, value in random_dict.items():
            if key in common_dict:
                if value > common_dict[key][0]:
                    common_dict[key] = (value, dict_index)
            else:
                common_dict[key] = (value, dict_index)

            if key in key_count:
                key_count[key] += 1
            else:
                key_count[key] = 1

        dict_index += 1

    return common_dict, key_count


def generate_final_dictionary(common_dict, key_count):
    final_common_dict = {}

    for key, (value, dict_index) in common_dict.items():
        if key_count[key] > 1:
            final_common_dict[f"{key}_{dict_index}"] = value
        else:
            final_common_dict[key] = value
    return final_common_dict


list_of_dicts = generate_random_dicts()
print("Original dict: ")
pprint(list_of_dicts)

data_about_values = collect_data_about_values(list_of_dicts)
common_dict = data_about_values[0]
key_count = data_about_values[1]
final_dict = generate_final_dictionary(common_dict, key_count)

print("Generated final dict:")
pprint(final_dict)