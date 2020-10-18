import cx_Oracle
import config

connection = None
cx_Oracle.init_oracle_client(lib_dir=r".\instantclient")

try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding
    )
    print(connection.version)
    cur = connection.cursor()
    for row in cur.execute("select * from gadi.t_empl"):
        print(row)

except cx_Oracle.Error as error:
    print(error)

finally:
    if connection:
        connection.close()