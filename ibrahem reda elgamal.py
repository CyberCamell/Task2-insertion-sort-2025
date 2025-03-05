def insert_student_score(categories, score):
    key = score 
    i = len(categories) - 1  
    
    while i >= 0 and categories[i] > key:
        i -= 1  
    
    categories.insert(i + 1, key) 

grades_A = []
grades_B = []
grades_C = []
grades_D = []
grades_F = []

scores = [85, 92, 58, 76, 99, 65, 45, 70, 80, 88]

for score in scores:
    if score >= 90:
        insert_student_score(grades_A, score)
    elif score >= 80:
        insert_student_score(grades_B, score)
    elif score >= 70:
        insert_student_score(grades_C, score)
    elif score >= 60:
        insert_student_score(grades_D, score)
    else:
        insert_student_score(grades_F, score)

print("الطلاب في الفئة A:", grades_A)
print("الطلاب في الفئة B:", grades_B)
print("الطلاب في الفئة C:", grades_C)
print("الطلاب في الفئة D:", grades_D)
print("الطلاب في الفئة F:", grades_F)
