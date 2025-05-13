from pydantic import BaseModel, HttpUrl, Field as f
from typing import Optional

class VacancySchema(BaseModel):
    name: str = f(description="Наименование вакансии")
    salary: Optional[int] = f(default=None, description="Зарплата")
    address: Optional[str] = f(default=None, description="Адрес")
    description: str = f(description="Описание")
    url: Optional[HttpUrl] = f(default=None, description="Ссылка на вакансию")