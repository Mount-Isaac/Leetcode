Algorithms Q: 1 Q Id: 1373958 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.14 Hard Difficulty:Medium
Topics:Algorithms
## Question

```Sort Array```

Emma has an array P consisting of the integer values from [1, 2, 3 …, N].
You are also given an integer K.
You can perform the following operations:
Choose any consecutive segment of at most K elements of the permutation P.
Sort it in increasing order.
Find the minimum number of operations required to sort the array in increasing order.

Note
N is always greater or equal to 3.
 
Function Description
In the provided code snippet, implement the provided sortArray(...) method to find the minimum number of operations required to sort the array in increasing order. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

Multiple test cases will be running, so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 , which can be modified. Additionally, you can add or remove these output variables.
 
Input Format
The first line contains 2 space-separated integers, N and K, denoting the length of the array P and an integer, respectively.
The second line contains N space-separated integers, denoting the elements of array P.

Sample Input
6 4                       -- denotes N and K
2 6 4 3 1 5           -- denotes P[i]
 
Constraints
3 <= N <= 105
Ceil value of (2N / 3) <= K <= N
1 <= Pi <= N
 
Output Format
The output contains an integer denoting the minimum number of operations required to sort the array in increasing order.
 
Sample Output
3
 
Explanation
N = 6
K = 4
A = [2, 6, 4, 3, 1, 5]
In this case, you can sort segments in the order:
P[2: 5], getting [2, 1, 3, 4, 6, 5].
P[1: 2], getting [1, 2, 3, 4, 6, 5]. 
P[5: 6], getting [1, 2, 3, 4, 5, 6].
Hence, the output is 3.
Used in number of tests : 0 Attempts : 0
Algorithms Q: 2 Q Id: 1373955 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.24 Hard Difficulty:Medium
Topics:Algorithms


## Question

```Sort the Array```

Given an array A[i] of length N.
Each array element has a fixed bit, known as the magic bit, i.e., 0 or 1.
You are allowed to perform the following operations on the array A[i] and sort the array in a non-decreasing order.

Choose a subarray of the array A[i] such that:
The first and last elements of the subarray have different magic bits.
Rearrange the elements in the subarray in any way you want.
Print the minimum number of operations required to sort the array in a non-decreasing order, or -1 if impossible.

Note
N is always greater than 0.
 
Function Description
In the provided code snippet, implement the provided SortArray(...) method to print the minimum number of operations required to sort the array in a non-decreasing order, or -1 if impossible. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running, so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404, which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains a single integer N, denoting the length of the array A[i].
The second line contains N space-separated integers, denoting the elements of the array A[i].
The third line contains a string S of length N, where the ith character of the string denotes the magic bit of the ith element of the array.

Sample Input
5                    -- denotes N
1 3 2 3 7        -- denotes A[i]
11010            -- denotes S

Constraints
1 ≤ N ≤ 2*105
1 ≤ A[i]  ≤ 109, where 1 ≤ i ≤ N

Output Format
The output contains an integer denoting the minimum number of operations required to sort the array in a non-decreasing order or -1 if impossible.
 
Sample Output
1
 
Explanation
A[i] = [1, 3, 2, 3, 7]
S = "11010"
Pick a sub-subarray [3, 2] (magic bits 1 and 0) that allows rearranging.
After rearranging the subarray, it becomes [2, 3].
So the entire array will be [1, 3, 2, 3, 7] -> [1, 2, 3, 3, 7].
Only 1 operation is required to sort the array in a non-decreasing order
Hence, the output is 1
Used in number of tests : 0 Attempts : 0
Algorithms Q: 3 Q Id: 1373954 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.20 Hard Difficulty:Medium
Topics:Algorithms
## Question

```Passing Game```

N players are playing a ball-passing game, and the players are standing in a row.
Initially, every player has their non-negative energy given in the form of an array A, where the ith player has energy A[i] (1 ≤ i ≤ N).
You are free to arrange the players circularly in any order.
Initially, the ball can be held by any player.

The players pass the ball by the following rule:
If the player has positive energy, they pass the ball to the immediate right player.
The act of passing the ball takes 1 second.
The game ends if the player holding the ball has non-positive energy.
After each pass, the energy of the player reduces by 1.
Print the maximum duration of the game.

Note
N is always greater than 0.
 
