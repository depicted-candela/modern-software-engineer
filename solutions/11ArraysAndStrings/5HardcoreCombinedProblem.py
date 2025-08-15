data_stream = "axbyabxyabxyc"
engagement_pattern = "abxy"
scores = [-1, 10, -5, 1, 8, -2, 4, 5, 2, 3, 6, -10, 20]
# Expected Output: 17
# Pattern "abxy" found at index 4. Segment is [8, -2, 4, 5, 2, 3, 6, -10, 20].
# Max subarray sum in this segment is [8, -2, 4, 5, 2] = 17.

data_stream_2 = "aaaaaaaa"
engagement_pattern_2 = "aa"
scores_2 = [1, -5, 4, -5, 4, -5, 4, -5]
# Expected Output: 4
# Occurrences at 0, 1, 2, 3, 4, 5, 6.
# Segment 0: [1, -5, 4, -5, 4, -5, 4, -5] -> Max sum is 4
# Segment 1: [-5, 4, -5, 4, -5, 4, -5] -> Max sum is 4
# ... and so on. The highest max is 4.

def kmp_search(stream, meaningful_pattern):
    """
    Searches for a meaningful_pattern within a stream using KMP.
    Returns a list of all starting indices of the marker.
    """
    n = len(stream)
    m = len(meaningful_pattern)
    lps = compute_lps_array(meaningful_pattern)
    
    i = 0  # Pointer for stream
    j = 0  # Pointer for meaningful_pattern
    found_indices = []
    
    while i < n:
        if meaningful_pattern[j] == stream[i]:
            i += 1
            j += 1
        
        if j == m:
            # We found the entire pattern!
            found_indices.append(i - j)
            # Use LPS to keep searching for the next match.
            j = lps[j - 1]
        elif i < n and meaningful_pattern[j] != stream[i]:
            # Mismatch after j matches.
            # This is the magic step: don't reset j to 0.
            # Use the LPS array to find the next best place to resume.
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return found_indices

def compute_lps_array(pattern):
    """
    Builds the LPS (Longest Proper Prefix which is also Suffix) array.
    This is the "déjà vu table" that stores information about the pattern's
    internal repetitions.
    """
    pattern_size = len(pattern)
    lps = [0] * pattern_size
    length = 0  # Length of the previous longest prefix suffix
    i = 1
    while i < pattern_size:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def maximum_sequence(sequence):
    local_maximum = sequence[0]
    global_maximum = sequence[0]
    for i in range(1, len(sequence)):
        current_signal = sequence[i]
        local_maximum = max(local_maximum, current_signal + local_maximum)
        global_maximum = max(local_maximum, global_maximum)
    return global_maximum

def max_score_for_patterned_segment(
        data_stream: str, 
        engagement_pattern: str,
        scores: list[int]
        ) -> int:
    meaningful_pattern_positions = kmp_search(data_stream, engagement_pattern)
    positional_patterns = []
    for position in meaningful_pattern_positions:
        positional_patterns.append(maximum_sequence(scores[position:position+len(engagement_pattern)]))
    return max(positional_patterns)

print(max_score_for_patterned_segment(data_stream, engagement_pattern, scores))
print(max_score_for_patterned_segment(data_stream_2, engagement_pattern_2, scores_2))
# print(compute_lps_array(engagement_pattern_2))