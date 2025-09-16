# The IP addresses to be removed
remove_list = ["192.168.99.1", "192.168.99.2", "192.168.99.3"]

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Open the file and read its contents into a string
# The `with` statement ensures the file is automatically closed.
# The "r" argument opens the file in read mode.
with open(import_file, "r") as file:
    # Use .read() to read the imported file and store it in a variable named ip_addresses
    ip_addresses = file.read()

# Use .split() to convert the string of IP addresses into a list
# By default, .split() separates the string by whitespace
ip_addresses = ip_addresses.split()

# Iterate through the IP addresses in the `remove_list`
for element in remove_list:
    # Create a conditional statement to check if the IP address from the `remove_list` is in the `ip_addresses` list
    if element in ip_addresses:
        # Use the .remove() method to remove the matching IP address from the `ip_addresses` list
        ip_addresses.remove(element)

# Convert the revised list of IP addresses back into a string
# The `\n` character places each IP address on a new line
ip_addresses = "\n".join(ip_addresses)

# Open the file again, this time in write mode ("w")
# This will overwrite the existing contents of the file
with open(import_file, "w") as file:
    # Use the .write() method to write the updated string back to the file
    file.write(ip_addresses)