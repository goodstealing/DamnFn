
#### English

---

### Simplifying the use of F1-F12 keys 🖱️

The purpose of this application is simple: it is designed to make your work easier when using the F1-F12 keys.

For example, if you encounter problems with the Fn key or the F keys, you can simply use this application. It runs in the Windows tray. If you need to close it, simply go to the tray and right-click, then select "Exit".

### Usage  🐱‍💻

To press keys F1-F9, use the combination F + number, and to press keys F10-F12, use the combination Alt + number (0, 1, 2).

### Installation ⚙
To install the application, simply go to the [Releases](https://github.com/goodstealing/DamnFn/releases/tag/release) section and download the executable file (.exe). It can be launched from any folder on your computer. For greater convenience, it is recommended to set up automatic startup of the application.

To build the project, the PyInstaller library was used with the following arguments:

```
pyinstaller --onefile --add-data "icon.png;." --noconsole --name DamnFn --icon=icon.ico --exclude-module --upx-dir=upx-4.2.3-win64 main.py
```

These arguments allow building the project into a single executable file, excluding the console window, specifying the name `DamnFn` for the .exe file, and adding the `icon.ico` icon. Additionally, the `upx-4.2.3-win64` directory is used for compressing the file using the UPX utility.

--- 


#### Russian

---

### Упрощение работы с клавишами F1-F12 🖱️

Суть этого приложения проста: оно предназначено для облегчения вашей работы при использовании клавиш F1-F12.

Например, если у вас возникли проблемы с работой клавиши Fn или клавиш F, вы можете просто воспользоваться этим приложением. Оно запускается в трее Windows. Если вам нужно закрыть его, достаточно перейти в трей и щелкнуть правой кнопкой мыши, а затем выбрать пункт "Exit".

### Использование  🐱‍💻

Для нажатия клавиш F1-F9 используется сочетание F + число, а для нажатия клавиш F10-F12 используется сочетание Alt + число (0, 1, 2).

### Установка ⚙
Для установки приложения просто перейдите в раздел [Релизы](https://github.com/goodstealing/DamnFn/releases/tag/release) и скачайте исполняемый файл (.exe). Его можно запускать из любой папки на вашем компьютере. Для большего удобства рекомендуется настроить автозапуск приложения.

Для сборки проекта была использована библиотека PyInstaller с указанными аргументами:

```
pyinstaller --onefile --add-data "icon.png;." --noconsole --name DamnFn --icon=icon.ico --exclude-module --upx-dir=upx-4.2.3-win64 main.py
```

Эти аргументы позволяют собрать проект в один исполняемый файл, исключив консольное окно, указав название `DamnFn` для .exe файла и добавив иконку `icon.ico`. Так-же, используется директория `upx-4.2.3-win64` для сжатия файла с помощью утилиты UPX.

---


