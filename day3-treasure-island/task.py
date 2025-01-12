print('''
              __....-----------...__                   
          .--'                      `--.               
        .'                              `.             
      .'                                  `.           
     ;                                      `.         
    :                                         :        
    ;                                          \       
   :                                            \      
   :                                             \     
   :                                              :    
   :                                              :    
   :                                              :    
   :                                              :    
   :                    .d$$$.                    :    
  .' .$$b.            .d$$$$$$                    :    
 ;   $$$$$b.  `.    .d$$$$$$$$                    :    
:    $$$$$$$   :   .$$$$$$$$$'   .                ;    
 \   `$$$$$$   '   $$$$$$$$P'     `.             :     
  `.   `$$$        ^$$$$$P'        `.            ;     
   :    .'_                         :           /      
  /    '.$$$.                       `.        _/       
 /      $$$$$.                       :     _.'         
:      d$$$$$$                       :_.--'            
'.     $$'`$$$                     .'                  
  \    $P  `$$                   .'                    
   :                           .'                      
   ;     :          :          \    [WILU]             
  :      :          :           `.                     
  :      ;          `.           :                     
  :     :            :           ;                     
  :     :            `.         :                      
   `.___:__           :      __.'                      
           ''''''-----'-----'
''')

print("Welcome to Treasure Island!\nYour mission is to find the treasure.")

choice1 = input("You're at a crossroad. Which way do you want to go?\n Type 'left' or 'right': ").lower()

if choice1 == "left":

    choice2 = input("You've come to a lake. In the middle, there is an island.\n Type 'wait' to wait for a boat, type 'swim' to go for it: ").lower()
    if choice2 == "wait":

        choice3 = input("The boat takes you to the island and you find a mysterious dungeon with 3 colored doors.\n Type 'red','blue', or 'yellow' to choose a door: ").lower()
        if choice3 == "yellow":
            print("You find the treasure! You win.")
        elif choice3 == "blue":
            print("A ferocious beast jumps out from the door and attacks you. Game over.")
        elif choice3 == "red":
            print("You set off a trap and an arrow one taps you. Game over.")
        else:
            print("MISINPUT! Try again.")

    elif choice2 == "swim":
        print("You get swallowed whole by a fish. Game over.")
    else:
        print("MISINPUT! Try again.")

elif choice1 == "right":
    print("You fall into a hole. Game over.")
else:
    print("MISINPUT! Try again.")
