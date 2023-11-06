def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_sequence = sequence[::-1]
    reverse_comp_sequence = ''.join(complement[base] for base in reverse_sequence)
    return reverse_comp_sequence

#Input DNA sequence
sequence = 'GCAGTTGCA'

#Call the function to get the reverse complement
reverse_comp = reverse_complement(sequence)

#Print the reverse complement
print("Original Sequence: ", sequence)
print("Reverse Complement: ", reverse_comp)
