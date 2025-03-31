fr = open('ciernobiely_obrazok_1.txt' , 'r', encoding='utf-8')
fw = open('konverzia_suboru_1_vystup.txt.', 'w',encoding='utf-8')




def spracuj_riadok(row):
    farby = ' '
    for postup in range (0, len(row)-1, 2):
        dec = int(row[postup:postup+2],16)
        if dec >= 128:
            farby += '1 '
        else:
            farby += '0 '
    farby = farby.strip()
    fw.write (farby + '\n')

        


first_line = fr.readline()
fw.write(first_line) 
sirka , dlzka = first_line.strip().split() 
for riadok in fr:
    spracuj_riadok(riadok)
fw.close()

