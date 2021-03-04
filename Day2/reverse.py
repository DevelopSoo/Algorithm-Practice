def reverse(number):

  str_nums = str(number)

  if number < 0:
    reverse_str = str_nums[-1:0:-1]

    result = int('-' + reverse_str)
  
  elif number == 0:
    return 0
  
  else:
    if str_nums[-1] == '0':
      reverse_str = str_nums[-2::-1]

      result = int(reverse_str)
    else:
      reverse_str = str_nums[::-1]

      result = int(reverse_str)

  return result