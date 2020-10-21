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

            value = func(*args, **kwargs, connection=this.connection)

        except cx_Oracle.Error as error:
            print(error)

        finally:
            if connection:
                connection.close()
    
    return wrapper_decorator

@connect
def print_command(command, connection=None):
    cur = connection.cursor()
    for row in cur.execute(command):
        print(row)

def main():
    print_command("select * from gadi.t_empl")

if __name__ == "__main__":
    main()