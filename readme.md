# Rat in a maze #
 Used to find different paths into a destination.
 
# Algorithm Techniques #
 - Recursion
 - Backtracking
# Language and Libraries #
 Python, Pygame
 
# Instruction #
choose .exe file from windows/linux folder.
- You can choose three different modes from main menu:   
        1. Short -- To find Shortest Path.
        2. Normal -- To find all different Path.  
        3. Longest -- To find the longest path.  

- **Start** -- Start the game
# Board Colors #
     1. Black -- represents  "barrier","wall" or "block".
     2. White -- represnts "allowed Way".
     3. Red -- represents "destination".
     4. Teal -- represents the path.

# Board Menu #
Show the colored path to the destination(red colored).
Each colored grid is labeled with a number representing step precedence.
-**->** press right arrow keys or **space bar** to show next path.
-if there is no new path,the boardmenu is returned back to mainmenu.
- **Esc** -- To go back to main menu

# Settings #
- **Gear icon** -- To change board settings.
- **W** -- press *W* to to create a new "allowed path" grid.
- **r** -- press *r* to change destination.
- **b** -- press *b* to create a new *barrier*,"wall" or "block".

# Warning #
1) You can change the board size, default is 10*10 (increasing higher than 15 is not recommended).
2) If your maze has more than 2222 paths,takes time huge amount of time to calculate(so now its not recommended to implement maze which need high looping,it will be solved after implementing same algorithm with *yield*).
3) Changing board size will not adjust main menu (not recommended).
 
