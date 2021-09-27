# f = open("Nitin.txt", "w")
# a = f.write("Nitin bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("Nitin2.txt", "a")
# a = f.write("Nitin bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("Nitin2.txt", "r+")
print(f.read())
f.write("thank you")

