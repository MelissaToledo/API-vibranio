from core.pyba_logic import PybaLogic


class PodaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getPodaById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM vibraniodb.poda where id={id};"
        result = database.executeQuery(sql)
        return result

    def getPodaAll(self):
        database = self.databaseObj
        sql = f"SELECT * FROM vibraniodb.poda;"
        result = database.executeQuery(sql)
        return result
