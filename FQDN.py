import re


def increment_ip_and_fqdn(ip, fqdn):
    # Extract the last octet of the IP address
    last_octet_ip = int(ip.split('.')[-1])

    # Extract the base part of the FQDN (without the last octet)
    fqdn_base = re.sub(r'\d+\.hytrust\.local$', '', fqdn)

    # Increment the last octet until it reaches 254
    while last_octet_ip < 254:
        last_octet_ip += 1
        new_ip = '.'.join(ip.split('.')[:-1] + [str(last_octet_ip)])
        new_fqdn = fqdn_base + str(last_octet_ip) + '.hytrust.local'

        # Print or process the new IP and FQDN
        print(new_ip, new_fqdn)



# Example usage
original_ip = "10.253.147.99"
original_fqdn = "node-10-253-147-102.hytrust.local"
increment_ip_and_fqdn(original_ip, original_fqdn)