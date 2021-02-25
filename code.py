'''
Description: To create the text file of given pattern and to display number of searched words repeated

Author: Sharath Neelappa Saunshi

Ps No : 99003765

Date  : 22/02/2021


'''

import re
class Find_Word:

    def __init__(self, pattern, f):
        self.pattern = pattern
        self.f = f


    def pattern_search(self,):

        count = 0
        
        match = re.findall(self.pattern, self.f, re.M | re.I)
        extension = ".txt"
        file_name = str(self.pattern) + extension
        f_out = open(file_name, "w+")
        f_out.write("The number of occurrences of keyword is:" + str(len(match)))
        f_out.write(str("\n\n"))
        split_f = self.f.split()
        f = open(file_name, "a+")
        for i in range(len(split_f)):
            match = re.match(self.pattern, split_f[i], re.M | re.I)
            if match:
                count += 1
                String = (split_f[i-1]+" "+split_f[i]+" "+split_f[i+1]+"\n")
                f.writelines(str(String))




if __name__ == '__main__':


    with open('input.txt') as input_file:
        read_file = input_file.read()
        
    for x in range(5):
        keyword = input("Enter the keyword you wanted to search in file:")
        d = Find_Word(keyword, read_file)
        d.pattern_search()


