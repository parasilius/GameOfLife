# Game Of Life
A simple implementation of Conway's Game of Life in Python  
## Introdution
This project was my first semester's task. The total score was 110, but I got 
132(an extra 10% of the total score for using good names and another extra 10% 
for using OOP).  
In this project we simulate a virtual dynamic world. The rules are as follows:  
## Explaining the World
**Time:** We consider the time in this world to be discrete. The program should 
start the simulation at the time zero and continue to infinity.  
**World Map:** This world is in the shape of a n * m grid consisting of 
live or dead cells. Every cell interacts with its eight neighbors, which are 
the cells that are horizontally, vertically, or diagonally adjacent. At each 
step in time, the following transitions occur:  
+ Any live cell with fewer than two live neighbors dies, as if by 
underpopulation.  
+ Any live cell with more than three neighbors dies, as if by overpopulation.  
+ Any live cell with two or three neighbors lives on to the next generation.  
+ Any live cell with two or three live neighbors survives.  
+ Any dead cell with three live neighbors becomes a live cell.  
Here is a world map with five live cells(all the other cells are considered to 
be dead):  
![a world map with five live cells](https://uupload.ir/files/c9mb_map.png)  
Here is a cell with its neighbors:  
![a cell with its neighbors](https://uupload.ir/files/0glm_neighbors.png)  
If we write a program to perform the rules in each seperate time unit, we 
would have a performance like this:  
![a sample performance](https://uupload.ir/files/3fba_output5.gif)  
## Simulation Details
+ Simulation starts with $t = 1$ and continues to infinity.  
+ For each $t$ the output buffer should be cleared completely(you are allowed 
to use the given tip) and the map for the corresponding time should be 
displayed in the output buffer.  
+ Use the symbols █ & ░ to display the live and dead cells correspondingly.  
### TIP: A Function for Clearing the Output Buffer
```
def clear():
    os.system('cls') if os.name == "nt" else os.system('clear')
```
## Input & Output
Your program should use a given `map.init` file(put in the same directory of 
your main file) and start the simulation from there and continue.  
The data in the `map.init` file makes up the initial world map.  
The output of your program should be the world map in which the rules are 
performed at the corresponding time. For instance in time t = 1 your program 
should print out the world map which is the result of performing the rules on 
the map inside `map.init`.  
### Sample `map.init`
░░░░░░░░░░░░░░░░░░░  
░███░░░░░░░░░░░░░░░  
░░░░░░░░░░░░░░██░░░  
░░░░░░░░░░░░░░██░░░  
░░░░░░░░░░░░░░░░██░  
░░░░░░░░░░░░░░░░██░  
░░░░░░░░░░░░░░░░░░░  
░░░██░░░░░░░░░░░░░░  
░░░██░░░░░░░░███░░░  
░░░░░░░░░░░░███░░░░  
░░░░░░░░░░░░░░░░░░░  
░░░█░░░░░░░░░░░░░░░  
░░░░█░░░░░░░░░░░░░░  
░░███░░░░░░░░░░░░░░  
░░░░░░░░░░░░░░░░░░░  
### Sample Output
t = 1:  
░░█░░░░░░░░░░░░░░░░  
░░█░░░░░░░░░░░░░░░░  
░░█░░░░░░░░░░░██░░░  
░░░░░░░░░░░░░░█░░░░  
░░░░░░░░░░░░░░░░░█░  
░░░░░░░░░░░░░░░░██░  
░░░░░░░░░░░░░░░░░░░  
░░░██░░░░░░░░░█░░░░  
░░░██░░░░░░░█░░█░░░  
░░░░░░░░░░░░█░░█░░░  
░░░░░░░░░░░░░█░░░░░  
░░░░░░░░░░░░░░░░░░░  
░░█░█░░░░░░░░░░░░░░  
░░░██░░░░░░░░░░░░░░  
░░░█░░░░░░░░░░░░░░░  
t = 2:  
░░░░░░░░░░░░░░░░░░░  
░███░░░░░░░░░░░░░░░  
░░░░░░░░░░░░░░██░░░  
░░░░░░░░░░░░░░██░░░  
░░░░░░░░░░░░░░░░██░  
░░░░░░░░░░░░░░░░██░  
░░░░░░░░░░░░░░░░░░░  
░░░██░░░░░░░░░░░░░░  
░░░██░░░░░░░░███░░░  
░░░░░░░░░░░░███░░░░  
░░░░░░░░░░░░░░░░░░░  
░░░░░░░░░░░░░░░░░░░  
░░░░█░░░░░░░░░░░░░░  
░░█░█░░░░░░░░░░░░░░  
░░░██░░░░░░░░░░░░░░  
t = 3:  
░░█░░░░░░░░░░░░░░░░  
░░█░░░░░░░░░░░░░░░░  
░░█░░░░░░░░░░░██░░░  
░░░░░░░░░░░░░░█░░░░  
░░░░░░░░░░░░░░░░░█░  
░░░░░░░░░░░░░░░░██░  
░░░░░░░░░░░░░░░░░░░  
░░░██░░░░░░░░░█░░░░  
░░░██░░░░░░░█░░█░░░  
░░░░░░░░░░░░█░░█░░░  
░░░░░░░░░░░░░█░░░░░  
░░░░░░░░░░░░░░░░░░░  
░░░█░░░░░░░░░░░░░░░  
░░░░██░░░░░░░░░░░░░  
░░░██░░░░░░░░░░░░░░  
## Scoring Rules
+ The code should be written solely by the programmer and not copied from other 
places(even a little help, except for what's given here is not allowed).  
+ The project will be tested with other input files(initial maps) in the time 
of interview. So make sure to use different `map.init`s.  
+ There will be an interview in which the programmer will be asked questions 
about his/her code(if rejected, the whole score will be 0).  
### Bonus
+ Definig proper functions, good naming and clear code will have extra points(
up to 10% of the total score).  
+ Using OOP will have extra points(based on the quality of classes, up to 10% 
of the total score).
