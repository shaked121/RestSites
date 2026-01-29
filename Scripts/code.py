import re
file1 = open("Data/orf_coding_all.fa.txt","r")
file2 = open("Result/output.txt","w")
gene=""
for line in file1:
    if line.startswith(">"):
        if gene!="":
            file2.write(line + "\n")
        else:
            Dsal = re.findall(R'CC[AG][CT]GG', gene)
            file2.write("There are"+ str(len(Dsal)) + "DsaI sites :\n")
            for x in range(len(Dsal)):
                file2.write(str(Dsal[x]) + "\n")
            SecI = re.findall(R'CC[ACGT]{2}GG', gene)
            file2.write("There are"+ str(len(SecI)) + "SecI sites :\n")
            for x in range(len(SecI)):
                file2.write(str(SecI[x]) + "\n")
            CjuI = re.findall(R'CA[CT][ACGT]{5}[AG]TG', gene)
            file2.write("There are"+ str(len(CjuI)) + "CjuI sites :\n")
            for x in range(len(CjuI)):
                file2.write(str(CjuI[x]) + "\n")
            file2.write(line + "\n")
    line = line.rstrip("\n")
    gene += line
