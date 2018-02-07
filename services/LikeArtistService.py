from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class LikeArtistService(DatabaseService):

   def get(self, id, serialize = False):
     from models.LikeArtist import LikeArtist
     likeArtist = None
     likeArtist = self.session.query(LikeArtist).get(id)
     return likeArtist

   def all(self):
     from models.LikeArtist import LikeArtist
     likeArtists = None
     likeArtists = self.session.query(LikeArtist).all()
     return likeArtists


   def add(self, likeArtist):
     from models.LikeArtist import LikeArtist
     if isinstance(likeArtist, LikeArtist):
        self.session.add(likeArtist)
        return self.session.commit()

   def update(self, likeArtist):
      from models.LikeArtist import LikeArtist
      current_sessions = self.session.object_session(likeArtist)
      current_sessions.flush()
      return current_sessions.commit()
