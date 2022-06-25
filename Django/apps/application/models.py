from django.db import models
from django.utils import timezone
import datetime

class Board(models.Model):
    board_name = models.CharField('Назва дошки', max_length = 200)
    board_path = models.CharField('Путь до дошки', max_length = 200)
    class Meta:
        verbose_name = "Дошка"
        verbose_name_plural = "Дошки"

    def __str__(self):
        return self.board_name

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    thread_title = models.CharField('Назва треду', max_length = 100)
    thread_text = models.TextField('Текст треду')
    pub_date = models.DateTimeField('Дата публикації')
    img = models.ImageField('Зображення', default = 0, null=True, blank=True)
    thread_id = id

    def __str__(self):
        return self.thread_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    def short(self):
        self.thread_short = str(self.thread_text[:300] + "...")
        if self.thread_short == str(self.thread_text + "..."):
            return self.thread_text
        else:
            return self.thread_short

    def short_ttl(self):
        self.thread_short_ttl = str(self.thread_title[:50] + "...")
        if self.thread_short_ttl == str(self.thread_title + "..."):
            return self.thread_title
        else:
            return self.thread_short_ttl



    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треди"


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete = models.CASCADE)
    comment_text = models.CharField('Текст комментаря', max_length = 200)
    pub_date = models.DateTimeField('Дата публикації')
    comment_id = id

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
