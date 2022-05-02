# ITFactory_test

## ТЗ
Создать простое API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.
### Создать сущности
1. ### "Работник":
* имя – char 255
* номер телефона – char 255
2. ### "Торговая точка"
* название
* ForeignKey к "Работник" (обязательно к заполнению) 
3. ### "Посещение"
* дата/время
* ForeignKey к "Торговая точка"
* latitude – float
* longitude – float
### Сделать методы
Для упрощения задания, вместо полноценной авторизации передавать в каждый запрос номер телефона Работника.
1. получить список Торговых точек привязанных к переданному номеру телефона.В ответе:
* список Торговых точек (PK Название)
2. выполнить посещение в Торговую точку. Принимает:
* PK Торговой точки и координаты

В ответе:
* PK Посещения Дата/время
* Проверять, что переданный номер телефона Работника привязан к
указанной ТТ, в противном случае возвращать ошибку.
* При создании Посещения в дата/время сохранить текущие дату/время
Админка
● Работник
○ создание
○ редактирование
○ удаление
○ поиск по имени ● Торговая точка
○ создание
○ редактирование
○ удаление
○ поиск по названию
● Посещение
○ просмотр
○ поиск по имени Работника
○ поиск по названию Торговой точки
