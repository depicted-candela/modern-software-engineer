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

print(user_database, indent=2)