import csv



with open('rawCompliments.txt', encoding='utf-8') as file:

	file = file.readlines()
	list = []
	for x in file:
		try:
			print(x)
		except UnicodeEncodeError:
			continue
		list.append(x.rstrip())
	print(list)
			


	