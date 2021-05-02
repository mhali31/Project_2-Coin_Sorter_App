import requests
import time
from colorama import init

import os
import sys

#required to install requests, colorama for this script to work
#variables to initialise the script
#initialise variables when script is not main
min_Coin = 0 #minimum amount the user can input
max_Coin = 10000
amount = 0 #the amount the user selects to convert into coins
single_mult = False #this is a switch between single coin and multiple, where single_mult is True for single coin and false for multiple coin
stay = False #used to break out a while loop in single and multiple coin functions in part 2
remainder = 0 #the amount remaining after the calculator has been run.

#the currency selected when the scripts are ran
currency = "GBP"
cf_currency = f"The currency selected is {currency}"
cf_min = f"The Minimum value you can input is {min_Coin}p"
cf_max = f"The Maximum value you can input is {max_Coin}p"

twoPound = False
onePound = False
fiftyp = False
twentyp = False
tenp = False
coin_dict={"selection": [twoPound, onePound, fiftyp, twentyp, tenp],
"value":[200,100,50,20,10],
"number":[0,0,0,0,0],
"coin":["£2","£1","50p","20p","10p"],
"coin_selector": [" - £2 (equivalent to 200p)"," - £1 (equivalent to 100p)"," - 50p"," - 20p"," - 10p", " - Go back to main menu"],
"counter": [1,2,3,4,5,6]}

#outcome = []

#init is from colorama to allow the print in colour functions to be used
init()
##https://www.geeksforgeeks.org/print-colors-python-terminal/ is the location that the print in colour was obtained from.
#printing in colour in the terminal was utilised to help with readability when running part 2
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def inLightGray(skk): input("\033[97m {}\033[00m" .format(skk))


#main menu function - no longer in use
def Menu():
    print("\n***Coin Sorter - Main Menu***")
    print("3 - Print Coin List")
    print("4 - Print Configuration")
    print("5 - Currency Converter")
    print("6 - Exit")
    while True:
        try:
            selection=int(input("Enter choice: "))

            if selection==3:
                coin_list()
                break
            elif selection==4:
                config()
            elif selection==5:
                currency_Converter()
            elif selection==6:
                break
            else:
                print("Enter a valid selection")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-6")
    exit


#this function is used in part 2 for the single and multiple coin selector. It will allow the user to deselect or select the coins they want depending on the function activated.
#in the first for loop the dictionary is looped through to create the list of coins option the user will see. The avail_function is the variable which is created and then printed on screen
#if the user is deselecting more than one coin, the list will decrease, this is done by removing the selected option from the list that has been created
#Therefore, when the list is recreated because of the while loop it will contain less entries.
#when selecting the coins, the select_mult variable will be utilised to make sure that the bool is toggled to True or False based on whether single coin or multiple coin is selected.
#stay bool is used to break out of the loop in the cal_mult and cal_single functions in part 2, so that the user can go back to the main menu if selecting False
#for the multiple coin option the user will be prompted to see whether they want to select more coins, if they select N, the coins selected will be printed and they will proceed to select an amount
#if they select Y the loop will continue and the new options will appear until there is only one left, which will lead the user to proceed to selecting an amount with the final coin not selected.
#cont bool is used to break out of the while loop.Exception handling has been utilised to prevent user from selecting an option that is not available and to prevent error message when Ctrl C is pressed.
def select_coin(coin_dict, single_mult):

    global stay
    stay = True

    for key, list in coin_dict.items():
            if key=="coin_selector":
                cont=True
                while cont==True or single_mult==False:
                    for select, count in zip(list, coin_dict["counter"]):
                        avail_options = str(count) + select
                        prYellow(avail_options)
                    try:
                        selection=int(input(" Enter choice: "))
                        for i, count in enumerate(coin_dict["counter"]):
                            if selection==count and not selection==6:
                                if single_mult == True:
                                    coin_dict["selection"][count-1] = True

                                    cont=False
                                    break
                                elif single_mult==False:
                                    coin_dict["selection"][count-1] = False
                                    list.remove(coin_dict["coin_selector"][i])
                                    coin_dict["counter"].remove(count)
                                    #print(counter, list)
                                    while True:
                                        try:
                                            answer = str(input(" Would you like to deselect more coins, Y or N? ")).upper()
                                            current=[]
                                            if answer=="Y":
                                                prGreen("\nThe following coins are currently selected")
                                                for key, select in enumerate(coin_dict["selection"]):
                                                    if select==True:
                                                        current.append(coin_dict["coin"][key])
                                                prYellow(", ".join(current))
                                                print("\n")

                                                if len(current) == 1:
                                                    single_mult = True
                                                    cont=False
                                                    break
                                                time.sleep(0.5)
                                                break
                                            elif answer=="N":
                                                prGreen("\nThe following coins have been selected:")
                                                for key, select in enumerate(coin_dict["selection"]):
                                                    if select==True:
                                                        current.append(coin_dict["coin"][key])
                                                prYellow(", ".join(current))
                                                print("\n")
                                                single_mult = True
                                                cont=False
                                                break
                                                time.sleep(0.5)
                                        except ValueError:
                                            print("\nEnter a valid selection")
                                        except KeyboardInterrupt:
                                            print('Warning: You pressed Ctrl + C, you will now exit the program')
                                            time.sleep(3)
                                            try:
                                                sys.exit(0)
                                            except SystemExit:
                                                os._exit(0)
                            elif selection==6:
                                stay=False
                                single_mult = True
                                cont=False
                                break

                    except ValueError:
                        prGreen("\nEnter a valid selection\n")
                    except KeyboardInterrupt:
                        print('Warning: You pressed Ctrl + C, you will now exit the program')
                        time.sleep(3)
                        try:
                            sys.exit(0)
                        except SystemExit:
                            os._exit(0)



