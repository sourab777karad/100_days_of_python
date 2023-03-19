#the death door
print('''             .
               .' `.
             .' .'. `.
           .' .'   `. `. 
         .' .'       `. `.
       .' .'           `. `.
     .' .'|  _________  |`. `.
      `'| | |         | | |`'
        | | |   _ _   | | |
        | | |  ( " )  } | |
        | | |   \ /   | | |
        | | |    "    | | |
        | | |         | | |
        | |,+'        | | |
        | | |         | | |
        | | |         | | |
        | | |         | | |
        | | |         | | |
        | | |         | | |
        | | |         | | |
        | | |         } | |
        | | |         | | |
,,,,,,,,|,|,|,,,,,,,,,|,|,|,,,,,,,,,,,,,,
''')

print("************WELCOME TO THE ONLY DOOR****************")
print("ONLY TWO WAY HOME OR DEATH")

DOOR1 = input('WELCOME\' CHOOSE ANY OF THE 2 DOORS ONE FOR FORWARD AND ONE FOR DEATH! "left" or "right".').lower()
if DOOR1 == "left":
    print("lucky fellow, lets see how faar you can run")
    DOOR2 = input('*****you\'have a basket of ice cream would you like to "eat" or "wait" untill it melts then drink it with a straw :*****').lower()
    if DOOR2 == "wait":
        print("you are lucky it had a cheat naming the hint of next safe door!!")
        print("----->the cheat had : PENNSYLVANIA AVENUE, US :)<------")
        print("----->use the cheat(brahmastra) you have buddy!!<------")
        DOOR3 = input('YOU \' are lucky this is the last door between death and home! there are 3 doors infront of you "RED", "WHITE" and "GREEN", "which one will you choose :').lower()
        if DOOR3 == "white":
            print("YOU ARE HOME BUDDY WELL PLAYED YOUR LUCK WAS GREATFULL TODAY")
            print("***********CHAMPION OF DEATHDOOR************")
        else:
            print("buddy almost there but not this time!!!!")
            print("you came this far to knock the deathdoor")
            print("YOU ARE DEAD")
            print("******************GAME OVER********************")
    else:
        print("have more icreams after the death door!!! ><")
        print("game over buddy!")
        print("***********************GAME OVER************************")
else:
    print("|NOT THIS ONE BUDDY|DEATH DOOR OPENS!!")
    print("***************************GAME OVER*************************")
    
     