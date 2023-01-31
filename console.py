import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist("Radiohead")
artist_2 = Artist("Muse")
# artist_repository.save(artist_1)
# artist_repository.save(artist_2)
# artist_repository.delete_all()
# all_artists = artist_repository.select_all()
# result = artist_repository.select(3)
# for artist in all_artists:
#     print(artist.__dict__)

album_1 = Album("The Bends", "Alt-rock", 17)
album_2 = Album("Showbiz", "Alt-rock", 18)
# album_repository.save(album_1)
# album_repository.save(album_2)
# album_repository.delete_all()
result = album_repository.select(2)


pdb.set_trace()
