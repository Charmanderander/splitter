import csv
import os
from collections import Counter, defaultdict

directory = "C:\Users\Chan Family\Desktop\merger"

entries = []
people = []
receiver_list = defaultdict(list)
index = 0

# Going through each file in the folder
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(filename,'r') as csvfile:
            header = 1
            reader = csv.reader(csvfile, delimiter="\t")
            for row in reader:
                if header == 1:
                    header = 0
                    continue
                entries.append(row)
                people.append(row[1])
                people.append(row[2])

            # Finding the seed
            count = Counter(people)
            seed = count.most_common(1)[0][0]

            # Finding the communications with the seed
            for entry in entries:
                if entry[1] == seed:
                    receiver = entry[2]
                else:
                    receiver = entry[1]

                receiver_list[receiver].append(index)
                index += 1
        continue
    else:
        continue

# Writing results to file
for key in receiver_list:
    f = open("text_" + key+".csv", "wb")
    writer = csv.writer(f)
    for entry in receiver_list[key]:
        writer.writerow(entries[entry])
    f.close()
