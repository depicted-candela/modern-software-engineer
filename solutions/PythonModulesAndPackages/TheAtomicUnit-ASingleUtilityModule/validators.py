def is_valid_id(item: str) -> bool:
    for character in item:
        if character.isnumeric(): return False
    return True

def has_required_keys(data: dict, keys: list) -> bool:
    return set(keys) in set(data.keys())