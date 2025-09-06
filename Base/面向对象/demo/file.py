from data import  Record

class FileReader:
    def read_data(self)->list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path=path
    #重写read_data
    def read_data(self) ->list[Record]:
        record_list:list[Record]=[]
        f=open(self.path,'r',encoding='UTF-8')
        for line in f.readlines():
            line=line.strip()
            data_list=line.split(',')
            record=Record(data_list[0],int(data_list[1]),int(data_list[2]))
            record_list.append(record)
        f.close()
        return record_list


if __name__=='__main__':
    reader=TextFileReader('./text.txt')
    print(reader.read_data()[:2])
