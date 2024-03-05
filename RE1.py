import re

original_fqdn = "node-10-253-147-102.hytrust.local"
fqdn_base = re.sub(r'\d+\.hytrust\.local$', '',original_fqdn)
print(fqdn_base)