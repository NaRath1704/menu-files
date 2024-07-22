import os

def read_memory(start_address, size):
    # Open the /dev/mem file
    with open("/dev/mem", "rb") as mem_file:
        # Seek to the starting address
        mem_file.seek(start_address)
        # Read the specified number of bytes
        data = mem_file.read(size)
        return data

if __name__ == "__main__":
    # Example usage
    start_address = 0x00000000  # Starting address (modify as needed)
    size = 4029  # Number of bytes to read (modify as needed)

    # Ensure the script is run with root privileges
    if os.geteuid() != 0:
        print("This script must be run as root.")
        exit(1)

    # Read memory and print the data
    memory_data = read_memory(start_address, size)
    print(memory_data)