Function Description
In the provided code snippet, implement the provided PassingGame(...) method to print the maximum duration of the game. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running, so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404, which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains a single integer N, denoting the number of players.
The second line contains N space-separated integers of the array A[i], denoting the energy of the players.

Sample Input
3              -- denotes N
2 1 1        -- denotes A[i]
 
Constraints
1 ≤ N ≤ 105
1 ≤ i ≤ N
1 ≤ A[i] ≤ 106
 
Output Format
The output contains a single integer denoting the maximum duration of the game.
 
Sample Output
4
 
Explanation
N = 3
A[i] = [2, 1, 1]
One of the optimal orders in which all the players can stand in a row is:
1 -> 2 -> 3 -> 1.
The ball is initially with Player 1.
Player 1, in one second, passes the ball to Player 2, and their energy becomes 1.
Player 2, in one second, passes the ball to Player 3, and their energy becomes 0.
Player 3, in one second, passes the ball to Player 1, and their energy becomes 0.
Player 1, in one second, passes the ball to Player 2, and their energy becomes 0.
Player 2 has 0 energy, so they drop the ball.
The game ends.

The maximum duration of the game is 4.

Hence, the output is 4.
Used in number of tests : 0 Attempts : 0
Mathematics Q: 4 Q Id: 1373953 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.14 Hard Difficulty:Medium
Topics:Mathematics

## Question

```Token Numbering```

There are N tokens; each token has a number written on it.
You are given three arrays named P, A, and B of length N.
The ith token can be numbered Ai with probability Pi percent.
For probability 100 - Pi percent, it can be numbered Bi.
It cannot have any other number than Ai and Bi.
A numbering of tokens is correct if all tokens have distinct token numbers.

Find the probability of the correctness of the numbering.

Note
N is always greater than 0.
 
Function Description
In the provided code snippet, implement the provided TokenNumbering(...) method to find the probability of the correctness of the numbering. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains an integer N, denoting the number of tokens.
The second line contains N space-separated integers of array P, denoting the array elements.
The third line contains N space-separated integers of array A, denoting the array elements.
The fourth line contains N space-separated integers of array B, denoting the array elements.

 Sample Input
2             -- denotes N
50 50      -- denotes P[i]
1 2          -- denotes A[i]
2 1          -- denotes B[i]
 
Constraints
1 ≤ N ≤ 50
1 ≤ i ≤ N
1 ≤ A[i], B[i] ≤ 16
0 ≤ P[i] ≤ 100

Output Format
The output contains a float value denoting the probability of the correctness of the numbering.

Sample Output
0.500000000
 
Explanation
P[i] = [50 50]
A[i] = [1 2]
B[i] = [2 1]
We have 2 tokens, so we put the number on token 1 in two ways and on token 2 in two ways.
So, the total number of events is 4.
We can correctly place the number on the token in two ways, i.e., either (1 on token 1 and 2 on token 2) or (2 on token 1 and 1 on token 2).
The number of favorable events is 2.
Probability = 2/4 = 1/2, i.e., 0.500000000.
Hence, the output is 0.500000000.
Used in number of tests : 0 Attempts : 0
Algorithms Q: 5 Q Id: 1373951 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.23 Hard Difficulty:Medium
Topics:Algorithms

## Question

```Minimum Moves```

A string of capital letters, S, represents N islands.
Jacob is stuck on the first island, S1.
He must reach the last island, SN, in a minimum number of moves.
He can only move from one island to another if it satisfies one of these conditions:
If he is currently on index i, he can move to the i+1 index if (i+1 <= N).
If he is currently on index i, he can move to the i-1 index if (i-1 >= 1).
If he is currently on index i, he can move to any island whose value is the same as S[i].
Find the minimum number of moves Jacob requires from island S1 to SN.

Function Description
In the provided code snippet, implement the provided MinMoves(...) method to find the minimum number of moves Jacob required from island S1 to SN. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains an integer N, denoting the size of the string.
The second line contains an N-sized string S, consisting of capital English letters denoting the islands.

Sample Input
9                         -- denotes N
ABCBDEEED     -- denotes S
 
Constraints
1 <= N <= 104

Output Format
The output contains an integer denoting the minimum number of moves Jacob required from island S1 to SN.

Sample Output
4
 
