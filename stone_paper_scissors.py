choices = ['rock', 'paper', 'scissor', 'scissors']
count = 5
score1 = 0
score2 = 0
while(count>0):
    while(1):
        play1 = input("\nPlayer 1 - Enter choice: ")
        play1.lower()
        if(play1 not in choices):
            print("Invalid input")
        else:
            break
    while(1):
        play2 = input("Player 2 - Enter choice: ")
        play2.lower()
        if(play2 not in choices):
            print("Invalid input")
        else:
            break
    if(play1 == choices[0]):
        if(play2 == choices[1]):
            score2+=1
            count-=1
        elif(play2 == choices[2] or play2 == choices[3]):
            score1+=1
            count-=1
    if(play1 == choices[1]):
        if(play2 == choices[0]):
            score1+=1
            count-=1
        elif(play2 == choices[2] or play2 == choices[3]):
            score2+=1
            count-=1
    if(play1 == choices[2] or play1 == choices[3]):
        if(play2 == choices[0]):
            score2+=1
            count-=1
        elif(play2 == choices[1]):
            score1+=1
            count-=1
            
print("Scores:\nPlayer 1:",score1,"\nPlayer 2:",score2)
if(score1 > score2):
    print("Player 1 won")
elif(score2 > score1):
    print("Player 2 won")
else:
    print("Game ties")