#function used to prompt the user to enter in an amount. limitations on the value set, has to be an integer between 0 and 10000 (inclusive for both)
#if a value is accepted it will be printed onto the screen for a final response the the user
#This function is only used in part 2, and it is utilised by both single and multiple coin options
def select_amount(amount):
    global max_Coin
    global min_Coin
    while True:
        try:
            value = int(input("Enter the amount here: "))

            if (value<=max_Coin) and (value>=min_Coin):
                prGreen(f"\n From a value of {value}p")
                return value
                break
            else:
                prPurple("\ntry again!")
                prRed(f"\nEnter a value between 0 and {max_Coin}p\n")
        except (TypeError, ValueError):
            prPurple("\ntry again!")
            prRed(f"\nEnter a value between 0 and {max_Coin}p\n")

        except KeyboardInterrupt:
            print('Warning: You pressed Ctrl + C, you will now exit the program')
            time.sleep(3)
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)


#used by both part 2 and 3 to calculate the amount of coins needed, assuming the user has selected it
#this is actually being ran in a For loop in both part 2 and 3 so that the count continually increases
#until the list has being iterated through. In the If statement, the number of coins are stored the coin_dict["number"] list and the coin_dict["coin"] is used to get the actually coin i.e £2 or 50p etc
#the amount is then set to the remainder calculated used the modulo operator function
#This function is used for both single and multiple coins selection
def calc(coin_dict, count):
    global amount
    global remainder

    if coin_dict["selection"][count]==True and amount>=coin_dict["value"][count]:
        coin_dict["number"][count] = amount//coin_dict["value"][count]
        remainder=amount%coin_dict["value"][count]
        coin_dict["selection"][count]=False
        number_of_coins = coin_dict["number"][count]
        coin_denom = coin_dict["coin"][count]

        #prGreen(f"There are {number_of_coins} {coin_denom} coins")
        time.sleep(1)
        amount = remainder
        return coin_dict, count


#coin list simply prints out the list of coins available in Yellow
def coin_list():
    prYellow("1. £2 (equivalent to 200p)")
    prYellow("2. £1 (equivalent to 100p)")
    prYellow("3. 50p")
    prYellow("4. 20p")
    prYellow("5. 10p")


#part 1 configuration settings simply prints of the config settings
def config():
    config_text()
    selection  = input("Press enter to go back to main menu")
    if selection == "":
        Menu()
#Prints out the configuration settings of the application. Variables are global
# and initialised at the top of the script. Will be called for in Part 1 and Part 2
def config_text():
    global cf_currency
    global cf_min
    global cf_max
    prGreen("\n\nConfiguration Settings\n")
    prCyan(cf_currency)
    prYellow(cf_min)
    prCyan(cf_max)

#currency converter - no error handling was used and will lead to fails if the user did not enter one of three choices
#was not altered to work perfectly like other functions because it is not in use. Would be similar to the set_currency coding structure if it was being utilised
def currency_Converter():
    #user enters in the currency code they want to convert to
    cur=input("Which currency would you like to convert to, USD or MGA? ").upper()
    #dictionary with the conversion code
    currency = {"USD": "GBP_USD", "MGA": "GBP_MGA"}
    #f string used so that the users selection allows for a dictionary of the right code to be entered
    #if the dictionary had more entries can easily be used to get any currency conversion
    r = requests.get(f"https://free.currconv.com/api/v7/convert?q={currency[cur]}&compact=ultra&apiKey=f607d3bc919cc7f49347")
    #the currency exchanged rate converted into a readable format.
    # r.json() type is dictionary, therefore, we are using currency[cur] to extract a value from it
    conversion_rate = r.json()[currency[cur]]
    #user enters the amount they want to convert
    amount = int(input("How much in GBP pence would you like to convert? "))
    #prints the calculated amount they would receive from the transaction
    print(f"Based on the current rate, you will receive {amount/100*conversion_rate} {cur}")
    time.sleep(2)
    #user prompted to press enter to go back to the main menu
    selection  = input("Press enter to go back to main menu")
    if selection == "":
        Menu()


#executing the code when this is ran on its own - No longer active after major modifications to the code
if __name__ == "__main__":
    Menu()
