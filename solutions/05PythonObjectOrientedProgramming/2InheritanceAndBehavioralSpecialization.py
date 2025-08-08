geodata_raw = {
    'id': 'GEO-55A', 
    'source': 'Telespazio', 
    'value': (6.2, -75.5), 
    'validated': False, 
    'epsg_code': 4326}
elevation_raw = {
    'id': 'ELEV-B2', 
    'source': 'IGAC', 
    'value': 1500.7, 
    'validated': True, 
    'vertical_datum': 'WGS84'}
elevation_duplicate = {
    'id': 'ELEV-B2', 
    'source': 'IGAC', 
    'value': 1500.7, 
    'validated': True, 
    'vertical_datum': 'WGS84'}

class BaseRecord:
    def __init__(self, id: str, source: str, value: str):
        self.id = id; self.source = source; self.value = value
    def get_record_type(self): return 'Base Record'
    def __eq__(self, value):
        return self.id, self.source == value.id, value.source

class GeospatialRecord(BaseRecord):
    def __init__(self, id: str, source: str, value: str, epsg_code: int):
        super().__init__(id, source, value)
        self.epsg_code = epsg_code
    def get_record_type(self): return 'Geospatial Record'
    
class ElevationRecord(BaseRecord):
    def __init__(self, id: str, source: str, value: str, vertical_datum: str):
        super().__init__(id, source, value)
        self.vertical_datum = vertical_datum
    def get_record_type(self): return 'Elevation Record'
    
georecord = GeospatialRecord(
    geodata_raw['id'], 
    geodata_raw['source'], 
    geodata_raw['value'], 
    geodata_raw['epsg_code'])
print(georecord.get_record_type())
elevrecord = ElevationRecord(
    elevation_raw['id'], 
    elevation_raw['source'], 
    elevation_raw['value'], 
    elevation_raw['vertical_datum'])
print(elevrecord.get_record_type())
elevdup = ElevationRecord(
    elevation_duplicate['id'], 
    elevation_duplicate['source'], 
    elevation_duplicate['value'], 
    elevation_duplicate['vertical_datum'])
print(elevdup.get_record_type())

assert elevrecord == elevdup
print("Assertion passed: elevrecord and elevdup are equal")