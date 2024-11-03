from collections import Counter

def cut_common_letters(str1, str2):
    count1 = Counter(str1)
    count2 = Counter(str2)
    new_str1 = []
    new_str2 = []
    for char in str1:
        if count1[char] > count2[char]:
            new_str1.append(char)
            count1[char] -= 1
        elif count1[char] > 0 and count2[char] > 0:
            count1[char] -= 1
            count2[char] -= 1
    for char in str2:
        if count2[char] > count1[char]:
            new_str2.append(char)
            count2[char] -= 1
    result_str1 = ''.join(new_str1)
    result_str2 = ''.join(new_str2)
    
    return result_str1, result_str2

def flames_game(name1, name2):
    result1, result2 = cut_common_letters(name1, name2)
    remaining_count = len(result1) + len(result2)
    flames = ["F", "L", "A", "M", "E", "S"]
    pos = 0
    while len(flames) > 1:
        pos = (pos + remaining_count - 1) % len(flames)
        flames.pop(pos)
    relationships = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings",
    }

    return relationships[flames[0]]
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
