class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Sorting approach

        # count_of_elements = {}

        # for element in nums:
            
        #     count_of_elements[element] = count_of_elements.get(element,0) + 1
            
        # list_of_element_counts = []

        # for key, value in count_of_elements.items():
        #     list_of_element_counts.append([value,key])

        # list_of_element_counts.sort()

        # final_output = []

        # while len(final_output) < k:
        #     final_output.append(list_of_element_counts.pop()[1])
            
        # return final_output

        # Time complexity: O(nlogn)
        # Space complexity: O(n)

        # Optimal approach by doing the bucket sort


        count_of_elements = {}

        for element in nums:
            
            count_of_elements[element] = count_of_elements.get(element,0) + 1
            
        # this is where optimization is happening by fixing the frequency size with length of input size
        freqency_based_on_input_size = [[] for i in range(len(nums)+1)]

        # appending each element based on the index of frequency list matches with count in the count of elem dict
        for elem,count in count_of_elements.items():

            freqency_based_on_input_size[count].append(elem)
        
        final_output = []

        # looping from the end of the list to get the top k frequent elemets
        for each_elem_list_in_freq in range(len(freqency_based_on_input_size)-1,0,-1):
            for list_of_elem in freqency_based_on_input_size[each_elem_list_in_freq]:
                final_output.append(list_of_elem)
                if len(final_output) == k:
                    return final_output