import turtle #used to draw

#function to display square using basic print statements
def square():
    print("........")
    print(".      .")
    print(".      .")
    print("........")

#function to display a triangle
def triangle():
    size = int(input("Pick a number between 1 and 5 to determine size - ")) #user chooses how big the shape is
    if 0 < size < 6: #keeping size within boundaries
        s = size
        t = 1
        u = ' '
        print('.')
        while s != 0: #iterates till shape is created
            print('.' + (t*u) + '.' )
            s=s-1
            t=t+1
        print((size+3) * '.')
    else:
        print("That's not a valid size")
        triangle() #restarts function

#function to display a circle
def circle():
    radius = int(input("How big would you like the circle? - "))
    if radius < 1: #size has to be positive
        print("That's not possible, try again")
        circle() #restarts function
    else:
        t=turtle.Turtle()
        r=radius * 10 #to make single digits radii more visible
        t.circle(r)

#function to choose to try again
def redo():
    again = input("Would you like to try again? (y or n) - ").lower()
    if again == "y":
        main() #restarts main function
    else:
        print("Bye :)")
        exit() #stops code

#main function to determine shape and redirect to other functions
def main():
    print('What shape would you like me to draw?')
    shape = input().lower() #so input is not case sensitive

    if shape == 'square':
        square()

    elif shape == 'triangle':
        triangle()
    elif shape == 'circle':
        circle()
    else:
        print("Sorry, i don't know how to draw that :(")

    redo()

main()