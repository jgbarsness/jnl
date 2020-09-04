import sys
from entry_mod.entry import Entry
from collection import Collection
from entry_mod.entrybox import TextBox
from strats import command_strats, strat
import constants as c
import os
from pathlib import Path
from file_handle import FileHandle

'''
idl is a command line tool used to manage text entries.
joseph barsness 2020
'''


def main(sys_arguement=None, title=None):
    'routes function calls'

    if sys_arguement is None:
        help_print()
        return

    # reduce calls to join
    joined_title = ' '.join(title)

    # skip to command if launched using sys arguement
    if sys_arguement == '-v':
        container.strategy = command_strats.ViewStrat()
        container.call_strat(joined_title)

    elif sys_arguement == '-wipe':
        if error_out("\ndefault entry file doesn't exist"):
            return
        FileHandle.wipe_collection()

    elif sys_arguement == '-wipe-all':
        if error_out('\nno collection folder'):
            return
        FileHandle.wipe_all()

    elif sys_arguement == '-b':
        if error_out("\ndefault entry file doesn't exist"):
            return
        FileHandle.backup_collection()

    elif sys_arguement == '-q':
        if error_out("\ndefault entry file doesn't exist"):
            return
        FileHandle.quick_delete(container.collection)

    elif sys_arguement == '-del':
        if not FileHandle.file_verify():
            print("\ndefault entry file doesn't exist")
            return
        # check for presence of entries. continue if so
        if (len(container.collection) != 0) and (len(joined_title) != 0):
            FileHandle.delete_entry(joined_title, container.collection)
        # if no keyword is supplied to search with, show syntax
        else:
            print('\nnothing to show\nformat: idl -del [keyword]')

    elif sys_arguement == '-h' or sys_arguement == '-help':
        print(c.HELP)

    elif sys_arguement == '-load':
        FileHandle.load_from_backup()

    elif sys_arguement == '-config':
        if FileHandle.check_dir() != False:
            # reset defaults
            folder = Path(c.DIR_NAME)
            FileHandle.gen_config('idl', c.DEFAULTS)
            print(c.YELLOW + '\nconfig updated as ' 
                  + c.PURPLE + os.path.abspath(folder / 'idl.ini') + c.END)

    elif sys_arguement == '-t':
        container.strategy = command_strats.TSearchStrat()
        container.call_strat(joined_title)

    elif sys_arguement == '-s':
        if len(title) != 0:
            if FileHandle.check_dir() != False:
                FileHandle.switch(joined_title)
        else:
            print("\nno name specified")


    elif sys_arguement == '-n':
        if FileHandle.check_dir() == False:
            return
        # if a title is supplied in the same line
        if (len(title) != 0):
            Entry(joined_title)
        else:
            # run a full entry
            experience = str(input('title:\n'))
            Entry(experience)

    elif sys_arguement == '-n1':
        if FileHandle.check_dir() == False:
            return
        if (len(title) != 0):
            Entry(joined_title, '-n1')
        else:
            experience = str(input('title:\n'))
            Entry(experience, '-n1')

    elif sys_arguement == '-n2':
        if FileHandle.check_dir() == False:
            return
        if (len(title) != 0):
            Entry(joined_title, '-n2')
        else:
            experience = str(input('title:\n'))
            Entry(experience, '-n2')

    elif sys_arguement == '-a':
        # must be at least two words long for both a tag and entry
        if len(title) > 1:
            if FileHandle.check_dir() == False:
                return
            # pass in tag as list to allow for formatting
            Entry(title, '-a')
        else:
            print('\nno tag selected')

    elif sys_arguement == '-nt':
        if FileHandle.check_dir() == False:
            return
        # force a textbox entry
        Entry(None, '-nt')

    else:
        if FileHandle.check_dir() == False:
            return
        # default to a one-lined title only entry
        Entry(' '.join(sys.argv[1:]), '-e')


def help_print():
    'prints out program info, including current active collections'

    # print out file locations
    if os.path.exists(c.DIR_NAME):
        if os.path.exists(c.COLLECTION_TITLE):
            print('current default: ' + c.PURPLE + os.path.abspath(c.COLLECTION_TITLE) + c.END)
        if os.path.exists(c.BACKUP_TITLE):
            print('backup: ' + c.PURPLE + os.path.abspath(c.BACKUP_TITLE) + c.END)
        collections = [f for f in os.listdir(c.DIR_NAME) if f.endswith('.txt')]
        d = Path(c.DIR_NAME)
        if len(collections) > 0:
            # check for presence of formatted entries
            entry = [f for f in collections if len(Collection(None).scan_collection(d / f)) > 0]
            if len(entry) > 0:
                print('collections: ' + c.PURPLE + ' '.join(entry) + c.END)
    print(c.HEADER + c.HELP)


def error_out(message: str):
    'prints out message and returns true, else returns false if no error'

    if not FileHandle.file_verify():
        print(message)
        return True
    return False


if __name__ == '__main__':
    container = Collection(None)
    # check if a sys arguement is present
    try:
        main(sys.argv[1], sys.argv[2:])
    except IndexError:
        main()
