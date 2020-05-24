import configparser


HEADER = '\n---\njnl\n---\nv0.01\nmade by joseph barsness\n\nthis is a command line tool for recording\
 and accessing things.\nnotes about entry\
 are recorded through a pop-up window.\nrunning with any command will\
 create a journal file.\n\'jnl arg title/keyword/etc\'\n\n' 

HELP = 'sys arguements:\n\
\'-n\': new entry with both notes and why sections\n\
\'-ng\': new entry with notes section\n\
\'-nw\': new entry with why section\n\
\'-e\': new title entry\n\
\'-a\': new tagged entry. format: \'jnl -a tag title\'\n\
\nentry titles can be one-lined like \'jnl arg title\'\n\n\
\'-v\': view journal\n\
\'-wipe\': delete entire journal\n\
\'-b\': create backup of journal\n\
\'-load\': load entries from backup\n\
\'-config\': generate config file in pwd. if config exists, defaults reset.\n\
           updating config may outdate journal\n\
\'-del\': delete entry\n\
\'-q\': quick delete the last entry made\
\n\'-k\': search for entries with keywork\
\n\'-t\': search for entries with a tag\n'

WHY = '\'enter\' key to open text box. prompt: why record this entry?'

NOTE = '\n\'enter\' key to open text box. prompt: general notes section'

ACTION = '\'o\' for new entry, \'p\' to view previous,\
\'k\' when done\n'

SCAN_REGEX = r'\n\n([A-Z])(?=[a-z]{2}\s[0-9]{2}[:][0-9]{2}[A-Z]{2}\s[A-Z][a-z]{2}\s[0-9]{2}\s[0-9]{4})'

CONFIG_MESSAGE = '\n# WRNG: updating may outdate journal in pwd\n\n\
# \'end_marker\' determines entry marker recorded in journal file. \
updating will outdate journal file in pwd.\n\
# \'datestamp_underline\' determines the series of underscores under the entry\
 date time stamp. may be changed without outdating anything.\n\
# \'journal_title\' determines the name of the journal file. set this to \
the desired default journal file, or change to create a new one.\n\
# \'backup_title\' determines the name of the backup file. set this to \
the desired default backup file, or change to create a new one.\n\
# \'notes_marker\' determines what should proceed an entry\'s \'notes\' \
section. may be changed without outdating anything.\n\
# \'why_marker\' determines what should proceed an entry\'s \'why\' \
section. may be changed without outdating anything.'

# use config values if present, else use default
try:
    config = configparser.ConfigParser()
    config.read('journal_mngr.ini')

    END_MARKER = config['DEFAULT']['END_MARKER']
    DATESTAMP_UNDERLINE = config['DEFAULT']['DATESTAMP_UNDERLINE']
    JOURNAL_TITLE = config['DEFAULT']['JOURNAL_TITLE'] + '.txt'
    BACKUP_TITLE = config['DEFAULT']['BACKUP_TITLE'] + '.txt'
    NOTES_MARKER = config['DEFAULT']['NOTES_MARKER']
    WHY_MARKER = config['DEFAULT']['WHY_MARKER']

except KeyError:
    END_MARKER = '#*#*#*#*#*#*#*#*#*#*#*#'
    DATESTAMP_UNDERLINE = '-----------------------'
    JOURNAL_TITLE = 'journal.txt'
    BACKUP_TITLE = 'backup_journal.txt'
    NOTES_MARKER = '-n:'
    WHY_MARKER = '-w:'
