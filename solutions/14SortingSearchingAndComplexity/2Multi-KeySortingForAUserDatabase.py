#   Exercise 2: Multi-Key Sorting for a User Database

# Description: You need to sort a large database of user profiles for 
# an administrative dashboard. The primary sorting key is the user's 
# account_level (e.g., "Admin", "Premium", "User"), and the secondary 
# key is their last_login_date. The final sorted list must have all 
# users of the same account_level grouped together, and within each 
# group, users should be sorted by their last_login_date (most recent 
# first). A crucial requirement is that the sorting process must be 
# predictable and have a guaranteed upper bound on performance, as 
# this operation is part of a critical nightly report generation.

#   Specifications & Theory:
# The sorting must be performed in two passes: first by 
# last_login_date, then by account_level. To ensure the secondary 
# sort doesn't disrupt the primary sort, the algorithm used for the 
# second pass (on account_level) must be stable.
# The solution must have a guaranteed worst-case time complexity of 
# O(n log n) to meet the performance predictability requirement. This 
# rules out algorithms with a potential O(n^2) worst-case.

import random
from datetime import date, timedelta

def generate_user_data(size=1000):
    levels = ["Admin", "Premium", "User"]
    users = []
    for i in range(size):
        delta = timedelta(days=random.randint(0, 365))
        users.append({
            "user_id": f"user_{i}",
            "account_level": random.choice(levels),
            "last_login_date": date(2023, 1, 1) + delta
        })
    return users

user_database = generate_user_data()
original_user_database = user_database.copy()

database_sorted_by_date = sorted(
    user_database, 
    key=lambda x: x['last_login_date'], 
    reverse=True
    )

level_orders = {'Admin': 0, 'Premium': 1, 'User': 2}
database_sorted_by_date_and_level = sorted(
    database_sorted_by_date, 
    key=lambda x: level_orders[x['account_level']]
    )

def validate_multi_key_sort(sorted_users):
    level_order = {"Admin": 0, "Premium": 1, "User": 2}

    for i in range(len(sorted_users) - 1):
        current_user = sorted_users[i]
        next_user = sorted_users[i + 1]

        current_level_val = level_order[current_user["account_level"]]
        next_level_val = level_order[next_user["account_level"]]

        # Primary key check
        assert current_level_val <= next_level_val, f"Primary key (account_level) sort failed at index {i}."

        # Secondary key check (if primary keys are equal)
        if current_level_val == next_level_val:
            assert current_user["last_login_date"] >= next_user["last_login_date"], \
                f"Secondary key (last_login_date) sort failed for account level {current_user['account_level']} at index {i}."

    print("Multi-Key Sort Validation Passed.")

validate_multi_key_sort(database_sorted_by_date_and_level)