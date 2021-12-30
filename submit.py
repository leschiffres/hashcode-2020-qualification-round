def submit(filename, total_submitted_libraries, library_ordering):
    with open(filename, 'w') as f:
        f.write(str(total_submitted_libraries) + "\n")
        for l in library_ordering:
            f.write(f"{l[0]} {l[1]}\n")
            f.write(' '.join([str(x) for x in l[2]]) + "\n")
        