movie_name = input()
student_ticket = 0
standard_ticket = 0
kid_ticket = 0

while movie_name != 'Finish':
    free_seats = int(input())
    tickets_movie = 0
    while free_seats > tickets_movie:  # for _ in range(free_seats)
        seat_type = input()
        if seat_type == 'End':
            break
        elif seat_type == 'student':
            student_ticket += 1
        elif seat_type == 'standard':
            standard_ticket += 1
        elif seat_type == 'kid':
            kid_ticket += 1
        tickets_movie += 1
    capacity = tickets_movie / free_seats * 100
    print(f'{movie_name} - {capacity:.2f}% full.')
    movie_name = input()
total_tickets = student_ticket + standard_ticket + kid_ticket
percent_students_tickets = student_ticket / total_tickets * 100
percent_standard_tickets = standard_ticket / total_tickets * 100
percent_kid_tickets = kid_ticket / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f'{percent_students_tickets:.2f}% student tickets.')
print(f'{percent_standard_tickets:.2f}% standard tickets.')
print(f'{percent_kid_tickets:.2f}% kids tickets.')
