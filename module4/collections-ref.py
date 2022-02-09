import random
import string


# Generate list if random number of dicts. Return: List of dicts.
def generate_random_list_of_dicts(number_of_dicts=10, dicts_values=100):
    if number_of_dicts < 2:
        print("Number of dicts must be equal or more than 2 !!! Used default value 10.")
        number_of_dicts = 10
    return [{random.choice(string.ascii_lowercase): random.randint(0, dicts_values) for _ in range(
        random.randint(0, len(string.ascii_lowercase)))} for _ in range(random.randint(2, number_of_dicts))]


# Aggregate values by key from all dictionaries in list. Return: Dict.
def aggregate_values_by_key(list_of_dicts):
    aggr_dict = dict()
    for dic in list_of_dicts:
        for k, v in dic.items():
            if k not in aggr_dict.keys():
                aggr_dict[k] = [v]
            else:
                aggr_dict[k].append(v)
    return aggr_dict


# Build dictionary where key:max(value) exist and rename key if key is not unique. Return: Dict.
def build_dict(list_of_dicts):
    aggr_dict = aggregate_values_by_key(list_of_dicts)
    dct = dict.fromkeys(aggr_dict)
    for key in aggr_dict.keys():
        dct[key] = max(aggr_dict[key])
        for dct in list_of_dicts:
            if key in dct.keys() and key in dct.keys():
                if max(aggr_dict[key]) == dct[key] and len(aggr_dict[key]) != 1:
                    new_key = key + '_' + str(list_of_dicts.index(dct) + 1)
                    dct[new_key] = dct.pop(key)
    return dct


# Function execution block.
random_list = generate_random_list_of_dicts()
final_dict = build_dict(random_list)

# Print block.
print(final_dict)
