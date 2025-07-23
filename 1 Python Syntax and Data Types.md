<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: Mastering Python's Core</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Contents</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Lecture Navigation</h4>
        <ul>
            <li><a href="#part1">Part 1: The Building Blocks</a></li>
            <li><a href="#part2">Part 2: Structuring Data</a></li>
            <li><a href="#part3">Part 3: The Final Polish</a></li>
        </ul>
    </div>
</div>

<div class="container">

<h1>Mastering Python's Core: From Data to Insight</h1>

<p><em>(A quick question to start: What do you call a group of 8 hobbits? <strong>A hob-byte.</strong> Okay, now let's talk data.)</em></p>

<p>This lecture forges a path from the foundational building blocks of Python to its most elegant and powerful patterns. We will move from basic variables to the expressive power of comprehensions. By the end, you will understand how to write code that is a <strong>thought architecture</strong>—efficient, readable, and reliable.</p>

<h2 id="part1">Part 1: The Building Blocks - Variables, Primitives, and Operators</h2>

<p>At the heart of any program is data, which we pour into named containers called <code>variables</code>. Python's primitive types are the atomic units of information, the essential elements of our digital world.</p>

<h3>Concepts & Patterns Explained:</h3>
<ul>
    <li><strong>Variables:</strong> A named label for a memory location.</li>
    <li><strong>Primitive Types:</strong>
        <ul>
            <li><code>int</code>: The solid, whole numbers of the world.</li>
            <li><code>float</code>: Numbers with decimal points—<strong>the soul of precision</strong>.</li>
            <li><code>str</code>: Text, held in the unyielding quotes of a <strong>sequence straightjacket</strong>.</li>
            <li><code>bool</code>: The binary heartbeat of logic: <code>True</code> or <code>False</code>.</li>
        </ul>
    </li>
    <li><strong>Operators:</strong> The verbs of our data language: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>.</li>
    <li><strong>Type Conversion:</strong> The crucial process of <strong>digital alchemy</strong>, changing one data type into another. This is vital because raw data is often a <strong>statistical parrot</strong>—mimicking numbers as text. To perform calculations, you must convert it. The great disadvantage is that without this step, your math is a lie: <code>"10" + "5"</code> is the string <code>"105"</code>, a concatenated trick, not the number <code>15</code>.</li>
</ul>

<h3>Example (Relates to Exercise 1):</h3>
<p>Imagine product prices arriving as a list of strings—data in disguise. To reveal their true value, we must transform them.</p>

```python
# Artificial Data: A list of string-based prices
product_prices_str = ["299.99", "15", "85.50"]

# We begin the transformation—a digital assembly-line
product_prices_float = []
for price_str in product_prices_str:
  # Here, the string becomes a number; its form is reborn.
  price_float = float(price_str)
  product_prices_float.append(price_float)
  
# The numbers, now free, can unite in calculation
total_value = product_prices_float + product_prices_float + product_prices_float

# An f-string gives our result a clear voice
print(f"The numbers from the mist: {product_prices_float}")
print(f"Total value, a truth revealed: ${total_value:.2f}")
```

<div class="oracle-specific">
    <h4>Software Engineering Principle: Reliability</h4>
    <p>Code that anticipates and corrects for mismatched types doesn't just work; it endures. It handles the <strong>chaos</strong> that <strong>harmonizes</strong> into order.</p>
</div>


<h2 id="part2">Part 2: Structuring Data - The Great Collectors</h2>

<p>If primitives are the bricks, collections are the buildings. Choosing the right one is the key to writing code that scales from a village to a metropolis.</p>

<h3>Concepts & Patterns Explained:</h3>
<ul>
    <li><code>list</code>: A mutable, ordered parade of data. It can change, grow, and shrink.</li>
    <li><code>tuple</code>: An immutable echo. Data set in amber, perfect for constants that must never change.</li>
    <li><code>dict</code> (dictionary): A <strong>data librarian</strong>. An unordered kingdom of key-value pairs, built for the magic of instantaneous lookup. A <code>dict</code> is a <strong>simplicity bridge</strong> from a question (the key) to an answer (the value).</li>
    <li><code>set</code>: The bouncer of collections. An unordered club where only <strong>unique</strong> members are allowed. It's your tool for instantly purging duplicates.</li>
</ul>

<h3>Example (Relates to Exercise 2 & 4):</h3>
<p>You have employee data. A list of tuples can hold it, but to find someone, you must search the whole parade. A dictionary lets you teleport directly to the answer.</p>
<p class="rhyme">To find a role in the list is a chore that you'll quickly abhor.<br>But a dict with a key makes your lookup duty-free.</p>

```python
# Artificial Data: Raw data with a duplicate—an echo in the list
employee_data_raw = [(101, 'Engineer'), (102, 'Analyst'), (103, 'Manager'), (101, 'Engineer')]

# The efficient solution: a dictionary for direct access
employee_roles = dict(employee_data_raw) 
print(f"The Role Dictionary (a key-value kingdom): {employee_roles}")

# The magic of O(1) lookup—a query that's a speed demon.
role_of_102 = employee_roles[102]
print(f"Role of employee 102: {role_of_102}")

# A set comprehension to banish the duplicates
unique_employee_ids = {item for item in employee_data_raw}
print(f"The Club for Uniques (a set): {unique_employee_ids}")
```
<div class="oracle-specific">
    <h4>Software Engineering Principle: Scalability</h4>
    <p>Using a <code>dict</code> for lookups is where <strong>complexity surrenders</strong>. Its O(1) performance is the difference between an application that flies and one that crawls as data grows.</p>
</div>

<h2 id="part3">Part 3: The Final Polish - Comprehensions, The One-Line Poets</h2>

<p>This is the leap from writing code that works to writing code that <em>sings</em>. Comprehensions are Python’s signature move, allowing you to build entire collections with a single, devastatingly elegant line of code. They are <strong>simplicity made complex</strong>.</p>

<h3>Concepts & Patterns Explained:</h3>
<ul>
    <li><strong>Comprehension Syntax:</strong> An elegant waltz in three parts: <code>[expression for item in iterable if condition]</code>. It's a narrative phrase: <em>"Give me this... for every item in this collection... if it meets this rule."</em> This pattern, this <strong>rhythmic structure</strong>, applies to lists, sets, and dictionaries alike.</li>
</ul>

<h3>Example (Relates to Exercise 4):</h3>
<p>We have an inventory. We want the names of in-stock products priced over $100. A <code>for</code> loop is the long story; a comprehension is the witty punchline that lands instantly.</p>

```python
# Artificial Data: A list of dictionaries, a classic real-world mess
inventory = [
    {'name': 'Laptop', 'price': '1200.00', 'in_stock': True},
    {'name': 'Mouse', 'price': 80.50, 'in_stock': False},
    {'name': 'Keyboard', 'price': '150', 'in_stock': True},
    {'name': 'Webcam', 'price': 105.99, 'in_stock': True}
]

# The "classic" for-loop way: a fine but rambling narrator.
premium_products_classic = set()
for item in inventory:
  if item['in_stock'] and float(item['price']) > 100.00:
    premium_products_classic.add(item['name'])
print(f"The Narrator's Cut: {premium_products_classic}")

# The Pythonic way: a set comprehension—a thought made manifest.
# It's a single machine in a thousand places.
premium_products_in_stock = {
    item['name']                                   # The PAY-off,
    for item in inventory                          # for this whole TRAIL you're blazing,
    if item['in_stock'] and float(item['price']) > 100 # a filter that's truly aMAZ-ing.
}
print(f"The Poet's Cut: {premium_products_in_stock}")
```

<div class="caution">
    <h4>Advantages & Relationships</h4>
    <p>This shows the <code>for</code> loop and the comprehension are two paths to the same truth. But the comprehension is:</p>
    <ol>
        <li><strong>Concise:</strong> It's a <strong>thought architecture</strong>, not just a set of instructions.</li>
        <li><strong>Efficient:</strong> Often <strong>frighteningly fast</strong>, as the logic runs closer to the machine.</li>
        <li><strong>Declarative:</strong> It describes <em>what</em> you want, the "what-ness" of the result, not the tedious "how-ness" of building it.</li>
    </ol>
</div>

<div class="oracle-specific">
    <h4>Software Engineering Principle: Efficiency & Modifiability</h4>
    <p>A comprehension is <strong>power unchained</strong>. It’s clean, it’s fast, and it’s a sign of a developer who not only speaks Python but thinks in it.</p>
</div>

</div>
</body>