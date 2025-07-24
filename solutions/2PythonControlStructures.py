# Exercise 1: Conditional Data Validation and Categorization
api_requests = [
    {'user_id': 101, 'payload_size': 1200, 'is_premium_user': True, 'payload': '...'},
    {'user_id': 102, 'payload_size': 800, 'is_premium_user': True, 'payload': '...'},
    {'user_id': 103, 'payload_size': 1500, 'is_premium_user': False, 'payload': '...'},
    {'user_id': 104, 'payload_size': 500, 'is_premium_user': False, 'payload': '...'},
    {'request_id': 901, 'payload_size': 2000, 'payload': '...'}, # Missing 'user_id'
    {'user_id': 105, 'is_premium_user': True, 'payload': '...'}, # Missing 'payload_size'
]

for request in api_requests:
    validators = {'user', 'payload'}
    if validators in set(request.keys()):
        request['category'] = 'High Priority' if request['payload_size'] > 1000 and request['is_premium_user'] else 'Standard Priority'
    else: request['category'] = 'Invalid'

import json
print(json.dumps(api_requests, indent=2))


print("____________________________________________________________________")
print("Exercise 2: Processing Parallel Data Streams with Iteration Patterns")
timestamps = [1678886400, 1678886401, 1678886402, 1678886403, 1678886404]
sensor_ids = ['A-101', 'B-202', 'A-101', 'C-303', 'B-202']
readings = [25.5, 99.9, 101.2, -5.0, 75.0]

import logging, sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s',
    stream=sys.stdout
)

complete_report = [] 
for step, (ts, si, r) in enumerate(zip(timestamps, sensor_ids, readings), start=1):
    status = "Success" if 0 < r and r > 100 else f"Badly formed reading value"
    logging.info(status)
    complete_report.append(f"With the status {status}, at {ts}, the sensor {si}, reading was {r}")

import json

logging.info("The entire report finally processed is")
print(json.dumps(complete_report, indent=3))



print("____________________________________________________________________")
print("Hardcore Combined Problem: Intelligent Log Processor")
import random
import time
import pprint

# --- Configuration ---

# Total number of log entries to generate
TOTAL_LOGS_TO_GENERATE = 100000

# Number of unique user IDs to simulate
NUM_USERS = 20

# The types of events a user can perform
# We can make 'login' and 'logout' special
EVENT_TYPES = ['heartbeat', 'purchase', 'view_page', 'add_to_cart']

# Starting point for timestamps (uses current time as a base)
# Using a fixed value makes the output reproducible if you also fix the random seed
# random.seed(42) # Uncomment for reproducible results
START_TIMESTAMP = int(time.time())

# The maximum time gap between consecutive events
MAX_TIME_JUMP_SECONDS = 15

# --- Session Simulation Probabilities ---
# Chance that the next log event is a new user logging in
NEW_LOGIN_PROBABILITY = 0.30 # 30%

# Chance that an active user will log out after an action
LOGOUT_PROBABILITY = 0.15 # 15%

# --- Batching Configuration ---
# The minimum and maximum number of logs in a single batch
MIN_BATCH_SIZE = 2
MAX_BATCH_SIZE = 5

# The probability of injecting a None into a batch
NONE_INJECTION_PROBABILITY = 0.10 # 10%


def generate_significant_log_data():
    """
    Generates realistic, structured log data by simulating user sessions.
    """
    all_logs = []
    active_users = {}
    current_timestamp = START_TIMESTAMP
    user_ids = list(range(1, NUM_USERS + 1))
    print(f"Generating {TOTAL_LOGS_TO_GENERATE} logs for {NUM_USERS} potential users...")
    while len(all_logs) < TOTAL_LOGS_TO_GENERATE:

        should_create_new_login = random.random() < NEW_LOGIN_PROBABILITY
        if not active_users:
            should_create_new_login = True
        log_entry = None

        if should_create_new_login:
            inactive_users = [uid for uid in user_ids if uid not in active_users]
            if not inactive_users:
                continue 
            user_id = random.choice(inactive_users)
            event_type = 'login'
            
            active_users[user_id] = current_timestamp
            log_entry = (current_timestamp, user_id, event_type)
        else:
            user_id = random.choice(list(active_users.keys()))
            event_type = random.choice(EVENT_TYPES)
            log_entry = (current_timestamp, user_id, event_type)
            if random.random() < LOGOUT_PROBABILITY:
                current_timestamp += random.randint(1, MAX_TIME_JUMP_SECONDS)
                logout_entry = (current_timestamp, user_id, 'logout')
                all_logs.append(logout_entry)
                
                del active_users[user_id]
        if log_entry:
            all_logs.append(log_entry)
        
        current_timestamp += random.randint(1, MAX_TIME_JUMP_SECONDS)

    log_batches = []
    random.shuffle(all_logs) 
    all_logs.sort(key=lambda x: x[0]) 

    remaining_logs = len(all_logs)
    batch_sizes = []
    while remaining_logs > 0:
        size = random.randint(MIN_BATCH_SIZE, MAX_BATCH_SIZE)
        batch_sizes.append(min(size, remaining_logs))
        remaining_logs -= size

    log_iterator = iter(all_logs)
    for size in batch_sizes:
        batch = []
        for _ in range(size):
            try:
                if random.random() < NONE_INJECTION_PROBABILITY:
                    batch.append(None)
                batch.append(next(log_iterator))
            except StopIteration:
                break
        if batch:
            log_batches.append(batch)
            
    print("Log generation complete.")
    return log_batches

def critical_sequence(generated_log_batches, max_logs):
    counter = 0
    limit_reached = False
    logged_users = dict()
    for batch in generated_log_batches:
        for step_m, movement in enumerate(batch):
            print("Movement:", movement)
            if not movement or movement[2] == 'heartbeat': continue
            counter =+ step_m
            if counter == max_logs: 
                limit_reached = True
                break
            if movement[2] == 'login': logged_users[id] = movement[0]
            if id in logged_users.keys() and movement[2] == 'purchase' and movement[0] - logged_users[id] < 61:
                logging.info(f"Critical sequence found at {movement}")
                limit_reached = True
                break
            if id in logged_users.keys() and movement[0] == 'logout':
                logged_users.pop(id)
        if limit_reached: break


# --- Main execution for the hardcore combined problem---
if __name__ == "__main__":
    # These are the original constants for comparison/context
    TIME_WINDOW = 60
    MAX_LOGS_TO_PROCESS = 100
    # Generate the new, random, significant data
    generated_log_batches = generate_significant_log_data()
    # Using pprint for a cleaner print of the nested list structure
    # pprint.pprint(generated_log_batches)
    # print("\n--- Generated Log Batches ---")
    critical_sequence(generated_log_batches, MAX_LOGS_TO_PROCESS)

