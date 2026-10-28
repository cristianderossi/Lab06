from select import select
import mysql.connector
from mysql.connector import cursor

from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO

        cnx = get_connection()
        if cnx is None:
            raise ConnectionError('Impossibile creare il database')

        cursor= cnx.cursor()
        try:
            query = """""
                    SELECT *
                    FROM Strumento
                    """''

            cursor.execute(query)


            lista_strumenti = []
            for row in cursor:
                lista_strumenti.append(Strumento(row[0],
                                       row[1],
                                       row[2],
                                       row[3],
                                       row[4],
                                       row[5]))

            return lista_strumenti

        finally:
            cursor.close()
            cnx.close()



    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO

        cnx = get_connection()
        if cnx is None:
            raise ConnectionError('Impossibile creare il database')

        cursor = cnx.cursor()
        try:
            query =        """""
                           SELECT *
                           FROM strumento
                           where tipo = %s
                            """""

            cursor.execute(query,(tipo,))

            lista_2 = []

            for row in cursor:
             lista_2.append(Strumento(row[0],
                                             row[1],
                                             row[2],
                                             row[3],
                                             row[4],
                                             row[5]))

            return lista_2

        finally:
            cursor.close()
            cnx.close()









