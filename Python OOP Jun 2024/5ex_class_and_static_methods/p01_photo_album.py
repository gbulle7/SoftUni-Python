from math import ceil


class PhotoAlbum:
    PHOTOS_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PAGE))

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return f"No more free slots"

    def display(self):
        photos = ["-" * 11]

        for row in self.photos:
            photos.append(("[] " * len(row)).rstrip())
            photos.append("-" * 11)

        return '\n'.join(photos)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
