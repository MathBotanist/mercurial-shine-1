import cx_Oracle
import config
import functools

def connect(func):
    @functools.wraps(func)

    def wrapper_decorator(*args, **kwargs):
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

            value = func(*args, **kwargs, conn=connection)

        except cx_Oracle.Error as error:
            print(error)

        finally:
            if connection:
                connection.close()
    
    return wrapper_decorator

@connect
def command(command, conn=None):
    cur = conn.cursor()
    return cur.execute(command)