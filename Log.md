# Log

## 2017.07.29   (Day 28)

213.house-robber-ii.py
> ✔ 74/74 cases passed (32 ms)
> - DP 2 times, (0~n-1 & 1~n)

210.course-schedule-ii.py 
> ✔ 37/37 cases passed (76 ms)
> - topological sort (BFS)

209.minimum-size-subarray-sum.py
> ✔ 15/15 cases passed (58 ms)
> - two pointer (like 076 minimum-window-substring) 

208.implement-trie-prefix-tree.py
> ✔ 14/14 cases passed (335 ms)
> - TrieNode has dictionary (childs) and bool (isWord)

207.course-schedule.py
> ✔ 37/37 cases passed (79 ms)
> - topological sort (BFS)

## 2017.07.28   (Day 27)

206.reverse-linked-list.py
> - ✔ 27/27 cases passed (38 ms) -- iter
> - ✔ 27/27 cases passed (48 ms) -- recur

205.isomorphic-strings.py 
> ✔ 30/30 cases passed (76 ms)
> - Use two dictionary (s2t, t2s) to check mapping 

204.count-primes.py
> ✔ 20/20 cases passed (1352 ms)
> - Sieve of Eratosthenes

203.remove-linked-list-elements.py 
> ✔ 65/65 cases passed (125 ms)
> - If the value of next node value is val, then we point to next.next node

202.happy-number.py
> ✔ 401/401 cases passed (38 ms)
> - while loop, use a set to store previous number and check if there is a cycle

## 2017.07.27   (Day 26)

201.bitwise-and-of-numbers-range.py
> ✔ 8266/8266 cases passed (112 ms)
> - Right Shift until m equals to n, then left shift back

200.number-of-islands.py
> ✔ 47/47 cases passed (75 ms)
> - DFS

199.binary-tree-right-side-view.py 
> ✔ 210/210 cases passed (46 ms)
> - BFS

198.house-robber.py
> ✔ 69/69 cases passed (36 ms)
> - DP

## 2017.07.26   (Day 25)

191.number-of-1-bits.py 
> ✔ 600/600 cases passed (39 ms)
> - To remove rightmost 1bit: `n &= (n-1)`

190.reverse-bits.py
> ✔ 600/600 cases passed (38 ms)
> - for-loop reverse 32bit

189.rotate-array.py
> ✔ 33/33 cases passed (128 ms)
> - Reverse 3 times

187.repeated-dna-sequences.py
> - ✔ 32/32 cases passed (195 ms) -- use substr as key
> - ✔ 32/32 cases passed (142 ms) -- mapping substr to integer then used as key
> - Use hash table to count each candidate

## 2017.07.25   (Day 24)

173.binary-search-tree-iterator.py
> ✔ 61/61 cases passed (159 ms)
> - Use stack to store left nodes

172.factorial-trailing-zeroes.py
> ✔ 502/502 cases passed (49 ms)
> - Just consider 5, 25, 125, ...

171.excel-sheet-column-number.py 
> - ✔ 1000/1000 cases passed (56 ms) -- mapping
> - ✔ 1000/1000 cases passed (45 ms) -- ord(ch) - 64
> - ord('A') == 64

## 2017.07.24   (Day 23)

169.majority-element.py
> ✔ 44/44 cases passed (52 ms)
> - Store local element and a counter (default 0), compare element to increase/decrease counter, update local element if counter == 0

168.excel-sheet-column-title.py 
> ✔ 18/18 cases passed (49 ms)
> - In each iteration, n minus 1 before mapping

166.fraction-to-recurring-decimal.py
> ✔ 35/35 cases passed (62 ms)
> - Use hash table store remainder to check repeating
> - Testcases: `0, -5 (0)`, `1, 6 (0.1(6))`, `-1, 5 (-0.2)`

## 2017.07.23   (Day 22)

167.two-sum-ii-input-array-is-sorted.py 
> - ✔ 16/16 cases passed (36 ms) -- Hash
> - ✔ 16/16 cases passed (39 ms) -- Two pointer

165.compare-version-numbers.py
> ✔ 71/71 cases passed (36 ms)
> - Testcases: `1, 1.1`, `1, 1.0`

162.find-peak-element.py
> ✔ 58/58 cases passed (35 ms)
> - Binary Search, compare nums[mid] & nums[mid+1]

160.intersection-of-two-linked-lists.py 
> ✔ 42/42 cases passed (425 ms)
> - Shift the longer one until they have same length, then compare

