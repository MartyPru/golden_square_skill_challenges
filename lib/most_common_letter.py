def get_most_common_letter(text):
    counter = {}
    print(f'* Starting for loop')
    for char in text:
        print(f' * Current character is {char}')
        counter[char] = counter.get(char, 0) + 1
    print(f'Ending for loop')
    print(f'counter.items is: {sorted(counter.items(), key=lambda item: item[1], reverse=True)}')
    sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    for item in sorted_items:
        if item[0].isalpha():
            return item[0]


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")