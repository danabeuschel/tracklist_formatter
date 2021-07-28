import re
import sys

PRINT_COLUMNS = ['Artist', 'Title', 'Label']

def convert_html_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.read()

    table_re = re.compile(r'\<table(.*)</table>', re.DOTALL)
    table_rows = table_re.findall(lines)[0].split('</tr>\n      <tr>\n')
    if not table_rows:
        print 'Your tracklist appears to be missing a table. Try opening it in a web browser to see if it appears correctly.'
        return

    col_name_re = re.compile(r'\<th>(.*?)\</th>')
    col_names = col_name_re.findall(table_rows[0])

    for col in PRINT_COLUMNS:
        if col not in col_names:
            print 'Error: file missing %s' % (col)
            return

    col_index = {col: i for i, col in enumerate(col_names)}

    row_data_re = re.compile(r'\<td>(.*?)\</td>')

    def parse_row(row):
        row_data = row_data_re.findall(row)
        return [row_data[col_index[col]].strip() for col in PRINT_COLUMNS]

    return list(map(parse_row, table_rows[1:]))


def main():
    args = sys.argv
    if len(args) == 1:
        print 'Oops! You didn\'t specify a file name! Try rerunning as python tracklist_formatter.py my_tracklist.html'
        return

    filename = sys.argv[1]
    if not filename.endswith('.html'):
        filename += '.html'

    print '\n\n\n'
    tracklist = convert_html_to_list(filename)

    if tracklist is None:
        return

    for track in tracklist:
        print '%s - %s [%s]' % tuple(track)

if __name__ == '__main__':
    main()



