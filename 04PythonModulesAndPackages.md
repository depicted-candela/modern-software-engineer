<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: Architecting Code with Python Modules and Packages</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Table of Contents</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Lecture Navigation</h4>
        <ul>
            <li><a href="#part1">Part 1: The Atomic Unit</a></li>
            <li><a href="#part2">Part 2: The Thought Architecture</a></li>
            <li><a href="#part3">Part 3: The Autonomous System</a>
                <ul>
                    <li><a href="#sub3-1">Standard Library</a></li>
                    <li><a href="#sub3-2">Module Constants</a></li>
                    <li><a href="#sub3-3">Relative Imports</a></li>
                    <li><a href="#sub3-4">Entry Point</a></li>
                </ul>
            </li>
            <li><a href="#synthesis">Part 4: Synthesis</a></li>
        </ul>
    </div>
</div>


<div class="container">

<h1>Architecting Code with Python Modules & Packages</h1>

<h2 id="part1">Part 1: The Module – The Atomic Unit of Code Organization</h2>

<p class="rhyme">Why did the Python function get kicked out of the module party? Because it couldn’t respect the namespace!</p>

<p>A module is a <b>code toolbox</b>. It’s a single <code>.py</code> file, a self-contained unit of logic, a foundational building block.</p>

<h3 id="sub1-1">Concept: Module Creation and Import Mechanics</h3>
<p>To use one module's tools in another, you <code>import</code> it. This command is a bridge, but it’s a bridge to a specific, named territory. Your code remains clean, importing only the functionality it needs.</p>

<h3 id="sub1-2">Pattern: Namespacing – A Polite Separation</h3>
<p>When you <code>import data_validators</code>, you are not dumping its contents into your file. You are creating a labeled portal. To access its functions, you must walk through that portal every time: <code>data_validators.is_numeric_id()</code>.</p>
<div class="postgresql-bridge">
This is a core design principle: it prevents a <b>logic collision</b>, a chaotic state where two functions with the same name might overwrite each other. It's the difference between a shared, organized workshop and a pile of unlabeled tools.
</div>

<h3 id="sub1-3">Example: The Validator Toolbox</h3>
<ol>
    <li>
        <p><b>The module, <code>data_validators.py</code>:</b></p>
        <p>This is a <b>digital ledger</b> of validation functions.</p>

```python
# data_validators.py
# A toolbox of functions for validating data records.

print("Validator toolbox opened...") # A one-time event upon first import

def is_numeric_id(record_id: str) -> bool:
    """A simple function to check if an ID is a pure number."""
    return record_id.isnumeric()

def has_required_keys(data: dict, required: list) -> bool:
    """A function to ensure a dictionary isn't a beautiful prison of incomplete data."""
    return all(key in data for key in required)
```
</li>
<li>
    <p><b>The application, <code>process_records.py</code>:</b></p>
    <p>This script uses our toolbox to process a manifest of cadastral records.</p>

```python
# process_records.py
# The main script that uses our validator toolbox.

import data_validators # Imports the module as a namespace

# Artificial Data: A manifest of cadastral records to be validated.
RECORDS = [
    {'id': '1024', 'user': 'nicolas', 'access_level': 'admin'},
    {'id': '10a25', 'user': 'castelblanco', 'access_level': 'user'}, # An invalid ID
    {'id': '2048', 'user': 'architect'}, # A record with a missing key
]
REQUIRED_KEYS = ['id', 'user', 'access_level']

for record in RECORDS:
    # Accessing functions through the namespace
    is_valid = data_validators.is_numeric_id(record.get('id', ''))
    has_keys = data_validators.has_required_keys(record, REQUIRED_KEYS)
    
    print(f"Record {record.get('id', 'N/A')}: Valid ID: {is_valid}, Complete Schema: {has_keys}")
```
</li>
</ol>
<p class="caution">With modules, your code is maintainable. Your logic is not a <b>lingering echo</b> from a past edit, but a tool you can pick up and use with precision.</p>

<p class="rhyme">To keep your project from causing pain, keep your modules in their own lane.</p>

<h2 id="part2">Part 2: The Package – A Thought Architecture</h2>

<p class="rhyme">A lone <code>.py</code> file sits in a directory. The directory says, "I'm just a folder." The file creates an empty <code>__init__.py</code> and asks, "How about now?" The directory replies, "Welcome to the package, pal."</p>

<p>When you have many toolboxes, you need a workshop. A package is that workshop: a directory containing modules and a special <code>__init__.py</code> file. This file is the <b>welcome mat</b> that tells Python, "This place is organized."</p>

<h3 id="sub2-1">Example: Structuring the <code>geotool</code> Workshop</h3>
<ol>
    <li>
        <p><b>The architecture blueprint:</b></p>

```
geotool/
├── __init__.py         # The welcome mat for the 'geotool' package
└── validators/
    ├── __init__.py     # Welcome mat for the 'validators' sub-package
    └── schema.py
└── processors/
    ├── __init__.py     # Welcome mat for the 'processors' sub-package
    └── converter.py
```

</li>
<li>
    <p><b>Using the architected package in <code>main_app_2.py</code>:</b></p>
    <p>Here, we cherry-pick tools from specific workshops within our system.</p>

