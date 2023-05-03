# Email Address Sort

# Opens the File Containing the List of Email Addresses to Sort
f = open("C:/Users/redho/OneDrive/emailaddresses.txt", "r")

# Reads the file and adds each line's contents into a list called "all", ommiting commas and new-line characters
all = list()
for l in f:
    r = l.replace(",", "")
    r = r.replace("\n", "")
    all.append(r)

# A Dictionary containing lists of emails of the same domain. The key is the common domain address  of the list
emailsbydomains = dict()

for m in all:
    parts = m.split("@")
    if len(parts) != 2:
        print("Error on line: '" + str(m) + "'")
        exit(1)
    
    domain = parts[1]

    if(domain not in emailsbydomains.keys()):
        emailsbydomains[domain] = list()
    
    emailsbydomains[domain].append(m)

for k in emailsbydomains.keys():
    print(k + ":")
    for addr in emailsbydomains[k]:
        print("\t* " + addr)
    print()