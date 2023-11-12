def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        SLIDING WINDOW CONCEPT
        Uses a list to store elements without duplicates 
        Uses a dictionary to store the above list as keys
        Returns the key with the longest length
        '''
        # print(colored(f'----Testcase {s} ----', 'yellow'))

        longest_key = ''
        max_length = 0
        substring = []
        substrings = {}
        i, j = 0, 0      
        

        while i < len(s):
            # print(substrings)
            while j < len(s):
                if s[j] in substring:
                    substrings.update({f'string{i}': substring})
                    # print(substring)
                    substring = []
                    # break
                else:
                    substring.append(s[j])
                    j += 1
            else:
                # print(substring)
                substrings.update({f'string{i}': substring})
                
                # print(substrings)
                # break
            i += 1
            j = i
        # print(substrings)
        
        
        # get the key with the highest lenght
        for key, val in substrings.items():
            if len(val) > max_length:
                max_length = len(val)
                longest_key = val

        # return f'Key:{"".join(longest_key)} Length:{max_length}'
        return max_length