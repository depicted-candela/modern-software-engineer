str_data = ["10.5", "20.2", "not_a_number", "7", "-5.88", "3.14e-2"]

def safe_to_float_converter(str_list):
    cleaned_list = list()
    for record in str_list: 
        try: 
            cleaned_list.append(float(record))
        except ValueError as e:
            print(f"Cleaned value {record} because of {e}")
            cleaned_list.append(0)
    return cleaned_list

if __name__ == "__main__":
    cleaned_list = safe_to_float_converter(str_data)
    print(f"Processed list {cleaned_list}")