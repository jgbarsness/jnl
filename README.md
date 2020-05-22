## journal mngr <br />
is a command line tool used to create and manage journal entries

#### sys arguments:

'**-n**': new entry with both notes and why sections<br />
'**-ng**': new entry with notes section<br />
'**-nw**': new entry with why section<br />
'**-e**': new title entry<br />
'**-a**': new tagged entry. format: 'journal -a [tag] [entry]'<br />
entry titles can be one-lined like 'journal -n my title'<br />
'**-v**': view journal<br />
'**-wipe**': delete entire journal<br />
'**-b**': create backup of journal<br />
'**-load**': load entries from backup<br />
'**-config**': generate config file in pwd. if config exists, defaults reset.
updating config may outdate journal<br />
'**-del**': delete entry<br />
'**-q**': quick delete the last entry made<br />
'**-k**': search for entries with keywork<br />
'**-t**': search for entries with a tag

'journal [sys_arg] [title_or_keyword]'