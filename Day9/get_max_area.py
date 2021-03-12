def get_max_area(height):
  biggest_area = 0


  for i in range(len(height)-1):
    for j in range(1, len(height)):
      if height[j] <= height[i]:
        area = (j-i)*height[j]
        if area > biggest_area:
          biggest_area = area
      else:
        area = (j-i)*height[i]
        if area > biggest_area:
          biggest_area = area

  return biggest_area
      