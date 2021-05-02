import Part1 as p1
import time
import os
import sys

from colorama import init
#required colorama to be installed to work.
#variables initialised at the beginning of the script
init()

#dictionary designed to allow for the app to adapted in the future so that number of coins can be increase or the dictionary changed so that it used using different coin denominations
#the structure of the code using the dictionary would mean that nothing would need to be changed in the main body of the code when changes are made to the dictionary variables.
twoPound = False
onePound = False
fiftyp = False
twentyp = False
tenp = False
p1.currency = "GBP"
p1.min_Coin = 0
p1.max_Coin = 10000
p1.single_mult = False #this is a switch between single coin vs multiple, when single_mult is True for single coin and false for multiple
coin_dict={"selection": [twoPound, onePound, fiftyp, twentyp, tenp],
"value":[200,100,50,20,10],
"number":[0,0,0,0,0],
"coin":["£2","£1","50p","20p","10p"],
"coin_selector": [" - £2 (equivalent to 200p)"," - £1 (equivalent to 100p)"," - 50p"," - 20p"," - 10p", " - Go back to main menu"],
"counter": [1,2,3,4,5,6]}


#main menu utilises the print colour function that are present on part 1
#prompt user to select a value between 1 and 6
#user can navigate to different parts of application by selecting one of the choices available
#excepting handling used to make sure user enter in 1-6 and to prevent them from entering a value that will cause an error
def mainMenu():
    p1.prGreen("\n***Coin Sorter - Main Menu***")
    p1.prYellow("1 - Coin Calculator")
    p1.prCyan("2 - Multiple coin calculator")
    p1.prYellow("3 - Print Coin List")
    p1.prCyan("4 - Set details")
    p1.prYellow("5 - Print Configuration Settings")
    p1.prRed("6 - Quit the program")
    while True:
        try:
            selection=int(input(" Enter choice: "))
            if selection==1:
                calc_single()
                break
            elif selection==2:
                calc_mult()
                break
            elif selection==3:
                list_of_coins()
                break
            elif selection==4:
                set_details()
                break
            elif selection==5:
                config()
                break
            elif selection==6:
                break
            else:
                p1.prRed("Invalid choice. Enter 1-6")

        except ValueError:
            p1.prRed("Invalid choice. Enter 1-6")
        except KeyboardInterrupt:
            print('Warning: You pressed Ctrl + C, you will now exit the program')
            time.sleep(3)
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
    exit

#functions that retrieves the list of coins from the coin_list function on part 1. The except handling allows for the user to proceed to the main menu after pressing enter
#and there won't an error if they type something in before hand.
def list_of_coins():
    print("\nList of Coins")
    p1.coin_list()
    try:
        input(" Press enter to go back to main menu")
    except SyntaxError:
        pass
    except KeyboardInterrupt:
        print('Warning: You pressed Ctrl + C, you will now exit the program')
        time.sleep(3)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    mainMenu()

#this is the set detail sub menu, it functions in the same way as the main menu. The print functions uses the colour functions present on part 1
def set_details():
    p1.prGreen("\n***Set Details - Sub-Menu***")
    p1.prYellow("1 - Set currency")
    p1.prCyan("2 - Set minimum coin input value")
    p1.prYellow("3 - Set maximum coin input value")
    p1.prCyan("4 - Return to main menu")
    while True:
        try:

            selection=int(input("Enter choice: "))
            if selection==1:
                set_currency()
                break
            elif selection==2:
                set_min_input()
                break
            elif selection==3:
                set_max_input()
                break
            elif selection==4:
                mainMenu()
                break
            else:
                print("Invalid Choice. Enter 1-4")
        except ValueError:
            p1.prGreen("Invalid choice. Enter 1-4")
        except KeyboardInterrupt:
            print('Warning: You pressed Ctrl + C, you will now exit the program')
            time.sleep(3)
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

