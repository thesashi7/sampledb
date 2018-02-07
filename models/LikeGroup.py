from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.LikeGroupService import LikeGroupService
from Model import Model

class LikeGroup(Model):
   __tablename__ = 'LikeGroup'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return LikeGroupService().all()

   @staticmethod
   def update(LikeGroup):
      LikeGroupService().update(LikeGroup)

   @staticmethod
   def getById(id):
      likeGroup = LikeGroupService().get(id)
      print likeGroup
      return likeGroup

   @staticmethod
   def add(likeGroup):
      service = LikeGroupService()
      service.add(likeGroup)
      return True

   @staticmethod
   def delete(likeGroup):
       return LikeGroupService().delete(likeGroup)
