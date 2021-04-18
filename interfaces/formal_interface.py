import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return(hasattr(subclass, 'load_data_source')and
        callable(subclass.load_data_source)and
        hasattr(subclass,'extract_text')and
        callable(subclass.extract_text))

class PDFParserNew:
    def load_data_source(self, path:str, file_name:str) -> str:
        pass
    def extract_text(self, full_file_name:str) -> dict:
        pass

class EmailParserNew:
    def load_data_source(self, path:str, file_name:str) -> str:
        pass
    
    def extract_text_from_email(self, full_file_name: str) -> dict:
        pass

print("pdf: ",issubclass(PDFParserNew, FormalParserInterface)) # True
print("email: ",issubclass(EmailParserNew, FormalParserInterface)) # False

print(PDFParserNew.__mro__) # (<class '__main__.PDFParserNew'>, <class 'object'>)
print(EmailParserNew.__mro__) # (<class '__main__.EmailParserNew'>, <class 'object'>)