Explanation 
N = 9
S = ABCBDEEED
One of the optimal ways is:
counter = 0
Go from index 1 to 2; (A → B) counter = 1.
Go from index 2 to 4; (B → B) counter = 2.
Go from index 4 to 5; (B → D) counter = 3.
Go from index 5 to 9; (D → D) counter = 4.
The minimum number of moves Jacob required from island S1 to SN is 4.
Hence, the output is 4.
Used in number of tests : 0 Attempts : 0
Dynamic Programming Q: 6 Q Id: 1364970 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.05 Hard Difficulty:Medium
Topics:Dynamic Programming

## Question

```Startup Names```

Bob has been working on creating a startup and needs to pick a name. He has been using a special algorithm to help him.
He is interested in using only the letters, 'x' and 'y'.
He has been trying out different combinations of names, starting from minLength to maxLength.

Bob has two rules for creating these names:
He must add the letter 'x' to the end of the name a certain number of times; let's call it cntOne.
He must add the letter 'y' to the end of the name a certain number of times; let's call it cntTwo.

Print the count of names that satisfy the criteria.

Note
The answer for test cases that are provided can be very large, so print it modulo M, where M = 1e9 + 7.

Example
The initial string is empty.
If cntOne = 3, adding character ‘x’ cntOne times in string str will update string str to “xxx”.
 
Function Description
In the provided code snippet, implement the provided StartupNames(...) method to print the count of names that satisfy the criteria. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running, so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404, which can be modified. Additionally, you can add or remove these output variables.

Input Format
The input contains 4 space-separated integers, minLength, maxLength, cntOne, and cntTwo, denoting the minimum length of the name, the maximum length of the name, the number of times 'x' is to be printed, and the number of times 'y' is to be printed, respectively.

Sample Input
2 3 1 2             -- denotes minLength, maxLength, cntOne, and cntTwo
 
Constraints
1 <= minLength, maxLength <= 105
1 <= cntOne, cntTwo <= minLength

Output Format
The output contains an integer denoting the count of names that satisfy the criteria.

Sample Output
5
 
Explanation
minLength = 2
maxLength = 4
cntOne = 2
cntTwo = 1
In this scenario, according to the rules set by Bob, the names are to be generated with the following specifications:
Names must be between 2 to 4 characters long.
He wants to add 'x' twice to the end and 'y' once to the end.
Based on these rules, the possible names Bob can generate are: "xx", "yy", "xxx", "xxy", and "xyy".
Hence, the output is 5.
Used in number of tests : 0 Attempts : 0
Dynamic Programming Q: 7 Q Id: 1364969 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.30 Medium Difficulty:Medium
Topics:Dynamic Programming

## Question

```Password Capacity```

You have N houses, each with K rooms numbered from 1 to K.
Every room has a single-digit password ranging from 1 to K.
You are given three integers: N (the number of houses), K (the number of rooms in each house), and C (the capacity).

Print the number of possible ways (out of the KN total ways) to open the rooms, such that the sum of the passwords of all rooms equals the capacity.

Note
The output for the provided test cases can be very large, so print it modulo M, where M = 1e9 + 7.
 
Function Description
In the provided code snippet, implement the provided PasswordCapacity(...) method to print the number of possible ways (out of the KN total ways) to open the rooms, such that the sum of the passwords of all rooms equals the capacity. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running, so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404, which can be modified. Additionally, you can add or remove these output variables.

Input Format
The input contains 3 space-separated integers: N, denoting the number of houses; K, denoting the number of rooms in each house; and C, denoting the capacity, respectively.

Sample Input
2 6 10      -- denotes N, K, and C
 
Constraints
1 <= N, K <= 30
1 <= C <= 1000  

Output Format
The output contains an integer denoting the number of possible ways (out of the KN total ways) to open the rooms, such that the sum of the passwords of all rooms equals the capacity.

Sample Output
3
 
Explanation
N = 2
K = 6
C = 10
You visit the following room with the password with a capacity of 10: (4 + 6), (6 + 4), (5 + 5).
The total number of ways is 3.

Hence, the output is 3.
Used in number of tests : 0 Attempts : 0
Dynamic Programming Q: 8 Q Id: 1363272 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.19 Hard Difficulty:Medium
Topics:Dynamic Programming

```## Question```

Maximum Result