155.min-stack.py
> ✔ 18/18 cases passed (85 ms)
> - Use additional list to record minimum value

154.find-minimum-in-rotated-sorted-array-ii.py
> ✔ 192/192 cases passed (42 ms)
> - Binary search, left-shift the right pointer if nums[mid] == nums[right]

153.find-minimum-in-rotated-sorted-array.py
> ✔ 146/146 cases passed (32 ms)
> - Binary search, compare nums[mid] & nums[right]

## 2017.07.22   (Day 21)
152.maximum-product-subarray.py
> ✔ 183/183 cases passed (48 ms)
> - Record current maximum and minimum (current min product negative number may be larger than current max)

## 2017.07.21   (Day 20)
150.evaluate-reverse-polish-notation.py
> ✔ 20/20 cases passed (88 ms)
> - Use stack to store operand, handle negative division
> - In Python3, `-1 // 2 == -1`, but we need `-(1 // 2) == 0`

147.insertion-sort-list.py
> ✔ 21/21 cases passed (262 ms)
> - To speed up, check value of the tail node of sorted list and inserting node before each iteration

145.binary-tree-postorder-traversal.py
> - ✔ 67/67 cases passed (42 ms) -- recur
> - ✔ 67/67 cases passed (39 ms) -- iter
> - Use stack, self-left-right then reverse ans array

144.binary-tree-preorder-traversal.py
> - ✔ 67/67 cases passed (46 ms) -- recur
> - ✔ 67/67 cases passed (36 ms) -- iter
> - Use stack, self-right-left

## 2017.07.20   (Day 19)
143.reorder-list.py 
> ✔ 13/13 cases passed (138 ms)
> - Find the middle node of list -> Reverse second-half list -> Merge

142.linked-list-cycle-ii.py 
> ✔ 16/16 cases passed (86 ms)
> - Two pointer (two step, one step)

141.linked-list-cycle.py
> ✔ 16/16 cases passed (106 ms)
> - Two pointer (two step, one step)

130.surrounded-regions.py
> ✔ 60/60 cases passed (99 ms)
> - BFS, traverse from border 'O's, all connections are remains 'O'

127.word-ladder.py
> ✔ 39/39 cases passed (819 ms)
> - BFS 

126.word-ladder-ii.py
> ✔ 39/39 cases passed (656 ms)
> - BFS, use a dictionary graph to record parents of word
> - Note: if endWord not in wordList: return []

## 2017.07.19   (Day 18)

133.clone-graph.py 
> ✔ 12/12 cases passed (99 ms)
> - To avoid a cycle, check if the node is visited

124.binary-tree-maximum-path-sum.py
> ✔ 92/92 cases passed (142 ms)
> - Recursion, cut if sum < 0

117.populating-next-right-pointers-in-each-node-ii.py
> ✔ 61/61 cases passed (105 ms) -- iter
> Use dummy to store the head node of next layer

116.populating-next-right-pointers-in-each-node.py
> - ✔ 14/14 cases passed (76 ms) -- recur
> - ✔ 14/14 cases passed (75 ms) -- iter
> - BFS, since it is perfect binary tree, recursion with parent's info

## 2017.07.16   (Day 17)

136.single-number.py
> ✔ 15/15 cases passed (42 ms)
> - Bitwise (xor)

137.single-number-ii.py
> - ✔ 11/11 cases passed (39 ms)
> - Bitwise (xor)

## 2017.07.15   (Day 16)

129.sum-root-to-leaf-numbers.py
> ✔ 109/109 cases passed (52 ms)
> - Recursion

128.longest-consecutive-sequence.py
> ✔ 68/68 cases passed (42 ms)
> - Union Find

125.valid-palindrome.py
> ✔ 476/476 cases passed (115 ms)
> - Use two pointer
> - ord('0') = 48, ord('9') = 57, ord('a') = 97, ord('z') = 122, ord('A') = 65, ord('Z') = 90

123.best-time-to-buy-and-sell-stock-iii.py 
> ✔ 198/198 cases passed (79 ms)
> - max_profit = max(prices[i:j], prices[j:k])

122.best-time-to-buy-and-sell-stock-ii.py 
> ✔ 198/198 cases passed (36 ms)
> - sell stock if the price is higher than next day

121.best-time-to-buy-and-sell-stock.py
> ✔ 200/200 cases passed (53 ms)
> - Use extra O(1) space to record max profit and min price

120.triangle.py 
> ✔ 43/43 cases passed (42 ms)
> - Bottom up

