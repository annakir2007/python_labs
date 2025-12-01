from dataclasses import *
from datetime import *

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        self._check_fio()
        self._check_birthdate()
        self._check_group()
        self._check_gpa()

    def _check_fio(self):
        """Проверка правильности ФИО"""

        if not isinstance(self.fio, str):
            raise TypeError("ФИО должно быть строкой")
        
        if len(self.fio.strip()) == 0:
            raise ValueError("ФИО не может быть пустым")
        
        for char in self.fio:
            if not(char.isalpha() or char.isspace() or char == "-"):
                raise TypeError("ФИО может содержать только буквы, пробелы и дефис")
            
        fio_words = self.fio.split()
        if len(fio_words) < 2:
            raise TypeError("ФИО должно содержать минимум 2 слова(имя и фамилия)")
        
        for word in fio_words:
            if not word[0].isupper():
                raise TypeError("Каждое слово в ФИО должно начинаться с заглавной буквы")

    def _check_birthdate(self):
        """Проверка даты рождения"""

        if not isinstance(self.birthdate, str):
            raise ValueError("Дата рождения должна быть строкой")
        
        if len(self.birthdate) != 10:
            raise ValueError("Дата рождения должна быть формата yyyy-mm-dd")
        
        if self.birthdate[4] != "-" or self.birthdate[7] != "-":
            raise ValueError("Дата рождения должна быть формата yyyy-mm-dd")
        
        year = self.birthdate[0:4]
        month = self.birthdate[5:7]
        day = self.birthdate[8:10]
        if not(year.isdigit() and month.isdigit() and day.isdigit()):
            raise TypeError("Дата рождения может содержать только цифры")
                
        try:
            birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Некорректная дата рождения")
        
        today = date.today()
        if birth_date > today:
            raise ValueError("Дата рождения не может быть в будущем")

    def _check_gpa(self):
        """Проверка GPA"""

        if not isinstance(self.gpa, float):
            raise ValueError("Оценка должна быть дробным числом")  
          
        if not (0 <= self.gpa <= 5):
            raise ValueError("Оценка должна быть от 0 до 5")

    def _check_group(self):
        """Проверка номера группы"""

        if not isinstance(self.group, str):
            raise TypeError("Группа должна быть строкой")
        
        if not self.group.strip():
            raise ValueError("Группа не может быть пустой")
        
        if len(self.group) < 5:
            raise ValueError("Группа слишком короткая")

    def age(self) -> int:
        """Вычисление возраста студента"""

        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age_years = today.year - birth_date.year
        
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age_years -= 1       
        return age_years

    def to_dict(self) -> dict:
        """Преобразование объекта в словарь"""

        if not self.fio or not self.fio.strip():
            raise ValueError("Поле 'fio' не может быть пустым")
        
        if not self.birthdate or not self.birthdate.strip():
            raise ValueError("Поле 'birthdate' не может быть пустым")
        
        if not self.group or not self.group.strip():
            raise ValueError("Поле 'group' не может быть пустым")
        
        if self.gpa is None:
            raise ValueError("Поле 'gpa' не может быть None")
        
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создание объекта из словаря"""

        return cls(
            fio=data['fio'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=data['gpa']
        )

    def __str__(self):
        """Строковое представление объекта"""

        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}"