
class InformalParserInterface:
    
    def load_data_source(self, path:str, file_name: str) -> str:
        """Load in the file for extracting text"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file """
        pass


class PDFParser(InformalParserInterface):
    def load_data_source(self, path:str, file_name:str) -> str:
        """Override InformalParserInterface.load_data_source()"""
        pass
    
    def extract_text(self, full_file_name: str) -> dict:
        """Override InformalParserInterface.extract_text()"""
        pass

class EmailParser(InformalParserInterface):
    def load_data_source(self, path:str, file_name:str) -> str:
        """Override InformalParserInterface.load_data_source()"""
        pass
    
    def extract_text_from_email(self, full_file_name: str) -> dict:
        """only belongs to EmailParser class"""
        pass



print("pdf: ",issubclass(PDFParser, InformalParserInterface)) # True
print("email: ",issubclass(EmailParser, InformalParserInterface)) # True

print(PDFParser.__mro__)
print(EmailParser.__mro__)
"""
# OUTPUT
pdf:  True
email:  True
(<class '__main__.PDFParser'>, <class '__main__.InformalParserInterface'>, <class 'object'>)
(<class '__main__.EmailParser'>, <class '__main__.InformalParserInterface'>, <class 'object'>)
"""