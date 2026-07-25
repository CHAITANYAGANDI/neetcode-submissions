class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        output = []

        for i in range(len(position)):
            
            time = (target - position[i])/speed[i]
            
            output.append((position[i],time))
            
        output.sort(reverse=True)

        count = 1

        stack =[output[0][1]]

        for j in range(len(output)):
            
            if output[j][1] > stack[-1]:
                
                stack.append(output[j][1])
        
            
        return len(stack)
        