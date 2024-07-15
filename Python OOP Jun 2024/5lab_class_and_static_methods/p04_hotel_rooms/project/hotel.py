from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if room_number == r.number:
                r.take_room(people)
                self.guests += people

    def free_room(self, room_number):
        for r in self.rooms:
            if room_number == r.number:
                room_guests = r.guests
                r.free_room()
                self.guests -= room_guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\nTaken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
