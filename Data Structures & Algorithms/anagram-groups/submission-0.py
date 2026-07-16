class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Sorting approach

        # result = defaultdict(list)

        # for i in strs:
            
        #     sorted_element = "".join(sorted(i))
            
        #     result[sorted_element].append(i)
            
        # print(list(result.values()))

        # Time complexity: O(m∗nlog⁡n)
        # Space complexity: O(m∗n)

        # best and optimized approach is by using hash table of length 26(as all the alphabets are 26 letters)

        result = defaultdict(list)

        for element in strs:

            count = [0] * 26 # Hash Table values[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            for each_letter in element:
                ## here the hash table values for the word eat will be like
                ##[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                count[ord(each_letter) -  ord('a')] +=1
            
            ## this one holds [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]: [ate, tea, eat]
            result[tuple(count)].append(element)
        
        return list(result.values())

