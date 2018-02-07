from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class ArtistService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Artist import Artist
     artist = None
     artist = self.session.query(Artist).get(id)
     return artist

   def all(self):
     from models.Artist import Artist
     artists = None
     artists = self.session.query(Artist).all()
     return artists


   def add(self, artist):
     from models.Artist import Artist
     if isinstance(artist, Artist):
        self.session.add(artist)
        return self.session.commit()

   def update(self, artist):
      from models.Artist import Artist
      current_sessions = self.session.object_session(artist)
      current_sessions.flush()
      return current_sessions.commit()
