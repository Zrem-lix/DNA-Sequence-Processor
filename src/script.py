# NAME: Angel Rivera

def load_data(file_name):
    """
    Load data from the input file containing DNA sequences.
    
    file_name (str): Name of the input file.
    
    Returns:
    list: A list of strings representing DNA sequences.
    """
    sequences = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if not line.startswith(">"):
                sequence = line.strip()
                sequences.append(sequence)
    return sequences

def count_nucl_freq(data):
    """
    Count the frequency of each nucleotide at each position in the DNA sequences.
    
    data (list): List of strings representing DNA sequences.
    
    Returns:
    dict: A dictionary where keys are positions in the DNA sequences
          and values are dictionaries with the frequency of each nucleotide ('A', 'C', 'G', 'T').
    """
    frequency_dict = {}
    sequence_length = len(data[0])
    
    for i in range(sequence_length):
        frequency_dict[i] = {'A': 0,
                             'C': 0,
                             'G': 0,
                             'T': 0
        }
        
    for sequence in data:
        index = 0
        for nucleotide in sequence:
            frequency_dict[index][nucleotide] += 1
            index += 1
            
    return frequency_dict

def find_consensus(frequency_data):
    """
    Find the consensus sequence based on the frequency of nucleotides at each position.
    
    frequency_data (dict): Dictionary containing the frequency of nucleotides at each position.
    
    Returns:
    str: The consensus sequence.
    """
    consensus_sequence = ""
    for counts in frequency_data.values():
        max_count = 0
        most_common_nucleotide = ''
        for nucleotide, count in counts.items():
            if count > max_count:
                max_count = count
                most_common_nucleotide = nucleotide
        consensus_sequence += most_common_nucleotide
        
    return consensus_sequence

def sort_counts_by_frequency(counts):
    """
    Sorts counts by frequency in descending order.
    
    counts (dict): Dictionary containing nucleotide counts.
    
    Returns:
    list: List of tuples (nucleotide, frequency) sorted by frequency in descending order.
    """
    # Convert the dictionary items to a list of tuples
    counts_list = list(counts.items())
    
    # Define a custom sorting function
    def sort_by_frequency(item):
        return item[1]
    
    # Sort the list of tuples by frequency in descending order
    sorted_counts = sorted(counts_list, key=sort_by_frequency, reverse=True)
    
    return sorted_counts

def process_results(frequency_data, output_filename):
    """
    Process the results, including the consensus sequence and the frequency of nucleotides at each position,
    and save them to an output file.
    
    frequency_data (dict): Dictionary containing the frequency of nucleotides at each position.
    output_filename (str): Name of the output file where the results will be saved.
    """
    consensus_sequence = find_consensus(frequency_data)
    print("Consensus:", consensus_sequence)
    
    with open(output_filename, 'w') as output_file:
        output_file.write("Consensus: " + consensus_sequence + '\n')
        for index, counts in frequency_data.items():
            sorted_counts = sort_counts_by_frequency(counts)
            output_file.write(f"Pos {index + 1}: ")
            for nucleotide, frequency in sorted_counts:
                output_file.write(f"{nucleotide}:{frequency}\t")
            output_file.write("\n")

def main():
    """
    Main function that coordinates the processing of DNA sequences.
    """
    INPUT_FILE = "DNAInput.txt"  # Input file containing DNA sequences.
    OUTPUT_FILE = "DNAOutput.txt"  # Output file where the results will be saved.
    
    sequences = load_data(INPUT_FILE)  # Load DNA sequences from the input file.
    frequency_data = count_nucl_freq(sequences)  # Calculate the frequency of nucleotides at each position.
    process_results(frequency_data, OUTPUT_FILE)  # Process the results and save them to the output file.
    
if __name__ == "__main__":
    main()
