#budget

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
budget = {}

print("Input your budget: ")
for i in range(len(week)):
	print(week[i].title())
	day = input()
	budget[week[i]] = day

weekly_budget = 0

print("\nThis is your budget breakdown:")
for k,v in budget.items():
	print(k + "--" + str(v))
	weekly_budget += int(v)

print("Your Budget per Week is: " + str(weekly_budget))
