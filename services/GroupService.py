from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class GroupService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Group import Group
     group = None
     group = self.session.query(Group).get(id)
     return group

   def all(self):
     from models.Group import Group
     groups = None
     groups = self.session.query(Group).all()
     return groups


   def add(self, group):
     from models.Group import Group
     if isinstance(group, Group):
        self.session.add(group)
        return self.session.commit()

   def update(self, group):
      from models.Group import Group
      current_sessions = self.session.object_session(group)
      current_sessions.flush()
      return current_sessions.commit()
