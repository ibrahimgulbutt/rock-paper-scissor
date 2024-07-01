import random

i=input("select rock papaer cissor ")
k=0
if  i=='rock':
    k=1
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
elif i=='paper':
    k=2
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
else:
    k=3
    print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

ran=random.randint(1,3)

if ran==1:
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

elif ran==2:
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

else:
    print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    

if ran==k:
    print("It's a draw! 🤝 Two mighty warriors, equally matched. Try again!")

elif ran==2 and k==1:
    #lost
    print("Oh no! 😢 You got wrapped up like paper over rock. Better luck next time!")
elif ran==3 and k==2:
    print("Oh no! 😢 You got wrapped up like paper over rock. Better luck next time!")

elif ran==1 and k==3:
    print("Oh no! 😢 You got wrapped up like paper over rock. Better luck next time!")

else: 
    #won
    print("Congratulations! 🎉 You crushed it like a rock smashing scissors!")