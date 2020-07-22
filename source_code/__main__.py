import sys
from entry import Entry
from collection import Collection
from entrybox import TextBox
import constants as c
import os

'''
jnl is a command line tool used to manage text entries.
joseph barsness 2020
'''


def main(sys_arguement=None, title=None):
    'routes function calls'

    if sys_arguement is None:
        if os.path.exists(c.JOURNAL_TITLE):
            print('collection: ' + c.PURPLE + os.path.abspath(c.JOURNAL_TITLE) + c.END)
        if os.path.exists(c.BACKUP_TITLE):
            print('backup: ' + c.PURPLE + os.path.abspath(c.BACKUP_TITLE) + c.END)
        if os.path.exists("jnl.ini"):
            print("config: " + c.PURPLE + os.path.abspath("jnl.ini") + c.END)
        print(c.HEADER + c.HELP)
        return
    # check files
    joined_title = ' '.join(title)
    stored_entries.file_check()
    stored_entries.scan_journal()

    # skip to command if launched using sys arguement
    if sys_arguement == '-v':
        # if there is a keyword to search with
        if (len(title) != 0):
            criteria = ' '.join(title)
            print(c.YELLOW + 'entries containing ' + c.END + '\'' + c.CYAN + criteria + c.END + '\'')
            stored_entries.show_keyword(' '.join(title))
        # if no keyword is present, print out entire journal
        else:
            if (len(stored_entries.collection) != 0):
                print(c.YELLOW + 'all entries:' + c.END)
                stored_entries.print_entries(stored_entries.collection)
            else:
                print('\nnothing here')
    elif sys_arguement == '-wipe':
        stored_entries.wipe_journal()
    elif sys_arguement == '-b':
        stored_entries.backup_journal()
    elif sys_arguement == '-q':
        stored_entries.quick_delete()
    elif sys_arguement == '-del':
        # check for presence of file. continue if so
        if (len(stored_entries.collection) != 0) and (len(title) != 0):
            stored_entries.delete_entry(' '.join(title))
        # if no keyword is supplied to search with, show syntax
        else:
            print('\nformat: jnl -del [keyword]' + c.END)
    elif sys_arguement == '-h' or sys_arguement == '-help':
        print(c.HELP)
    elif sys_arguement == '-load':
        stored_entries.load_from_backup()
    elif sys_arguement == '-config':
        stored_entries.gen_config()
    elif sys_arguement == '-t':
        if (len(stored_entries.collection) != 0) and (len(title) != 0):
            print(c.YELLOW + 'searching for tag ' + c.END + '\'' + c.CYAN + ' '.join(title) + c.END + '\'')
            stored_entries.show_keyword('(' + ' '.join(title) + ')')
        else:
            print('\nformat: jnl -t [tag]')

    elif sys_arguement == '-n':
        # if a title is supplied in the same line
        if (len(title) != 0):
            # keep 'new' as a variable to possibly reference in later formatting decisions
            new = Entry(joined_title)
        else:
            # run a full entry
            experience = str(input('title:\n'))
            new = Entry(experience)
        printout()
    elif sys_arguement == '-n1':
        if (len(title) != 0):
            new = Entry(joined_title, '-n1')
        else:
            experience = str(input('title:\n'))
            new = Entry(experience, '-n1')
        printout()
    elif sys_arguement == '-n2':
        if (len(title) != 0):
            new = Entry(joined_title, '-n2')
        else:
            experience = str(input('title:\n'))
            new = Entry(experience, '-n2')
        printout()
    elif sys_arguement == '-a':
        # must be at least two words long for both a tag and entry
        if len(title) > 1:
            # pass in tag as list to allow for formatting
            new = Entry(title, '-a')
            printout()
        else:
            print('\nno tag selected')
    elif sys_arguement == '-nt':
        # force a textbox entry
        new = Entry(None, '-nt')
        printout()
    else:
        # default to a one-lined title only entry
        new = Entry(' '.join(sys.argv[1:]), '-e')
        printout()


def printout():
    'prints out the entry'

    # refresh searchable list after every entry
    stored_entries.scan_journal()
    # print out entry info + title
    print(c.YELLOW + '\nnew entry in ' + c.PURPLE + os.path.abspath(c.JOURNAL_TITLE) + c.END)


if __name__ == '__main__':
    stored_entries = Collection()
    # check if a sys arguement is present
    try:
        main(sys.argv[1], sys.argv[2:])
    except IndexError:
        main()
