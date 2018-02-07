from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.ArtworkService import ArtworkService
from Model import Model

class Artwork(Model):
   __tablename__ = 'Artwork'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return ArtworkService().all()

   @staticmethod
   def update(artwork):
      ArtworkService().update(artwork)

   @staticmethod
   def getByName(name):
      artw = ArtworkService().get(name)
      print artw
      if (artw != None):
        artw.new = False
      return artw

   @staticmethod
   def getByArtist(aname):
      artw = ArtworkService().getByArtist(aname)
      print artw
      return artw

   @staticmethod
   def add(artwork):
      service = ArtworkService()
      service.add(artwork)
      return True

   @staticmethod
   def delete(artwork):
       return ArtworkService().delete(artwork)
