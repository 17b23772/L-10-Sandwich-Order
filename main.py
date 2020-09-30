#Pizza order
total_order = 0
print ("Choose Your Pizza Base. You Can Either Have Thick Or Thin.")
pizza_base = input() 
if input() == "Thick":
  total_order = + 8.00
else: 
  total_order = + 10.00
print ("\n")
print ("How Large Would You Like Your Pizza? You Can Eiter have 8, 10, 12, 14 or 18")
pizza_size = input()
if pizza_size == "8":
  total_order = + 0
else: 
  total_order = + 2
print ("\n")
print ("Would You Like Cheese On Your Pizza")
choice_cheese = input()
print ("\n")
print ("What Pizza Type Would You Like?")
print ("You Can Choose From: Margherita, Vegetable, Vegan, Hawaiian or Meat Feast")
pizza_topping = input()
print ("\n")
print("Thanks For Shopping With Us! Here Is The Bill") 
print (total_order)



