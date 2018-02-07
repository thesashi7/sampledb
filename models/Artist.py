from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.ArtistService import ArtistService
from Model import Model

class Artist(Model):
   __tablename__ = 'Artist'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return ArtistService().all()
      
   @staticmethod
   def update(artist):
      ArtistService().update(artist)

   @staticmethod
   def getByName(name):
      artist = ArtistService().get(name)
      print artist
      if (artist != None):
        artist.new = False
      return artist

   @staticmethod
   def add(artist):
      service = ArtistService()
      service.add(artist)
      return True

   @staticmethod
   def delete(artist):
       return ArtistService().delete(artist)
