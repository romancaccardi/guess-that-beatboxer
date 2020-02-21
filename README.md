# guess-that-beatboxer
A Python script simulating the classic Human Beatbox game "Guess That Beatboxer"

## How to play
First, make sure that you have installed Python3!

Then, navigate to the appropriate directory in your command line tool of choice and run:
$ python guessThatBeatboxer.py

You will be asked to pick a mode.  The modes are all different permutations of 4 different pools of beatboxers
contained in separate text files:

1. Easy   (easyMode.txt)    -- these beatboxers are very well-known and usually easy to imitate
1. Hard   (hardMode.txt)    -- the largest pool, these beatboxers are either lesser-known or very challenging to imitate
1. Unfair (whatTheHeck.txt) -- a small group of extremely obscure beatboxers
1. Constant (constants.txt) -- beatboxers who are included in every mode, regardless of difficulty.  Feel free to modify this list as you see fit!

You will need to press "Enter" after starting in order to begin displaying beatboxers.

After starting, press "Enter" to navigate to the next beatboxer name.  The game ends when all beatboxers in the pool have been exhausted.

## Modifying the game
If you are familiar with coding in Python, of course you are welcome to modify the rules as you see fit!  One change
you might consider making is the addition of a timer into rounds.

As mentioned above, you are also free to add or remove beatboxers from each list as you see fit.