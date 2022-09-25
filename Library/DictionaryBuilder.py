from .DataExtractor import DataExtractor

class DictionaryBuilder:
    # key must be an array []
    def __init__(self,path,key,obj):
        # getting data
        data=DataExtractor()
        data_obj=data.extractRows(path,key,obj)

        # creating dict
        self.info=dict()     
        for d in data_obj:           
            self.info.update({vars(d).pop(key[0]): vars(d)})

