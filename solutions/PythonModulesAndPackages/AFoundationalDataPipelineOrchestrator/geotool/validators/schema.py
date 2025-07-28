from ..config import REQUIRED_HEADERS

def is_valid_polygon_id(item: str) -> bool:
    for character in item:
        if character.isnumeric(): return False
    return True

def has_required_fields(headers: list) -> bool:
    return all(header for header in headers if header in REQUIRED_HEADERS)