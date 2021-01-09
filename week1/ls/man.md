### Name
ls - list directory contents

### Synopsis

**ls** [*OPTION*]... [*FILE*]...

### Description
List information about the FILEs (the current directory by default). Sort entries alphabetically if 
none of **-cftuvSUX** nor **--sort**.

Mandatory arguments to long options are mandatory for short options too.

Options

     -@  TODO
         Display extended attribute keys and sizes.

     -1  --one    
         (The numeric digit 'one'.)  Force output to be one entry per line.
         This is the default when output is not to a terminal.

     -a  --all    
         List all entries including those starting with a dot .
     
     -A  --almost-all    
         List all entries including those starting with a dot .
         Except for . and ..
         This option is always set for the superuser (via sudo).

     -B  TODO
         Force printing of non-printable characters (as defined by
         ctype(3) and current locale settings) in file names as \xxx,
         where xxx is the numeric value of the character in octal.

     -b  TODO
         As -B, but use C escape codes whenever possible.

     -C  TODO
         Force multi-column output; this is the default when output is to
         a terminal.

     -c  TODO
         Use time when file status was last changed for sorting or printing.

     -d  TODO
         Directories are listed as plain files (not searched recursively).

     -F  TODO
         Display a slash / immediately after each pathname that is a
         directory, an asterisk * after each that is executable, an at
         sign @ after each symbolic link, an equals sign = after
         each socket, a percent sign % after each whiteout, and a
         vertical bar | after each that is a FIFO.

     -f  TODO
         Output is not sorted.

     -G  TODO
         Enable colour output.
         This option is equivalent to defining CLICOLOR in the environment.(See below.)

     -g  TODO
         This option is deprecated. This option is only available for compatibility
         with POSIX; it is used to display the group name in the long (-l) format output
         (the owner name is suppressed).

     -H  TODO
         Symbolic links on the command line are followed.
         This option is assumed if none of the -F, -d, or -l options are specified.

     -h  TODO
         When used with the -l option, use unit suffixes: Byte, Kilobyte,
         Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the
         number of digits to three or less using base 2 for sizes.

     -i  TODO
         For each file, print the file's file serial number 
         (inode number).

     -k  TODO
         If the -s option is specified, print the file size allocation in
         kilobytes, not blocks.  This option overrides the environment
         variable BLOCKSIZE.

     -L  TODO
         If argument is a symbolic link, list the file or directory the
         link references rather than the link itself.  This option cancels
         the -P option.

     -l 
         List in long format. Ownership, Date/Time etc (See below)
         For terminal output, a total sum of all the file sizes is 
         output on a line before the long listing.
         If the file is a symbolic link the pathname of the linked-to file is
         preceded by ->

     -m  TODO
         Stream output format; list files across the page, separated by commas.

     -n  TODO
         Display user and group IDs numerically rather than converting to
         a user or group name in a long (-l) output. This option turns on the -l option.

     -O  TODO
         Include the file flags in a long (-l) output.

     -o  TODO
         List in long format, but omit the group id.

     -P  TODO
         If argument is a symbolic link, list the link itself rather than
         the object the link references.  This option cancels the -H and
         -L options.

     -p  TODO
         Write a slash (/) after each filename if that file is a directory.

     -q  TODO
         Force printing of non-graphic characters in file names as the
         character `?'; this is the default when output is to a terminal.

     -R  TODO
         Recursively list subdirectories encountered.

     -r  TODO
         Reverse the order of the sort to get reverse lexicographical
         order or the oldest entries first.
         (or largest files last, if combined with sort by size)

     -S  TODO
         Sort files by size

     -s  TODO
         Display the number of file system blocks actually used by each
         file, in units of 512 bytes, where partial units are rounded up
         to the next integer value.   If the output is to a terminal, a
         total sum for all the file sizes is output on a line before the
         listing.  The environment variable BLOCKSIZE overrides the unit
         size of 512 bytes.

     -T  TODO
         When used with the -l (lowercase letter ``ell'') option, display
         complete time information for the file, including month, day,
         hour, minute, second, and year.

     -t  TODO
         Sort by time modified (most recently modified first) before
         sorting the operands by lexicographical order.

     -u  TODO
         Use time of last access, instead of last modification of the file
         for sorting (-t) or printing (-l).

     -v  TODO
         Force unedited printing of non-graphic characters.
         This is the default when output is not to a terminal.

     -W  TODO
         Display whiteouts when scanning directories. (-S) flag).

     -w  TODO
         Force raw printing of non-printable characters.  This is the
         default when output is not to a terminal.

     -x  TODO
         The same as -C, except that the multi-column output is produced
         with entries sorted across, rather than down, the columns.

Using color to distinguish file types is disabled both by default and with --color=never. With --color=auto, ls emits color codes only when standard output is connected to a terminal. The LS_COLORS environment variable can change the settings. Use the dircolors command to set it.

**The Long Format**

If the -l option is given, the following information is displayed for each file: `file mode, number of links, owner name, group name, number of bytes in the file, abbreviated month, day-of-month file was last modified, hour file last modified, minute file last modified, and the pathname.`

In addition, for each directory whose contents are displayed, the total number of 512-byte blocks used by the files in the directory is displayed on a line by itself, immediately before the information for the files in the directory. If the file or directory has extended attributes, the permissions field printed by the -l option is followed by an @ character. Otherwise, if the file or directory has extended security information, the permissions field printed by the -l option is followed by a + character.

If the modification time of the file is more than 6 months in the past or future, then the year of the last modification is displayed in place of the hour and minute fields.

If the owner or group names are not a known user or group name, or the -n option is given, the numeric ID's are displayed.

If the file is a character special or block special file, the major and minor device numbers for the file are displayed in the size field. If the file is a symbolic link, the
pathname of the linked-to file is preceded by ``->''.

The file mode printed under the -l option consists of the entry type, owner permissions, and group permissions. The entry type character describes the type of file, as follows:

    b Block special file.
    c Character special file.
    d Directory.
    l Symbolic link.
    s Socket link.
    p FIFO.
    - Regular file.

The next three fields are three characters each: owner permissions, group permissions, and other permissions. Each field has three character positions:

1. If r, the file is readable; if -, it is not readable.

2. If w, the file is writable; if -, it is not writable.

3. The first of the following that applies:

    S If in the owner permissions, the file is not executable and set-user-ID mode is set. If in the group permissions, the file is not executable and set-group-ID mode is set.
    s If in the owner permissions, the file is executable and set-user-ID mode is set. If in the group permissions, the file is executable and setgroup-ID mode is set.
    x The file is executable or the directory is searchable.
    - The file is neither readable, writable, executable, nor set-user-ID nor set-group-ID mode, nor sticky. (See below.)

These next two apply only to the third character in the last group (other permissions).

    T The sticky bit is set (mode 1000), but not execute or search permission. (See chmod(1) or sticky(8).)
    t The sticky bit is set (mode 1000), and is searchable or executable. (See chmod(1) or sticky(8).)

ls-F passes its arguments to ls if it is given any switches, so `alias ls ls-F' generally does the right thing.

### Exit status:
1. if OK,
2. if minor problems (e.g., cannot access subdirectory),
3. if serious trouble (e.g., cannot access command-line argument).
