# input the first exam score 
first_exam= float(input("enter first exam score:"))/100
second_exam= float(input("enter second exam score:"))/100
#display total
total_score= (first_exam * 0.60) + (second_exam * 0.40)
print(f"display total score {total_score:.2f}")
