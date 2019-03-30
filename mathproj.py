# Calculate fractiles

people_heights = {}
filename = 'name.txt'

with open(filename, 'r') as f:
    #DATA FORMAT = NAME - HEIGHT in inches
    text = f.read().strip()
    people = text.split('\n')
    for person in people:
        person = person.split(' - ')
        print(person)
        people_heights.setdefault(person[0].title(), person[1])

def ft_to_cm(ft):
    # height = ft.split('\'')
    # ft = int(height[0])
    # inches = int(height[1])
    #
    # ft = ft * 12
    #
    # inches = inches + ft
    # cm = inches * 2.54 # 2.54 Constant for converting inch to cm
    return int(ft)


# Array of all heights
heights = []

for height in people_heights.values():
    height = round(ft_to_cm(height), 2)
    heights.append(height)

# Clean the heights
heights = sorted(heights)

print(heights)

def fractile(type, heights):
    if type == 'quartile':
        type = 'Q'
        fractile_limit = 4
    elif type == 'decile':
        type = 'D'
        fractile_limit = 10
    elif type == 'percentile':
        type = 'P'
        fractile_limit = 100

    fractiles = {}

    for k in range(1, fractile_limit):
        fractile_place = ((k * len(heights) / fractile_limit )) + 0.5
        fractiles.setdefault(type + str(k), fractile_place)

    return fractiles

def find_all_fractiles(heights):
    quartiles = fractile('quartile', heights)
    deciles = fractile('decile', heights)
    percentiles = fractile('percentile', heights)

    print('DECILES')
    for d, place in deciles.items():
        print(d, '=', str(place) + 'th', 'or Value :', round(place_to_value(place, heights), 2))

    print('\nQUARTILES')
    for q, place in quartiles.items():
        print(q, '=', str(place) + 'th', 'or Value :', round(place_to_value(place, heights), 2))

    print('\nPERCENTILES')
    for p, place in percentiles.items():
        print(p, '=', str(round(place, 2)) + 'th', 'or Value :', round(place_to_value(place, heights), 2))

def place_to_value(place, heights):
    place = float(place)
    place = str(place)
    place = place.split('.')

    decimal = float('0.'+place[1])
    if int(place[0]) == len(heights):
        ones = int(place[0])
        value = heights[len(heights)-1]
    elif int(place[0]) != 0:
        ones = int(place[0]) - 1
        value = heights[ones] + (decimal * (heights[ones+1] - heights[ones]))
    else:
        ones = 0
        value = decimal * (heights[0])

    return value

# find_all_fractiles(heights)
# print(fractile('percentile', [140,148,150,152,155,157,159,160,161,164,165,166]))
# find_all_fractiles([140,148,150,152,155,157,159,160,161,164,165,166])
# print(len(heights))
# print(ft_to_cm('1\'0')
print('MATH DATA')
i = 1
for person, height in people_heights.items():
    print(str(i)+'.', person, 'is', height, 'cm tall.')
    i += 1

print('Total number of data:', len(heights), 'or n =', len(heights))

print('FRACTILES (Quartile, Decile, Percentile)')
find_all_fractiles(heights)
