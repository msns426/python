def count_words():
    file = open("story.txt","r")
    count = 0
    for line in file:
        words = line.split()
        for word in words:
            count += 1
    print("Total words are",count)

count_words()