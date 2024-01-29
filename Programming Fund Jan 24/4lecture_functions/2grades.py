def convert_grades_word(grade):
    grade_word = ''  # if return 'Fail'...etc. are used, del. this line
    if 2 <= grade_value < 3:
        grade_word = 'Fail'
        # return 'Fail
    elif 3 <= grade_value < 3.5:
        grade_word = 'Poor'
        # return 'Poor'
    elif 3.5 <= grade_value < 4.5:
        grade_word = 'Good'
        # return 'Good'
    elif 4.5 <= grade_value < 5.5:
        grade_word = 'Very Good'
        # return 'Very Good'
    elif 5.5 <= grade_value <= 6:
        grade_word = 'Excellent'
        # return 'Excellent'
    return grade_word  # if return 'Fail'...etc. are used, del. this line


grade_value = float(input())
print(convert_grades_word(grade_value))
