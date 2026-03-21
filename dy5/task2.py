student_scores = [78, 85, 92, 67, 74, 88, 90, 56, 81, 69,
                  95, 72, 60, 83, 77, 91, 68, 84, 79, 87]
max_score = 0
for scores in student_scores:
   if scores > max_score:
       max_score = scores
print(max_score)