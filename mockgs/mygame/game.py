# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

'''
In this example, the game module imports the draw module, 
which enables it to use functions implemented in that module.
The main function uses the local function play_game to run the game,
and then draws the result of the game using a function implemented in the draw module called draw_game. 
To use the function draw_game from the draw module, we need to specify in which module the function is implemented, 
using the dot operator. To reference the draw_game function from the game module,
we need to import the draw module and then call draw.draw_game().

When the import draw directive runs,
the Python interpreter looks for a file in the directory in which the script was executed with the module name and a .py suffix.
In this case it will look for draw.py. If it is found, 
it will be imported. If it's not found, it will continue looking for built-in modules.

You may have noticed that when importing a module, a .pyc file is created.
This is a compiled Python file.
Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded. 
If a .pyc file exists, it gets loaded instead of the .py file. This process is transparent to the user.
'''