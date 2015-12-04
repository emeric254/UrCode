import sqlite3

nomBDD = 'example.db'


class gestionnaire():

    def __init__(self):
        self.conn = sqlite3.connect(nomBDD)
        print("gestionnaire de bd cree !")

    def setUti(self, nom, prenom, typeU):
        c = self.conn.cursor()
        c.execute("insert into utilisateur(nom, prenom, type) values (?,?,?)", (nom, prenom, typeU))
        self.conn.commit()

    def setNote(self, fk_idU, valeur):
        c = self.conn.cursor()
        c.execute("insert into note(fk_idU, valeur) values (?,?)", (fk_idU, valeur))
        self.conn.commit()

    def setCata(self, appellation, dateDebut, dateFin, lieu, gravite):
        c = self.conn.cursor()
        c.execute("insert into cata(appellation, dateDebut, dateFin,lieu, gravite) values (?,?,?,?,?)",
                  (appellation, dateDebut, dateFin, lieu, gravite))
        self.conn.commit()

    def setActu(self, date, fk_idC, fk_idU, information):
        c = self.conn.cursor()
        c.execute("insert into Actu(idDate, fk_idC , fk_idU, information) values (?,?,?,?)",
                  (date, fk_idC, fk_idU, information))
        self.conn.commit()

    def getUti(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM utilisateur")
        tout = c.fetchall()
        return tout

    def getNote(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM note")
        tout = c.fetchall()
        return tout

    def getCata(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM cata")
        tout = c.fetchall()
        return tout

    def getActu(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM actu")
        tout = c.fetchall()
        return tout

    def getUtiP(self, idU):
        c = self.conn.cursor()
        c.execute("SELECT * FROM utilisateur where idU=" + str(idU))
        tout = c.fetchall()
        return tout

    def getNoteP(self, idN):
        c = self.conn.cursor()
        c.execute("SELECT * FROM note where idN=" + str(idN))
        tout = c.fetchall()
        return tout

    def getCataP(self, idC):
        c = self.conn.cursor()
        c.execute("SELECT * FROM cata where idC=" + str(idC))
        tout = c.fetchall()
        return tout

    def getActuP(self, idA):
        c = self.conn.cursor()
        c.execute("SELECT * FROM actu where idDate=" + str(idA))
        tout = c.fetchall()
        return tout

    def getActuC(self, idC):
        c = self.conn.cursor()
        c.execute("SELECT * FROM actu where fk_idC=" + str(idC) + " order by idDate desc")
        tout = c.fetchall()
        return tout




def creaTables():
    print("Creation tables")
    conn = sqlite3.connect(nomBDD)
    c = conn.cursor()

    # Create table
    c.execute('CREATE TABLE utilisateur '
              '(idU INTEGER, nom text, prenom text, type text, '
              'PRIMARY KEY (idU))')

    c.execute('CREATE TABLE note '
              '(idN INTEGER, fk_idU INTEGER, valeur INTEGER, '
              'FOREIGN KEY (fk_idU) REFERENCES utilisateur(idU) ON DELETE CASCADE, '
              'PRIMARY KEY (idN))')

    c.execute('CREATE TABLE cata '
              '(idC INTEGER, appellation text, dateDebut text, dateFin text, lieu text, gravite INTEGER, '
              'PRIMARY KEY (idC))')

    c.execute('CREATE TABLE actu '
              '(idDate text, fk_idC INTEGER, fk_idU INTEGER, information text, '
              'FOREIGN KEY (fk_idC) REFERENCES cata(idC) ON DELETE CASCADE, '
              'FOREIGN KEY (fk_idU) REFERENCES utilisateur(idU) ON DELETE CASCADE, '
              'PRIMARY KEY (idDate, fk_idC, fk_idU))')

    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    print("fait !")


def suprTables():
    conn = sqlite3.connect(nomBDD)
    c = conn.cursor()

    # supr table
    c.execute("DROP TABLE actu")
    c.execute("DROP TABLE cata")
    c.execute("DROP TABLE note")
    c.execute("DROP TABLE utilisateur")

    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def creaTuples():
    bd = gestionnaire()

    bd.setUti("chewbaca", "Chewi", "passant")
    bd.setUti("C3PO", "6PO", "Famille")
    bd.setUti("Empereur", "Palpatine", "Empereur")
    bd.setUti("Solo", "Hans", "inutile")

    bd.setNote(1, 10)
    bd.setNote(1, 8)
    bd.setNote(1, 7)
    bd.setNote(1, 7)
    bd.setNote(2, 10)
    bd.setNote(3, 8)
    bd.setNote(3, 10)
    bd.setNote(4, 2)

    bd.setCata("Caterine", "23/10/92", "25/10/92", "floridaison", 8)
    bd.setCata("Caterine", "26/10/92", "30/10/92", "floridaison", 10)
    bd.setCata("yannick", "22/10/92", "22/10/92", "paridaison", 2)
    bd.setCata("daesh", "13/11/15", "13/11/15", "paris", 6)
    bd.setCata("yeah", "32/02/64", "34/13/66", "nowere", 10)

    bd.setActu("24/10/92", 1, 1, "whesh ya du vent")
    bd.setActu("24/10/92", 1, 2, "whesh tavu")
    bd.setActu("25/10/92", 1, 1, "whesh ya toujours du vent")
    bd.setActu("05/11/93", 1, 3, "wesh trop pas du vent")
