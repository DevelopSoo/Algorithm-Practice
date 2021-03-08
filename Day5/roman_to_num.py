def roman_to_num(s):
  # 여기에 코드를 작성해주세요.
  roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  result_list = []

  i = 0
  while i < len(s):
    if roman_dict[s[i]] >= roman_dict[s[i+1]]:
        result_list.append(roman_dict[s[i]])
        if i+2 == len(s):
          result_list.append(roman_dict[s[i+1]])
          return sum(result_list)        
        i += 1


    else:
        subtracted_num = roman_dict[s[i+1]] - roman_dict[s[i]]
        result_list.append(subtracted_num)
        
        i += 2
  
  return sum(result_list)

  




