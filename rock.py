import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input("""
GAME START..........
1 YES

2 NO /EXIT
          """))


    if uc==1:
      for a in range(1,10):
        userinput=int(input("""
 1. Rock
 2. scissor
 3. paper                  
                   """))
        if userinput==1:
           uchoice="rock"
        elif userinput==2:
            uchoice="scissor"
        elif userinput==3:
            uchoice="paper"
        cchoice=random.choice(l)
        if cchoice==uchoice:
                print("COMPUTER VALUE",cchoice)
                print("USER VALUE", uchoice)
                print("GAME DRAW")
                ucount=ucount+1
                ccount=ccount+1
        elif(uchoice=="rock"and cchoice=="scissor")or(uchoice=="paper"and cchoice=="rock")or(uchoice=="scissor"and cchoice=="paper"):
            print("COMPUTER VALUE", cchoice)
            print("USER VALUE", uchoice)
            print("YOU WIN")
            ucount=ucount+1
        else:
            print("COMPUTER VALUE", cchoice)
            print("USER VALUE", uchoice)
            print("COMPUTER WIN")
            ccount=ccount+1
