'''
Description: To create the text file of given pattern and to display number of searched words repeated

Author: Sharath Neelappa Saunshi

Ps No : 99003765

Date  : 22/02/2021


'''

import re  # importing Regular Expression Package
class Find_Word:  # creating class
    def __init__(self, pattern, f):  # initialising variables
        self.pattern = pattern
        self.f = f
    def pattern_search(self):  # Creating methods for pattern search
        count = 0  # Initialising search count to zero
        match = re.findall(self.pattern, self.f, re.M | re.I)
        # Searching for given pattern and ignoring cases
        extension = ".txt"
        file_name = str(self.pattern) + extension
        # Converting pattern given to string and adding txt extension
        f_out = open(file_name, "w+")  # opening o/p file with Read,write mode
        f_out.write("The count of words:" + str(len(match)))
        f_out.write(str("\n\n"))
        split_f = self.f.split()  # Splitting up of sentences
        f = open(file_name, "a+")
        for i in range(len(split_f)):   # opening input file in apend mode
            match = re.match(self.pattern, split_f[i], re.M | re.I)
            # matching pattern to splitted words
            if match:
                count += 1                        
                String = (split_f[i-1]+" "+split_f[i]+" "+split_f[i+1]+"\n")
                # creating the matched string
                f.writelines(str(String))

if __name__ == '__main__':  # creating main
    with open('input.txt') as input_file:  # opening input.txt
        read_file = input_file.read()  # reading innput file
    for x in range(5):  # Searching for maximum 5 words at a stretch
        keyword = input("Enter the keyword you wanted to search in file:")
        d = Find_Word(keyword, read_file)  # creating objects,pointing to class
        d.pattern_search()      
    