#This function is activated in the set details menu by selection option 2. The user is prompted to decided whether they want to change the currency.
#The user won't be able to enter a value other than Y or N. If they select N they go back to the set details menu
#If the user selects Y, they proceed to entering in one of three currency code. Once they select one of the currencies they will go back to the sub menu
#The exception handling used are to make sure the customer enters the right value and to make sure no errors occur when pressing control + c
def set_currency():
    p1.prGreen("\n***Set Currency***")
    p1.prYellow("Currency option: GBP, USD and MGA")
    p1.prCyan(f"The currency is set to {p1.currency}, would you like to change it?")
    while True:

        selection = str(input(" Select either Y or N?" )).upper()
        if selection=="Y":
            while True:
                try:
                    p1.currency = str(input("Which currency would you like to select?")).upper()
                    if p1.currency=="GBP" or p1.currency=="MGA" or p1.currency=="USD":
                        p1.prCyan(f"Thank You! You have selected {p1.currency} as your currency.\
                        \nHowever you have not been granted permissions to change the settings.")
                        time.sleep(2)
                        p1.prYellow("You will now be directed to the Set Details Menu")
                        time.sleep(2)
                        break
                    else:
                        p1.prRed("The options are GBP, MGA and USD")
                except ValueError:
                    p1.prRed("The options are GBP, MGA and USD")
                except KeyboardInterrupt:
                    print('Warning: You pressed Ctrl + C, you will now exit the program')
                    time.sleep(3)
                    try:
                        sys.exit(0)
                    except SystemExit:
                        os._exit(0)
            break
        elif selection=="N":
            p1.prGreen("You will now be directed to the Set Details Menu")
            time.sleep(2)
            break
        else:
            p1.prRed("Error!")
    set_details()


#This function is activated in the set details menu by selection option 2. The user is prompted to decided whether they want to change the minimum input.
#The user won't be able to enter a value other than Y or N. If they select N they go back to the set details menu
#If the user selects Y, they proceed to entering in the new value. This has to be numeric and once they have entered a value they will be told it won't have any effect and sent back to the sub menu
#The exception handling used are to make sure the customer enters the right value and to make sure no errors occur when pressing control + c
def set_min_input():
    while True:

        selection = str(input(f"The current minimum input is set to {p1.min_Coin}p GBP.\nWould you like to change it? Select either Y or N? ")).upper()
        if selection=="Y":
            while True:
                try:
                    min_input = int(input("Enter the new value: "))
                    if not min_input > 0:
                        p1.prRed("Enter a value greater than 0")
                    else:
                        break
                except ValueError:
                    p1.prRed("Enter a numeric value")
                except KeyboardInterrupt:
                    print('Warning: You pressed Ctrl + C, you will now exit the program')
                    time.sleep(3)
                    try:
                        sys.exit(0)
                    except SystemExit:
                        os._exit(0)

            time.sleep(1)
            p1.prRed(f"Whoops!! Unfortunately you don't have permission to change the value from {p1.min_Coin}p to {min_input}p")
            p1.prPurple("You will now be directed to the Set Details Menu")
            time.sleep(2)
            break
        elif selection=="N":
            p1.prPurple("You will now be directed to the Set Details Menu")
            time.sleep(2)
            break
        else:
            p1.prRed("Error")


    set_details()


#This function is activated in the set details menu by selection option 3. The user is prompted to decided whether they want to change the maximum input.
#The user won't be able to enter a value other than Y or N. If they select N they go back to the set details menu
#If the user selects Y, they proceed to entering in the new value. This has to be numeric and once they have entered a value they will be told it won't have any effect and sent back to the sub menu
#The exception handling used are to make sure the customer enters the right value and to make sure no errors occur when pressing control + c
def set_max_input():
    while True:
        selection = str(input(f"The current maximum input is set to {p1.max_Coin}p GBP.\nWould you like to change it? Select either Y or N? ")).upper()
        if selection=="Y":
            while True:
                try:
                    max_input = int(input("Enter the new value: "))
                    if not max_input > 0:
                        p1.prRed("Enter a value greater than 0")
                    else:
                        break
                except ValueError:
                    p1.prRed("Enter a numeric value")
                except KeyboardInterrupt:
                    print('Warning: You pressed Ctrl + C, you will now exit the program')
                    time.sleep(3)
                    try:
                        sys.exit(0)
                    except SystemExit:
                        os._exit(0)
            time.sleep(1)
            p1.prRed(f"Whoops!! Unfortunately you don't have permission to change the value from {p1.max_Coin}p to {max_input}p")
            p1.prRed("You will now be directed to the Set Details Menu")
            time.sleep(2)
            break
        elif selection=="N":
            p1.prPurple("You will now be directed to the Set Details Menu")
            time.sleep(2)
            break
        else:
            p1.prRed("Error")
    set_details()

