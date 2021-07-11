from core.pyba_logic import PybaLogic


class ElectricidadLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getElectricidadById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM vibraniodb.electricidad where id={id};"
        result = database.executeQuery(sql)
        return result

    def getElectricidadAll(self):
        database = self.databaseObj
        sql = f"SELECT * FROM vibraniodb.electricidad;"
        result = database.executeQuery(sql)
        return result
