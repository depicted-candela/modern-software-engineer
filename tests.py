def compute_lps_array(pattern):
    """
    Builds the LPS (Longest Proper Prefix which is also Suffix) array.
    This is the "déjà vu table" that stores information about the pattern's
    internal repetitions.
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0: length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(dna_strand, gene_marker):
    """
    Searches for a gene_marker within a dna_strand using KMP.
    Returns a list of all starting indices of the marker.
    """
    n = len(dna_strand)
    m = len(gene_marker)
    lps = compute_lps_array(gene_marker)
    print(f"LPS: {lps}")
    
    i = 0  # Pointer for dna_strand
    j = 0  # Pointer for gene_marker
    found_indices = []
    
    while i < n:
        if gene_marker[j] == dna_strand[i]:
            i += 1
            j += 1
        if j == m:
            # We found the entire pattern!
            found_indices.append(i - j)
            # Use LPS to keep searching for the next match.
            j = lps[j - 1]
        elif i < n and gene_marker[j] != dna_strand[i]:
            # Mismatch after j matches.
            # This is the magic step: don't reset j to 0.
            # Use the LPS array to find the next best place to resume.
            if j != 0: j = lps[j - 1]
            else: i += 1
                
    return found_indices

# --- Real-World Scenario Data ---
dna_strand = "ACGTACGTACGTABACGTACGTACGT"
gene_marker = "ACGTAC"

indices = kmp_search(dna_strand, gene_marker)
print(indices)