# OTUS_selenium_UI
Структура проекта:
OTUS_selenium_UI/
│
├── page_objects/           # Реализация Page Object для каждой страницы
├── tests/                  # Каталог с тестами
│   └── test_start.py/      # Тесты
│
├── progs/                  # Вспомогательные программы
│   ├── allure-2.13.9.tgz   # Архив для установки Allure
│   ├── cm_linux_amd64      # Бинарный файл для запуска Selenoid
│
├── requirements.txt        # Список пакетов необходимых для работы проекта
├── docker-compose.yml      # Конфигурация Docker Compose для запуска OpenCart, БД и админки
├── conftest.py             # Конфигурационный файл для тестов
├── pytest.ini              # Конфигурационный файл для настроек запуска тестов
└── README.md               # Описание проекта и инструкции по запуску
В папке tests находятся тесты 
В папке progs находится:
-allure-2.13.9.tgz - для первичной установки аллюра
-cm_linux_amd64 - для запуска селенойда
Проект работает примерно так:
selemoid запускается командой - ./cm_linux_amd64 selenoid start
selemoid-ui запускается - docker run -d --name selenoid-ui --network selenoid -p 8090:8080 aerokube/selenoid-ui:1.10.11 --selenoid-uri http://selenoid:4444
opencart, bd и админка запускаются командой - OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker compose up
jenkins запускается командой - docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk21
В jenkins запускается джоба Selenium_tests_opencart
Джоба запускается с настраиваемыми параметрами:
-Адрес executor (selenoid)
-Адрес приложения opencart
-Браузер
-Версию браузера
-Количество потоков
Отчетность собирается в allure по итогам прогона джобы, при падении теста в отчет прикрепляется скриншот

