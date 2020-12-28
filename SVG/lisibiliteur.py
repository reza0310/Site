with open("C:\\Users\\dupre\\OneDrive\\Bureau\\svg de base.txt", "r") as logo:
    logo = logo.readlines()
    logo_origin = logo.copy()
    logo.clear()
    for l in logo_origin:
        buffer = "<"
        for c in l[1:]:
            if c == "<":
                logo.append(buffer+"\n")
                buffer = "<"
            elif c == "\n":
                logo.append(buffer+"\n")
                buffer = ""
            else:
                buffer += c
    logo.append(buffer+"\n")
print("\n\n")
for l in logo:
    print(l)
with open("C:\\Users\\dupre\\Downloads\\svg de base.svg", "w") as log:
    log.writelines(logo)
print("Travail terminé")