114.flatten-binary-tree-to-linked-list.py 
> - ✔ 225/225 cases passed (52 ms) -- iter (w/ stack)
> - ✔ 225/225 cases passed (52 ms) -- recur (w/ stack)
> - ✔ 225/225 cases passed (49 ms) -- recur (w/o stack)
> - Preorder

> - ✔ 225/225 cases passed (42 ms) -- iter (w/o stack)
> - Move curr.right below the rightmost node of curr.left 

110.balanced-binary-tree.py
> - ✔ 226/226 cases passed (99 ms) -- iter
> - ✔ 226/226 cases passed (72 ms) -- recur
> - Calculate the height of left tree and right tree and check isBalanced in each recursion

## 2017.07.14   (Day 15)
119.pascals-triangle-ii.py 
> ✔ 34/34 cases passed (39 ms)
> - 0th [1], 1th [1,1], 2th [1,2,1]

118.pascals-triangle.py
> ✔ 15/15 cases passed (39 ms)
> - `[1,2,1] -> [1] + [1+2, 2+1] + [1] == [1,3,3,1]`

## 2017.07.13   (Day 14)

113.path-sum-ii.py 
> - ✔ 114/114 cases passed (82 ms) -- recur
> - ✔ 114/114 cases passed (72 ms) -- iter 

112.path-sum.py 
> - ✔ 114/114 cases passed (55 ms) -- recur
> - ✔ 114/114 cases passed (62 ms) -- iter

111.minimum-depth-of-binary-tree.py
> - ✔ 41/41 cases passed (72 ms) -- recur
> - ✔ 41/41 cases passed (99 ms) -- iter

109.convert-sorted-list-to-binary-search-tree.py
> ✔ 32/32 cases passed (262 ms)
> - set mid node as root

108.convert-sorted-array-to-binary-search-tree.py
> ✔ 32/32 cases passed (119 ms)
> - set array[mid] as root

106.construct-binary-tree-from-inorder-and-postorder-traversal.py
> ✔ 202/202 cases passed (205 ms)
> - postorder[-1] is root node, use node's index in inorder array to split into left and right subtree

105.construct-binary-tree-from-preorder-and-inorder-traversal.py
> ✔ 202/202 cases passed (192 ms)
> - preorder[0] is root node, use node's index in inorder array to split into left and right subtree

103.binary-tree-zigzag-level-order-traversal.py
> ✔ 33/33 cases passed (42 ms)
> - insert element into the head or tail of array by checking node's level is odd or even

006.zigzag-conversion.py
> ✔ 1158/1158 cases passed (122 ms)
> - mapping idx by mod (2n - 2)

## 2017.07.12   (Day 13)

107.binary-tree-level-order-traversal-ii.py 
> ✔ 34/34 cases passed (42 ms)
> - Same as 102

104.maximum-depth-of-binary-tree.py
> - ✔ 38/38 cases passed (76 ms) -- recur
> - ✔ 38/38 cases passed (78 ms) -- iter

102.binary-tree-level-order-traversal.py
> - ✔ 34/34 cases passed (52 ms) -- recur
> - ✔ 34/34 cases passed (55 ms) -- iter (Use Queue)

101.symmetric-tree.py 
> - ✔ 193/193 cases passed (52 ms) -- recur
> - ✔ 193/193 cases passed (38 ms) -- iter
> - Recursion: check (p, q) (p.left, q.right) (p.right, q.left)
> - Iterative: Use two stack 

100.same-tree.py
> ✔ 54/54 cases passed (55 ms)
> - Recursion check node's val

098.validate-binary-search-tree.py 
> - ✔ 74/74 cases passed (68 ms) -- inorder
> - Traverse inorder to generate arr, arr is sorted if it is a valid BST
> - ✔ 74/74 cases passed (98 ms) -- recur
> - Recursion: compare node.val and min & max

095.unique-binary-search-trees-ii.py
> ✔ 9/9 cases passed (85 ms)
> - Recursion: for each node i, leftTrees = genBST(min, i-1), rightTrees = genBST(i+1, max), do combination

## 2017.07.11   (Day 12)

096.unique-binary-search-trees.py 
> ✔ 19/19 cases passed (32 ms)
> - Use DP (Sum up all possible combinations for each node as root)

094.binary-tree-inorder-traversal.py
> ✔ 68/68 cases passed (32 ms) -- recursion
> ✔ 68/68 cases passed (39 ms) -- iterative (use stack)

090.subsets-ii.py
> ✔ 19/19 cases passed (75 ms)
> - sort and then recursion, skip duplicates by checking nums[i] == nums[i-1]

