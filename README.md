# TicTacToe
## A Python3 class exercise
### Procedural Programming
First exercise: a procedural implementation

    $ python tictactoe_procedural.py

### Object Oriented Programming
Second exercise: reconceptualize as interacting objects and implement.

    $ python tictactoe_oo.py

The interacting objects are:

- Game Board (layout)
- Game Play (rules and turns)
- Player (opponents)

Bonus 3 objects are:

- Game Board Position (9 positions total)
- Game Board Stripe (rows, columns, diagonals)
- Smart Move Calculator (calculate best next move)

## Bonus Exercises
For extra credit:

Bonuses must be done in this order for credit.  No skipping around.

- Bonus 1: Implement linting
- Bonus 2: Implement unit testing and get code coverage above 95%.
- Bonus 3: Implement a smart computer player what can win games.
- Bonus 4: Randomize the selected best next move.
- Bonus 5: Implement a GUI interface (not included in this example)

### Unit testing
    pytest --cov-report xml --cov-report term-missing --cov=tictactoe
