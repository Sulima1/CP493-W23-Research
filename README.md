[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# CP493-W23-Research

## Abstract

The term "Big Data" encompasses the enormous quantities of data that are produced daily fromvarious sources, including finance, healthcare, retail, and manufacturing. The sheer volume, velocity, and variety of this data can be overwhelming, but with the right tools and techniques, it can be harnessed to derive valuable insights. This specific problem, Tripartite Integer Partitioning Problem, consists of three large text files consisting of millions of rows of integers and 50 columns. Given a positive integer λ, we must calculate 3 rows _L<sub>A</sub>_, _L<sub>B</sub>_, _L<sub>C</sub>_ in files A, B, C respectively so that _L<sub>A</sub> (n) + L<sub>B</sub> (n) + L<sub>C</sub> (n) = λ_. In order to find a valid solution, a complicated algorithm must be applied. By taking the first column of each text file and applying _L<sub>k</sub> (n) ≡ r(mod 10)_, where _k_ is each text file and _r_ is the remainder, we can simplify and narrow down the number of valid rows. Then by applying a hashmap function to each column where _{key:value}is {L<sub>k</sub> (n) ≡ r (mod 10):the index of the correlated value}_ we can further isolate the valid rows. Ideally, this algorithmic solution can reduce the number of possible rows by just over half eachtime and complete the problem as close to _O(n)_ runtime as possible. Practical applications of this solution can lead to correlation properties which can improve services in areas such as wireless communication, drug design, cryptography, and radar technology.

## Problem Statement

Given a positive integer λ and 3 text files A, B, and C, each having k columns and 10 million rows, the goal is to find 3 rows LA, LB, LC in files A, B, C respectively such that:

```

_L<sub>A</sub>(1) + L<sub>B</sub>(1) + L<sub>C</sub>(1) = λ_
...
_L<sub>A</sub>(k) + L<sub>B</sub>(k) + L<sub>C</sub>(k) = λ_
```
## Desired Outcome

The solution should work for a 3-way matching with files _A_, _B_, and _C_ having 10 million rows each and around k = 50 columns. The number of rows can vary, but the order of magnitude should be 10 million.

## Algorithm

The current solution under development uses a combination of hash-threading to achieve the desired results. The algorithm creates a 2D array as a sort of hash table to store the first column value indexes of file _B_. A hash table allows for _O(1)_ lookup of any element by using the element as an index. The algorithm then calculates the Bx value by using the equation _A - (λ - C) = B_ and searches for the _B_ value in the hash table. If a value is found within _B_, the indexes of _A_ and _C_ along with the hash table within B are stored. Once all potential combinations are stored, they are processed using threads. Each thread checks a specific combination of _A_ row, _B_ row, and _C_ row to verify if all elements are equal to _λ_. If a thread fails to meet this requirement, it is released, and a new combination is tested.

## General Steps

1. Grab the first  coloumn of file A file B file C

2. place each of them into their own seperate hash 1000 slots long (k<=1000) k is defined 
   as the value of a number in the files. Each number in the coloumn represents its position in the hash.
   the values stored are the indexes of the numbers. So if 35 is found at index 3,7,8 in col a----> col a hash 
   slot 35 will contain string "3,5,8".

3. for coloumn  of a b and c, loop through a and c hash
    if a[i] hash slot empty or c[j] hash slot empty, continue
    else do eqaution b_val=lam-j-i. check b_hash[b_value]. if is
    empty string continue else store (i, b_val, j) in a potential array.

4. gather all the potentials for a col 1, b col 1 ,c col 1 so that they are in seperate sets

5. repeat steps 1-4 for coloumn two of A,B,C

6. do intersection of sets Acol1 and A col2, B col 1 b col 2 , c col 1  c col 2

7. repeat step 2 but this time add a constraint to only hash the values which are found within the intersection

8. repeat step 3

9. loop step 7 and 8 for all coloumns of A B and C (starting from coloumn three as steps 1-6 use the first two col)
