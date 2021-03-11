def is_valid(string):
    # 여기에 코드를 작성해주세요.
  p_stack = []

  left_parenthesis  = ["(", "[", "{"]
  right_parenthesis = [')', ']', '}'] 

  for i in string:
    if not p_stack:
      if i in right_parenthesis:
        return False
    
    if i == left_parenthesis[0]:
      p_stack.append(i)
    
    elif i == left_parenthesis[1]:
      p_stack.append(i)
    
    elif i == left_parenthesis[2]:
      p_stack.append(i)

    
    if i == right_parenthesis[0]:
      if p_stack[-1] == left_parenthesis[0]:
        p_stack.pop()
      else:
        return False
      
    elif i == right_parenthesis[1]:
      if p_stack[-1] == left_parenthesis[1]:
        p_stack.pop()
      else:
        return False
    
    elif i == right_parenthesis[2]:
      if p_stack[-1] == left_parenthesis[2]:
        p_stack.pop() 
      else:
        return False
    
  if not p_stack:
    return True
  else:
    return False
    

      
    
    

  
      


