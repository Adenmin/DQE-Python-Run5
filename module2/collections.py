import random
import string

# Part 1
# Create list if random number of dicts.
random_list = [{random.choice(string.ascii_lowercase): random.randint(0, 1000) for i in range(
    random.randint(0, len(string.ascii_lowercase)))} for j in range(random.randint(2, 10))]

# Part 2
# Collect values by key from all dictionaries.
aggr_dict = dict()
for dic in random_list:
    for k, v in dic.items():
        if k not in aggr_dict.keys():
            aggr_dict[k] = [v]
        else:
            aggr_dict[k].append(v)

# Find index of dictionary where key:max(value) exist and rename key if key is not unique.
final_dict = dict.fromkeys(aggr_dict)
for key in aggr_dict.keys():
    final_dict[key] = max(aggr_dict[key])
    for dct in random_list:
        if key in dct.keys() and key in final_dict.keys():
            if max(aggr_dict[key]) == dct[key] and len(aggr_dict[key]) != 1:
                new_key = key + '_' + str(random_list.index(dct) + 1)
                final_dict[new_key] = final_dict.pop(key)

print(final_dict)
