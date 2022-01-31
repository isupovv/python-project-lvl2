import json


def generate_diff(parsed_args):
    only_in_first_json = {}
    in_two_jsons = {}
    only_in_second_json = {}
    keys = set()
    with open(parsed_args.first_file, 'r') as first:
        first_json = json.load(first)
        with open(parsed_args.second_file, 'r') as second:
            second_json = json.load(second)
            for k, v in first_json.items():
                keys.add(k)
                new_v = second_json.get(k)
                if new_v == None:
                    only_in_first_json[k] = v
                elif new_v != v:
                    only_in_first_json[k] = v
                    only_in_second_json[k] = new_v
                else:
                    in_two_jsons[k] = new_v
            for k, v in second_json.items():
                keys.add(k)
                old_v = first_json.get(k)
                if old_v == None:
                    only_in_second_json[k] = v
                elif old_v != v:
                    only_in_first_json[k] = old_v
                    only_in_second_json[k] = v
                else:
                    in_two_jsons[k] = old_v
    result = '{'
    new_keys = list(keys)
    new_keys.sort()
    for key in new_keys:
        old_value = only_in_first_json.get(key)
        if old_value != None:
            result += f'\n  - {key}: {old_value}'
        value = in_two_jsons.get(key)
        if value != None:
            result += f'\n  - {key}: {value}'
        new_value = only_in_second_json.get(key)
        if new_value != None:
            result += f'\n  - {key}: {new_value}'
    result += '\n}'
    print(result)
