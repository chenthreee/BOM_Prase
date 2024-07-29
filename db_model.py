from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase('k3bom.db')

class K3Data(Model):
    k3code = CharField()
    type_name = CharField()
    specification = CharField()

    class Meta:
        database = SqliteDatabase('k3bom.db')
        db_table = 'k3bom'
