def flames_game(name1, name2):
    # Step 1: Remove spaces and convert names to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Step 2: Remove common letters
    for letter in name1[:]:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)

    # Step 3: Count remaining letters
    remaining_count = len(name1) + len(name2)

    # Step 4: FLAMES list for determining relationship
    flames = ["F", "L", "A", "M", "E", "S"]

    # Loop through FLAMES and remove characters based on count
    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1
        if split_index >= 0:
            # Rotate list to bring the split index to the end and remove it
            flames = flames[split_index + 1 :] + flames[:split_index]
        else:
            # If split index is -1, remove the last element
            flames.pop()

    # Determine the final relationship
    relationship = flames[0]
    relationships = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings",
    }

    return relationships[relationship]


# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get and print the result
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
