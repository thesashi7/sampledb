from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class ArtworkService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Artwork import Artwork
     artwork = None
     artwork = self.session.query(Artwork).get(id)
     return artwork

   def getByArtist(self, aname):
      from models.Artwork import Artwork 
      artworks = None
      artworks  = self.session.query(Artwork).filter(Artwork.AName == str(aname)).all()
      return artworks

   def all(self):
     from models.Artwork import Artwork
     artworks = None
     artworks = self.session.query(Artwork).all()
     return artworks


   def add(self, artwork):
     from models.Artwork import Artwork
     if isinstance(artwork, Artwork):
        self.session.add(artwork)
        return self.session.commit()

   def update(self, artwork):
      from models.Artwork import Artwork
      current_sessions = self.session.object_session(artwork)
      current_sessions.flush()
      return current_sessions.commit()
