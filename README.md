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

## Bonus Exercises
For extra credit:

Bonus must be done in this order for credit.  No skipping around.

- Bonus 1: Implement linting
- Bonus 2: Implemment unit testing and get code coverage as close to 100% as possible.
- Bonus 3: Implement a smart computer player
- Bonus 4: Implement a GUI interface (not included in this example)

### Unit testing
    pytest --cov-report xml --cov-report term-missing --cov=tictactoe

### New Objects for Bonus 3
- Game Board Position
- Game Board Stripe (rows, columns, diagonals)
- Smart Move Calculator