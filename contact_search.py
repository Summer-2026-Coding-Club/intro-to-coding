contacts = [
    {"id": "1", "name": "Ahmed Sami", "phone": "0598926087"},
    {"id": "2", "name": "Elyanna Montuk", "phone": "0598237629"},
    {"id": "3", "name": "Nora Fathi", "phone": "0598080807"},
    {"id": "4", "name": "Muath Fathi", "phone": "0594171783"},
    {"id": "5", "name": "Raju Rastugi", "phone": "0596666669"},
    {"id": "6", "name": "Farhan Quraishi", "phone": "0598722833"},
    {"id": "7", "name": "Mohamed Faraj", "phone": "0595102047"},
    {"id": "8", "name": "Talat Khairy", "phone": "0598182839"},
    {"id": "9", "name": "Fawzy Sameer", "phone": "0599369350"},
    {"id": "10", "name": "Ahmed Ali", "phone": "059904688"},
    {"id": "11", "name": "Sami Harazeen", "phone": "0598723862"},
    {"id": "12", "name": "Khaled Faraj", "phone": "0598702376"},
    {"id": "13", "name": "Farhan Louh", "phone": "0599029362"},
    {"id": "14", "name": "Mahmoud Sameer", "phone": "0592836293"},
    {"id": "15", "name": "Alexander Khusanov", "phone": "059201677"},
]


def search(user_input):
    result = []
    for contact in contacts:
        if user_input.strip().lower() in contact["name"].strip().lower():
            result.append(contact)
    return result


def display(results, user_input):
    if results:
        print(f"Found {len(results)} result(s):")
        for contact in results:
            print(f"  {contact['name']} => {contact['phone']}")
    else:
        print(f"'{user_input}' not found!")


def main():
    print("Contact Book")
    while True:
        user_input = input("Please enter a name to search (or 'quit' to exit): ")
        if user_input.lower() == "quit":
            break
        results = search(user_input)
        display(results, user_input)


if __name__ == "__main__":
    main()
