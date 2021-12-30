def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        total_books, total_libraries, total_days = [int(w) for w in lines[0].strip().split()]
        
        scores = [int(w) for w in lines[1].strip().split()]
        
        libraries = []
        for i in range(2, len(lines), 2): 
            total_library_books, signup, books_per_day = [int(w) for w in lines[i].strip().split()]
            book_list = [int(w) for w in lines[i+1].strip().split()]
            libraries.append([(total_library_books, signup, books_per_day), book_list])
            
            # [scores[book_id] for book_id in book_list]
            
    return total_books, total_libraries, total_days, scores, libraries