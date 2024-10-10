#Example 2 :Set Operations

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1 | set2
print("Union set :",union_set)

intersection_set = set1 & set2
print("Intersection set :",intersection_set)

difference_set = set1 - set2
print("Difference Set : ",difference_set)

symmetric_difference_set = set1 ^ set2
print("Symmetric difference Set : ",symmetric_difference_set)