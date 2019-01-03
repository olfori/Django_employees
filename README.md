# Django_test_task
Test task

  При выполнении задания использовал:
- Django 2.1
- MySQL 5.6
- Python 3.7

# Выполнил часть 1:

  Создал веб страницу, которая выводит иерархию сотрудников в древовидной форме:
Информация о каждом сотруднике хранится в базе данных и содержит следующие данные:
- ФИО;
- Должность;
- Дата приема на работу;
- Размер заработной платы;

У каждого сотрудника есть 1 начальник.

База данных содержит 51 100 сотрудников и 5 уровней иерархий.

Отображена должность каждого сотрудника.


# Выполнил часть 2:

1. Создал базу данных, используя миграции Django
2. Использовал DB seeder для Django ORM, для заполнения базы данных
3. Использовал Twitter Bootstrap v4.1 для создания базовых стилей страницы
4. Создал еще одну страницу и вывел на ней список сотрудников со всей 
имеющейся о сотруднике информацией из базы данных. Добавил возможность
сортировать по любому полю.
5. Добавил возможность поиска сотрудников по любому полю для страницы
созданной в задаче 4.
6. Добавил возможность сортировать и искать по любому полю без перезагрузки
страницы, используя ajax.
7. Осуществил аутентификацию пользователя для раздела, 
доступного только для зарегистрированных пользователей.
8. Перенес функционал разработанный в задачах 4, 5 и 6 (используя ajax
запросы) в раздел доступный только для зарегистрированных пользователей.
9. В разделе доступном только для зарегистрированных пользователей,
реализовал остальные CRUD операции для записей сотрудников. 
Все поля касающиеся пользователей редактируемы, включая начальников.
10. Осуществил возможность загружать фотографию сотрудника и отобразил ее
на странице, где можно редактировать данные о сотруднике. 
Добавил дополнительную колонку с уменьшенной фотографией сотрудника на
странице списка всех сотрудников.
11. Осуществил возможность перераспределения сотрудников в случае
изменения начальника.
12. Реализовал ленивую загрузку для дерева сотрудников: показываю
первые два уровня иерархии по умолчанию и подгружаю следующие
уровни, при клике на сотрудника второго уровня.
13. Реализовал возможность менять начальника сотрудника используя drag-n-drop
сразу в дереве сотрудников.

14. От себя: добавил ajax пагинацию для страницы с таблицей
