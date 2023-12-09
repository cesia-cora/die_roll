# Dice Rolling Probability

## Description
<hr>

This project simulates a simple roll a die game. It possess two modes of dice rolling: unbiased dice rolling and biased dice rolling. The first one simulates a basic roll of all equally likely outcomes, while the second one favors one side of the die (left or right). ASCII art is used for dice faces, probability results and statistical plots are shown for addition.

## project.py
The first input asks the user which dice mode is gonna be played:

* <i>1</i> for unbiased dice
* <i>2</i> for biased dice.

### Unbiased dice:
After entering <i>1</i>, the user has to choose an amount of rollings (this amount can be any integer, but it's recommended to avoid any extremely high number). The outcome will print an array (same length as amount). Finally, the probabilities that each integer had, will be printed as well.

### Biased dice:
After entering <i>2</i>, just as unbiased dice, the user has to choose an amount. In this case, an input of a "favored side" will be prompted. If user chooses the left side there will be a higher probability for numbers 1, 2 and 3 to appear on the final array. On the contrary, if the right side is chosen there will be a higher probability for numbers 4, 5 and 6. And finally, the probabilities of each integer will be printed too.

### Dice art diagrams:
Dice art diagrams are arranged in a dictionary where keys are integers from 1 to 6 and values are ASCII representations of dice faces corresponding to each integer.
Dice faces will be shown below the final array in a single row. Be sure to have enough width on your terminal to print characters correctly.