import random
from matplotlib import pyplot as plt

# Number of tests to perform
nTests = 100000

# Wins initialization
changeWins = 0
notChangeWins = 0

# Perform the tests
for i in range(nTests):

    # Shuffle the doors
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    # Randomly select a door
    selection = random.randint(0, 2)

    # Randomly select one of the goat doors to open. It must be different from the previosuly selected door
    openDoor = random.choice([i for i in range(len(doors)) if doors[i] == 'goat' and i != selection])

    # Calculate the index of the remaining door, the one the contestants can change their initial selection to.
    doorIndices = [0, 1, 2]
    doorIndices.remove(selection)
    doorIndices.remove(openDoor)
    remainingDoor = doorIndices[0]

    # Add the wins for change and not change
    if doors[selection] == 'car':
        notChangeWins += 1
    elif doors[remainingDoor] == 'car':
        changeWins += 1

# Plot
plt.bar(['No cambio', 'Cambio'], [100 * notChangeWins / nTests, 100 *changeWins / nTests], width=0.1, align='center')
plt.ylabel('%')
plt.show()
