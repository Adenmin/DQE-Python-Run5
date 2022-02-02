import random
import string

# Part 1
# Create list if random number of dicts.
random_dict = dict()
random_list = []
for i in range(random.randint(2, 10)):
    for j in range(random.randint(0, 10)):
        random_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 1000)
    random_list.append(random_dict.copy())
    random_dict.clear()

# Part 2
# Collect values by key from all dictionaries.
aggr_dict = dict()
for dic in random_list:
    for key in dic.keys():
        if key not in aggr_dict.keys():
            aggr_dict[key] = [dic[key]]
        else:
            aggr_dict[key].append(dic[key])

# Find max value for each key.
max_val_dict = dict.fromkeys(aggr_dict)
for key in aggr_dict:
    max_val_dict[key] = max(aggr_dict[key])

# Find index of dictionary where key:max(value) exist and rename key if key is not unique.
final_dict = max_val_dict.copy()
for key in max_val_dict:
    for dct in random_list:
        if key in dct.keys():
            if max_val_dict[key] == dct[key] and len(aggr_dict[key]) != 1:
                new_key = key + '_' + str(random_list.index(dct) + 1)
                final_dict[new_key] = final_dict.pop(key)

print(final_dict)
