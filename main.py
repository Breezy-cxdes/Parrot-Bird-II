class Parrot:
    # Class attribute
    species = "bird"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# Access the class attribute
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# Access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


        