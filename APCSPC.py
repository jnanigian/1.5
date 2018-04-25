

import time
codelist=[10000000,11000000,11100000,11110000,11111000]

games="No"


def start():
    print("This app is made to make it easier to add your friends in all your apps and games,")
    time.sleep(1)
    print("You insert a specific code of the person you would like to add and thern that person's phone number is added to your contacts,")
    time.sleep(1)
    print("You are also given the option to add these friends to your games")
    time.sleep(1)
    code=int(input("What is the code for the person you would like to add?"))
    if code==codelist[0]:
        print("This is a code for Mason Ross!")
        time.sleep(1)
        print("This person's number will be added to your contacts!")
        time.sleep(1)
        print("Mason Ross Contact Information")
        time.sleep(1)
        print("Phone Number:856-325-3392")
        time.sleep(1)
        print("Residence:California")
        time.sleep(1)
        game= str(input("Would you like to add this person to your games?"))
        if games=="yes" or "Yes":
            print("Great!")
            gamenum= int(input("How many games would you like to add this person to?"))
            for i in range(gamenum):
                game=str(input("What Game would you like to add this person to?"))
                print("Mason Ross has been added to " + game)
        else:
            print("Okay, Thanks for using this app!")
        print("This person is now on your phone")



    if code==codelist[1]:
        print("This is a code for Devin Patel!")
        time.sleep(1)
        print("This person's number will be added to your contacts!")
        time.sleep(1)
        print("Devin Patel Contact Information")
        time.sleep(1)
        print("Phone Number:852-322-3396")
        time.sleep(1)
        print("Residence:California")
        time.sleep(1)
        game= str(input("Would yo like to add this person to your games?"))
        if games=="yes" or "Yes":
            print("Great!")
            gamenum= int(input("How many games would you like to add this person to?"))
            for i in range(gamenum):
                game=str(input("What Game would you like to add this person to?"))
                print("Devin Patel has been added to " + game)
        else:
            print("Okay, Thanks for using this app!")
        print("This person is now on your phone")

















pygame.quit()
start()
