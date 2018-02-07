from DatabaseService import DatabaseService
from sqlalchemy.orm.attributes import flag_modified

class LikeGroupService(DatabaseService):

   def get(self, id, serialize = False):
     from models.LikeGroup import LikeGroup
     likeGroup = None
     likeGroup = self.session.query(LikeGroup).get(id)
     return likeGroup

   def all(self):
     from models.LikeGroup import LikeGroup
     likeGroups = None
     likeGroups = self.session.query(LikeGroup).all()
     return likeGroups


   def add(self, likeGroup):
     from models.LikeGroup import LikeGroup
     if isinstance(likeGroup, LikeGroup):
        self.session.add(likeGroup)
        return self.session.commit()

   def update(self, likeGroup):
      from models.LikeGroup import LikeGroup
      current_sessions = self.session.object_session(likeGroup)
      current_sessions.flush()
      return current_sessions.commit()
