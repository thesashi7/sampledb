from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class ClassifyService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Classify import Classify
     classify = None
     classify = self.session.query(Classify).get(id)
     return classify

   def all(self):
     from models.Classify import Classify
     classifys = None
     classifys = self.session.query(Classify).all()
     return classifys


   def add(self, classify):
     from models.Classify import Classify
     if isinstance(classify, Classify):
        self.session.add(classify)
        return self.session.commit()

   def update(self, classify):
      from models.Classify import Classify
      current_sessions = self.session.object_session(classify)
      current_sessions.flush()
      return current_sessions.commit()

      
