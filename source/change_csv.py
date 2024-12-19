# Read the original file
with open('/c:/_git/Python/source/asa-saj-d.txt', 'r') as file:
    lines = file.readlines()

# Process each line and write to a new file
with open('/c:/_git/Python/source/asa-saj-a.txt', 'w') as new_file:
    for line in lines:
        # Replace 'd' with 'a' in the second column
        parts = line.split('\t')
        if len(parts) > 1:
            parts[1] = parts[1].replace('d', 'a')
        
        # Replace 'd01' with 'a01' in the third column
        if len(parts) > 2:
            parts[2] = parts[2].replace('d01', 'a01')
        
        # Write the modified line to the new file
        new_file.write('\t'.join(parts))