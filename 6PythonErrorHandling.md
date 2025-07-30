<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: The Core Building Blocks of Python</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Lecture Navigation</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Outline</h4>
        <ul>
            <li><a href="#part1">Part 1: The Safety Net</a></li>
            <li><a href="#part2">Part 2: The Specialist's Clinic</a></li>
            <li><a href="#part3">Part 3: Forging Your Own Alarms</a></li>
            <li><a href="#part4">Part 4: The Unbreakable Promise</a></li>
            <li><a href="#part5">Part 5: The Detective's Bulletin Board</a></li>
        </ul>
    </div>
</div>

<div class="container">

<h1 id="top">Python Error Handling: From Chaos to Control</h1>

<h3 id="part1">Part 1: The Safety Net – <code>try</code> and <code>except</code></h3>

<p>Imagine you're a circus performer on a high wire. Walking the wire is your main task—the <code>try</code> block. This is where you perform your daring, "risky" operations. But what happens if you slip? You don't just fall to the floor. You fall into a safety net.</p>
<p>That net is the <code>except</code> block. It’s a <strong>Safety Valve</strong> designed to catch a specific kind of fall. Its job is not to prevent the slip, but to manage the consequence, ensuring the whole show doesn’t come to a crashing halt.</p>

<h4>Property-Based View</h4>
<ul>
    <li><strong>Entity:</strong> The <code>try...except</code> statement is a <strong>Controlled Environment</strong>.</li>
    <li><strong>Utility:</strong> It transforms a program from a fragile crystal, which shatters at the first error, into a resilient system that can absorb shocks.</li>
</ul>

<h4>Example: The Data Converter's Net</h4>
<p>We have a stream of sensor data, but some of it is just static. We need to convert it, but we can't let one bad signal end the transmission.</p>

```python
# --- Artificial Data ---
# A mixed-signal broadcast from a remote outpost.
str_data = ["10.5", "20.2", "not_a_number", "7", "-5.88", "3.14e-2"]
processed_signals = []

# --- Structural Usage ---
for signal in str_data:
    try:
        # We attempt the high-wire act: converting the signal.
        value = float(signal)
        processed_signals.append(value)
    except ValueError:
        # The safety net. It catches ONLY the expected slip-up (a ValueError).
        # We handle it by logging the issue and providing a safe default.
        print(f"Signal corrupted: '{signal}'. Substituting with 0.0.")
        processed_signals.append(0.0)

print("Final Processed Signals:", processed_signals)
```

<h4>Software Engineering Principle: Robustness</h4>
<p>Why did the Python program stop working? Because it had an <em>uncaught</em> exception it couldn't get over. Our program, however, moves on. It handles the fall and is ready for the next act.</p>
<p><small>Source: Python Tutorial: 8.3. Handling Exceptions</small></p>

<h3 id="part2">Part 2: The Specialist's Clinic – Multiple Exceptions and the <code>else</code> Ward</h3>

<p>Imagine your <code>try</code> block is an emergency room. A patient comes in. They might have a broken bone (<code>ZeroDivisionError</code>) or a strange allergic reaction (<code>TypeError</code>). You don’t send every patient to the same doctor. You send them to specialists. Multiple <code>except</code> blocks are your team of specialists, each trained to handle one specific problem.</p>
<p>And what about the <code>else</code> block? That's the discharge office. You <em>only</em> go there after the specialists confirm you're perfectly healthy. It’s where the "successful outcome" logic lives, completely separated from the triage and treatment areas.</p>

<h4>Property-Based View</h4>
<ul>
    <li><strong>Entity:</strong> <code>try...except...else</code> is a <strong>Diagnostic Funnel</strong>.</li>
    <li><strong>Specific Property:</strong> Using <code>else</code> creates a <strong>Sanitized Success Zone</strong>. It prevents a bug in your success-logic (e.g., a typo in a <code>print</code> statement) from being accidentally caught by your error specialists.</li>
</ul>

