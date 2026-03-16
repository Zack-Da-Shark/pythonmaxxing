def minion_game(string):
    
    # Determine the players, bribed with bananas btw
    kevin = 0
    stuart = 0
    
    # This method uses 1 loop only in a smart way as it will count the amount of possible substrings instead!
    start = 0
    
    # Remember the cases dummy
    string = string.lower()
    
    while start < len(string):
        
        # Check starting chracter real quickly
        if string[start] == "a" or string[start] == "e" or string[start] == "i" or string[start] == "o" or string[start] == "u":
            kevin += len(string) - start
        else:
            stuart += len(string) - start
        
        start += 1
        
        #print("still have ", string[start:], " left to go")
        
    # Determine Winner
    if kevin == stuart:
        print("Draw")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print(f"Kevin {kevin}")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)
