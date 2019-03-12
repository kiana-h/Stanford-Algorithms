def inversion_count(a):

  #basecase: if the list has only one element there are 0 inversions  
  if len(a)==1:
    return 0,a
  
  else:
      #split the list in two
      n = int(len(a)/2)
      a1_count,a1 = inversion_count(a[:n])
      a2_count,a2 = inversion_count(a[n:])
      
      #piggyback on mergesort
      merged = []
      i = j = 0
      count = 0 + a1_count + a2_count
      

      while i < len(a1) and j < len(a2):
          if a1[i]<a2[j]:
              merged.append(a1[i])
              i+=1
          else:
              merged.append(a2[j])
              j+=1
              
              #if there is a number in a2 that is smaller than a number in a1,
              #and given that a1 is sorted,
              #that means that element in a2 is smaller than all the remaining elements in a1 
              count += (len(a1) - i)

         
      merged += a1[i:]
      merged += a2[j:]
  
  return count,merged



  
with open('IntegerArray.txt') as f:
    number_list = [int(x) for x in f]

print(len(number_list)," numbers loaded!")
print(inversion_count(number_list)[0], "inversions!")

