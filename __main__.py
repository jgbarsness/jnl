import app
import sys


if __name__ == '__main__':
    # check if a sys arguement is present
    try:
        app.main(sys.argv[1], sys.argv[2:])
    except IndexError:
        app.main()
