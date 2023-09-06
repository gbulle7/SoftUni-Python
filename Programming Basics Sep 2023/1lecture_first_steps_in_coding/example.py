import pyqrcode

address = 'https://www.youtube.com/'
url = pyqrcode.create(address)
url.png('yt.png', 10)
