while True:
    try:
        noun1 = input("Enter a noun (person, place or thing): ")
        float(noun1)
    except ValueError:
        break
    else:
        continue

while True:
    try:
        adjective1 = input("Enter an adjective (description): ")
        float(adjective1)
    except ValueError:
        break
    else:
        continue

while True:
    try:
        verb1 = input("Enter a verb in the present continuous tense (ending in 'ing'): ")
        float(verb1)
    except ValueError:
        break
    else:
        continue

print(f"Today I went to a {adjective1} scrapyard.")
print(f"Over there, I saw a {noun1}.")
print(f"The {noun1} was {verb1}")