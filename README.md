# Battleship Project in python with Flask UI

Description
===========
This is battleship game made in python that was supposed to have both command line input and Flask graphical UI. As of now, the UI is not working for some reasons.

How to Run
==========
To change the placements of battle ships:
1. open placement.json
2. You will now see some values attached to each ship.  eg. Aircraft_Carrier":["0","0","h"]
3. in the above example the first numerical variable is the x coordinate and the secont the y coordinate. Both can be set between 0~9.
4. The third variable stands for the alignment of the ship, with "h" being horizontal and "v" being vertical.

For commandline input:
1. Copy mp_game_engine.py as path
2. Open terminal
3. paste{ python [path] } in the command terminal
4. each time you will have to enter two values between 0~9, The first ones for the x coordinates and the latter y
5. If you manage to destroy all enemy ships, you win.

For Flask UI:
N/A

Pytest
======
At first I ran into some failures. After a few adjustments, I manage to make it Failure free.

Self assesment/ Conclusion
==========================
This is my first time coding a python app. It didn't went as well as I hoped. I struggled alot with the frontend, finding it tricky to do the "/attack" method. Whenever I run main.py, It would take me to main.html with a 4x4 grid, and clicking on the tile will run into errors. I did tried my best but my skill are still lacking.
