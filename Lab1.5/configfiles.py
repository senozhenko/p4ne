import glob
mydir = "C:\\Users\\se.nozhenko\\Seafile\\p4ne_training\\config_files"
file_list = glob.glob(mydir + "\*.txt")
documents = []
for filename in file_list:
    with open(filename) as current_file:
        for line in current_file:
            if line.find("ip address") != -1:
                line2 = line.replace("ip address", "").strip()
                documents.append(line2)

print(documents)
