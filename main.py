from grid import Grid
import os
from time import sleep

def clear():
    os.system('cls') if os.name == "nt" else os.system('clear')

# grid = Grid()
# grid.initialize()
# grid.show()
# print('..................')
# grid.update()
# grid.show()
# print('..................')
# grid.update()
# grid.show()
# print('..................')
# grid.update()
# grid.show()
# print('..................')
# grid.update()
# grid.show()

def main():
    grid = Grid()
    grid.initialize()
    grid.show()
    while True:
        sleep(0.5)
        clear()
        grid.update()
        grid.show()

if __name__ == '__main__':
    main()
