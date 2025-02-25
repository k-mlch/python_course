import random
import string
from pprint import pprint

#random number of dictionaries (between 2 and 10)
num_dicts = random.randint(2, 10)
print("Number of dicts", num_dicts)

#new empty list of dictionaries
list_of_dicts = []

#generating dictionaries
for dictionary in range(num_dicts):
    number_of_keys = random.randint(2, 10) #genarate random number of keys that dictionary will be between 2 to 10 for better visibility
    keys = random.sample(string.ascii_lowercase, number_of_keys) #generate random keys from letters

    random_dict = {}
    for key in keys: #for every key generate random value from 0 to 100
        random_dict[key] = random.randint(0, 100)

    #add dictionary to the list
    list_of_dicts.append(random_dict)

#print list of dictionaries
pprint(list_of_dicts)

#new empty common dictionary
common_dict = {}

dict_index = 1  #dictionary index
for random_dict in list_of_dicts:
    for key, value in random_dict.items():
        if key in common_dict:  #if key present in common dictionary already
            if value > common_dict[key][0]:  #if current value is greater than stored value in common_dict
                common_dict[key] = (value, dict_index)  #then update common_dict with new value and current dictionary index
        else:
            common_dict[key] = (value, dict_index)  #if key is not in common dictionary then we add it
    dict_index += 1  #change counter +1, since we go to the next dictionary


#final dictionary with correct key names
final_common_dict = {}
for key, (value, dict_index) in common_dict.items():
    count = 0 #count the number of dictionaries where key appears
    for dictionary in list_of_dicts:
        if key in dictionary:
            count += 1
    if count > 1: #if key appeared in multiple dictionaries then add dictionary index to the key
        final_common_dict[f"{key}_{dict_index}"] = value
    else: #if key appeared only in one dictionary the use the key as it is
        final_common_dict[key] = value


#print the final result
pprint(final_common_dict)