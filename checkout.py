from datetime import datetime

class Checkout:
    def __init__(self, user_id, isbn):
        self._user_id = user_id
        self._isbn = isbn
        self._checkout_time = self.get_checkout_time()

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def isbn(self):
        return self._isbn
    
    @user_id.setter
    def user_id(self, id):
        self._user_id = id

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def checkout_time(self):
        return self._checkout_time
    
    @checkout_time.setter
    def checkout_time(self, time):
        try:
            if type(time) != str:
                raise Exception
            else:
                self._checkout_time = time
        except Exception as e:
            print(e)

    def get_checkout_time(self):
        """
            Method to return current time. 
            Used to populate information related to checkout time.
        """
        now = datetime.now()
        current_time = now.strftime("%H:%M %m/%d/%y")
        return current_time
    
    def get_details(self):
        return [self.user_id, self.isbn, self.checkout_time]
    
