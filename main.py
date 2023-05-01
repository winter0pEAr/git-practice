# Test python env
def print_hello():
    animals = ['dog', 'cat', 'hamster'] # in one line
    foods = [
            'stagetti',
             'pizzs'
             ] # w/o trailing comma
    names = [
            'john',
            'jane',
            'Gill-dong'
            ] # w/ trailing comma
    for f_name in names:
        print(f'hello,{f_name}')

if __name__ == '__main__':
    print_hello()

