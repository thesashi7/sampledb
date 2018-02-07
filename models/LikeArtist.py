from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.LikeArtistService import LikeArtistService
from Model import Model

class LikeArtist(Model):
   __tablename__ = 'LikeArtist'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return LikeArtistService().all()

   @staticmethod
   def update(likeArtist):
      LikeArtistService().update(likeArtist)

   @staticmethod
   def getById(id):
      likeArtist = LikeArtistService().get(id)
      print likeArtist
      return likeArtist

   @staticmethod
   def add(likeArtist):
      service = LikeArtistService()
      service.add(likeArtist)
      return True

   @staticmethod
   def delete(likeArtist):
       return LikeArtistService().delete(likeArtist)
