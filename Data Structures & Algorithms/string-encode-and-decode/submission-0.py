class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ""

        for each_elem in strs:
            
            ## encoding with generalized pattern as I am appending length of each elem in the list and hash symbol along with element
            encoded_string+= str(len(each_elem)) + "#" + each_elem

        return encoded_string
            
        # res = "5#Hello5#World"

    def decode(self, s: str) -> List[str]:

        decoded_list, index_value = [], 0

        while index_value < len(s):
            
            position = index_value
            
            # incrementing the position until we reach the # symbol so that after that "#" symbol which we can access the element we want to decode
            while s[position] != "#":
                position+=1
                
            # accessing the length of each element to decode the string the output here is 5 which is the length of hello word

            length = int(s[index_value:position])
            
            # appending the decoded string to the list by accessing the position of each element after "#" char - position + 1 and 
            # position + 1 + length will go upto end of the each real elem

            decoded_list.append(s[position+1:position+1+length])

            # changing the position of the index value to the next elem or to reach end of the string
            index_value = position+1+length
            
        return decoded_list
