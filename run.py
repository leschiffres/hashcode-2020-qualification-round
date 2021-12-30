from parser import parse_file
from submit import submit
from implementation import heuristic

filenames = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']
f = filenames[2]
input_filename = './input/' + f
output_filename = './output/' + f 
total_books, total_libraries, total_days, scores, libraries = parse_file(input_filename)

print(f"Total days: {total_days}")
print(f"Total Libraries: {total_libraries}")
print(f"Total Books: {total_books}")

total_submitted_libraries, library_ordering = heuristic(total_books, total_libraries, total_days, scores, libraries)

submit(output_filename, total_submitted_libraries, library_ordering)