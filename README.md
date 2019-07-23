### Dhagey

An email thread analyzer.

##### Dependencies

1. Python 3

2. graphviz
 `sudo apt-get install graphviz`

3. python3-gv
 `sudo apt-get install python3-gv`

##### Input Data

1. A file named "thread.txt" placed in the dir in which the program is run. Generate it by choosing print all in the gmail interface and then printing to a text file.

##### Output

1. from => to pairs in text format
 `python3 -m dhagey.main`

2. a graph in png format
 `python3 -m dhagey.main g > out.png`