name = (input("Enter your name: "))
print(f"Welcome, {name} to the adventure.")

ans = input("You are on a dirt road, and you have two ways to go left or right, which way would you go?(left/right): ")
if ans == "left":
    ans = input("You have come to a river, now you can walk across the road or can swim in the river.(swim/walk): ")
    if ans == "swim":
       print("you were swimming through the river and were eaten by a alligator. GAME OVER")
    elif ans == "walk":
       print("you were walking for too long and ran out of water. GAME OVER")
    else:
        print("You have choosen an invalid syntax, You lose!")

elif ans == "right":
     ans = input("You have came to an bridge and it looks wobby, do you want to go back or cross the bridge(back/cross): ")
     if ans == "back":
        print("you went back and were eaten by a hungry lion. GAME OVER")
     elif ans == "cross":
        print("you crossed the bridge. And WON!")
     else:
         print("You have choosen an invalid syntax, You lose!")
    
else:
     print("You have choosen an invalid syntax, You lose!")