#Name: Maxim Chopivskyy
#ID number: 118364841

#Question 2

def search_file(filename, searchword):        #opens a file and outputs lines with searchword in it
    input = open(filename, 'r')               #open file we search as input
    output = open('fieldsModified.txt', 'w')  #creates file to write output to

    line_count = 0


    for line in input:
        line_count += 1
        #gets line number

        test_line = line.lower().split()   #brings words to lowercase and separate in list
                                           #makes easier to search line

        if searchword.lower() in test_line:
            l = str(line_count) + ' - ' + line #creates line with number line preceding
            print(l)
            output.write(l)                    #writes line to output file



    input.close()
    output.close()
    #important to close for memory




search_file('fields.txt', "fields")