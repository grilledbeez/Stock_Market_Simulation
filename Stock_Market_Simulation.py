import random
from time import sleep
# import tkinter


"""
QUESTIONS/GOALS
Would I need to directly define each company and it's info?
Will I have to use "+=" to keep the values true through each year?
Should I make it Oregon Trail Style???
How would I implement a candlestick graph
Add random economic events that effect the economy
"""

#STOCK MARKET SIMULATION

MIN_REV = 5000000
MAX_REV = 150000000

#BASE BUSINESS INFO

"""
businesses = [("Amazon"), ("Target"), ("Walmart"), ("Tesla"),
              ("Sony"), ("Apple"), ("ESPN"), ("Tiktok")]

businesses1 = [("Amazon", 1), ("Target", 2), ("Walmart", 3), ("Tesla", 4),
              ("Sony", 5), ("Apple", 6), ("ESPN", 7), ("Tiktok", 8)]
"""

#FIRST ATTEMPT AT ASSIGNING NEW BUSINESSES

# BusinessName = [Name, Start Base Revenue, Base Share Percentage, Percent of Increase/Decrease, True or False if Projection Should Be Displayed]
amazon = ["amazon", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
target = ["target", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
walmart = ["walmart", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
nike = ["nike", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
apple = ["apple", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
microsoft = ["microsoft", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
disney = ["disney", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
tesla = ["tesla", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]
meta = ["meta", random.randint(MIN_REV, MAX_REV), (round(random.uniform(0.01, 0.1), 2)), (round(random.uniform(.95, 1.05), 3)), False]



businesses = [amazon, target, walmart, nike, apple, microsoft, disney, tesla, meta]
business_names = [amazon[0], target[0], walmart[0], nike[0], apple[0], microsoft[0], disney[0], tesla[0], meta[0]]
cap_business_names = ["Amazon", "Target", "Walmart", "Nike", "Apple", "Microsoft", "Disney", "Tesla", "Meta"]
my_stocks = []
invest_choices = []


def rules():
    print("Welcome to the Stock Market Simulation!")
    input("Press Enter to begin...")
    print("RULES")
    sleep(1)
    print("    Investing:\n•You can only invest in a certian company once per year\n•You have the option to go into debt when investing")
    sleep(1)
    print("    Researching Stocks: \n•You can only research 3 businesses per year \n•There is a 60% chance that your research is correct ")
    sleep(1)
    print("    Stocks:\n•Your stocks change in value after a year\n•You can sell your stocks whenever needed\n•Stocks may have an unknown projection value")
    sleep(1)
    print("WARNING: THIS IS JUST A SIMULATION. THIS HAS NO CORRELATION WITH THE REAL STOCK MARKET")
    input("Press Enter to continue...")


def research(search):
    #index = 0
    # Index
    for company in businesses:
        if search == company[0]:
            company[4] = True
        # if search == index:
        #     business_info(company)
            #RESEARCH ON WHAT INFO WILL BE NEEDED
        # else:
        #     business_info("N")

def add_stock(stock_name, price, stock_projection):
    # print(stock_name)
    arrow = ""
    for company in cap_business_names:
        if company == stock_name:
            my_stock = [stock_name, price, stock_projection]
            if stock_projection == "???":
                print("Stock: [" + my_stock[0] + " / $" + str(my_stock[1]) + " / Stock: ???]")
                sleep(.5)
                my_stocks.append(my_stock)
            else:
                if my_stock[2] > 1:
                    arrow = "↗"
                elif my_stock[2] < 1:
                    arrow = "↘"
                elif my_stock[2] == 1:
                    arrow = "→"
                print("Stock: [" + my_stock[0] + " / $" + str(my_stock[1]) + " / Stock: " + str(my_stock[2]) + "% " + arrow + "]")
                sleep(.5)
                my_stocks.append(my_stock)

            #RUNS ACCORDING TO PLAN

    #stock_name = business_name
    #business_name = [stock_name, price, stock_projection]

def buy_stock(price, CASH, stock_name, stock_projection):
    if CASH < price:
        print("You don't have enough money")
        sleep(.5)
        debt = input("Would you like to go into debt(Y/N)? ")
        sleep(.2)
        debt = debt.upper()
        global NEWCASH
        if debt == "Y":
            FIRSTCASH = CASH
            CASH = round(CASH - price, 2)
            add_stock(stock_name, price, stock_projection)
            NEWCASH = CASH
            print("$" + str(FIRSTCASH) + " - $" + str(price) + " = $" + str(CASH) + " (Please never do this in real life)")
            print("-------------------------")
        elif debt != "N":
            print("Please type \"Y\" or \"N\"")
        else:
            print("You did not purchase a stock")
    elif CASH >= price:
        FIRSTCASH = CASH
        # global NEWCASH
        CASH = round(CASH - price, 2)
        NEWCASH = CASH
        sleep(.5)
        add_stock(stock_name, price, stock_projection)
        print("$" + str(FIRSTCASH) + " - $" + str(price) + " = $" + str(CASH))
        print("-------------------------")
        #print("buy stock")


def check_search(search, guesses):
    if search in guesses:
        print("You have already researched this business.")
        sleep(.5)
    # elif search <= 0 or search >= (len(businesses) + 1):
    #     print("You must type the corresponding number with the company")
    elif search not in business_names:
        print("This business does not exist")
        sleep(.5)
    # else:
    #     print(search)

def company_graph(company):
    print("")


def company_info():
    index = 0
    arrow = ""
    for company in businesses:
        if company[4] == True:
            if company[3] > 1:
                arrow = "↗"
            elif company[3] < 1:
                arrow = "↘"
            elif company[3] == 1:
                arrow = "→"
            print("Company Name: " + cap_business_names[index] +
                  "\nBase Revenue:  $" + str(company[1]) +
                  "\nBase Share Percentage: " + str(company[2]) + "%" +
                  "\nStock Projection: " + str(company[3]) + "% " + arrow +
                  "\n-------------------------")
            sleep(.6)
            index += 1
        else:
            print("Company Name: " + cap_business_names[index] +
                  "\nBase Revenue:  $" + str(company[1]) +
                  "\nBase Share Percentage: " + str(company[2]) + "%" +
                  "\nStock Projection: " + "???" +
                  "\n-------------------------")
            sleep(.6)
            index += 1
    input("Press Enter to continue... ")


def print_business_names():
    index  = 1
    sleep(.25)
    for name in cap_business_names:
        print(str(index) + ". " + name)
        sleep(.25)
        index += 1

def invest():
    print_business_names()
    sleep(.4)
    print("What company would you like to invest in? (COMPANY NAME)")
    investing = (input(""))
    investing = investing.lower()
    if investing not in business_names:
        print("This business does not exist, remember to type the BUSINESS NAME!")
    elif investing in invest_choices:
            print("You have already invested in this company!")
            #investing == "INVALID"
    else:
        invest_choices.append(investing)
        index = 0
        for company in businesses:
            if investing == company[0]:
                saved_index = index
                global price
                price = (round(company[1] * (company[2] * .01), 2))
                #check_money(price)
                print("-------------------------")
                sleep(.2)
                print(cap_business_names[index] + " Revenue: $" + str(company[1]))
                sleep(.2)
                print("The price of " + cap_business_names[index] + "'s " + str(company[2]) + "% stock is $" + str(price))
                sleep(.2)
                if company[4] == True:
                    stock_projection = company[3]
                    if company[3] > 1:
                        print(cap_business_names[index] + "'s stock is projected to increase at " + str(company[3]) + "% (RESEARCHED)")
                    elif company[3] == 1:
                        print(cap_business_names[index] + "'s stock is projected to stay the same (RESEARCHED)")
                    else:
                        print(cap_business_names[index] + "'s stock is projected to decrease at " + str(company[3]) + "% (RESEARCHED)")
                    sleep(.2)
                else:
                    stock_projection = "???"
                    print(cap_business_names[index] + "'s stock projection is UNKNOWN (NOT RESEARCHED)")
                sleep(.2)
            index += 1
        yorn = (input("Invest in " + cap_business_names[saved_index] + " (Y/N)? "))
        yorn = yorn.upper()
        stock_name = cap_business_names[saved_index]
        sleep(.5)
        if yorn == "Y":
            buy_stock(price, CASH, stock_name, stock_projection)
            sleep(1)
        elif yorn != "N":
            print("Please type \"Y\" or \"N\"")
            sleep(1)
        else:
            print("You did not purchase a stock")
            sleep(1)


def stocks():
    arrow = ""
    index = 1
    print("Your Stocks: ")
    sleep(.85)

    if len(my_stocks) == 0:
        print("[NONE]")
        sellQ = False
    else:
        for stock in my_stocks:
            if stock[2] == "???":
                print(str(index) + ". [" + stock[0] + " / $" + str(stock[1]) + " / Stock: ???]")
                sleep(.7)
                index += 1
            else:
                if stock[2] > 1:
                    arrow = "↗"
                elif stock[2] < 1:
                    arrow = "↘"
                else:
                    arrow = "→"
                print(str(index) + ". [" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "% " + arrow + "]")
                sleep(.7)
                index += 1
            #print("!!!!!!! " + stock[0:1])

def sell_stocks():
    sleep(1)
    if len(my_stocks) == 0:
        print("You don't have any stocks to sell!")
    else:
        index = 1
        stocks()
        print("Which stock would you like to sell? (TYPE THE CORRESPONDING NUMBER)")
        stocky = int(input(""))
        sleep(.5)
        global NEWCASH
        for stock in my_stocks:
            if (stocky <= 0) or stocky >= len(my_stocks) + 1:
                print("Please type the corresponding number!")
                sleep(.8)
            elif stocky == index:
                if stock[2] == "???":
                    print(str(index) + ". [" + stock[0] + " / $" + str(stock[1]) + " / Stock: ???]")
                    FIRSTCASH = NEWCASH
                    print("$" + str(FIRSTCASH) + " + $" + str(stock[1]) + " = $" + str(round(NEWCASH + stock[1], 2)))
                    yorn = input("Are you sure you'd like to sell(Y/N)? ")
                    yorn = yorn.upper()
                    if yorn == "Y":
                        NEWCASH += stock[1]
                        my_stocks.pop(index - 1)
                    else:
                        print("You did not sell a stock")
                else:
                    if stock[2] > 1:
                        arrow = "↗"
                    elif stock[2] < 1:
                        arrow = "↘"
                    else:
                        arrow = "→"
                    if stocky == index:
                        print(str(index) + ". [" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "% " + arrow + "]")
                        FIRSTCASH = NEWCASH
                        print("$" + str(FIRSTCASH) + " + $" + str(stock[1]) + " = $" + str(round(NEWCASH + stock[1], 2)))
                        yorn = input("Are you sure you'd like to sell(Y/N)? ")
                        yorn = yorn.upper()
                        if yorn == "Y":
                            NEWCASH += stock[1]
                            my_stocks.pop(index - 1)
                        else:
                            print("You did not sell a stock")
            index += 1
            print("-------------------------")


def main_menu():
    stop = False
    global CASH
    # NEWCASH = 70000
    # price = 0
    while (stop == False):
        CASH = NEWCASH
        print("You have $" + str(round(NEWCASH, 2)))
        sleep(1)
        print("TYPE THE CORRESPONDING NUMBER")
        sleep(.8)
        print("1. Company Info")
        sleep(.25)
        print("2. Invest")
        sleep(.25)
        print("3. Your Stocks")
        sleep(.25)
        print("4. Sell Stocks")
        sleep(.25)
        print("5. Continue")
        sleep(.25)
        print("-------------------------")
        try:
            menu_num = int(input(""))
        except ValueError:
            print("PLEASE TYPE A VALID CHARACTER")
            sleep(1)
        else:
            if menu_num == 1:
                company_info()
            elif menu_num == 2:
                invest()
            elif menu_num == 3:
                stocks()
                print("-------------------------")
            elif menu_num == 4:
                sell_stocks()
            elif menu_num < 1 or menu_num > 5:
                print("TYPE A VALID NUMBER")
            else:
                stop = True


def intermission():
    for choice in invest_choices:
        invest_choices.pop(0)
    # print(invest_choices)
    print("Progressing to the next year...")
    sleep(1)
    print("-------------------------")
    sleep(1)
    # for company in businesses:
    #     print(company[3])
    for company in businesses:
        company[2] = (round(random.uniform(0.01, 0.1), 2))
        #print(company[0].upper())
        if company[4] == True:
            #print("dummy1")
            randy = (random.randrange(1, 11))
            if randy <= 6:
                #print("dummy2")
                company[1] = round(company[1] * company[3], 2)
                index = 0
                for stock in my_stocks:
                    if company[0] == stock[0].casefold():
                        ogStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")#+ arrow + "]"))
                        researched = stock[2]
                        print("The researched stock projection of your " +
                                stock[0] + " stock of $" + str(stock[1]) + " was correct.")
                        stock[1] = round(stock[1] * company[3], 2)
                        newStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
                        if stock[2] > 1:
                            print("The price of your " + stock[0] + " stock increased to $" + str(stock[1]))
                        elif stock[2] < 1:
                            print("The price of your " + stock[0] + " stock decreased to $" + str(stock[1]))
                        else:
                            print("The price of your " + stock[0] + " stock stayed the same at $" + str(stock[1]))
                        print("Researched projection: " + str(researched) + "% → Actual projection: " + str(stock[2]) + "%")
                        sleep(.5)
                        print(ogStock + " → " + newStock)
                        sleep(.5)
                        print("-------------------------")
                        sleep(1)
                    index += 1
            else:
                actualProj = (round(random.uniform(.95, 1.05), 3))
                company[1] = round(company[1] * actualProj, 2)
                company[3] = actualProj
                index = 0
                for stock in my_stocks:
                    if company[0] == stock[0].casefold():
                        ogStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
                        researched = stock[2]
                        print("The researched stock projection of your " +
                              stock[0] + " stock of $" + str(stock[1]) + " was incorrect.")
                        stock[1] = round(stock[1] * actualProj, 2)
                        #stock[1] = round(stock[1] * company[3], 2)
                        stock[2] = actualProj
                        if actualProj > 1:
                            print("The price of your " + stock[0] + " stock increased to $" + str(stock[1]))
                        elif actualProj < 1:
                            print("The price of your " + stock[0] + " stock decreased to $" + str(stock[1]))
                        else:
                            print("The price of your " + stock[0] + " stock stayed the same at $" + str(stock[1]))
                        print("Researched projection: " + str(researched) + "% → Actual projection: " + str(stock[2]) + "%")
                        newStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
                        sleep(.5)
                        print(ogStock + " → " + newStock)
                        sleep(.5)
                        print("-------------------------")
                        sleep(1)
                    index += 1
        else:
            # for stock in my_stocks:
            #     if stock[2] != "???"

        #For ??? stocks
            randy = (random.randrange(1, 11))
            if randy <= 10:
                company[1] = round(company[1] * company[3], 2)
                for stock in my_stocks:
                    if company[0] == stock[0].casefold():
                        if stock[2] != "???":
                            ogStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
                            researched = stock[2]
                            print("Your " + stock[0] + " stock of $" + str(stock[1]) + " changed.")
                            stock[1] = round(stock[1] * company[3], 2)
                            # stock[1] = round(stock[1] * company[3], 2)
                            stock[2] = company[3]
                            newStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
                            if stock[2] > 1:
                                print("The price of your " + stock[0] + " stock increased to $" + str(stock[1]))
                            elif stock[2] < 1:
                                print("The price of your " + stock[0] + " stock decreased to $" + str(stock[1]))
                            else:
                                print("The price of your " + stock[0] + " stock stayed the same at $" + str(stock[1]))
                            sleep(.5)
                            print(ogStock + " → " + newStock)
                            sleep(.5)
                            print("-------------------------")
                            sleep(1)
                        else:
                            ogStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: ???]")
                            stock[1] = (round(stock[1] * company[3], 2))
                            stock[2] = company[3]
                            newStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
                            print("The stock projection of your unknown " + stock[0] + " stock is " + str(stock[2]) + "%")
                            print("Unknown projection: ??? → Actual projection: " + str(stock[2]) + "%")
                            sleep(.5)
                            print(ogStock + " → " + newStock)
                            sleep(.5)
                            print("-------------------------")
                            sleep(1)
                company[3] = (round(random.uniform(.95, 1.05), 3))
            # else:
            #     actualProj = (round(random.uniform(.95, 1.05), 3))
            #     company[1] = round(company[1] * actualProj, 2)
            #     company[3] = actualProj
            #     for stock in my_stocks:
            #         if company[0] == stock[0].casefold():
            #             ogStock = ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: ???]")
            #             stock[1] = (stock[1] * actualProj)
            #             stock[2] = company[3]
            #             newStock =  ("[" + stock[0] + " / $" + str(stock[1]) + " / Stock: " + str(stock[2]) + "%]")
            #             print("The stock projection of your unknown " + stock[0] + " stock is " + str(stock[2]) + "%")
            #             print("Unknown projection: ??? → Actual projection: " + str(stock[2]) + "%")
            #             sleep(.5)
            #             print(ogStock + " → " + newStock)
            #             sleep(.5)
            #             print("-------------------------")
            #             sleep(1)

    sleep(1)
    for company in businesses:
        company[4] = False
    print("")
    input("Press Enter to continue... ")
    print("")
    #print("Your stocks: ")
    #for stocks in my_stocks:

    #company_info()
    #for stock in my_stocks:
    #     if stock[2] == "???":
    #         print("")
    #     else:



""" 
#QUESTIONS  
#Should check the number the user inputs and 
#Ask the player what year they'd like to play too?
#Maybe look at how to print w/ color?
"""
CASH = 70000
NEWCASH = 70000
index = 0
simulate = True
rules()
def simulation():
    YEAR = 2023
    # global CASH
    # global NEWCASH
    # CASH = 70000
    while simulate == True:
        sleep(.3)
        print("YEAR: " + str(YEAR))
        sleep(.7)
        print_business_names()
        guesses = []
        print("Pick 3 business to research by typing it's name")
        for i in range(3):
            search = (input("Research: "))
            search = search.lower()
            check_search(search, guesses)
            guesses.append(search)
            #print(guesses)
        for search in guesses:
            research(search)
        guesses = []
        #print(guesses)
        company_info()
        sleep(.5)
        main_menu()
        intermission()
        YEAR += 1
        if YEAR == 2034:
            print("Finished")
            simulate == False


simulation()

#reset at the end of each year
#"""
