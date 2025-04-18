import random
name = "John"
question = "Should I go on a date with Katie?"
answer = ""
random_number = random.randint(1, 10)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Yes, but be cautious"
else:
  answer = "Error"

if name == "" and question == "":
  print("Please provide a name and a question")
elif name == "":
  print(f"Question: {question}")
  print(f"Magic 8-Ball's answer: {answer}")
elif question == "":
  print("Please ask a question")
else:
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer: {answer}")