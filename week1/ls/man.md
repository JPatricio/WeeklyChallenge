### Name
ls - list directory contents

### Synopsis

**ls** [*OPTION*]... [*FILE*]...

### Description
List information about the FILEs (the current directory by default). Sort entries alphabetically if 
none of **-cftuvSUX** nor **--sort**.

Mandatory arguments to long options are mandatory for short options too.

**-a, --all**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not ignore entries starting with .

-A, --almost-all
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not list implied . and ..
--author
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with -l, print the author of each file
-b, --escape
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print octal escapes for nongraphic characters
--block-size=SIZE
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; use SIZE-byte blocks. See SIZE format below
-B, --ignore-backups
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not list implied entries ending with ~
-c
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with -lt: sort by, and show, ctime (time of last modification of file status information) with -l: show ctime and sort by name otherwise: sort by ctime
-C
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list entries by columns
--color[=WHEN]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; colorize the output. WHEN defaults to 'always' or can be 'never' or 'auto'. More info below
-d, --directory
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list directory entries instead of contents, and do not dereference symbolic links
-D, --dired
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; generate output designed for Emacs' dired mode
-f
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not sort, enable -aU, disable -ls --color
-F, --classify
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; append indicator (one of */=>@|) to entries
--file-type
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; likewise, except do not append '*'
--format=WORD
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; across -x, commas -m, horizontal -x, long -l, single-column -1, verbose -l, vertical -C
--full-time
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; like -l --time-style=full-iso
-g
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; like -l, but do not list owner
--group-directories-first
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; group directories before files.
augment with a --sort option, but any
use of --sort=none (-U) disables grouping
-G, --no-group
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; in a long listing, don't print group names
-h, --human-readable
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with -l, print sizes in human readable format (e.g., 1K 234M 2G)
--si
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; likewise, but use powers of 1000 not 1024
-H, --dereference-command-line
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; follow symbolic links listed on the command line
--dereference-command-line-symlink-to-dir
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; follow each command line symbolic link that points to a directory
--hide=PATTERN
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not list implied entries matching shell PATTERN (overridden by -a or -A)
--indicator-style=WORD
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; append indicator with style WORD to entry names: none (default), slash (-p), file-type (--file-type), classify (-F)
-i, --inode
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print the index number of each file
-I, --ignore=PATTERN
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not list implied entries matching shell PATTERN
-k
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; like --block-size=1K
-l
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; use a long listing format
-L, --dereference
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; when showing file information for a symbolic link, show information for the file the link references rather than for the link itself
-m
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fill width with a comma separated list of entries
-n, --numeric-uid-gid
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; like -l, but list numeric user and group IDs
-N, --literal
print raw entry names (don't treat e.g. control characters specially)
-o
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; like -l, but do not list group information
-p, --indicator-style=slash
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; append / indicator to directories
-q, --hide-control-chars
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print ? instead of non graphic characters
--show-control-chars
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; show non graphic characters as-is (default unless program is 'ls' and output is a terminal)
-Q, --quote-name
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; enclose entry names in double quotes
--quoting-style=WORD
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; use quoting style WORD for entry names: literal, locale, shell, shell-always, c, escape
-r, --reverse
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; reverse order while sorting
-R, --recursive
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list subdirectories recursively
-s, --size
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print the allocated size of each file, in blocks
-S
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sort by file size
--sort=WORD
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sort by WORD instead of name: none -U, extension -X, size -S, time -t, version -v
--time=WORD
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with -l, show time as WORD instead of modification time: atime -u, access -u, use -u, ctime -c, or status -c; use specified time as sort key if --sort=time
--time-style=STYLE
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with -l, show times using style STYLE: full-iso, long-iso, iso, locale, +FORMAT. FORMAT is interpreted like 'date'; if FORMAT is FORMAT1<newline>FORMAT2, FORMAT1 applies to non-recent files and FORMAT2 to recent files; if STYLE is prefixed with 'posix-', STYLE takes effect only outside the POSIX locale
-t
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sort by modification time
-T, --tabsize=COLS
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; assume tab stops at each COLS instead of 8
-u
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with -lt: sort by, and show, access time with -l: show access time and sort by name otherwise: sort by access time
-U
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; do not sort; list entries in directory order
-v
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; natural sort of (version) numbers within text
-w, --width=COLS
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; assume screen width instead of current value
-x
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list entries by lines instead of by columns
-X
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sort alphabetically by entry extension
-1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list one file per line

Using color to distinguish file types is disabled both by default and with --color=never. With --color=auto, ls emits color codes only when standard output is connected to a terminal. The LS_COLORS environment variable can change the settings. Use the dircolors command to set it.

### Exit status:
1. if OK,
2. if minor problems (e.g., cannot access subdirectory),
3. if serious trouble (e.g., cannot access command-line argument).

### Author
Written by Richard M. Stallman and David MacKenzie.

### Reporting Bugs
Report ls bugs to bug-coreutils@gnu.org

GNU coreutils home page: <http://www.gnu.org/software/coreutils/>

General help using GNU software: <http://www.gnu.org/gethelp/>

Report ls translation bugs to <http://translationproject.org/team/>

### Copyright
Copyright Â© 2010 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.

This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

### See Also
The full documentation for ls is maintained as a Texinfo manual. If the info and ls programs are properly installed at your site, the command