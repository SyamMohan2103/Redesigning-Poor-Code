
class User:
    
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, id):
        self._user_id = id

    def get_details(self):
        return [self.name, self.user_id]
