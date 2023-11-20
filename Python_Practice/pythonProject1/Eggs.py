#PRP411
#Question 1
#Program that prompts a user for the number of eggs they wish to order and calculates the total amount owed, along with a detailed breakdown of the order:

#Prompt the user for the number of eggs:

num_eggs = int(input("How many eggs would you like to order? "))

#Calculate the number of dozens and loose eggs:

num_dozens = num_eggs // 12
num_loose_eggs = num_eggs % 12

#Calculate the total cost:

cost_of_dozens = num_dozens * 3.25
cost_of_loose_eggs = num_loose_eggs * 0.45

total_cost = cost_of_dozens + cost_of_loose_eggs

#Display the final amount owed and order breakdown:

print(f"You ordered {num_eggs} eggs. That's {num_dozens} dozen at R3.25 per dozen and {num_loose_eggs} loose eggs at 45c each for a total of R{total_cost}")