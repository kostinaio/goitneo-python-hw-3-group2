



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please enter the correct format. Command is invalid."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError

@input_error    
def show_phone(args, contacts):
    if len(args) < 1:
        return "Invalid command. Please enter: phone [name]" 

        # Return message not from Errors wraper, because Value Error message is incorrect for this case.
        # Format here "phone [name]"
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error    
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        raise KeyError

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()