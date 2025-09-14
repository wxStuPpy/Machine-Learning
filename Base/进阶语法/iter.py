class MyIterator:
    def __init__(self,max_value):
        self.max_value=max_value
        self.cur_value=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_value>=self.max_value:
            raise StopIteration
        value=self.cur_value
        self.cur_value+=1
        return value
    
if __name__ == '__main__':
    iterator = MyIterator(5)
    print(next(iterator))
    