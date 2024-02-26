

def print_greeting(name):
    # Greeting message with the person's name in each line
    greeting = f"Hello, {name}! Welcome to our community."
    line2 = f"We are delighted to have you, {name}."
    line3 = f"{name}, if there's anything you need, feel free to ask."

    # Print the three-line greeting
    print(greeting)
    print(line2)
    print(line3)

# Example usage:
person_name = input("Enter a name: ")
print_greeting(person_name)