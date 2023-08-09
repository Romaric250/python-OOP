class GetSet(object):
    instance_count = 0 #public

    _manage_name = 'no privacy' #special var

    def __init__(self, value):
        self._attrval = value
        GetSet.instance_count +=1

    @property
    def var(self):
        print("getting the var attribute")
        return self._attrval
    @var.setter
    def var(self, value):
        self._attrval =value

    @var.deleter
    def var(self):
        self._attrval = None
    
cc = GetSet(5)
cc.var = 50

print(cc._attrval)
