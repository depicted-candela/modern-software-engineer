def calculate_ratios(tuples: list[tuple]):
    result = 0
    for (numerator, denominator) in tuples:
        try:
            if not isinstance(denominator, (int, float)): 
                raise TypeError(f"Error: Non-numeric denominator '{denominator}' found.")
            if denominator == 0: 
                raise ZeroDivisionError("Error: Division by zero attempted.")
            result = numerator / denominator
        except TypeError as e: print(f"TypeError: {e}")
        except ZeroDivisionError as e: print(f"ZeroDivisionError: {e}")
        else: print(f"Correct result {result}")

division_tasks = [(10, 2), (5, 0), (8, "four"), (15, 3), (20, 5.0)]
calculate_ratios(division_tasks)