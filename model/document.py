class Document:

    def __init__(self, name, content):
        self.__name = name
        self.__content = content

    def get_name(self):
        return self.__name
    
    def get_content(self):
        return self.__content
