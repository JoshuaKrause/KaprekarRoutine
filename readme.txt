KaprekarRoutine by Joshua Krause (jkrause@joshuakrause.net)

Returns the number of iterations in Kaprekar's Routine, which is as follows:

Given a 4-digit number that has at least two different digits, take that number's descending digits, and subtract that number's ascending digits. For example, given 6589, you should take 9865 - 5689, which is 4176. Repeat this process with 4176 and you'll get 7641 - 1467, which is 6174.
Once you get to 6174 you'll stay there if you repeat the process. In this case we applied the process 2 times before reaching 6174, so our output for 6589 is 2.

Done as an exercise from reddit.com/r/dailyprogrammer/.