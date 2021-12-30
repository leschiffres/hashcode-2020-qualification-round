
import time

def heuristic(total_books, total_libraries, total_days, scores, libraries):

    books_submitted = {}
    libraries_submitted = []

    library_scores = {}

    total_time = 0

    start = time.time()
    while total_time < total_days:
        
        # sunolikos_xronos = round(time() - start, 2)
        # print(sunolikos_xronos)
        
        for i in range(len(libraries)):
            # for each library keep the books that have not been submitted yet.
            libraries[i][1] = [book for book in libraries[i][1] if book not in books_submitted.keys()]
            book_list = libraries[i][1]

            # compute the total weight of all books for this library
            total_weight = sum([scores[book_id] for book_id in book_list])
            
            # we create a time metric where we add the library signup cost with the number of days a library needs
            # to send all of the books it has (books it contains divided by the books it can send per day)
            time_metric = libraries[i][0][1] + (len(libraries[i][1]) / libraries[i][0][2])

            # we then divide the sum of total weight for the library cost divided by the previous time metric.
            # with this score we basically express, the importance of the books a library contains
            # over it's speed to deliver value
            library_scores[i] = total_weight/time_metric

            
        # we sort libraries by the total score and signup the library with that maximizes the above score
        library_scores = {k: v for k, v in sorted(library_scores.items(), key=lambda item: item[1], reverse=True)}
        i = list(library_scores.keys())[0]

        total_time += libraries[i][0][1]
        if total_time >= total_days:
            break
        else:
            for b in libraries[i][1]:
                books_submitted[b] = 0

            signup = libraries[i][0][1]
            new_books = [book for book in libraries[i][1]]        
            libraries_submitted.append((i, signup, new_books))

    total_submitted_libraries = len(libraries_submitted)
    library_ordering = libraries_submitted
    return total_submitted_libraries, library_ordering