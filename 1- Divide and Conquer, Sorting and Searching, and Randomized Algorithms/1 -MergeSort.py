def merge(a1,a2):
  merged = []
  i = j = 0

  while i < len(a1) and j < len(a2):
      if a1[i]<a2[j]:
        merged.append(a1[i])
        i+=1
      else:
        merged.append(a2[j])
        j+=1
  if i < len(a1):
    merged.extend(a1[i:])
  if j < len(a2):
    merged.extend(a2[j:])

  return merged
  

def mergesort(a):
  print (a)
  if len(a)==1:
    return a
  
  n = int(len(a)/2)
  a1 = a[:n]
  a2 = a[n:]

  return merge(mergesort(a1),mergesort(a2))


print(mergesort([6,3,2,10,1,3,7]))