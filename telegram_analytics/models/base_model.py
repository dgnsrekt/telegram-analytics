from peewee import PostgresqlDatabase, Model

# TODO: add a config file that sets the database name
db = PostgresqlDatabase('telegram')


def getCurrentDateTime():
    return datetime.utcnow()


class BaseModel(Model):

    class Meta:
        database = db
