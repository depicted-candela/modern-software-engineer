import json # Assume json is imported for this example

# --- Custom Alarms for Mission Control ---
class RoverConnectionError(Exception): pass
class TelemetryParsingError(ValueError): pass
class MissionReport(ExceptionGroup): pass

# --- Mock Telemetry Stream ---
telemetry_from_rovers = {
    "Curiosity": '{"temp": -60, "wind": 15}',
    "Perseverance": '{"temp": -55, "wind": "corrupted', # Will cause a parsing error
    "Opportunity": None # Rover is offline
}

# --- Structural Usage: The Mission Control Detective ---
failures = []
for rover, data in telemetry_from_rovers.items():
    try:
        if data is None:
            raise RoverConnectionError("Signal Lost")
        
        # This operation is a potential point of failure
        parsed = json.loads(data)
        
    except RoverConnectionError as e:
        e.add_note(f"Rover '{rover}' is offline.")
        failures.append(e)
    except Exception as e: # Catching the original parsing error
        # Create the full case file, linking the low-level error to our high-level one.
        report = TelemetryParsingError("Garbled transmission received")
        report.add_note(f"Failure occurred while processing telemetry from '{rover}'.")
        failures.append(report)

# After the loop, create the final bulletin board.
if failures:
    raise MissionReport("Multiple anomalies detected in telemetry stream", failures)