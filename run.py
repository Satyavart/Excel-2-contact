import xlrd

loc='D:\OneDrive\Desktop\\1.xlsx'
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
name=[]
no=[]
size = "size of list"
for i in range(size):
    name.append(sheet.cell_value(i, 0))
    no.append(int(sheet.cell_value(i, 1)))

vcf = open('contact.vcf','w')
for i in range(size):
    vcf.write("BEGIN:VCARD\nVERSION:3.0\n")
    vcf.write("N:"+name[i]+";;;\n")
    vcf.write("FN:"+name[i]+"\n")
    vcf.write("TEL;TYPE=VOICE,CELL;VALUE=text:"+str(no[i])+"\n")
    vcf.write("END:VCARD\n")
vcf.close()
