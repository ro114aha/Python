input_file = 'c:/_git/Python/source/asa-saj-a.txt'
output_file = 'c:/_git/Python/source/asa-saj-a.csv'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Replace tabs with commas
        line = line.replace('\t', ',')
        outfile.write(line + '\n')

print(f"Conversion complete. Output saved to {output_file}")