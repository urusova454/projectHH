from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, HttpUrl, Field


class Area(BaseModel):
    id: str
    name: str
    url: HttpUrl

class Address(BaseModel):
    city: Optional[str] = None
    street: Optional[str] = None
    building: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    description: Optional[str] = None
    raw: Optional[str] = None

class Experience(BaseModel):
    id: str
    name: str

class Schedule(BaseModel):
    id: str
    name: str


class Employment(BaseModel):
    id: str
    name: str


class LogoUrls(BaseModel):
    original: HttpUrl
    size_90: HttpUrl = Field(..., alias="90")
    size_240: HttpUrl = Field(..., alias="240")


class Employer(BaseModel):
    id: str
    name: str
    url: HttpUrl
    alternate_url: HttpUrl
    logo_urls: Optional[Any] = None
    vacancies_url: HttpUrl
    accredited_it_employer: bool
    trusted: bool


class KeySkill(BaseModel):
    name: str


class ProfessionalRole(BaseModel):
    id: str
    name: str


class EmploymentForm(BaseModel):
    id: str
    name: str


class WorkFormat(BaseModel):
    id: str
    name: str

class WorkScheduleByDays(BaseModel):
    id: str
    name: str

class WorkingHours(BaseModel):
    id: str
    name: str

class Snippet(BaseModel):
    requirement: str
    responsibility: Optional[str] = None


class Type(BaseModel):
    id: str
    name: str

class Vacancy(BaseModel):
    id: str
    premium: bool
    billing_type: Optional[Any] = None
    relations: List[Any]
    name: str
    insider_interview: Optional[Any]
    response_letter_required: bool
    area: Area
    salary: Optional[Any]
    salary_range: Optional[Any]
    type: Optional[Any] = None
    address: Optional[Address] = None
    allow_messages: bool
    experience: Experience
    schedule: Schedule
    employment: Employment
    department: Optional[Any] = None
    show_contacts: bool
    contacts: Optional[Any]
    description: str
    branded_description: Optional[str]
    vacancy_constructor_template: Optional[Any]
    key_skills: List[KeySkill]
    accept_handicapped: bool
    accept_kids: bool
    archived: bool
    response_url: Optional[HttpUrl]
    specializations: List[Any]
    professional_roles: List[ProfessionalRole]
    code: Optional[str]
    hidden: bool
    quick_responses_allowed: bool
    driver_license_types: List[Any]
    accept_incomplete_resumes: bool
    employer: Employer
    published_at: datetime
    created_at: datetime
    initial_created_at: datetime
    negotiations_url: Optional[HttpUrl]
    suitable_resumes_url: Optional[HttpUrl]
    apply_alternate_url: HttpUrl
    has_test: bool
    test: Optional[Any]
    alternate_url: HttpUrl
    working_days: List[Any]
    working_time_intervals: List[Any]
    working_time_modes: List[Any]
    accept_temporary: bool
    languages: List[Any]
    approved: bool
    employment_form: EmploymentForm
    fly_in_fly_out_duration: List[Any]
    internship: bool
    night_shifts: bool
    work_format: List[WorkFormat]
    work_schedule_by_days: List[WorkScheduleByDays]
    working_hours: List[WorkingHours]
    show_logo_in_search: Optional[Any] = None

class GeneralVacancy(BaseModel):
    id: str
    premium: bool
    name: str
    department: Optional[Any] = None
    has_test: bool
    response_letter_required: bool
    area: Area
    salary: Optional[Any] = None
    salary_range: Optional[Any] = None
    type: Type
    address: Optional[Any] = None
    response_url: Optional[Any] = None
    sort_point_distance: Optional[Any] = None
    published_at: datetime
    created_at: datetime
    archived: bool
    apply_alternate_url: HttpUrl
    show_logo_in_search: Optional[Any] = None
    insider_interview: Optional[Any] = None
    url: HttpUrl
    alternate_url: HttpUrl
    relations: List[Any]
    employer: Employer
    snippet: Snippet
    show_contacts: bool
    contacts: Optional[Any] = None
    schedule: Type
    working_days: List[Any]
    working_time_intervals: List[Any]
    working_time_modes: List[Any]
    accept_temporary: bool
    fly_in_fly_out_duration: List[Any]
    work_format: List[Any]
    working_hours: List[WorkingHours]
    work_schedule_by_days: List[WorkScheduleByDays]
    night_shifts: bool
    professional_roles: List[ProfessionalRole]
    accept_incomplete_resumes: bool
    experience: Experience
    employment: Employment
    employment_form: EmploymentForm
    internship: bool
    adv_response_url: Optional[Any] = None
    is_adv_vacancy: bool
    adv_context: Optional[Any] = None