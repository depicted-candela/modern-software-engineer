class DataOutOfRangeError(ValueError):
    """Valid pressure kPa values for sea-level Earth measurements is between 87 to 109"""
    pass

def validate_atmospheric_pressure(pressure_readings: list):
    for reading in pressure_readings:
        try:
            if not 87 > reading > 109: 
                raise DataOutOfRangeError(f"Inalid pressure kPa value {reading}, sea-level measurements are between 87 to 109")
        except DataOutOfRangeError as e:
            print(f"DataOutOfRangeError: {e}")

pressure_readings = [101.3, 99.8, 112.5, 85.0, 105.7]

validate_atmospheric_pressure(pressure_readings)