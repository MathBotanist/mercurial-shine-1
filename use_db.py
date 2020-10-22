import db_connect

buffer = ''

while True:

    command = input('>')
    if command != 'exit':
        
        if command != ';':
            buffer = f'{buffer} {command}'
        else:
            out = db_connect.command(buffer)
            buffer = ''
            if out:
                print(out)
            
            else:
                print('Query returned null')
    else:
        break