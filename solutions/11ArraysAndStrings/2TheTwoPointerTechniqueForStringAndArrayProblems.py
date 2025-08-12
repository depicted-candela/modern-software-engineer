test_case_1 = "A man, a plan, a canal: Panama"
test_case_2 = "race a car"
test_case_3 = ".,_,"
test_case_4 = "Was it a car or a cat I saw?"

cases = [test_case_1, test_case_2, test_case_3, test_case_4]

def is_palindrome_alphanumeric(s: str) -> bool:
    length = len(s)
    left = 0
    right = length - 1
    while left < right:
        left_c = s[left]
        right_c = s[right]
        if not (left_c.isalpha()): 
            left += 1
            continue
        if not (right_c.isalpha()): 
            right -= 1
            continue
        left_c = left_c.upper()
        right_c = right_c.upper()
        if (left_c != right_c): return False
        left += 1
        right -= 1
    return True

for case in cases:
    print(is_palindrome_alphanumeric(case))