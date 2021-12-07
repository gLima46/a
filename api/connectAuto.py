import mysql.connector
from credentials import usr, pswd

def insert_db(value1,value2,value3,value4, value5):
    try:  
        mydb = mysql.connector.connect(
            host = "localhost",
            user = usr,
            password = pswd,
            database = "serverhealers"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor()


            sql_query = "INSERT INTO tbDadosPython(fkMaquinas,disco,ram,cpuComp, temperatura, dataCaptura) VALUES (%s,%s,%s,%s,%s,now())"
            val = [value1,value2,value3,value4,value5]
            mycursor.execute(sql_query, val)

            mydb.commit()


            print(mycursor.rowcount, "registro inserido")
            
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")


def qntDeMaquinasTotais():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = usr,
        password = pswd,
        database = "serverhealers"
        )

        mycursor = mydb.cursor()

        sql_maquinas = "select count(idMaquinas) from tbMaquinas;"
        mycursor.execute(sql_maquinas)
        maquinas = mycursor.fetchall()
        
        for row in maquinas:
            qntMaquinas = row[0]
            # print("Maquinas: ", qntMaquinas)
        
        print("Quantidade de maquinas totais: ",qntMaquinas)
            
    except mysql.connector.Error as e:
        print("Erro ao ler data da tabela do Mysql", e)
        
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            # print("ESTÁ PEGANDO!")

def funcMaquinas():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = usr,
        password = pswd,
        database = "serverhealers"
        )

        mycursor = mydb.cursor()

        sql_maquinas = "SELECT idMaquinas from tbMaquinas;"
        mycursor.execute(sql_maquinas)
        maquinas = mycursor.fetchall()
        maquina = []
        for row in maquinas:
            maquina.append(row[0])

            # print(maquinas)

        return maquina

            # print("Maquina: ", nomeMaquinas)
            
    except mysql.connector.Error as e:
        print("Erro ao ler data da tabela do Mysql", e)
        
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            # print("ESTÁ PEGANDO!")