# Изменение размера изображения
Скрипт принимает на вход изображение и кладёт изображение с новым размером куда скажет пользователь или рядом с исходным. У него есть обязательный аргумент – путь до исходной картинки. И несколько необязательных: width - ширина результирующей картинки, height - её высота, scale - во сколько раз увеличить изображение (может быть меньше 1), output - куда класть результирующий файл.


Скрипт принимает на вход изображение и кладёт изображение с новым размером куда скажет пользователь или рядом с исходным. У него есть обязательный аргумент – путь до исходной картинки. И несколько необязательных: `width` - ширина результирующей картинки, `height` - её высота, `scale` - во сколько раз увеличить изображение (может быть меньше 1), `output` - куда класть результирующий файл.

# Как установить
Для работы скрипта Вам потребуется библиотека PIL
Для того, чтобы ее установить выполните следующую команду.
```bash
pip install -r requirements.txt # alternatively try pip3
```
Рекомендуется использовать виртуальное окружение
# Быстрый старт
В командной строке введите
``` bash
python image_resize.py -scale 2 -i photo.jpg -o ./resized_img/resize_image
```

# Цели проекта
Код создан в учебных целях. В рамках учебного курса по веб-разработке -  [DEVMAN.org](https://devman.org/)
