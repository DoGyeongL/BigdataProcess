import sys

def process_uber_data(input_file, output_file):
    region_day_data = {}

    # Read data from the input file
    with open(input_file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            region, date, vehicles, trips = data[0], data[1], int(data[2]), int(data[3])
            day = date.split('/')[1]  # Extract the day from the date

            # Combine region and day as a key
            key = f"{region},{day}"

            # Update the dictionary with vehicles and trips information
            if key in region_day_data:
                region_day_data[key][0] += vehicles
                region_day_data[key][1] += trips
            else:
                region_day_data[key] = [vehicles, trips]

    # Write the result to the output file
    with open(output_file, 'w') as output:
        for key, value in region_day_data.items():
            region, day = key.split(',')
            vehicles, trips = value
            output.write(f"{region},{day} {vehicles},{trips}\n")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 UBERStudent<Your ID>.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_uber_data(input_file, output_file)
    print("Data processed successfully. Results written to", output_file)
