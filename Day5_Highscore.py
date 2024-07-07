# Input a list of student scores, find the highest score using for loop

student_scores = input("Enter the scores with a space inbetween:\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max = 0
for num in student_scores:
  if max >= num:
    max = max
  elif max < num:
    max = num

print (f"The highest score in the class is: {max}")
