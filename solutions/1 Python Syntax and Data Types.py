# Part 1: Exercises for Chunk 1: Python Syntax and Data Types

## Exercise 1: Primitive Types, Operators, and Type Conversion
daily_sales_str = ["150.50", "200", "99.99", "75", "300.10"]
daily_sales_float = [float(sale) for sale in daily_sales_str]
print(f"Daily sales float: {daily_sales_float}")
total_sales = sum(daily_sales_float)
average_sales = sum(daily_sales_float) / len(daily_sales_float)
print(f"Total sales: ${total_sales}, Average: ${average_sales}")


## Exercise 2: Collection Types and Basic Operations
user_data = [(101, "aqua_dev"), (102, "beta_user"), (103, "gamma_guru")]
user_mapping = dict(user_data)
print(f"User 102 is {user_mapping[102]}")
user_mapping[104] = "delta bug"
print(f"The new map for users info is {user_mapping}")


## Exercise 3: Advanced String and List Manipulation
participants = ["  alex thorn  ", "  JANE DOE", " betty Crocker  "]
cleaned_participants = []
[cleaned_participants.append(participant.strip().title()) for participant in participants]
for clean_participant in cleaned_participants:
    print(f"Participant: {clean_participant}")


## Exercise 4 (Layered Combination): Comprehensions and Mixed-Type Data
inventory = [
    {'name': 'Laptop', 'price': '1200.00', 'in_stock': True},
    {'name': 'Mouse', 'price': 80.50, 'in_stock': False},
    {'name': 'Keyboard', 'price': '150', 'in_stock': True},
    {'name': 'Webcam', 'price': 105.99, 'in_stock': True}
]
premium_products_in_stock = {product['name'] for product in inventory 
    if product['in_stock'] and float(product['price']) > 100
}
print(f"The exercise 4:", premium_products_in_stock)


# Part 2: Hardcore Combined Problem for Chunk 2: Python Control Structures

log_stream = [
    (1668837600, 'INFO', 'User admin logged in successfully'),
    (1668837601, 'DEBUG', 'Database connection established'), # Should be ignored
    (1668837602, 'ERROR', 'Failed login attempt for user guest from IP 192.168.1.100'),
    (1668837603, 'ERROR', 'Failed login attempt for user guest from IP 192.168.1.100'),
    (1668837604, 'INFO', 'User alex logged in successfully'), # Breaks the consecutive error pattern
    (1668837605, 'ERROR', 'Failed login attempt for user guest from IP 192.168.1.100'),
    (1668837606, 'WARN', 'High CPU load detected'),
    (1668837607, 'ERROR', 'Service unavailable: connection timeout to payment_gateway'),
]
system_metrics = [
    (1668837600, 10, 256),
    (1668837601, 12, 258),
    (1668837602, 15, 260),
    (1668837603, 18, 262),
    (1668837604, 13, 270),
    (1668837605, 25, 280),
    (1668837606, 95, 300), # Correlates with the 'High CPU load' warning
    (1668837607, 88, 290),
]

BRUTE_FORCE_THRESHOLD = 3
CPU_WARNING_THRESHOLD = 90

incident_report = []
ip_fail_count = {}

for step, entry in enumerate(zip(log_stream, system_metrics)):
    if entry[0][1] == 'DEBUG': 
        pass
        continue
    status = 'CRITICAL' if entry[0][1] == 'ERROR' else 'NORMAL'
    failingIp = entry[0][0] if status == 'ERROR' else None
    if failingIp in ip_fail_count.keys(): 
        ip_fail_count[failingIp] += 1
    else:
        ip_fail_count[failingIp] = 0
    if failingIp and ip_fail_count[failingIp] == BRUTE_FORCE_THRESHOLD:
        count = step
        while zip(log_stream, system_metrics)[count][0][1] == 'ERROR':
            print(f"Keeps failing with logs {zip(log_stream, system_metrics)[count][0]}")
            count += 1
        if count > 1: incident_report.append('BRUTE-FORCE ALERT')
    if entry[0][1] == 'WARN' and entry[1][1] > CPU_WARNING_THRESHOLD: incident_report.append('RESOURCE EXHAUSTION ALERT')
else:
    print('System Scan Complete. All logs processed.')