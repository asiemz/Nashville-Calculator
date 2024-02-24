

class Main:
    def __init__(self):

        people = int(input('Enter number of people going to Smashville: '))

        totalPrice = float(input('Enter the price of the AirBnB: '))

        ppp = totalPrice/people

        alexaDaniTotal = ppp/2

        remainder = alexaDaniTotal * 2

        newTotalPrice = totalPrice - remainder

        newppp = newTotalPrice/(people-2)

        print(f'The total price for people staying the whole time would be {newppp}, the price for Alexa and Dani would be {alexaDaniTotal}, ')

Main()
input("press Enter to exit...")


