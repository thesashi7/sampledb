from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class CustomerService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Customer import Customer
     customer = None
     customer = self.session.query(Customer).get(id)
     return Customer

   def all(self):
     from models.Customer import Customer
     customers = None
     customers = self.session.query(Customer).all()
     return customers


   def add(self, customer):
     from models.Customer import Customer
     if isinstance(customer, Customer):
        self.session.add(customer)
        return self.session.commit()

   def update(self, customer):
      from models.Customer import Customer
      current_sessions = self.session.object_session(customer)
      current_sessions.flush()
      return current_sessions.commit()
