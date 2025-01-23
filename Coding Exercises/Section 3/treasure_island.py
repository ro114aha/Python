# Treasure Island
# Your mission is to find
# You can use ASCII ART 
print('''
 Welcome to escape from Dragon Island
**************************************
*                    \||/            *           
*                    |  @___oo       *
*        /\  /\   / (__,,,,|         *
*        ) /^\) ^\/ _)               *
*        )   /^\/   _)               *
*        )   _ /  / _)               *
*    /\  )/\/ ||  | )_)              *
*    <  >      |(,,) )__)            *
*    ||      /    \)___)             *
*    | \____(      )___) )___        *
*    \______(_______;;; __;;;        *
*                                    *
**************************************
Your mission is to escape from Dragon Island
''')
choise_1 =input("Do you want to go left or right? => ").lower()
# if choise_1 == "left" or choise_1 == "Left" or choise_1 == "LEFT":
if choise_1 == "left" or choise_1 == "Left" or choise_1 == "LEFT":
    print('Good choise your still alive!:"Good to know".')
    choise2 = input('You\'re come to a lake.'
                    'There is a house with 2 doors.\n A red door and a green door\n'
                    'Make a choise by entering "Red" or "Green" => ').lower()
    if choise2 == "red":
        print('That\'s" the correct door')
    else:
        print("Wrong. Your out of the game!")
              
else:
    print('''
*******************************************************************************
                 __.-/|
             \`o_O'
              =( )=  +---------+
                U|   |Game Over|
      /\  /\   / |   +---------+
     ) /^\) ^\/ _)\     |
     )   /^\/   _) \    |
     )   _ /  / _)  \___|_
 /\  )/\/ ||  | )_)\___,|))
<  >      |(,,) )__)    |
 ||      /    \)___)\
 | \____(      )___) )____
  \______(_______;;;)__;;;)      
*******************************************************************************
                         EATEN BY THE DRAGON 
''')
