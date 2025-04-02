from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class Area(BaseModel):
    id: str
    name: str
    url: str


class Salary(BaseModel):
    from_: Optional[int] = Field(None, alias="from")
    to: Optional[int]
    currency: str
    gross: bool


class Mode(BaseModel):
    id: str
    name: str


class Frequency(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class SalaryRange(Salary):
    mode: Mode
    frequency: Optional[Frequency] = None


class VacancyType(BaseModel):
    id: str
    name: str


class MetroStation(BaseModel):
    pass  # Дополните при необходимости


class Address(BaseModel):
    city: Optional[str] = None
    street: Optional[str] = None
    building: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    description: Optional[str] = None
    raw: Optional[str] = None
    id: Optional[str] = None


class Employer(BaseModel):
    id: Optional[str] = None
    name: str
    url: Optional[str] = None
    alternate_url: Optional[str] = None
    logo_urls: Optional[Dict[str, str]] = None
    accredited_it_employer: bool
    trusted: bool


class Snippet(BaseModel):
    requirement: Optional[str] = None
    responsibility: Optional[str] = None


class Contacts(BaseModel):
    pass  # Дополните при необходимости


class Schedule(BaseModel):
    id: str
    name: str


class WorkFormat(BaseModel):
    id: str
    name: str


class WorkingHours(BaseModel):
    id: str
    name: str


class WorkScheduleByDays(BaseModel):
    id: str
    name: str


class ProfessionalRole(BaseModel):
    id: str
    name: str


class Experience(BaseModel):
    id: str
    name: str


class Employment(BaseModel):
    id: str
    name: str


class EmploymentForm(BaseModel):
    id: str
    name: str

class BillingType(BaseModel):
    id: str
    name: str


class GeneralVacancy(BaseModel):
    id: str
    premium: bool
    name: str
    department: Optional[str] = None
    has_test: bool
    response_letter_required: bool
    area: Area
    salary: Optional[Salary] = None
    salary_range: Optional[SalaryRange] = None
    type: VacancyType
    address: Optional[Address] = None
    response_url: Optional[str] = None
    sort_point_distance: Optional[float] = None
    published_at: datetime
    created_at: datetime
    archived: bool
    apply_alternate_url: str
    show_logo_in_search: Optional[bool] = None
    insider_interview: Optional[Dict[str, Any]] = None
    url: str
    alternate_url: str
    relations: List[Dict[str, Any]] = []
    employer: Employer
    snippet: Optional[Snippet] = None
    show_contacts: bool
    contacts: Optional[Contacts] = None
    schedule: Schedule
    working_days: List[Dict[str, Any]] = []
    working_time_intervals: List[Dict[str, Any]] = []
    working_time_modes: List[Dict[str, Any]] = []
    accept_temporary: bool
    fly_in_fly_out_duration: List[Dict[str, Any]] = []
    work_format: List[WorkFormat]
    working_hours: List[WorkingHours]
    work_schedule_by_days: List[WorkScheduleByDays]
    night_shifts: bool
    professional_roles: List[ProfessionalRole]
    accept_incomplete_resumes: bool
    experience: Experience
    employment: Employment
    employment_form: EmploymentForm
    internship: bool
    adv_response_url: Optional[str] = None
    is_adv_vacancy: bool
    adv_context: Optional[Dict[str, Any]] = None

class Vacancy(BaseModel):
    id: str
    premium: bool
    billing_type: BillingType
    relations: List[Dict[str, Any]] = []
    name: str
    insider_interview: Optional[Dict[str, Any]] = Field(None, alias="insider_interview")
    response_letter_required: bool
    area: Area
    salary: Optional[Salary] = None
    salary_range: Optional[SalaryRange] = None
    type: VacancyType
    address: Optional[Address] = None
    allow_messages: bool
    experience: Experience
    schedule: Schedule
    employment: Employment
    department: Optional[str] = None
    show_contacts: bool
    contacts: Optional[Dict[str, Any]] = None
    description: str
    branded_description: Optional[str] = None
    vacancy_constructor_template: Optional[Dict[str, Any]] = None
    key_skills: List[Dict[str, Any]] = []
    accept_handicapped: bool
    accept_kids: bool
    archived: bool
    response_url: Optional[str] = None
    specializations: List[Dict[str, Any]] = []
    professional_roles: List[ProfessionalRole]
    code: Optional[str] = None
    hidden: bool
    quick_responses_allowed: bool
    driver_license_types: List[Dict[str, Any]] = []
    accept_incomplete_resumes: bool
    employer: Employer
    published_at: datetime
    created_at: datetime
    initial_created_at: datetime
    negotiations_url: Optional[str] = None
    suitable_resumes_url: Optional[str] = None
    apply_alternate_url: str
    has_test: bool
    test: Optional[Dict[str, Any]] = None
    alternate_url: str
    working_days: List[Dict[str, Any]] = []
    working_time_intervals: List[Dict[str, Any]] = Field([], alias="working_time_intervals")
    working_time_modes: List[Dict[str, Any]] = []
    accept_temporary: bool
    languages: List[Dict[str, Any]] = []
    approved: bool
    employment_form: EmploymentForm
    fly_in_fly_out_duration: List[Dict[str, Any]] = []
    internship: bool
    night_shifts: bool
    work_format: List[WorkFormat]
    work_schedule_by_days: List[WorkScheduleByDays]
    working_hours: List[WorkingHours]
    show_logo_in_search: Optional[bool] = None