from core.pyba_logic import PybaLogic


class ConstruccionLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getConstruccionById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM vibraniodb.construccion where id={id};"
        result = database.executeQuery(sql)
        return result

    def getConstruccionAll(self):
        database = self.databaseObj
        sql = f"SELECT * FROM vibraniodb.construccion;"
        result = database.executeQuery(sql)
        return result
