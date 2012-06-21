Tic-Tac-Toe in Python
Michael Kristofik <kristo605@gmail.com>

SUMMARY

This is a simple text-based tic-tac-toe game written in Python.  I wrote it so
I could experiment with AI algorithms in games.  Teaching a computer to play
tic-tac-toe *well* is surprisingly difficult without using a giant lookup table
(cf. http://xkcd.com/832/).  See ai.py for the algorithms I used.

USAGE

python tic.py
    Play against the computer.  Human player goes first.
python tac.py
    Play against the computer.  Computer player goes first.
python toe.py [2]
    Computer plays against itself, a naive algorithm vs. a smarter algorithm.
    Naive player goes first.  Use the command-line argument 2 to let the smart
    algorithm go first.

LICENSE

Copyright Michael Kristofik 2011-2012.
Distributed under the Boost Software License, Version 1.0.
(See accompanying file LICENSE_1_0.txt or copy at 
http://www.boost.org/LICENSE_1_0.txt)
