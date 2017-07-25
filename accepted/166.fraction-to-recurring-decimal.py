#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal
#
# Medium (17.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n5'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
#
#
#
# Credits:Special thanks to @Shangrila for adding this problem and creating all
# test cases.
#


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        isNeg = (numerator ^ denominator) < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        q, r = (numerator // denominator), numerator % denominator

        # Case 1, no fractional part
        if r == 0:
            return ('', '-')[isNeg] + str(q)

        ans = [str(q) + '.']
        idx = len(ans)
        table = {r: idx}

        while True:

            r *= 10
            q = r // denominator
            r = r % denominator
            ans.append(str(q))

            # Case 2, the fractional part is repeating
            if r in table:
                ans.insert(table[r], '(')
                ans.append(')')
                break

            # Case 3, the fractional part is non-repeated
            if r == 0:
                break

            idx += 1
            table[r] = idx

        return ('', '-')[isNeg] + "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.fractionToDecimal(1, 2))
    print(sol.fractionToDecimal(2, 1))
    print(sol.fractionToDecimal(2, 3))
    print(sol.fractionToDecimal(1, 6))
    print(sol.fractionToDecimal(0, -5))
    print(sol.fractionToDecimal(1, -5))

