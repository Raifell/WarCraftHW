from django.db import models
from django.utils.text import slugify


class Game(models.Model):
    title = models.CharField('Game', max_length=255)

    def __str__(self):
        return self.title


class Description(models.Model):
    text = models.TextField('Description')
    game = models.ForeignKey('Game', on_delete=models.DO_NOTHING, verbose_name='Game')

    def __str__(self):
        return self.game.title


class Picture(models.Model):
    picture = models.ImageField('Picture', upload_to='picture/%Y/%m/%d')
    game = models.ForeignKey('Game', on_delete=models.DO_NOTHING, verbose_name='Game')
    slug = models.SlugField('Slug', unique=True, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.picture)
        super(Picture, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.game.title, self.slug)


class Video(models.Model):
    video = models.FileField('Video', upload_to='video/%Y/%m/%d')
    game = models.ForeignKey('Game', on_delete=models.DO_NOTHING, verbose_name='Game')

    def __str__(self):
        return self.game.title


class Audio(models.Model):
    title = models.CharField('Title', max_length=255, null=True)
    audio = models.FileField('Audio', upload_to='audio/%Y/%m/%d')
    game = models.ForeignKey('Game', on_delete=models.DO_NOTHING, verbose_name='Game')

    def __str__(self):
        return '{} - {}'.format(self.title, self.game.title)

