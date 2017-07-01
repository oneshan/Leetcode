# Log

## 2017.06.30

001.two-sum.py
> ✔ 19/19 cases passed (38 ms)
> Use hash Table to store number position: `pos[target - num]=idx`

002.add-two-numbers.py
> ✔ 1562/1562 cases passed (119 ms)
> Note1. l1, l2 may contains different length.
> Note2. Don't forget to check carry value after adding

003.longest-substring-without-repeating-characters.py
> ✔ 983/983 cases passed (85 ms)
> Use hash table to record the last position of character
> update left bound to `pos[ch]+1` when hitting the repeating char (ch).

005.longest-palindromic-substring.py 
> ✔ 94/94 cases passed (1422 ms)
> For each char in the string, check if it is a middle of palindromic (even and odd case)

007.reverse-integer.py
> ✔ 1032/1032 cases passed (56 ms)
> Record the sign of num and then use while-loop to get the reverse of abs(num)

009.palindrome-number.py
> ✔ 11507/11507 cases passed (426 ms)
> Negative numbers are not palindrome, compare original integer and its reverse

011.container-with-most-water.py 
> ✔ 49/49 cases passed (122 ms)
> Use two pointer, the size of container depends on shorter line


