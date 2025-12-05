import random

def text(prompt):
    value = input(prompt).strip()
    while not value:
        value = input("Input can't be empty. Try again: ").strip()
    return value


def num(prompt):
    value = input(prompt).strip()
    while not value.isdigit():
        value = input("Please enter a numeric value: ").strip()
    return int(value)

print("Choose a story template: ")
print("1. Magical Adventure")
print("2. Space Trouble")
print("3. Vacation Disaster")
print("4. (<Random story>)")

choice = input("Choose which story you want: ").strip()

while choice not in ["1", "2", "3", "4"]:
    choice = input("Please choose 1, 2, 3, or 4: ").strip()


if choice == "4":
    choice = random.choice(["1", "2", "3"])
    print(f"Randomly selected template: {choice}")

PName = text("Input Person Name: ")
noun = text("Input noun: ")
adj1 = text("Input adjective(feeling): ")
verb1 = text("Input verb: ")
adj2 = text("Input adjective(feeling): ")
animal = text("Input an animal: ")
verb2 = text("Input verb: ")
color1 = text("Input a color: ")
verb_ing = text("Input a verb + ing: ")
adverb = text("Input an adverb: ")
num1 = num("Input a number: ")
measure = text("Measure of time: ")
color2 = text("Input another color: ")
animal2 = text("Input another animal: ")
num2 = num("Input a number: ")
silly_word = text("Input a silly word: ")
noun2 = text("Input a noun again: ")

# Story1
story1 = f"""
One {measure}, {PName} discovered a {color1} portal behind a {noun}.
Feeling {adj1}, they decided to {verb1} through it.
On the other side, a {animal} wearing a {color2} hat was {verb_ing}.
"{silly_word}!" shouted {PName}, feeling {adj2}.
It was the beginning of a truly {adverb} journey with {num1} {noun2}s and {num2} {animal2}s.
"""


# Story 2
story2 = f"""
Captain {PName} boarded the {silly_word} spaceship with their loyal {animal}.
They had exactly {num1} seconds to stop the {color1} comet!
Feeling {adj1}, the captain tried to {verb1}, but the controls were {adj2}.
The ship started {verb_ing} toward a {color2} planet full of {animal2}s.
In the end, they saved the galaxy using a {noun} and {num2} {noun2}s.
"""


# Story 3
story3 = f"""
{PName} went on vacation with a {animal} and a {noun}.
Everything was perfect until it started {verb_ing} nonstop!
The hotel turned {color1} and smelled like {silly_word}.
Feeling {adj1} but still {adverb}, {PName} decided to {verb1} into the ocean.
A {color2} {animal2} stole their {noun2}, but they laughed for {num1} {measure}.
It was the most {adj2} trip ever — {num2} stars out of ten!
"""


if choice == '1':
    print(story1)
elif choice == '2':
    print(story2)
elif choice == '3':
    print(story3)
