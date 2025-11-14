from pdb import find_function
def find_duplicates(lst):
   seen = set()
   duplicates = []
   for item in lst:
       if item in seen:
           duplicates.append(item)
       else:
           seen.add(item)
   return duplicates

# Example usage
l1 = [1, 2, 3, 1, 2, 4, 5, 6, 5]
l2 = [10,501,22,37,10,501]
l3 = [10,501,2,5,99,30,55,23,55,23]
print("Duplicates from list 1 :", find_duplicates(l1))
print("Duplicates from list 2 :", find_duplicates(l2))
print("Duplicates from list 3 :", find_duplicates(l3))

