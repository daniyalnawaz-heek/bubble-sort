def bubblesort(list):
  for i in range(0,len(list)-1):
    for j in range(0,len(list)-1-i):
      if list[j]>list[j+1]:
        temp=list[j]
        list[j]=list[j+1]
        list[j+1]=temp 
  return list       
 
my_list=[38,73,69,27,53,79,38,58,22,75]
print(bubblesort (my_list))
