#Grace Anspach and Saerin Bong
#7
dict={
"apple":"red",
"banana":"yellow",
"pear":"green",
"blueberry":"blue"
}

a=dict.values()
print(a)

#5
dict={
"Stephen King":"The Shining",
"Tolkien":"The Lord of the Rings",
"The Book Thief":"Zusak"
}

a=dict.keys()
print(a)

#8

guess=int(input("Guess the number:"))
def random(guess):
    import random
    n=random.randint(1,10)
    if n==guess:
        print("Conrgatulations, you guessed the number!")
    else:
        print("Sorry, try again!")

random(guess)
