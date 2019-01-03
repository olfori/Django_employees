from django_seed import Seed
from faker import Faker
import random

from tree.models import Employees


def first_rec():
    e = Employees(
        name='Потапов Виктор Геннадиевич',
        position='Генеральный директор',
        emp_date='2010-02-16',
        salary='40000'
    )
    e.save()


def fill_emp(count, pos, year, salary, parent_min, parent_max):
    seeder = Seed.seeder()
    fake = Faker('ru_RU')
    with Employees.objects.disable_mptt_updates():
        seeder.add_entity(Employees, count, {
            'name': lambda x: fake.name(),
            'position': pos,
            'emp_date': '{}-{}-{}'.format(year, random.randint(1, 12), random.randint(1, 28)),
            'salary': lambda x: random.randint(salary-4000, salary+4000),
            'parent': lambda x: Employees.objects.get(id=random.randint(parent_min, parent_max)),
        })
        seeder.execute()


def del_obj():
    with Employees.objects.disable_mptt_updates():
        objs = Employees.objects.all()
        objs.delete()
    Employees.objects.rebuild()


def run():
    first_rec()
    fill_emp(10, 'Региональный директор', 2011, 34000, 1, 1)
    fill_emp(100, 'Топ менеджер', 2012, 24000, 2, 11)
    fill_emp(1000, 'Менеджер', 2012, 16000, 12, 111)
    fill_emp(40000, 'Младший менеджер', 2013, 12000, 112, 1111)   # about 5 minutes
    fill_emp(10000, 'Стажер', 2014, 10000, 1112, 41111)     # 3.5 minutes
    Employees.objects.rebuild()
    pass
