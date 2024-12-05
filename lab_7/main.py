def count_word_frequency(file_path):    try:
        with open(file_path, 'r') as file:            text = file.read()
                import string
        text = text.lower().translate(str.maketrans('', '', string.punctuation))        
        words = text.split()        
        word_count = {}        for word in words:
            word_count[word] = word_count.get(word, 0) + 1          
        return word_count    
    except FileNotFoundError:        print("The file was not found. ")
        return {}
file_path ='just.txt'word_frequencies = count_word_frequency(file_path)
if word_frequencies:
    print("Word Frequencies:")  
for word, count in sorted(word_frequencies.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}: {count}")