<h4>Example: The Division Triage</h4>
<p>We have a list of calculations, a mix of the routine, the impossible, and the nonsensical.</p>

```python
# --- Artificial Data ---
# A log of requested computations from various systems.
division_tasks = [(10, 2), (5, 0), (8, "four"), (15, 3)]

# --- Structural Usage ---
for numerator, denominator in division_tasks:
    print(f"Task: {numerator} / {denominator}")
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        # Specialist 1: The Mathematician.
        print("  Diagnosis: A division by zero. This is a tear in the fabric of mathematics.")
    except TypeError:
        # Specialist 2: The Data Typist.
        print(f"  Diagnosis: Incompatible types. We cannot operate on a {type(denominator).__name__}.")
    else:
        # The Discharge Office: Only for patients with a clean bill of health.
        print(f"  Outcome: Healthy. The result is {result}.")
```

<h4>Software Engineering Principle: Specificity</h4>
<p>This pattern makes our intent crystal clear. We're not just handling errors; we're diagnosing specific failures and have a dedicated place for celebrating success.</p>
<p><small>Source: Python Tutorial: 8.3. Handling Exceptions</small></p>

<h3 id="part3">Part 3: Forging Your Own Alarms – <code>raise</code> and Custom Exceptions</h3>

<p>Python gives you a standard set of fire alarms: <code>ValueError</code>, <code>TypeError</code>, etc. But what if you're engineering a deep-sea submersible and you need an alarm for "Catastrophic Hull Pressure Imminent"? A generic <code>ValueError</code> just won't do.</p>
<p>You must forge your own alarms. This is what creating a custom exception is. It’s an act of <strong>Domain Modeling</strong>—of creating a precise language for the unique problems your system can face. The <code>raise</code> keyword is the big red button you press to sound that alarm.</p>

<h4>Property-Based View</h4>
<ul>
    <li><strong>Entity:</strong> A custom exception is a <strong>Semantic Signal</strong>.</li>
    <li><strong>Advantage:</strong> It turns your error messages from cryptic codes into self-documenting headlines. A <code>DataOutOfRangeError</code> is a <strong>structured failure</strong>; it's infinitely more meaningful than a generic error.</li>
</ul>

<h4>Example: The Submersible's Pressure Gauge</h4>
<p>We're monitoring the hull pressure. There's a very specific safe range. Deviating isn't just an "error"; it's a critical event.</p>

```python
# --- Artificial Data ---
# A series of pressure readings from the submersible's hull.
pressure_readings = [101.3, 99.8, 112.5, 85.0]
SAFE_KPA_MIN, SAFE_KPA_MAX = 87.0, 109.0

# --- Structural Usage: Forging the Alarm ---
class HullPressureError(ValueError):
    """Alarm raised when hull pressure exceeds safe operational limits."""
    pass

def validate_hull_pressure(kpa):
    if not (SAFE_KPA_MIN <= kpa <= SAFE_KPA_MAX):
        # We press the big red button, raising our specific, high-stakes alarm.
        raise HullPressureError(
            f"CRITICAL: Pressure {kpa} kPa is outside safe limits of {SAFE_KPA_MIN}-{SAFE_KPA_MAX} kPa!"
        )
    return True

# --- Structural Usage: Heeding the Alarm ---
for pressure in pressure_readings:
    try:
        validate_hull_pressure(pressure)
        print(f"Pressure {pressure} kPa is nominal.")
    except HullPressureError as e:
        print(f"DANGER: {e}")
```

<h4>Software Engineering Principle: Abstraction</h4>
<p>We have abstracted a specific domain rule into a reusable, meaningful alarm. The code now speaks the language of the problem it's solving.</p>
<p><small>Source: Python Tutorial: 8.4 & 8.6, Raising and User-defined Exceptions</small></p>

<h3 id="part4">Part 4: The Unbreakable Promise – <code>finally</code> and <code>with</code></h3>

