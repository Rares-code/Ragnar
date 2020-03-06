import sys
import printing
import reports 

file_name = "gamesin.txt"
genre = ""
title = ""
year = 0
source_file_name = sys.argv[1]
target_file_name = sys.argv[2]
year = sys.argv[3]
genre = sys.argv[4]
title = sys.argv[5]
is_in_year = reports.get_latest(source_file_name)
genres = reports.count_by_genre(source_file_name, genre)
try:
    line = reports.get_line_number_by_title(source_file_name, title)
except:
    print("This title is not in this file.")
with open(target_file_name, 'a+') as f:
    f.write(f"{is_in_year} {genres} {line}")