from django.db import models

class Directors(models.Model):
    """ Директора команд """
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    photo = models.ImageField('Фото', upload_to='directors/')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директора'


class Commands(models.Model):
    """ Команды Ф1 """
    name = models.CharField('Название команды', max_length=150)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Лого команды', upload_to='commands/')
    directors = models.ForeignKey(Directors, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Cars(models.Model):
    """ Болиды """
    name = models.CharField('Название болида', max_length=150)
    command = models.ForeignKey(Commands, on_delete=models.SET_NULL, null=True)
    max_speed = models.PositiveIntegerField('Максимальная скорость', default=0)
    best_laps = models.PositiveIntegerField('Лучшие круги за сезон', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Болид'
        verbose_name_plural = 'Болиды'


class PhotoCars(models.Model):
    """ Фото болидов """
    car = models.ForeignKey(Cars, on_delete=models.SET_NULL, null=True )
    photo = models.ImageField('Фото', upload_to='cars/')

    def __str__(self):
        return f"{self.car}"

    class Meta:
        verbose_name = 'Фотография болида'
        verbose_name_plural = 'Фотографии болидов'


class Countries(models.Model):
    """ Страны """
    name = models.CharField('Название страны', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Pilots(models.Model):
    """ Пилоты Ф1 """
    name = models.CharField('ФИО Пилота', max_length=150)
    age = models.PositiveIntegerField('Возраст', default=0)
    image = models.ImageField('Фотографии', upload_to='pilots/')
    command = models.ForeignKey(Commands, verbose_name='Команда', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Cars, verbose_name='Болид', on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Countries, verbose_name='Страна', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пилот'
        verbose_name_plural = 'Пилоты'


class RaitingStar(models.Model):
    """ Звёзды для рейтинга """
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звёзды рейтинга'

class Raiting(models.Model):
    """ Рейтинг """
    ip = models.CharField('IP adress', max_length=15)
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    pilot = models.ForeignKey(Pilots, on_delete=models.CASCADE, verbose_name='Пилот')

    def __str__(self):
        return f"{self.pilot} - {self.star}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


