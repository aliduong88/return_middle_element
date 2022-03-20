def middle_element(lst):
  if len(lst) % 2 != 0:
    return lst[int(len(lst)/2)]
  else:
    first_middle = lst[int(len(lst)/2) - 1]
    second_middle = lst[int(len(lst)/2)]
    average = (first_middle + second_middle) / 2
    return average
    

print(middle_element([5, 2, -10, -4, 4, 5,]))