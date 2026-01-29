import re

file1 = open("Data/orf_coding_all.fa.txt", "r")
file2 = open("Result/output.txt", "w")

gene = ""
header = ""
count = 0

for line in file1:
    line = line.strip()

    if line.startswith(">"):
        # analyze previous gene
        if gene != "":
            DsaI = re.findall(r"CC[AG][CT]GG", gene)
            SecI = re.findall(r"CC[ACGT]{2}GG", gene)
            CjuI = re.findall(r"CA[CT][ACGT]{5}[AG]TG", gene)
            if(len(DsaI) == 0 and len(SecI) == 0 and len(CjuI) == 0):
                file2.write("No restriction sites found.\n")
            else:
                count += 1
                file2.write("There are " + str(len(DsaI)) + " DsaI sites:\n")
                for x in DsaI:
                    file2.write(x + "\n")

                file2.write("There are " + str(len(SecI)) + " SecI sites:\n")
                for x in SecI:
                    file2.write(x + "\n")

                file2.write("There are " + str(len(CjuI)) + " CjuI sites:\n")
                for x in CjuI:
                    file2.write(x + "\n")


            file2.write("\n")

        header = line
        file2.write(header + "\n")
        gene = ""   # IMPORTANT reset

    else:
        gene += line
file2.write("Number of Protein with any kind of site: " + str(count) + "\n")
file1.close()
file2.close()
