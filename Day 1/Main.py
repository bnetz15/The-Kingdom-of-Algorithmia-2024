# Part 1
# Open the file in read mode
with open('Part1Input.txt', 'r') as file:
    # Read lines into a list
    lines = file.readlines()

# Remove newline characters from each line
lines = [line.strip() for line in lines]

ans = 0

# Loop through each line in the list
for line in lines:
    # Loop through each character in the line
    for char in line:
        # If the character is equal to B, add 1 to the answer since 1 potion is required
        ans += (char == 'B')
        # If the character is equal to C, add 3 to the answer since 3 potions are required
        ans += (char == 'C') * 3
print("Part 1 answer:", ans)

# Part 2
# Open the file in read mode
with open('Part2Input.txt', 'r') as file:
    # Read lines into a list
    lines = file.readlines()

# Remove newline characters from each line
lines = [line.strip() for line in lines]

ans = 0

# Loop through each line in the list
for line in lines:
    # Loop through each character in the line
    for i in range(0, len(line), 2):
        # If they are paired up, add 2 extra potions
        if(line[i] != 'x' and line[i + 1] != 'x'):
            ans += 2
        # If the character is equal to B, add 1 to the answer since 1 potion is required
        ans += (line[i] == 'B') + (line[i + 1] == 'B')
        # If the character is equal to C, add 3 to the answer since 3 potions are required
        ans += (line[i] == 'C') * 3 + (line[i + 1] == 'C') * 3
        # If the character is equal to D, add 5 to the answer since 5 potions are required
        ans += (line[i] == 'D') * 5 + (line[i + 1] == 'D') * 5
print("Part 2 answer:", ans)

# Part 3
# Open the file in read mode
with open('Part3Input.txt', 'r') as file:
    # Read lines into a list
    lines = file.readlines()

# Remove newline characters from each line
lines = [line.strip() for line in lines]

ans = 0

# Loop through each line in the list
for line in lines:
    # Loop through each character in the line
    for i in range(0, len(line), 3):
        # Check to see if the creatures are coming in groups and add the according number of potions
        groups = 0
        groups += (line[i] == 'x') + (line[i + 1] == 'x') + (line[i + 2] == 'x')
        if groups == 1:
            ans += 2
        elif groups == 0:
            ans += 6
        # If the character is equal to B, add 1 to the answer since 1 potion is required
        ans += (line[i] == 'B') + (line[i + 1] == 'B') + (line[i + 2] == 'B')
        # If the character is equal to C, add 3 to the answer since 3 potions are required
        ans += (line[i] == 'C') * 3 + (line[i + 1] == 'C') * 3 + (line[i + 2] == 'C') * 3
        # If the character is equal to D, add 5 to the answer since 5 potions are required
        ans += (line[i] == 'D') * 5 + (line[i + 1] == 'D') * 5 + (line[i + 2] == 'D') * 5
print("Part 3 answer:", ans)
