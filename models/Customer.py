from sqlalchemy.orm import relationship
from services.DatabaseService import DatabaseService
from services.CustomerService import CustomerService
from Model import Model

class Customer(Model):
   __tablename__ = 'Customer'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   @staticmethod
   def all():
      return CustomerService().all()

   @staticmethod
   def update(customer):
      CustomerService().update(customer)

   @staticmethod
   def getById(id):
      customer = CustomerService().get(id)
      print customer
      return customer

   @staticmethod
   def add(customer):
      service = CustomerService()
      service.add(customer)
      return True

   @staticmethod
   def delete(customer):
       return CustomerService().delete(customer)
