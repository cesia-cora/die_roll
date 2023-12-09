# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
height = len(dice_art[1])
width = len(dice_art[1][0])
separator = " "

# %%
def main():
    type_of_dice = int(input('Enter 1 for unbiased dice, enter 2 for biased dice: '))

    if type_of_dice == 2:
        choice_n = int(input('For weighted dice on left enter 1, for right enter 2: '))

        if choice_n not in [1, 2]:
            raise ValueError('Choice should be 1 or 2')
        amount = int(input('Enter amount of rolls: '))
        
        if choice_n == 1:
            print(biased_dice_on_left(amount))
        else:
            print(biased_dice_on_right(amount))

    elif type_of_dice == 1:
        amount = int(input('Enter amount of rolls: '))
        print(unbiased_dice(amount))

    else:
        raise ValueError('Input should be 1 or 2')

def unbiased_dice(i):
    try:
        dice = np.random.randint(1, 7, i)

        probabilities = []

        for j in range(1, 7):
            prob = np.round(np.sum(dice == j) / len(dice), decimals=1)
            probabilities.append(prob)

        labels = ['1', '2', '3', '4', '5', '6']
        bar_colors = ['#ffd380', '#ffa600', '#ff8531', '#ff6361', '#bc5090', '#8a508f']
        plt.bar(labels, probabilities, color=bar_colors, edgecolor='black')
        plt.xlabel('Dice sides')
        plt.ylabel('Probability')
        plt.title('Probability of each dice side')
        plt.show()

        df_unbiased = pd.DataFrame({'Results': dice})

        result_string = f'{ df_unbiased.to_string(index=False) } \n {dice_faces(dice)} \n'
        for j in range(6):
            result_string += f'{j+1} had a probability of {probabilities[j] * 100}% \n'
        return result_string
    except:
        raise ValueError('Input is not an integer')

def biased_dice_on_left(i):
    try:
        dice = np.random.choice(range(1, 7), size=i, p=[0.2, 0.2, 0.2, 0.15, 0.15, 0.1])

        probabilities = []

        for j in range(1, 7):
            prob = np.round(np.sum(dice == j) / len(dice), decimals=1)
            probabilities.append(prob)

        labels = ['1', '2', '3', '4', '5', '6']
        bar_colors = ['#ffd380', '#ffa600', '#ff8531', '#ff6361', '#bc5090', '#8a508f']
        plt.bar(labels, probabilities, color=bar_colors, edgecolor='black')
        plt.xlabel('Dice sides')
        plt.ylabel('Probability')
        plt.title('Probability of each dice side')
        plt.show()

        df_unbiased = pd.DataFrame({'Results': dice})

        result_string = f'{ df_unbiased.to_string(index=False) } \n {dice_faces(dice)} \n'
        for j in range(6):
            result_string += f'{j+1} had a probability of {probabilities[j] * 100}% \n'
        return result_string
    except:
        raise ValueError('Input is not an integer')

def biased_dice_on_right(i):
    try:
        dice = np.random.choice(range(1, 7), size=i, p=[0.1, 0.15, 0.15, 0.2, 0.2, 0.2])

        probabilities = []

        for j in range(1, 7):
            prob = np.round(np.sum(dice == j) / len(dice), decimals=1)
            probabilities.append(prob)

        labels = ['1', '2', '3', '4', '5', '6']
        bar_colors = ['#ffd380', '#ffa600', '#ff8531', '#ff6361', '#bc5090', '#8a508f']
        plt.bar(labels, probabilities, color=bar_colors, edgecolor='black')
        plt.xlabel('Dice sides')
        plt.ylabel('Probability')
        plt.title('Probability of each dice side')
        plt.show()

        df_unbiased = pd.DataFrame({'Results': dice})

        result_string = f'{ df_unbiased.to_string(index=False) } \n {dice_faces(dice)} \n'
        for j in range(6):
            result_string += f'{j+1} had a probability of {probabilities[j] * 100}% \n'
        return result_string
    except:
        raise ValueError('Input is not an integer')

def dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(dice_art[value])

    dice_faces_rows = []
    for row_idx in range(height):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = separator.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    diagram_header = " Dice faces: ".center(width, " ")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

if __name__ == "__main__":
    main()