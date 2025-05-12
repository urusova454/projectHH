from typing import Optional, Dict, Any
from pydantic import BaseModel, HttpUrl, Field as f
from uuid import UUID, uuid4


class Vacancy(BaseModel):
    id: UUID = f(default_factory=uuid4, description="Идентификатор вакансии")
    name: str = f( description="Наименование вакансии")
    salary: Optional[Dict[str, Any]] = f(default=None, description="Зарплата")
    address: Optional[str] = f(default=None, description="Адрес")
    description: str = f(description="Описание")
    url: Optional[str] = f(default=None, description="Ссылка на вакансию")