<p>Some promises must never be broken. In programming, the most sacred of these is "I will clean up after myself." The <code>finally</code> clause is this <strong>unbreakable promise</strong> in code form. It's the part of your program that runs no matter what—through success, failure, or even an abrupt <code>return</code>. It’s the janitor who cleans the room after the party, regardless of whether it was a quiet get-together or a raging disaster.</p>
<p>The <code>with</code> statement is the elegant evolution of this promise. It's a <strong>Pact of Guaranteed Cleanup</strong>. By wrapping a resource in a <code>with</code> block, you are hiring a professional service that handles both the setup and the cleanup automatically and perfectly, every time.</p>

<h4>Property-Based View</h4>
<ul>
    <li><strong>Entity:</strong> <code>with</code> statement.</li>
    <li><strong>Paradoxical Advantage:</strong> It achieves <strong>effortless safety</strong>. The most robust way to manage resources is also the cleanest and requires the least code.</li>
</ul>
<div class="caution">
    <p><strong>Risk of Omission:</strong> Forgetting cleanup is a <strong>lingering vulnerability</strong>, a <strong>bleeding wound</strong> in your application that slowly leaks resources until the system collapses.</p>
</div>

<h4>Example: The Self-Cleaning Database Connection</h4>

```python
# --- Artificial Data (Mock Resource with the Pact) ---
class DatabaseConnection:
    def __enter__(self):
        print("Pact initiated: DB connection opened, resources allocated.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Pact fulfilled: DB connection closed. Cleanup is complete.")
    
    def write(self, data):
        if data is None: raise ValueError("Null write violation.")
        print("Data written.")

# --- Structural Usage with the 'with' Pact ---
try:
    with DatabaseConnection() as db:
        print("Operating within the safety of the pact...")
        db.write("system_log")
        db.write(None) # This will break the pact's terms!
        print("This will never be reached.")
except ValueError as e:
    print(f"Operation failed: {e}")

# Notice the __exit__ message printed even after the error. The promise was kept.
```

<h4>Software Engineering Principle: Resource Safety</h4>
<p>Using <code>with</code> is not a suggestion; it is the hallmark of a professional Python programmer who values creating applications that are not just clever, but stable and safe.</p>
<p><small>Source: Python Tutorial: 8.7 & 8.8, Defining and Predefined Clean-up Actions</small></p>


<h3 id="part5">Part 5: The Detective's Bulletin Board – Chaining, Notes, and Groups</h3>
<p>A single error is a clue. A full error report is a solution. Modern Python gives you a complete detective's kit for investigating failures in complex systems.</p>
<h4>The Detective's Toolkit</h4>
<ul>
    <li><strong>Exception Chaining (<code>raise from</code>):</strong> This is the <strong>Causality Chain</strong>. It prevents a low-level clue (a <code>ConnectionError</code>) from being lost when you report a high-level crime (a <code>DataFetchError</code>). The original crime scene is preserved.</li>
    <li><strong>Notes (<code>add_note</code>):</strong> This is your detective's notebook. As you investigate, you can add context—"Failure occurred on record #57," "User ID was 'admin'"—directly onto the exception object itself. This is <strong>annotated failure</strong>.</li>
    <li><strong>Exception Groups:</strong> This is the <strong>bulletin board in the precinct</strong>. When you run multiple tasks at once and several fail, you don't just report the first one. You collect all the failed case files and pin them to the board. It's a single report of <strong>organized chaos</strong>, a unified story of multiple, simultaneous failures.</li>
</ul>

<h4>Example: Mission Control Telemetry Pipeline</h4>
<p>We are processing telemetry from multiple Mars rovers at once. Failure is not just an option; it's a daily reality.</p>

```python
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
```

<h4>Software Engineering Principle: Fault Tolerance & Observability</h4>
<p>This is how you build systems that survive in the real world. You don’t crash; you collect intelligence. You embrace failure not as an end, but as data. You create systems where <em>latency dies</em> and <em>complexity surrenders</em>.</p>
<p><small>Source: Python Tutorial: 8.5, 8.9, 8.10, Exception Chaining, Groups, and Notes</small></p>

</div>
</body>
</html>