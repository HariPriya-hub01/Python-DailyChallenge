# Input a Python list of student heights and find the average using for loop.

#my code
student_heights = input("Enter the heights with space inbetween: \n").split()
total = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) #till this line already given
  total = total + student_heights[n] 

avg = total / len(student_heights)

print (f"total height = {total}")
print (f"number of students = {len(student_heights)}")
print (f"average height = {round(avg)}")

