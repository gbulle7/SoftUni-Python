jury_number = int(input())
text = input()
presentation_number = 0
all_presentations_score = 0

while text != 'Finish':
    presentation_score = 0
    presentation_number += 1
    for _ in range(jury_number):
        grade = float(input())
        presentation_score += grade
        all_presentations_score += grade
    average_presentation_score = presentation_score / jury_number
    print(f'{text} - {average_presentation_score:.2f}.')
    text = input()
total_average_score = all_presentations_score / (presentation_number * jury_number)
print(f"Student's final assessment is {total_average_score:.2f}.")
