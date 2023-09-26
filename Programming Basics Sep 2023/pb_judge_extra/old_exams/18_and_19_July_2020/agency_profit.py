airline = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
service_fee = float(input())
child_ticket_price = adult_ticket_price * 0.3
total_service_fee = (adult_tickets + child_tickets) * service_fee
total_price = adult_ticket_price * adult_tickets + child_ticket_price * child_tickets + total_service_fee
revenue = total_price * 0.2

print(f'The profit of your agency from {airline} tickets is {revenue:.2f} lv.')
