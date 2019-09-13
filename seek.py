with open("file1.txt") as file:
    file.seek(0,2)
    position=file.tell()
    while(position>=0):
        file.seek(position)
        ch = file.read(1)
        print(ch,end="")
        position = position-1
