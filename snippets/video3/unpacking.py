cordinates = (40.650002, -73.949997)
lan, lon = cordinates
print(lan)

colors = ['blue', 'red', 'orange', 'brown', 'green','purple']
first, *_, last = colors
print(_)

full_name = 'gwen pena'.split()
first_name, _ = full_name
print(first_name)

def average_nums(*nums):
    print(f'the average is: {sum(nums)/len(nums)}')

average_nums(4, 565, 859)
