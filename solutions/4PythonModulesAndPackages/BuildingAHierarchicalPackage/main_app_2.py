from geotool.validators import schema
from geotool.processors import converter

POLYGON_RECORD = {
    'id': '500123',
    'fields': ['id', 'owner', 'geometry'],
    'geometry': 'POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))'
}
REQUIRED_FIELDS = ['id', 'geometry']

for key in REQUIRED_FIELDS:
    prefix = f"{key} is"
    prefix += "" if schema.is_valid_polygon_id(key) else "not "
    print(prefix+" polygon id")
print(f"Converted polygon is {converter.wkt_to_coords(POLYGON_RECORD)}")