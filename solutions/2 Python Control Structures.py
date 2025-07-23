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


# Exercise 2: Processing Parallel Data Streams with Iteration Patterns
