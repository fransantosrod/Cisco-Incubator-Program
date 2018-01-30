#Library to create a RegEx
import re
#Library to know the commons elements
import collections

#Open the file "reading" mode
file = open ("commands.txt", "r")

#Create the RegEx
command_pattern = re.compile('(switchport trunk allowed vlan)(.)(.*)')

#Array to save the vlans of the commands
vlans_id = []
#Array yo save the number of correct commands
commands = []

#Loop to read the file
for line in file:
    
    #Looking for the pattern
    correct_command = command_pattern.search(line)
    
    #If we detect any command that is similar to the RegEx
    if correct_command:
        #Save the 3th group (VLANS of the commands) in our RegEx
        vlans_id.extend(correct_command.group(3).split(','))
        #Save the correct command
        commands.append(correct_command.group(0));
    else:
        continue
        
#Close the file
file.close()

commons_vlans = []
unique_vlans = []

#Looking for the duplicates entries
for vlan, count in collections.Counter(vlans_id).items():
    if count > len(commands)-1:
        commons_vlans.append(int(vlan))
    else:
        unique_vlans.append(int(vlan))
        
commons_vlans.sort()
commons_vlans = str(commons_vlans)
unique_vlans.sort()
unique_vlans = str(unique_vlans)

print ("List_1=" + commons_vlans)
print ("List_2=" + unique_vlans)