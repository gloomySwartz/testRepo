from datetime import datetime as dt
from hello_printer import print_hello


def main():
    print(
        f'This is a test program. Current time: {dt.now().isoformat()}'
    )
    print_hello()


if __name__ == '__main__':
    main()
