class ParserMeta(type):
    """A parser metaclass that will be used for parser class creation"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass,'load_data_source')and
        callable(subclass.load_data_source)and
        hasattr(subclass,'extract_text')and
        callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass


class PDFParser:
    def load_data_source(self, path:str, file_name:str) -> str:
        """Override UpdatedInformalParserInterface.load_data_source()"""
        pass
    
    def extract_text(self, full_file_name: str) -> dict:
        """Override UpdatedInformalParserInterface.extract_text()"""
        pass

class EmailParser:
    def load_data_source(self, path:str, file_name:str) -> str:
        """Override UpdatedInformalParserInterface.load_data_source()"""
        pass
    
    def extract_text_from_email(self, full_file_name: str) -> dict:
        """only belongs to EmailParser class"""
        pass


print("pdf: ",issubclass(PDFParser, UpdatedInformalParserInterface)) # True
print("email: ",issubclass(EmailParser, UpdatedInformalParserInterface)) # False

print(PDFParser.__mro__)
print(EmailParser.__mro__)

"""
# OUTPUT
pdf:  True
email:  False
(<class '__main__.PDFParser'>, <class 'object'>)
(<class '__main__.EmailParser'>, <class 'object'>)

# even though UpdatedInformalParserInterface did not appear in the EmlParserNew MRO. 
# That’s because UpdatedInformalParserInterface is a virtual base class of EmlParserNew.

"""