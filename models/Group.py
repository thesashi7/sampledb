from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.GroupService import GroupService
from Model import Model

class Group(Model):
   __tablename__ = 'Group'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return GroupService().all()

   @staticmethod
   def update(group):
      GroupService().update(group)

   @staticmethod
   def getById(id):
      group = GroupService().get(id)
      print group
      return group

   @staticmethod
   def add(group):
      service = GroupService()
      service.add(group)
      return True

   @staticmethod
   def delete(group):
       return GroupService().delete(group)
