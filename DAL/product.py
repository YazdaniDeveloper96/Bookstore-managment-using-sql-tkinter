class Book:
    def __init__(self,Record_number,Help_number,Title,Author,Publishing_Specifications) -> None:
        self.record_number=Record_number
        self.help_number=Help_number
        self.title=Title
        self.author=Author
        self.publishing_Specifications=Publishing_Specifications
    def __str__(self) -> str:
        return f'record number:{self.__record_number}\nhelp number;{self.__help_number}\ntitle:{self.__title}\nauthor:{self.__author}\nPublishing Specifications:{self.__publishing_Specifications}'