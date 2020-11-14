try:
    fileinput = open('yourtexthere.txt')
    try:
        input = list(fileinput.read())
        #change eventh character to uppercase
        for x in range(0, len(input), 2):
            if input[x] != ' ':
                input[x] = input[x].upper()
        #change odd(th) character to lowercase
        for x in range(1, len(input), 2):
            if input[x] != ' ':
                input[x] = input[x].lower() 
        input = ''.join(input)
        open('theresult.txt', 'w').write(input)
    finally:
        fileinput.close()
except:
    open('yourtexthere.txt', 'w')