## 2017.07.10   (Day 11)

092.reverse-linked-list-ii.py
> ✔ 44/44 cases passed (49 ms)
> 1. Reverse node from position m to n
> 2. Let original mth node points to (n+1)th node
> 3. Let original (m-1)th node points to nth node

091.decode-ways.py 
> ✔ 259/259 cases passed (49 ms)
> - Use DP, Initial: `dp[1] = 1, dp[i] = 0`
> - dp[i] += dp[i-1] if 1 <= Y <= 9      ("AB" (1 2))
> - dp[i] += dp[i-2] if 10 <= XY <= 26   ("L" (12))

## 2017.07.09   (Day 10)

089.gray-code.py
> - ✔ 12/12 cases passed (35 ms)
> - ✔ 12/12 cases passed (49 ms) -- math
> - Math Formula: `Gray[n] = n ^ (n / 2)`
> - To generate n-bit gray code, prefix 0 with (n-1)bit list append prefix 1 with reversed (n-1)bit list

088.merge-sorted-array.py
> ✔ 59/59 cases passed (49 ms)
> Merge from end to begin

086.partition-list.py
> ✔ 166/166 cases passed (39 ms)
> - 1. Create two head node h1, h2 for smaller and greater/equal list
> - 2. Go through the original list, put nodes into one of list according its value
> - 3. Let the last node of greater list point to `None` and put the list behind smaller one

## 2017.07.08   (Day 09)

083.remove-duplicates-from-sorted-list.py
> ✔ 164/164 cases passed (49 ms)
> - Edit node.next if there are duplicates

082.remove-duplicates-from-sorted-list-ii.py
> ✔ 168/168 cases passed (52 ms)
> - Use two pointer

080.remove-duplicates-from-sorted-array.py
> - ✔ 164/164 cases passed (55 ms) -- ver1
> - ✔ 164/164 cases passed (59 ms) -- ver2
> - Use two pointer

079.word-search.py
> ✔ 87/87 cases passed (382 ms)
> - DFS

078.subsets.py
> ✔ 10/10 cases passed (42 ms)
> - Recursion

076.minimum-window-substring.py
> ✔ 268/268 cases passed (99 ms)
> - Use hash table to store the occurance of chars in t
> - If window found (count == 0), minimize the windows size and update answer candidate

071.simplify-path.py
> ✔ 252/252 cases passed (66 ms)
> - Use stack to store part of path
> - insert `/` to ease the coding

## 2017.07.07   (Day 08)

075.sort-colors.py 
> ✔ 86/86 cases passed (38 ms)
> - Use two pointer i, j point the beginning and end of array
> - Then go through the array and move 0 & 2 to those pointer

074.search-a-2d-matrix.py
> ✔ 136/136 cases passed (35 ms)
> - Binary Search 

073.set-matrix-zeroes.py 
> ✔ 157/157 cases passed (362 ms)
> - Use the first col and the first row as zero mark

072.edit-distance.py
> ✔ 1146/1146 cases passed (212 ms)
> - Use DP, `dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])`

070.climbing-stairs.py
> ✔ 45/45 cases passed (29 ms)
> - Use DP, formula: `dp[1] = 1, dp[2] = 2, dp[i] = dp[i-1] + dp[i-2]`

069.sqrtx.py
> ✔ 1017/1017 cases passed (46 ms)
> - Binary Search
> - Testcase: sqrt(1) = 1, sqrt(5) = 2

067.add-binary.py
> ✔ 294/294 cases passed (59 ms)

066.plus-one.py
> ✔ 108/108 cases passed (52 ms)

## 2017.07.06   (Day 07)

064.minimum-path-sum.py
> ✔ 61/61 cases passed (75 ms)
> - Use DP
>   1. Initial `grid[i][0] += grid[i-1][0], grid[0][j] += grid[0][j - 1]`
>   2. Formula: `grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]` i = 1~m, j = 1~n

063.unique-paths-ii.py 
> ✔ 43/43 cases passed (45 ms) -- 2-d ver.
>
> ✔ 43/43 cases passed (35 ms) -- 1-d ver.
> - Additional Condition: `dp[i][j] = 0 if obstacleGrid[i][j] == 1 `

062.unique-paths.py 
> ✔ 61/61 cases passed (42 ms) -- 2-d ver.
>
> ✔ 61/61 cases passed (29 ms) -- 1-d ver.
> - Use DP, Initial: `dp[i][0] = dp[0][j] = 1`, Formula: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

