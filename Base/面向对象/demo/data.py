class Record:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def __str__(self):
        return  f"Record(name='{self.name}', age={self.age}, id={self.id})"

    def __repr__(self):
        return self.__str__()