def config():
    p1.config_text()
    try:
        input("\n Press enter to go back to main menu")
    except SyntaxError:
        pass
    mainMenu()




#This is activated when Single coin is selected. It initialises the coin_dict with new values
#to prevent the previous running of this function from having an impact on the final outcome
#For this calculator the coin_dict["selection"] bools are set to False as the user will be selecting the coins in the select_coin function
#single_mult has been toggled to True which lets the application know to select coin in p1.select_coin which will set the coin_dict["selection"][index] to True if selected
#The stay bool is used to break out of the loop if the user tries to go back to main menu
#amount_calc is the function which is used by both single and multiple coins, see below.
#The remainder will be printed out in this function before proceeding to the main menu
def calc_single():
    global coin_dict
    coin_dict={"selection": [twoPound, onePound, fiftyp, twentyp, tenp],
    "value":[200,100,50,20,10],
    "number":[0,0,0,0,0],
    "coin":["£2","£1","50p","20p","10p"],
    "coin_selector": [" - £2 (equivalent to 200p)"," - £1 (equivalent to 100p)"," - 50p"," - 20p"," - 10p", " - Go back to main menu"],
    "counter": [1,2,3,4,5,6]}

    p1.amount = 0
    coins = [False, False,False, False, False]
    coin_dict["selection"] = coins
    p1.single_mult = True
    p1.prGreen("\n***Single Coin Calculator***")
    while True:
        p1.prPurple("\nWhich coin would you like to select")

        p1.select_coin(coin_dict, p1.single_mult)
        if p1.stay==False:
            break
        amount_calc()

        p1.prGreen(f"The amount remaining is {p1.amount}p.")
        break
    mainMenu()

#This is activated when Multiple Coin is selected. It initialises the coin_dict with new values
#to prevent the previous running of this function from having an impact on the final outcome
#For this calculator the coin_dict["selection"] bools are set to True as the user will be deselecting the coins in the select_coin Function
#single_mult has been toggled to False which lets the application know to deselect coin in p1.select_coin, which will set the coin_dict["selection"][index] to False is selected
#The stay bool is used to break out of the loop if the user tries to go back to main menu
#amount_calc is the function which is used by both single and multiple coins, see below
#The remainder will be printed out in this function before proceeding to the main menu

def calc_mult():
    global coin_dict
    coin_dict={"selection": [twoPound, onePound, fiftyp, twentyp, tenp],
    "value":[200,100,50,20,10],
    "number":[0,0,0,0,0],
    "coin":["£2","£1","50p","20p","10p"],
    "coin_selector": [" - £2 (equivalent to 200p)"," - £1 (equivalent to 100p)"," - 50p"," - 20p"," - 10p", " - Go back to main menu"],
    "counter": [1,2,3,4,5,6]}
    p1.amount = 0
    p1.single_mult = False
    coins = [True, True, True, True, True]
    coin_dict["selection"] = coins

    p1.prGreen("\n***Multiple Coin Calculator***")
    while True:
        p1.prPurple("\nWhich coin would you like to exclude")
        p1.select_coin(coin_dict, p1.single_mult)
        if p1.stay==False:
            break
        amount_calc()

        p1.prGreen(f"The amount remaining is {p1.amount}p.")
        time.sleep(1)
        break
    mainMenu()

#This function is used by the single and multiple coin calculator by first informing the user to enter an amount and then using
#the p1.amount function from part 1 to gather the Information
#The coin_dict dictionary is then looped through twice to find the coins the customer's picked
#if they picked a coin select == True and calculator function (p1.calc) is used to work out how many coins there are in a given amount
#Finally the results are printed out in Green and a delay is used so that the information isn't thrown at once to the user

def amount_calc():

    p1.prPurple("\nHow much would you like to convert?")
    p1.prYellow(f"Enter in a value up to {p1.max_Coin}p to be converted")
    p1.amount = p1.select_amount(p1.amount)
    for key, list in coin_dict.items():
        if key=="selection":
            for count, select in enumerate(list):
                if select==True:
                    p1.calc(coin_dict, count)
                    if coin_dict["number"][count]>0:
                        p1.prGreen("There are " + str(coin_dict["number"][count]) + " " + coin_dict["coin"][count] + " coin(s)")
                        time.sleep(1)

#if this script is run, then main is true and the main Menu will be loaded
if __name__ == "__main__":
    mainMenu()