061.rotate-list.py 
> ✔ 230/230 cases passed (59 ms)
> - k may be zero or larger than the size of list
> - Use two pointer, rotate if p1.next != head

059.spiral-matrix-ii.py 
> ✔ 21/21 cases passed (43 ms)
> - Same as p054

058.length-of-last-word.py
> ✔ 59/59 cases passed (32 ms)
> - search from right to left until find the second non-adjacent space

057.insert-interval.py
> ✔ 154/154 cases passed (72 ms)
> - Use two pointer

056.merge-intervals.py
> ✔ 169/169 cases passed (79 ms)
> - sort by interval.start before merge

## 2017.07.05   (Day 06)

055.jump-game.py
> ✔ 75/75 cases passed (62 ms)
> - store max distance you can jump

054.spiral-matrix.py 
> ✔ 22/22 cases passed (32 ms)
> - record boardary and run four direction

053.maximum-subarray.py
> ✔ 202/202 cases passed (89 ms)
> - O(n): record currSum and maxSum, reset when currSum < 0

050.powx-n.py
> ✔ 300/300 cases passed (46 ms)
> - Use recursion, `x ** n = (x * x) ** (n >> 1) * (1 or x)`

049.group-anagrams.py 
> ✔ 101/101 cases passed (209 ms)
> - Use Hash table
> - map each char to a different prime number, and multiply all of chars as its key (or simply use sorted string as key)

048.rotate-image.py 
> ✔ 20/20 cases passed (39 ms)
> - Flip anti diagonal and then flip vertical

047.permutations-ii.py 
> ✔ 30/30 cases passed (99 ms)
> - sort before DFS (for skipping duplicate)

046.permutations.py 
> ver1 ✔ 25/25 cases passed (66 ms)
>
> ver2 ✔ 25/25 cases passed (75 ms)
> - Use DFS

045.jump-game-ii.py 
> ✔ 92/92 cases passed (62 ms)
> - Use greedy, keep updating the current maximum jump, count and the next maximum jump

042.trapping-rain-water.py 
> ✔ 315/315 cases passed (45 ms)
> - Use two pointer and record maximum boardary, trapped water depends on lower one


## 2017.07.04   (Day 05)

041.first-missing-positive.py
> ✔ 156/156 cases passed (42 ms)
> - Use array elements as index, move element if the index is valid (`size > nums[i] >= 0`)

040.combination-sum-ii.py
> ✔ 172/172 cases passed (96 ms)
> - Similar to 039, but need to sort and skip duplicate combination

039.combination-sum.py
> ✔ 168/168 cases passed (85 ms)
> - Use DFS

038.count-and-say.py
> ✔ 18/18 cases passed (59 ms)
> - Store prev char and its occurance, use for-loop to compare the current char with the previous one

037.sudoku-solver.py
> ✔ 6/6 cases passed (1232 ms) 
> - Use DFS backtracking

036.valid-sudoku.py
> ✔ 501/501 cases passed (92 ms)
> - For each numbers, check if its value occurs just once in row, column, and sub-box

035.search-insert-position.py 
> ✔ 62/62 cases passed (58 ms)
> - Use Binary Search, return left if target not found

034.search-for-a-range.py
> ✔ 87/87 cases passed (36 ms)
> - Use Binary Search to find the target, left boundary and right boundary

033.search-in-rotated-sorted-array.py 
> ✔ 196/196 cases passed (39 ms)
> - Find the rotated pivot, then compare target and nums[0] to decide the boundary of Binary Search
> - Binary Search (One Pass ver.): Check whether target locates at the sorted part


## 2017.07.03   (Day 04)

032.longest-valid-parentheses.py
> ✔ 229/229 cases passed (68 ms)
> - DP: `dp[i] = dp[i-1] + 2 (+ dp[i-dp[i]] )`
> - Stack: store index of beginning of valid string

031.next-permutation.py 
> ✔ 265/265 cases passed (68 ms)
> For example: {4, 7, 5, 3, 1}
>
> Since {7, 5, 3, 1} are decreasing array, we need to swap 4 (nums[j-1]) and its successor 5 (nums[i])
> And then reverse nums[j:] to get its next permutation {5, 1, 3 ,4, 7} 


## 2017.07.02   (Day 03)

029.divide-two-integers.py 
> ✔ 988/988 cases passed (59 ms)
> - Record the sign and set the two numbers to absolute value before calculate
> - Repeat subtract cumulative `2^k * divisor`

