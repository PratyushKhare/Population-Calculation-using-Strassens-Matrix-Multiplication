# Population-Calculation-using-Strassens-Matrix-Multiplication

This project gives population of lizards at a time k, given the life table of lizards at time k-1.

Introduction:

- Matrices are frequently used in all the biological fields as organizers of numerical information since they greatly increase the ease and efficiency of analyzing data. 
- The Leslie matrix is one of the most well known ways to describe the growth of populations.
- I have merged the concept of population growth, matrix multiplication and Leslie’s Matrix to get an important application of Strassen’s Algorithm.

Problem Statement:

Given the life table on lizards at time ‘k-1’ as follows:
![Life Table](/images/1.png)
Using Leslie Matrix and the concept of matrix multiplication, find number of lizards of each age group alive at time ‘k’.

Working:
It has four steps:- 
1. Divide the input matrices A and B and output matrix C into four  n/2 x n/2 submatrices.
2. Create 10 matrices S1, . . . . , S2, S10, each of which is n/2 x n/2 and is the sum or difference of two matrices created in step 1. We can create all 10 matrices in O(n^2) time. 
3. Using the submatrices created in step 1 and the 10 matrices created in step 2, recursively compute seven matrix products P1, P2 , . . . . , P7. Each matrix Pi is “n/2 x n/2”. 
4. Compute the desired submatrices C11, C12, C21, C22 of the result matrix C by adding and subtracting various combinations of the Pi matrices. We can compute all four submatrices in O(n^2) time.

