import json

# File path for the rules text file
input_file = "swiftlint_rules.txt"
output_file = "swiftlint_rules.json"

# Initialize an empty list to hold the parsed rules
rules = []

# Open and read the file
with open(input_file, "r") as file:
    # Skip the header line
    headers = file.readline().strip().split("|")
    
    # Process each line after the header
    for line in file:
        # Split line into columns based on tabs
        columns = line.strip().split("|")
        
        # Create a dictionary for each rule, matching columns to headers
        rule = dict(zip(headers, columns))
        
        # Append the rule dictionary to the list of rules
        rules.append(rule)

# Write the structured data to a JSON file
with open(output_file, "w") as json_file:
    json.dump(rules, json_file, indent=2)

print(f"Rules successfully parsed and saved to {output_file}")