028.implement-strstr.py 
> ✔ 74/74 cases passed (39 ms)
> - Test cases: empty needle, contains part of needle, contains full needle
> - Optimized solution: [KMP algo](http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/), [Rabin-Karp algo](http://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/)

027.remove-element.py 
> ✔ 113/113 cases passed (39 ms)
> - Similar to p026, copy num into nums[idx] and increment idx if we don't remove it.

026.remove-duplicates-from-sorted-array.py 
> ✔ 161/161 cases passed (85 ms)
> - Go thought the whole array, increment idx and copy num into nums[idx] when it is not a duplicate value (i.e. num != nums[idx])

024.swap-nodes-in-pairs.py 
> ✔ 55/55 cases passed (52 ms)
> - In each iteraition, we update three reference from `curr->p1->p2->p2.next` to `curr->p2->p1->p2.next`

022.generate-parentheses.py
> ✔ 8/8 cases passed (65 ms)
> - Use DFS backtracking
> - At each position, the number of right parenthese <= the number left parenthese

021.merge-two-sorted-lists.py 
> ✔ 208/208 cases passed (49 ms)
> - Compare the value of l1, l2, append the smaller node to the new list, then advance it and the new list.

020.valid-parentheses.py
> ✔ 73/73 cases passed (42 ms)
> - Use stack to store `{[(`
> - Test cases: valid - `{}(){()}`, invalid - `]`, `[`, `{]}`

019.remove-nth-node-from-end-of-list.py 
> ✔ 207/207 cases passed (46 ms)
> - Use two pointer and dummy node, initial: p1 = head, p2 = dummy
>   1. Advance the pointer p1 n steps
>   2. Advance both pointer until p1 reaches None, p2 will point to n-1 th node from the end of list.
>   3. Remove nth node by p2.next = p2.next.next
> - Test cases: remove head, tail and middle node

018.4sum.py
> ✔ 282/282 cases passed (1042 ms)
> - Same as p015

017.letter-combinations-of-a-phone-number.py 
> ✔ 25/25 cases passed (42 ms)
> Generate letter mapping and then use DFS to track all possible string
> - mapping: 2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7:pqrs, 8: tuv, 9: wxyz

016.3sum-closest.py
> ✔ 125/125 cases passed (112 ms)
> - Similar to p015, but this time, check the closest num before updating the two pointers



## 2017.07.01   (Day 02)

015.3sum.py
> ✔ 313/313 cases passed (969 ms)
> - sort the number array, then use one for-loop and two pointer to approach zero, O(n^2)

014.longest-common-prefix.py
> ✔ 117/117 cases passed (39 ms)
> - sort the string array, the longest common prefix will be the common-prefix of the first and the last one
> - other solution: [binary search](http://www.geeksforgeeks.org/longest-common-prefix-set-4-binary-search/)

013.roman-to-integer.py
> ✔ 3999/3999 cases passed (142 ms)
> - minus the value if next numerals is larger, for example: IV = -1 + 4

012.integer-to-roman.py
> ✔ 3999/3999 cases passed (126 ms)
> - Roman numerals I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
> - Specific cases: IV: 4, IX: 9, XL: 40, XC: 90, CD: 400, CM: 900

008.string-to-integer-atoi.py 
> ✔ 1047/1047 cases passed (55 ms)
> - Care about sign mark '+/-'

## 2017.06.30   (Day 01)

011.container-with-most-water.py 
> ✔ 49/49 cases passed (122 ms)
> - Use two pointer, the size of container depends on shorter line

009.palindrome-number.py
> ✔ 11507/11507 cases passed (426 ms)
> - Negative numbers are not palindrome, compare original integer and its reverse

007.reverse-integer.py
> ✔ 1032/1032 cases passed (56 ms)
> - Record the sign of num and then use while-loop to get the reverse of abs(num)

005.longest-palindromic-substring.py 
> ✔ 94/94 cases passed (1422 ms)
> - For each char in the string, check if it is a middle of palindromic (even and odd case)

003.longest-substring-without-repeating-characters.py
> ✔ 983/983 cases passed (85 ms)
> - Use hash table to record the last position of character
> - update left bound to `pos[ch]+1` when hitting the repeating char (ch).

002.add-two-numbers.py
> ✔ 1562/1562 cases passed (119 ms)
> - l1, l2 may contains different length.
> - Don't forget to check carry value after adding

001.two-sum.py
> ✔ 19/19 cases passed (38 ms)
> - Use hash Table to store number position: `pos[target - num]=idx`
