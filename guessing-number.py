import random

def main():
    nmb = random.randint(1,100)   
    trys = 0
    start_nmb = None

    while start_nmb!=nmb:
        try:
            start_nmb = int(input("Wähle eine ganze Zahl zwischen 0 und 100: "))
            if start_nmb == nmb:
                trys+=1
                if trys == 1:
                    print("Oh WOW! Du hast die Zahl beim ersten Versuch erraten!")
                else:
                    print(f"Herzlichen Glückwunsch! Du hast {trys} Versuche gebraucht, um die Zahl zu erraten.")
                
            elif start_nmb < nmb:
                trys+=1
                print("Die gesuchte Zahl ist größer als Deine geratene Zahl!")
            
            elif start_nmb > nmb:
                trys+=1
                print("Die gesuchte Zahl ist kleiner als Deine geratene Zahl!")
            else:
                print("eS iSt ETwaS schIeFGelAUfeN ;/")
        except:
            print("Wähle eine ganze Zahl!")
    wiederholen()

def wiederholen():
    print("Du bist ein wahrer Champion vom Guessing-Numbers-Game.\n\n1: Weiterspielen, 2: Aufhören")
    again = input("Was ist deine Wahl? ")
    if again =="1":
        print("----------------------------------------------------------------")
        main()
    elif again =="2":
        print("\nOkay, Bye Bye :(")
        input("Please press Enter...")

if __name__=="__main__":
    print('-----Herzlich Willkommen zum Guessing-Numbers-Game-----')
    print('Gerade wurde eine Zufallszahl zwischen 0 und 100 generiert.\nDeine Aufgabe ist es nun, zu erraten, welche Zahl es ist')
    main()