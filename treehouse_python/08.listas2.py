import time

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print(books[0])

books[1] = "Python for Data Analysis - Wes McKinney"
print(books[-1])
print(len(books) -1)

print("Suggested git: {}".format(books[0]))

books.insert(0, "Learning Python: Powerful Object-Oriented Programming")
print(books)

lyrics = "Books, check 'em out! "
print(lyrics[0])


craigs_lunch = "\N{TACO}"
print(craigs_lunch)

carne_asada = craigs_lunch

del craigs_lunch

print(carne_asada)

recommendation = books[0]
del books[0]

print(books.pop())
print(books.pop(0))

print("Books:")
for book in books:
    print("* " + book)

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

continents = ["Africa", "Asia", "Europe"]
for continent in continents:
    if continent[0] == "A":
        print(continent)

def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gif = wishes.pop(0)
    print("====>", suggested_gif, "<=====")
    for item in items:
        print("* " + item)
    print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
display_wishlist("Video Games", video_games)


inventory = ["shield", "apple", "sword"]
inventory.remove("apple")
print(inventory)

for item in inventory:
    inventory.remove(item)

print(inventory)

inventory = ["shield", "apple", "sword"]

for item in inventory.copy():
    inventory.remove(item)

quotes = "The greatest teacher failure is"
words = quotes.split()
print(words)

for word in words:
    print(word)
    time.sleep(.5)

























