#----------- STEP 1 Importing the required Libraries (line 3-6)--------------

# Import SeqIO module to read biological sequence files
from Bio import SeqIO
# SeqIO is used to read biological sequence files like FASTA.
from Bio.Seq import Seq


#------------ STEP 2 Here we are reading the DNA Sequence (line 10-13)-------------

# Extraction of the DNA Sequence from the file named simple.fasta
record = SeqIO.read("sample.fasta", "fasta")
dna = record.seq
print(dna)


#------------ STEP 3 Here we are finding the length of the Sequence (line 17-18)-------------

# length command is used to find the length of the DNA Sequence 
print("Length:", len(dna))


#------------ STEP 4 Counting the number of bases separately (line 22-29)-------------

# Count number of Adenine (A)
print("A =", dna.count("A"))
# Count number of Thymine (T)
print("T =", dna.count("T"))
# Count number of Guanine (G)
print("G =", dna.count("G"))
# Count number of Cytosine (C)
print("C =", dna.count("C"))


#------------ STEP 5 Finding the GC Content of the DNA Sequence (line 33-37) --------------

# Formula --> (Number of G + Number of C) / Total Length of DNA × 100
g = dna.count("G")
c = dna.count("C")
gc = (g + c) / len(dna) * 100
print("GC Content =", round(gc,2), "%")


#------------- STEP 6 Converting the DNA Sequence to RNA (line 41-42)--------------

rna = dna.transcribe()
print(rna)


#------------- STEP 7 Forming the complement DNA Sequence (line 46-47)------------

complement = dna.complement()
print(complement)


#------------ STEP 8 Forming the reverse complement of the DNA Sequence (line 51-52)------------

reverse = dna.reverse_complement()
print(reverse)


#--------------STEP 9 Save Analysis Results into Text File (line 56-74)-------------

with open("result.txt","w") as file:

    file.write(f"Sequence Length : {len(dna)}\n")

    file.write(f"A : {dna.count('A')}\n")

    file.write(f"T : {dna.count('T')}\n")

    file.write(f"G : {dna.count('G')}\n")

    file.write(f"C : {dna.count('C')}\n")

    file.write(f"GC Content : {round(gc,2)}%\n")

    file.write(f"RNA : {rna}\n")

    file.write(f"Complement : {complement}\n")

    file.write(f"Reverse Complement : {reverse}\n")

#------------- STEP 10 Confirmation Message (line 85-89)--------------

# Inform user that analysis is completed
print("\n--------------------------------")
print("DNA Analysis Completed Successfully!")
print("Results have been saved in result.txt")
print("--------------------------------")