class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        



        # Brute force approach

        # while len(tokens) > 1:
            
        #     for i in len(range(tokens)):
                
        #         if tokens[i] in operators:
                    
        #             # taking the first operand which is 2 places before the operator
        #             left_operand = tokens[i-2]

        #             # taking the second operand which is one place before the operator
        #             right_operand = tokens[i-1]
                    
        #             if tokens[i] == "+":
                        
        #                 result = left_operand+right_operand
                        
        #             elif tokens[i] == "-":
                        
        #                 result = left_operand-right_operand
                        
        #             elif tokens[i] == "*":
                        
        #                 result = left_operand*right_operand
                        
        #             else:
                        
        #                 result = int(left_operand/right_operand)
                    
        #             # making calculations inside the tokens list itself as operator will be 2 places after the operands
        #             tokens[i-2:i+1] = [str(result)]
                    
        #             # exit the for loop to start with again the newly modified tokens list
        #             break
                
        # return int(tokens[0])
                    
                    
        # Optimized approach

        stack = []

        for token in tokens:
            if token == "+":
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                stack.append(left_operand+right_operand)
                
            elif token == "-":
                
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                stack.append(left_operand-right_operand)
                
            elif token == "*":
                
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                stack.append(left_operand*right_operand)
                
            elif token == "/":
                
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                stack.append(int(left_operand/right_operand))
                
            else:
                
                stack.append(int(token))
                
        return stack[-1]