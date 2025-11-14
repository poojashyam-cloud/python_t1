def find_nonrepeat(lst):
   seen = set()
   nr = []
   for item in lst:
       if item in seen:
           nr.append(item)
       else:
           seen.add(item)
   return nr

# Example usage
l1 = [1, 2, 3, 4, 1,5, 6, 5,10,11,3,20,20]
print("Non repeating element from the given lst :", find_nonrepeat(l1))
