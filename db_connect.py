#!/usr/bin/env python3
import cx_Oracle
import config
import functools

cx_Oracle.init_oracle_client(lib_dir=r".\instantclient")

def connect(func):
    @functools.wraps(func)

    def wrapper_decorator(*args, **kwargs):
        connection = None
        
        try:
            connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding
            )

            return func(*args, **kwargs, conn=connection)

        except cx_Oracle.Error as error:
            return f"error: {error}"

        finally:
            if connection:
                connection.close()
    
    return wrapper_decorator

@connect
def command(command, conn=None):
    with conn.cursor() as cur:
        out = cur.execute(command)
        out_string = ''

        for row in out:
            out_string = f'{out_string}\n{row}'
        
        return out_string