#anonymous function

points=[(1,2),(3,1),(5,0),(2,4)]
# sort by second element in tuple using lambda
sorted_points=sorted(points,key=lambda x:x[1])
print(sorted_points)