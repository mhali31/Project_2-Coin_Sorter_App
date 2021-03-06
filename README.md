# Project_2-Coin_Sorter_App

IN4.0 Group Capstone Project 2 - Collaborated with Georgios Evangelinos during this project. My contributions was the Solution Design, Development and Test Plan. 

Part 1:
You are required to develop a coin sorting program, using Pound sterling (£) as the default currency. Note: 1 pound is equal to 100 pennies e.g. £1 = 100p.
The following coins (in order of priority) are in circulation in the scope of this program:
• £2 (equivalent to 200p)
• £1 (equivalent to 100p)
• 50p
• 20p
• 10p
Do not add any additional coins. The minimum input value for exchange in pennies is 0 (inclusive). The maximum input value for exchange in pennies is capped at 10,000 (inclusive). The program should enable the user to check how many coins of a certain denomination can be exchanged given an input value in pennies and the denomination. It should also print the remainder. For example, given the input value of 352 pennies and the input denomination of £1 coins, the output should be three £1 coins and a remainder of 52p.
Given a total value in pennies and a coin denomination to exclude, the program should also allow the user to determine how many coins and what denominations (prioritising the higher denominations) they can exchange for while excluding a certain coin denomination. The remainder should also be printed. For example, given 563 pennies and excluding the £2 coin, we can exchange for five £1 coins, one 50p coin and one 10p coin, with a remainder of 3p.
The user should also be able to print the current configurations of the program (current currency, min/max coin to exchange). Finally, the user should be able to covert from pounds sterling to US dollars AND Malagasy ariary using a real time currency converter such as https://free.currencyconverterapi.com/.

Part 2:
Create a text menu for the coin sorter. The user should be presented with the following menu:
Coin Sorter - Main Menu
1 - Coin calculator
2 - Multiple coin calculator
3 - Print coin list
4 - Set details
5 - Display program configurations
6 - Quit the program
These menu choices should be repeated until the user quits. Option 1 and 2 should prompt the user to enter some values, where the input values should be validated before being passed to the relevant methods in order to generate some results.
When Option 4 is chosen, the user should be presented with the following sub-menu allowing them to interactively set the following details for the program:
Set Details Sub-Menu
1 - Set currency
2 - Set minimum coin input value
3 - Set maximum coin input value
4 - Return to main menu
These menu choices should be repeated until the user chooses Option 4 in the Sub-Menu and returns to the main menu. Again, all user input values should be validated.

Part 3:
Create a GUI for the menu. The user should be presented with a graphical menu based on the structure of the textual menu created in Part 2. You should make any changes necessary to the original text menu code to meet the requirements of Part 3.
You can use either PyQT or PyGUI. The technology choice has no impact on the marking process; you should ensure that the GUI components are:
• Appropriately selected for the intended purpose e.g. you shouldn’t use checkboxes for menu options.
• You should investigate and implement a range of GUI components e.g. the GUI shouldn’t only consist of a single textbox duplicated across all options.
• All information and options are clearly indicated in the design e.g. the user can intuitively understand what, where and how information should be input/output.
