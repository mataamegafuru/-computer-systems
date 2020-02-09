import math
import os.path

file_name = input("Enter file name: ")
with open(file_name, 'rb') as text:
    string = text.read()
    freq = {}
    for i in string:
        freq[i] = string.count(i)/len(string)

    for key in freq.keys():
        print(f"{key}: %.10f" % freq[key])

    print("Total symbols: " + str(len(string)))

    entropy = 0
    for i in freq:
      entropy+= -(freq[i] * math.log(freq[i], 2))
    print("Entropy: ", entropy)
    inform = (entropy * len(string))/8
    print("The quantity of information: ", inform, "\nFile size: ", os.path.getsize(file_name))

