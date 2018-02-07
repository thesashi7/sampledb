from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.ClassifyService import ClassifyService
from Model import Model

class Classify(Model):
   __tablename__ = 'Classify'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return ClassifyService().all()

   @staticmethod
   def update(classify):
      ClassifyService().update(classify)

   @staticmethod
   def getById(id):
      classify = ClassifyService().get(id)
      print classify
      return classify

   @staticmethod
   def add(classify):
      service = ClassifyService()
      service.add(classify)
      return True

   @staticmethod
   def delete(classify):
       return ClassifyService().delete(classify)
