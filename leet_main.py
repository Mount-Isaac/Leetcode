from leet_funcs import Solution

# Testcase string data
longestSubstringData = ["abcabcbb", "bbbbb", "pwwkew", " ", "", "du", "dvdf", "aab"]
convertData = []


if __name__ == "__main__":
    # func that takes user input and tests the algorithm
    def testcases(lists):
        # instantiate an instance of the class
        substring = Solution()

        # iterate strings passed & pass them as params to func

        # Longest substrings
        print('LENGTH OF LONGEST SUBSTRING')
        for element in lists:
            print(substring.lengthOfLongestSubstring(element))

        # Zigzag conversion
        print('\nZIGZAG CONVERSION')
        for element in lists:
            print(substring.convert(element, 9))

    # call the function
    testcases(longestSubstringData)