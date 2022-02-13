import random
import string


# User exception for generating random list.
class GenerationException(Exception):
    """Raised when something wrong with random list generation."""
    def __init__(self, message):
        self.message = message


# Generate list if random number of dicts. Return: List of dicts.
def generate_random_list_of_dicts(number_of_dicts: int = 10, dicts_values: int = 100) -> [{}]:
    try:
        if number_of_dicts > 0:
            return [{random.choice(string.ascii_lowercase): random.randint(0, dicts_values) for _ in range(
                random.randint(0, len(string.ascii_lowercase)))} for _ in range(random.randint(0, number_of_dicts))]
        else:
            raise GenerationException("Number of dicts should be more than zero!")
    except GenerationException as e:
        print(e.message)


# Aggregate values by key from all dictionaries in list. Return: Dict.
def aggregate_values_by_key(list_of_dicts: [{}]) -> {}:
    aggr_dict = dict()
    for dic in list_of_dicts:
        for k, v in dic.items():
            if k not in aggr_dict.keys():
                aggr_dict[k] = [v]
            else:
                aggr_dict[k].append(v)
    return aggr_dict


# Build dictionary where key:max(value) exist and rename key if key is not unique. Return: Dict.
def build_dict(list_of_dicts: [{}]) -> {}:
    aggr_dict = aggregate_values_by_key(list_of_dicts)
    dct = dict.fromkeys(aggr_dict)
    for key in aggr_dict.keys():
        dct[key] = max(aggr_dict[key])
        for dct in list_of_dicts:
            if key in dct.keys() and key in aggr_dict.keys():
                if max(aggr_dict[key]) == dct[key] and len(aggr_dict[key]) != 1:
                    new_key = key + '_' + str(list_of_dicts.index(dct) + 1)
                    dct[new_key] = dct.pop(key)
    return dct


# Function execution block.
random_list = generate_random_list_of_dicts()
final_dict = build_dict(random_list)

# Print block.
print(final_dict)
