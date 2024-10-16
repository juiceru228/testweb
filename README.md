# Основная информация
**testweb** - простое приложение, которое выводит мои или ваши персональные данные в открытый доступ. Так же предоставляет возможность управления через панель суперпользователя.<br />
Создано вебприложение было с целью ознакомления с django, его базовыми функциями и структурой.<br />

 # Статус
 На данный момент реализованны такие страницы, как:<br />
**main**: по пути "/", экран приветствия с кнопками для перехода по остальным адресам;<br />
**name**: по пути "/name", где указанны имя и фамилия; <br />
**group**: по пути "/group", где указанна группа; <br />
**age**: по пути "/age", где указан возраст; <br />
**common**: по пути "/common", где указанна вся вышеперечисленная информация сразу; <br />
**admin**: по пути "/admin", админ панель.<br />

 # Доступ к админ панели:
login: root<br />
password: rootPass<br />

# Требования:
Windows и любые unix-подобные операционные системы(bsd, gnu/linux, macos).<br />
Тестировалось на дистрибутивах gnu/linux debian trixie и gentoo.

Python 3.x<br />
Django 3.x или выше<br />

# Установка
В пустой папке в терминале(bash) написать следующие команды:<br />
git clone https://github.com/juiceru228/testweb;<br />
python3 -m venv .venv;<br />
source .venv/bin/activate;<br />
pip install django;<br />
python3 testweb/savchenko/manage.py runserver;<br />

далее перейти в браузере по странице:<br />
http://127.0.0.1:8000/
