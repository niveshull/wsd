# define the list of words to search for
search_words = ["zaprem", "zapreš", "zapre", "zapreva", "zapreta", "zapremo", "zaprete", "zaprejo", "zaprl", "zaprla", "zaprli",
                "zaprle", "zaprlo", "zapreti", "zapirati"]

# open the file for reading
with open('ccKres_skupni.txt', 'r', encoding='utf-8') as f:
    # loop through each line in the file
    for line in f:
        # loop through each word in the line
        for word in line.split():
            # check if the word is in the list of search words
            if word in search_words:
                # print the whole line
                print(line.strip())
                # break out of the inner loop to avoid printing the line multiple times
                break