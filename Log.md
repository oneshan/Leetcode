# Log

## 2017.07.03   (Day 04)
031.next-permutation.py 
> ✔ 265/265 cases passed (68 ms)
> For example: {4, 7, 5, 3, 1}
>
> Since {7, 5, 3, 1} are decreasing array, we need to swap 4 (nums[j-1]) and its successor 5 (nums[i])
> And then reverse nums[j:] to get its next permutation {5, 1, 3 ,4, 7} 

032.longest-valid-parentheses.py
> ✔ 229/229 cases passed (68 ms)
> - DP: `dp[i] = dp[i-1] + 2 (+ dp[i-dp[i]] )`
> - Stack: store index of beginning of valid string

## 2017.07.02   (Day 03)

016.3sum-closest.py
> ✔ 125/125 cases passed (112 ms)
> - Similar to p015, but this time, check the closest num before updating the two pointers

017.letter-combinations-of-a-phone-number.py 
> ✔ 25/25 cases passed (42 ms)
> Generate letter mapping and then use DFS to track all possible string
> - mapping: 2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7:pqrs, 8: tuv, 9: wxyz

018.4sum.py
> ✔ 282/282 cases passed (1042 ms)
> - Same as p015

019.remove-nth-node-from-end-of-list.py 
> ✔ 207/207 cases passed (46 ms)
> - Use two pointer and dummy node, initial: p1 = head, p2 = dummy
>   1. Advance the pointer p1 n steps
>   2. Advance both pointer until p1 reaches None, p2 will point to n-1 th node from the end of list.
>   3. Remove nth node by p2.next = p2.next.next
> - Test cases: remove head, tail and middle node

020.valid-parentheses.py
> ✔ 73/73 cases passed (42 ms)
> - Use stack to store `{[(`
> - Test cases: valid - `{}(){()}`, invalid - `]`, `[`, `{]}`

021.merge-two-sorted-lists.py 
> ✔ 208/208 cases passed (49 ms)
> - Compare the value of l1, l2, append the smaller node to the new list, then advance it and the new list.

022.generate-parentheses.py
> ✔ 8/8 cases passed (65 ms)
> - Use DFS backtracking
> - At each position, the number of right parenthese <= the number left parenthese

024.swap-nodes-in-pairs.py 
> ✔ 55/55 cases passed (52 ms)
> - In each iteraition, we update three reference from `curr->p1->p2->p2.next` to `curr->p2->p1->p2.next`

026.remove-duplicates-from-sorted-array.py 
> ✔ 161/161 cases passed (85 ms)
> - Go thought the whole array, increment idx and copy num into nums[idx] when it is not a duplicate value (i.e. num != nums[idx])

027.remove-element.py 
> ✔ 113/113 cases passed (39 ms)
> - Similar to p026, copy num into nums[idx] and increment idx if we don't remove it.

028.implement-strstr.py 
> ✔ 74/74 cases passed (39 ms)
> - Test cases: empty needle, contains part of needle, contains full needle
> - Optimized solution: [KMP algo](http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/), [Rabin-Karp algo](http://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/)

029.divide-two-integers.py 
> ✔ 988/988 cases passed (59 ms)
> - Record the sign and set the two numbers to absolute value before calculate
> - Repeat subtract cumulative `2^k * divisor`

## 2017.07.01   (Day 02)

008.string-to-integer-atoi.py 
> ✔ 1047/1047 cases passed (55 ms)
> - Care about sign mark '+/-'

012.integer-to-roman.py
> ✔ 3999/3999 cases passed (126 ms)
> - Roman numerals I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
> - Specific cases: IV: 4, IX: 9, XL: 40, XC: 90, CD: 400, CM: 900

013.roman-to-integer.py
> ✔ 3999/3999 cases passed (142 ms)
> - minus the value if next numerals is larger, for example: IV = -1 + 4

014.longest-common-prefix.py
> ✔ 117/117 cases passed (39 ms)
> - sort the string array, the longest common prefix will be the common-prefix of the first and the last one
> - other solution: [binary search](http://www.geeksforgeeks.org/longest-common-prefix-set-4-binary-search/)

015.3sum.py
> ✔ 313/313 cases passed (969 ms)
> - sort the number array, then use one for-loop and two pointer to approach zero, O(n^2)


## 2017.06.30   (Day 01)

001.two-sum.py
> ✔ 19/19 cases passed (38 ms)
> - Use hash Table to store number position: `pos[target - num]=idx`

002.add-two-numbers.py
> ✔ 1562/1562 cases passed (119 ms)
> - l1, l2 may contains different length.
> - Don't forget to check carry value after adding

003.longest-substring-without-repeating-characters.py
> ✔ 983/983 cases passed (85 ms)
> - Use hash table to record the last position of character
> - update left bound to `pos[ch]+1` when hitting the repeating char (ch).

005.longest-palindromic-substring.py 
> ✔ 94/94 cases passed (1422 ms)
> - For each char in the string, check if it is a middle of palindromic (even and odd case)

007.reverse-integer.py
> ✔ 1032/1032 cases passed (56 ms)
> - Record the sign of num and then use while-loop to get the reverse of abs(num)

009.palindrome-number.py
> ✔ 11507/11507 cases passed (426 ms)
> - Negative numbers are not palindrome, compare original integer and its reverse

011.container-with-most-water.py 
> ✔ 49/49 cases passed (122 ms)
> - Use two pointer, the size of container depends on shorter line


