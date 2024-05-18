num_guests = int(input())
reservations = set()

for _ in range(num_guests):
    reservation_code = input()
    reservations.add(reservation_code)

present_guest = input()
while present_guest != "END":
    if present_guest in reservations:
        reservations.remove(present_guest)
    present_guest = input()
print(len(reservations))

for reservation in sorted(reservations):
    print(reservation)


# num_guests = int(input())
# vip_guests = set()
# regular_guests = set()
#
# for _ in range(num_guests):
#     reservation_code = input()
#     if reservation_code[0].isdigit():
#         vip_guests.add(reservation_code)
#     else:
#         regular_guests.add(reservation_code)
#
# present_guest = input()
# while present_guest != "END":
#     if present_guest in vip_guests:
#         vip_guests.remove(present_guest)
#     elif present_guest in regular_guests:
#         regular_guests.remove(present_guest)
#     present_guest = input()
#
# if vip_guests or regular_guests:
#     print(len(vip_guests) + len(regular_guests))
#     print(*sorted(vip_guests), sep="\n")
#     print(*sorted(regular_guests), sep="\n")
