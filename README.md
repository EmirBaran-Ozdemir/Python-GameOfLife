# Python-GameOfLife
Conway's Game Of Life recreated using Python
#### Rules
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.
#### Examples of Patterns
Many different types of patterns occur in the Game of Life, which are classified according to their behaviour. Common pattern types include: still lifes, which do not change from one generation to the next; oscillators, which return to their initial state after a finite number of generations; and spaceships, which translate themselves across the grid.

![Blinker](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#/media/File:Game_of_life_blinker.gif)

#### Required Libraries
- [numpy]
- [pygame]
- time -- _Default Python library_
#### Installation
```sh
git clone https://github.com/EmirBaran-Ozdemir/Python-GameOfLife.git
pip install -r requirements.txt
python main.py
```
#### BADGES
[![GitHub issues](https://img.shields.io/github/issues/EmirBaran-Ozdemir/Python-GameOfLife?style=plastic)](https://github.com/EmirBaran-Ozdemir/Python-GameOfLife/issues) [![GitHub forks](https://img.shields.io/github/forks/EmirBaran-Ozdemir/Python-GameOfLife?style=plastic)](https://github.com/EmirBaran-Ozdemir/Python-GameOfLife/network) [![GitHub stars](https://img.shields.io/github/stars/EmirBaran-Ozdemir/Python-GameOfLife?style=plastic)](https://github.com/EmirBaran-Ozdemir/Python-GameOfLife/stargazers) [![GitHub license](https://img.shields.io/github/license/EmirBaran-Ozdemir/Python-GameOfLife?color=succes&style=plastic)](https://github.com/EmirBaran-Ozdemir/Python-GameOfLife/blob/main/LICENSE)  
[![Twitter](https://img.shields.io/twitter/url?label=Personal-Twitter&style=social&url=https%3A%2F%2Ftwitter.com%2FWileLord)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FEmirBaran-Ozdemir%2FOpenCVPython)

[numpy]:<https://pypi.org/project/numpy/>
[pygame]:<https://pypi.org/project/pygame/>