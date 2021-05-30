# Alphabets-Problem

Given string str consisting of letters only and an integer n, the task is to replace every character of the given string by a character which is n times more than it. If the letter exceeds ‘z’, then start checking from ‘a’ in a cyclic manner.

Examples:
Input: str = “abc”, n = 2
Output: cde
a is moved by 2 times which results in character c
b is moved by 2 times which results in character d
c is moved by 2 times which results in character e

Input: str = “abc”, n= 28
Output: cde
a is moved 25 times, z is reached. Then the 26th character will be a, 27th b and 28th c.
b is moved 24 times, z is reached. 28-th is d.
c is moved 23 times, z is reached. 28-th is f.

Question: 
a/ Write an algorithm to solve the above issue. Please consider the complexity of the algorithm.


b/ What is the disadvantage of using the ASCII value of the letters to solve this problem?


Answer a) python file above.


Answer b) The problem is solved using ascii values which have 128 charcters and every character entered in string will be converted to charter+n'th 
          character, We could probably solve this porblem by making a list/array of alphabets both inlcuding capital as well as small case , And then solve using
          list. There also a problem in this code because after "Z" it does continue with alphabets but displays character after "Z" like "[ /" etc.
