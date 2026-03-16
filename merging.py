def merge_the_tools(string, k):
    # Idea is to split the strings into characters and then store them in a list of lists of size k
    # Change of plans :3
    # Gonna populate a list with enough letters to make a k-length word then sort out that word
    start = 0
    iterate = 0
    add = []
    while start + k <= len(string):
        
        # Put the characters into the list
        
        add.append(string[start + iterate])
        
        iterate += 1
        
        # The conditional statement will run whenever the list has enough letters to be a k-length word
        
        if iterate == k:

            # Reset the iterator
            iterate = 0

            # Incremenet the count
            start += k
            
            # Remove duplicates in list
            
            add = list(dict.fromkeys(add))
            
            # Print the list
            
            print("".join(add))
            
            # Reset the list
            
            add = []
