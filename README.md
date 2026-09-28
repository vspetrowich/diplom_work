##Дипломная работа профессии "Python-разработчик"

Идём на официальный сайт virtualbox

https://www.oracle.com/virtualization/virtualbox/

Скачиваем установщик для Вашей ОС (в нашем случае - Win):

https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html?source=:ow:o:p:nav:mmddyyVirtualBoxHero&intcmp=:ow:o:p:nav:mmddyyVirtualBoxHero

Скачиваем Ubuntu-образ для установки на виртуальную машину:
Download Ubuntu Desktop
в нашем случае релиз: Ubuntu 26.04.1 LTS
https://ubuntu.com/download/desktop

Начинаем наполнение нашей виртуальной машины:

обновляем все установленные пакеты:
sudo apt update -y

Устанавливаем Python:
sudo apt install python3-venv python3-pip postgresql -y

проверяем версию python в терминале:
python3 --version
проверяем версию git в терминале:
git --version
если нет, то установливаем:
sudo apt install git

скачиваем PyCharm:
https://www.jetbrains.com/ru-ru/pycharm/download/other/
в нашем случае релиз: Версия: 2026.1.5
После этого настраиваем и передаём скаченный файл через "Общие папки".
В общем можно скачать и установить всё через интернет, как в следующей инструкции, но если сайт недоступен отовсюду, то качаем отдельно и передаём файл:
https://help.sweb.ru/kak-ustanovit6-pycharm-na-ubuntu-i-debian_1495.html

В нашем случае актуальна: Установка из архива .tar.gz
В процессе установки, перед установкой PyCharm из архива необходимо установить java:
Для установки java и безошибочной прогрузки и установки PyCharm необходимо установить:
sudo apt-get install openjdk-26-jdk

Установить AI-плагин из списка:
Установка Плагина CASCADE(Windsurf Plugin for Python,​ JS,​ Java,​ Go.​.​.)
Скачиваем Zip-файл через браузер с VPN:
https://plugins.jetbrains.com/files/20540/1084904/codeium-2.12.24.zip?updateId=1084904&pluginId=20540&family=INTELLIJ

устанавливаем пакет:
sudo apt install python3-virtualenv

virtualenv --python=python3.14 venv
активируем пространство:
source venv/bin/activate
деактивируем:
deactivate
если необходимо удалить скрытую папку: rm -rf /home/vboxuser/diplom_work/.venv

pip install -r requirements.txt

устанавливаем текстовый редактор:

sudo snap install code --classic