from validators import is_valid_id, has_required_keys

RECORDS = [
    {'id': '1024', 'user': 'nicolas', 'access_level': 'admin'},
    {'id': '10a25', 'user': 'castelblanco', 'access_level': 'user'},
    {'id': '2048', 'user': 'architect'},
]
REQUIRED_KEYS = ['id', 'user', 'access_level']

for key in REQUIRED_KEYS:
    prefix = f"{key} is "
    prefix += "" if is_valid_id(key) else "not "
    print(prefix+" key")
for record in RECORDS:
    prefix = f"Record {record} "
    prefix += " has" if has_required_keys(record, REQUIRED_KEYS) else " does not have"
    print(prefix+" keys")