```python
# main_app_2.py
# Importing from specific submodules within our package

from geotool.validators import schema
from geotool.processors import converter

# Artificial Data: A single, structured geospatial record, a digital ghost.
POLYGON_RECORD = {
    'id': '500123',
    'geometry': 'POLYGON((30 10, 40 40))' # Simplified WKT
}

if schema.has_required_fields(POLYGON_RECORD, ['id', 'geometry']):
    coords = converter.wkt_to_coords(POLYGON_RECORD['geometry'])
    print(f"Geometry for ID {POLYGON_RECORD['id']} is now a living number: {coords}")
```

</li>
</ol>

<p>This structure is <b>scalable</b>. It turns a potential <b>information swamp</b> into a clean, navigable system with a clear hierarchy.</p>


<h2 id="part3">Part 3: Advanced Patterns for an Autonomous System</h2>

<h3 id="sub3-1">Standard Library (<code>os</code>, <code>sys</code>) – The Digital Senses</h3>
<p>Your code doesn't exist in a vacuum. The <code>os</code> module is its sense of touch, letting it interact with files. The <code>sys</code> module is its sense of self, letting it know how it was invoked. We use <code>sys.argv</code> to read command-line arguments—the user's direct instructions.</p>

<h3 id="sub3-2">Module-level Constants (<code>config.py</code>) – The Project's North Star</h3>
<p>Instead of scattering values like <code>'id'</code> or <code>'.csv'</code> throughout your code (which are <b>time-delay poisons</b>), you centralize them in a <code>config.py</code> module. This creates a <b>single source of truth</b>. If a requirement changes, you change one line, not fifty. The system becomes <b>reactively autonomous</b>.</p>

<h3 id="sub3-3">Relative Imports – The Family Secret</h3>
<p>Within a package, modules can talk to each other directly. <code>from . import sibling_module</code> is a <b>whispered conversation</b>. <code>from .. import config</code> is asking a parent package for advice. This makes the package a self-contained unit, a portable machine that works anywhere you place it.</p>

<h3 id="sub3-4">The Entry Point (<code>if __name__ == "__main__":</code>) – The Split Personality</h3>
<p>A Python file has a secret identity. When imported, its <code>__name__</code> is its filename (e.g., <code>"pipeline"</code>). But when you run it directly (<code>python run_pipeline.py</code>), its <code>__name__</code> becomes <code>"__main__"</code>.</p>
<div class="oracle-specific">
This block is a stage. Code inside it <i>only</i> runs when the file is the star of the show. This allows a file to be both a reusable module and an executable script—the ultimate <b>competing artifice</b>.
</div>

<h3 id="sub3-5">Example: The Pipeline as a Capstone Immersion Joke</h3>
<p>Let's build our <code>geotool</code> pipeline. The <b>Technical Superstrate</b> is a serious data processor. The <b>Humorous Substrate</b>, revealed only through context, is that we are processing a global census of garden gnomes.</p>
<ol>
    <li><b><code>geotool/config.py</code>:</b>

```python
# geotool/config.py
REQUIRED_HEADERS = ['gnome_id', 'location_wkt']
```

</li>
<li><b><code>geotool/processors/pipeline.py</code>:</b>

```python
# geotool/processors/pipeline.py
from .. import config # A family secret, a relative import
# ... other imports

def process_gnome_census(directory):
    # ... logic to scan CSVs, validate rows using config.REQUIRED_HEADERS
    print("Gnome census processing complete. Report generated.")
```

</li>
<li><b><code>run_pipeline.py</code> (The Semantic Catalyst):</b>

```python
# run_pipeline.py
import sys
from geotool.processors import pipeline

# The stage where the script puts on its cape.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # The user provides the path to the gnome data.
        pipeline.process_gnome_census(sys.argv)
    else:
        print("Usage: python run_pipeline.py <path_to_gnome_data_dir>")
```

</li>
</ol>
<p>The user runs a serious tool for a ridiculous purpose. The learning is real; the memorability is absolute. The structure is sound, the outcome profound.</p>


<div class="comparison-grid">
    <div class="feature-name">Architectural Primitives</div>
    <div class="grid-header">Module</div>
    <div class="grid-header">Package</div>
    <div class="grid-cell">
        <ul>
            <li><b>Form:</b> A single <code>.py</code> file.</li>
            <li><b>Analogy:</b> A toolbox.</li>
            <li><b>Purpose:</b> Encapsulates related functions and data.</li>
            <li><b>Key Pattern:</b> Namespacing (<code>module.function</code>).</li>
        </ul>
    </div>
    <div class="grid-cell">
        <ul>
            <li><b>Form:</b> A directory with <code>__init__.py</code>.</li>
            <li><b>Analogy:</b> A workshop of toolboxes.</li>
            <li><b>Purpose:</b> Structures a module namespace for scalability.</li>
            <li><b>Key Pattern:</b> Dotted imports (<code>package.module</code>).</li>
        </ul>
    </div>
</div>


<h2 id="synthesis">Part 4: Synthesis – The Architectural Ladder</h2>

<p>We have built a system from first principles, a true <b>thought architecture</b>.</p>
<ol>
    <li><b>Functions:</b> Are <b>tools</b>, sharp and specific.</li>
    <li><b>Modules:</b> Are <b>toolboxes</b>, organized and namespaced.</li>
    <li><b>Packages:</b> Are <b>workshops</b>, structured and scalable.</li>
    <li><b>An Architected System:</b> Is a <b>factory</b>, autonomous and reliable.</li>
</ol>

<p class="rhyme">From function parts to a package whole,<br>You give your growing code a soul.</p>
</div>
</body>