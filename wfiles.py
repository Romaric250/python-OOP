class Date(object):
    @classmethod
    def get_date(self):
        return "20/23/04"

    def __str__(self):
        return "this is an object"
class Inherit():
    @staticmethod
    def get_me(self):
        return "hey there this is romeo"

class Time(Date, Inherit):
    def get_time(self):
        return "20:30:04"
    

class Logger(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger

obj1 = Logger()
obj2 = Logger()
print(obj1, obj2)


dt= Date()
td = Time()
print(dt)
print(dt.get_date())
print(td.get_time(), td.get_date())
print(td.get_me())