from datetime import datetime, date, timedelta
import peewee
import enum


db = peewee.SqliteDatabase('hello_word.db')
UNIX_start = datetime.fromtimestamp(0)


class State(enum.Enum):
    untouched = 0
    learning = 1
    master = 2


class Base(peewee.Model):
    class Meta:
        database = db


class Word(Base):
    en = peewee.CharField(default="")
    ch = peewee.CharField(default="")
    stage = peewee.IntegerField(default=0)
    is_master = peewee.CharField(default=False)
    next_review = peewee.DateField(default=UNIX_start.date())


class Review(Base):
    word_id = peewee.IntegerField(default=0)
    review_at = peewee.DateTimeField(default=UNIX_start)
    error_count = peewee.IntegerField(default=0)
    stage_before = peewee.IntegerField(default=0)
    stage_after = peewee.IntegerField(default=0)


def create_table():
    db.create_tables([Word, Review])


def word_init():
    Word.insert_many([
        {'en': 'hello', 'ch': '你好', 'stage': 0, 'is_master': False, 'next_review': date.today()},
        {'en': 'word', 'ch': '单词', 'stage': 0, 'is_master': False, 'next_review': date.today()},
    ]).execute()


if __name__ == '__main__':
    create_table()
    word_init()
