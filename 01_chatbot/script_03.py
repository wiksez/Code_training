# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  dessert_type = get_dessert()
  print(f"Alright, that's a {size} {drink_type}!")
  if dessert_type != None:
    print(f"And {dessert_type} as your dessert!")
  name = input("Can I get your name please? ")
  print(f"Thanks, {name}! Your drink will be ready shortly.")  

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return "small"
  elif res == 'b':
    return "medium"
  elif res == 'c':
    return "large"
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n")
  if res == 'a':
    return "brewed coffee"
  elif res == 'b':
    return "mocha"
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n")
  if res == 'a':
    return "latte"
  elif res == 'b':
    return "non-fat latte"
  elif res == 'c':
    return "soy latte"
  else:
    print_message()
    return order_latte()
  
def get_dessert():
  res = input("Would you like some kind of dessert to go with your drink? \n[a] Yes \n[b] No\n")
  if res == 'a':
    return order_dessert()
  elif res == 'b':
    return None
  else:
    print_message()
    return get_dessert()

def order_dessert():
  res = input("And what kind of desser for your drink? \n[a] Cookies \n[b] Donut \n[c] Muffin\n")
  if res == 'a':
    return "cookies"
  elif res == 'b':
    return "donut"
  elif res == 'c':
    return "muffin"
  else:
    print_message()
    return order_dessert()
# Call coffee_bot()!

coffee_bot()