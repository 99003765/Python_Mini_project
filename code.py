import re


class Find_Word():

    def __init__(self, pattern, f):
        self.pattern = pattern()
        self.f = f

    def pattern_search(self,):

        count = 0
        match = re.findall(self.pattern(), self.f, re.M | re.I)
        extension = ".txt"
        file_name = str(self.pattern) + extension
        f_out = open(file_name, "w+")
        f_out.write("The number of occurrences of keyword is:" + str(len(match)))
        f_out.write(str("\n\n"))
        split_f = self.f.split()
        f = open(file_name, "a+")
        for i in range(len(split_file_text)):
            match = re.match(self.keyword_given, split_file_text[i], re.M | re.I)
            if match:
                count += 1
                x = (split_f[i-1]+" "+split_f[i]+" "+split_f[i+1]+"\n")
                f.writelines(str(x))


