import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist("Radiohead")
artist_2 = Artist("Muse2", 22)
# artist_repository.save(artist_1)
# artist_repository.save(artist_2)
# artist_repository.delete_all()
# all_artists = artist_repository.select_all()
# result = artist_repository.select(3)
# for artist in all_artists:
#     print(artist.__dict__)
# artist_repository.delete(17)
# artist_repository.update(artist_2)
results = artist_repository.albums(artist_2)
for result in results:
    print(result.__dict__)

album_1 = Album("The Bends", "Alt-rock", 21)
album_2 = Album("Showbiz", "Alt-rock", 22)
album_3 = Album("Drone", "Alt-rock", 22, 4)
# album_repository.save(album_1)
# album_repository.save(album_2)
# album_repository.save(album_3)
# album_repository.delete_all()
# result = album_repository.select(2)
# album_repository.delete(2)
# album_repository.update(album_3)


pdb.set_trace()
