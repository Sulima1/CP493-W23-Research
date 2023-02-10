# CP493-W23-Research


## Problem Statement

Given a positive integer λ and 3 text files A, B, and C, each having k columns and 10 million rows, the goal is to find 3 rows LA, LB, LC in files A, B, C respectively such that:

```scss

LA(1) + LB(1) + LC(1) = λ
...
LA(k) + LB(k) + LC(k) = λ
```
## Desired Outcome

The solution should work for a 3-way matching with files A, B, and C having 10 million rows each and around k = 40 columns. The number of rows can vary, but the order of magnitude should be 10 million.

## Algorithm

The current solution under development uses a combination of hash-threading to achieve the desired results. The algorithm creates a 2D array as a sort of hash table to store the first column value indexes of file B. A hash table allows for O(1) lookup of any element by using the element as an index. The algorithm then calculates the Bx value by using the equation A - (λ - C) = Bx and searches for the Bx value in the hash table. If a value is found within B, the indexes of A and C along with the hash table within B are stored. Once all potential combinations are stored, they are processed using threads. Each thread checks a specific combination of A row, B row, and C row to verify if all elements are equal to λ. If a thread fails to meet this requirement, it is released, and a new combination is tested.

## General Steps

1. Store index values in the hash table by adding strings.
2. Loop through the first column of file B and insert the index values of the given elements into the hash table.
3. Create a nested loop to run through all the potential combinations of A with C.
4. Process the stored values into strings consisting of Axindex, Bxindex, and Cxindex.
5. Pass strings to 8 threads, with each string checking a specific row. If a combination of a row from A, B, and C is not equal to λ, the thread is released.
6. When a thread search on a particular group of rows is complete and it is confirmed that all values are equal to λ, return the original string in an array along with other passed groups as a set of answers.
