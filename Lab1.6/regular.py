import re
import ipaddress
import glob

mydir = "C:\\Users\\se.nozhenko\\Seafile\\p4ne_training\\config_files"
file_list = glob.glob(mydir + "\*.txt")
documents = []
for filename in file_list:
    with open(filename) as current_file:
        for line in current_file:
            m = re.search('ip address ((?:[0-9]{1,3}\.?){4}) ((:?[0-9]{1,3}\.?){4})$', line)
            if m:
                print('ip:' , m.group(1))
                print('mask:', m.group(2))
            m1 = re.search('^hostname (.+)', line)
            if m1:
                print('hostname:', m1.group(1))



