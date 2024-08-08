from wines import wine_list

wines = wine_list.keys()

tags = []
# Collect input on wine body
print("What level of body do you like in wine? (light, medium, full) ")
while True:
    body = input("> ")
    if body in ["light", "medium", "full"]:
        tags.append(body + "-bodied")
    elif body == "":
        break
    else:
        print("Please enter 'light', 'medium', or 'full'.")

# Collect input on wine sweetness
print("What sweetness do you like in wine? (absolute dry, very dry, dry, semi-dry, sweet)")
while True:
    sweetness = input("> ")
    if sweetness in ["absolute dry", "very dry", "dry", "semi-dry", "sweet"]:
        tags.append(sweetness)
    elif sweetness == "":
        break
    else:
        print("Please enter 'dry', 'semi-dry', or 'sweet'.")

# Collect input on wine color
print("What colour of wine do you prefer? (white, red, rose)")
while True:
    color = input("> ")
    if color in ["white", "red", "rose"]:
        tags.append(color)
    elif color == "":
        break
    else:
        print("Please enter 'white', 'red', or 'rose'.")

# Collect input on wine flavors
print("What flavors do you like in wine? (apple, pear, orange, gooseberry, citrus, floral, spice, tropical, berries, butter, oak, strawberry, cherry, plum, peppercorn, raspberry, mushroom, dark chocolate, vanilla, honey, apricot, peach, lychee, toasty, mineral, earthy, pipe tobacco, cranberry)")
while True:
    flavor = input("> ")
    if flavor in ["apple", "pear", "orange", "gooseberry", "citrus", "floral", "spice", "tropical", "berries", "butter", "oak", "strawberry", "cherry", "plum", "peppercorn", "raspberry", "mushroom", "dark chocolate", "vanilla", "honey", "apricot", "peach", "lychee", "toasty", "mineral", "earthy", "pipe tobacco", "cranberry"]:
        tags.append(flavor)
    elif flavor == "":
        break
    else:
        print("Please enter a valid flavor.")

# Find wines that match the user's preferences
matches = {}
for wine in wines:
    count = 0
    for tag in set(tags):
        if tag in wine_list[wine]:
            count += 1
    matches[wine] = count / len(wine_list[wine])

sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)

print("Here are some wines that match your preferences:")
print(str(sorted_matches[0][0]) + " (" + str(int(sorted_matches[0][1]*100)) + "% match)")
print(str(sorted_matches[1][0]) + " (" + str(int(sorted_matches[1][1]*100)) + "% match)")
print(str(sorted_matches[2][0]) + " (" + str(int(sorted_matches[2][1]*100)) + "% match)")

print("\nHere are some wines that don't match your preferences:")
print(str(sorted_matches[-1][0]) + " (" + str(int(sorted_matches[-1][1]*100)) + "% match)")
print(str(sorted_matches[-2][0]) + " (" + str(int(sorted_matches[-2][1]*100)) + "% match)")
print(str(sorted_matches[-3][0]) + " (" + str(int(sorted_matches[-3][1]*100)) + "% match)")



