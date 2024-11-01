def process_input(data):
    if isinstance(data, int):
        return data ** 2  # Square a number
    elif isinstance(data, str):
        return data.upper()  # Convert string to uppercase
    elif isinstance(data, list):
        return [element * 2 for element in data] # Doubling each item in the list 
    else:
        return "Unsupported type"

# Example of use
print(process_input(5))         
print(process_input("hello"))   
print(process_input([1, 2, 3]))  
