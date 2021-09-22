import qrcode

# Просим пользователя ввести данные для кодирования
data = input('Введите текст или ссылку: ')

# Создаем экземпляр объекта qr для qr-кода, у которого определяем
qr = qrcode.QRCode(
    version=1,  # Какую версию используем
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Коррекция ошибки
    box_size=10,  # Размер бокса
    border=4,  # Границы
)
# Добавляем data в QR-код
qr.add_data(data)
# Компилируем данные в массив qr-кодов \ создаем qr-код
qr.make()

# Генерируем qr код в картинку
img = qr.make_image(fill_color="black", back_color="white")

# Используя библиотеку pillow сохраняем картинку
img.save('test.jpg', 'JPEG')
