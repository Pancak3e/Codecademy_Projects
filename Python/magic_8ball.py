#v.1.0
#Magic 8 Ball is a project from Codecademy
#
#
# Magic 8 Ball is a simplistic replica of the popular childrens toy
# You can ask Magic 8 Ball any question (by entering any string of information)
# and Magic 8 Ball will give you a forshadowing into your query..
#
# This current project was coded by Pancak3e a.k.a sys4dmin
# The project "answer" outputs and idea were all 
# supplied by Codecademy
#
#
#BEGIN
#
#
import random
import os
print("Please phrase your question in 'Yes' or 'No' statements.")
question = input()
answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:\
    answer = "Very doubtful."
else:
    answer = "Error"

print(answer)
os.system("pause")
#
#
#END
