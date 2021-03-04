def get_len_of_str(s):
  str_list = []
  new_str  = ""
  for word in s:
    if word not in new_str:
        new_str += word
    else:
        str_list.append(len(new_str))
        new_str = ""
        new_str += word

  str_list.append(len(new_str))



  return max(str_list)