Given is a matrix A of size N x N, consisting of two characters (+, -).
We have the result initialized with zero and must maximize it by moving around in the matrix.
At each step, the result gets:
Incremented by the step count for '+'.
Decremented by the step count for '-'.
For example, if the second step is on ‘+’, the result will get incremented by 2.

Find the single integer denoting the maximum result of the matrix.

Function Description
In the provided code snippet, implement the provided maxResult(...) method to find the single integer denoting the maximum result of the matrix. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Note
Initially, we will start with the index (0, 0).
We can only move either right or downwards.
If we are standing at index (i, j), we can move to (i + 1, j) or (i, j + 1) only.

Input Format
The first line contains an integer N, denoting the size of the string.
The second line contains N x N space-separated integers for N rows and N columns, denoting the elements of matrix A.

Sample Input
6                          -- denotes N 
+ - - + + +            -- denotes A[i][j]
- + + - - +
- - + + - -
- - + + + +
+ + - - - +
- - - + - +

Constraints
1 <= N <= 100

Output Format
The output contains a single integer denoting the maximum result of the matrix.

Sample Output
53
 
Explanation
We will first move to the right, then down once; by following the path of all ‘+’, we will get the result of 53, which is the maximum.
Following a similar procedure for '-' will not fetch the maximum result of the matrix.
Hence, the output is 53.
Used in number of tests : 0 Attempts : 0
Recursion Q: 9 Q Id: 1363271 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.05 Hard Difficulty:Medium
Topics:Recursion

## Question

```Maximum Energy```

For a given N power band, the ith power band has a power of Ai.
In a day, we can choose a power band in order from 1 to N.
If we choose the ith power band on a jth day, we will get A[i] x j energy.
The power of each band will decrease by 1 each day.
Given is an N-sized array representing the initial power of each band.

Find the maximum energy we can get.
 
Note
We can complete the first task or the last task.
 
Function Description
In the provided code snippet, implement the provided findmaxscore(...) method to find the maximum energy we can get. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains a single integer N, denoting the size of the array.
The second line contains N space-separated integers A1, A2, A3, …, AN, denoting the elements of the array.

Sample Input
5                     -- denotes N
2 7 1 14 5       -- denotes Ai
 
Constraints
1 <= N <= 100
-1000 <= Ai <= 1000

Output Format
The output contains a single integer denoting the maximum energy we can get.

Sample Output
60
 
Explanation
Initially, we have energy.
We can choose the 1st power band on day 1, so the energy becomes 0 + (2 - 0) *1 = 2.
We can choose the 2nd power band on day 2, so the energy becomes 2 + (7 - 1) * 2 = 14.
We can choose the 3rd power band on day 3, so the energy becomes 14 + (1 - 2) * 3 = 11.
We can choose the 4th power band on day 4, so the energy becomes 11+ (14 - 3) *4 = 55.
We can choose the 5th power band on day 5, so the energy becomes 55 + (5 - 4) *5 = 60.
There is no other way to get an answer greater than 60.
Hence, the output is 60.
Used in number of tests : 0 Attempts : 0
Recursion Q: 10 Q Id: 1363270 Category: Coding Points: 15 Assigned difficulty: Medium Difficulty Index: 0.14 Hard Difficulty:Medium
Topics:Recursion

## Question

```Points Earned```

An N task numbered 1 to N is given.
Each day, you can complete the first task or the last task.
You are given an array of N integers and an integer, K.
The point earned from the ith task on a jth day is A[i] * (k - j).
For a day greater than K, you get zero points.

Find the maximum point earned by you.
 
Note
You can complete the first task or last task, and so on.
Elements of array A are always positive numbers.

Function Description
In the provided code snippet, implement the provided findMaxPoint(...) method to find the maximum point earned by you. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains two integers, N, denoting the size of the array, and an integer, K.
The second line contains N space-separated integers, denoting the elements of array A.

Sample Input
4 3                           -- denotes N and K
45 85 67 32             -- denotes A
 
Constraints
1 <= N <= 400
1 <= K <= 400
1 <= Ai <= 103

Output Format
The output contains a single integer denoting the maximum point earned by you.

Sample Output
175
 
Explanation
You can complete the first task on the 1st day and get 45 * (3 - 1) = 90 points.
On the second, you can complete the second task and get 85 * (3 - 2) = 85 points.
The total point you can get is 90 + 85 = 175.
You cannot get more than 175 points.
Hence, the output is 175.