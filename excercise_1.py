#Import the library for check IP address
import ipaddress

#------------- Cheking IP ----------------
while (1):
    ip_address = input ("Enter Ip address:")

    try:
        check_ip = ipaddress.ip_address(ip_address)
        break
    except ValueError:
        print ("Invalid IP address format")
        continue
#--------------------------------------------
#----------- Checking netmask ---------------
while (1):
    subnet_mask = input ("Enter subnet mask in decimal format:")
    if (int(subnet_mask[1:])>=0 and int(subnet_mask[1:])<=32) and (subnet_mask[0] == "/" ):
        break
    else:
        print ("Subnet mask is invalid")
        continue
#--------------------------------------------

#---------------- IP Address -----------------
#Split the IP address by "."
sub_ip_add = ip_address.split(".")

#Create an array to save the IP address in binary and decimal format
ip_bin=[]
ip_dec=[]

#create a loop to show each number of the Ip address
for number in sub_ip_add:
    
    #Save the number in decimal format with 10 width of symbols
    ip_dec.append(number);
    #Save the number in binary format with 8bits
    ip_bin.append("{:08b}".format(int(number)));

#Create an array for both types of address
IP_dec_bin=[]
IP_dec_bin.append(ip_dec)
IP_dec_bin.append(ip_bin)

#Loop to print the IP address
for item in IP_dec_bin:
    for item1 in item:
        #Align the output to right
        #Also with "end=''" avoid the "\n" after each call to print
        print("{:>10}".format(item1), end='')
    print ("\n")
#---------------------------------------------

#----------------- Netmask ------------------
#Delete the "/" of the netmask
netmask = subnet_mask[1:]

#Variable to save the netmask in binary format
netmask_bin = ''
#Create an array with the netmask
mask_bin = [1]*int(netmask) + [0]*(32-int(netmask))

#Aux var to set the "." in the netmask
count = 0

#Loop to create the string
for bit in mask_bin:
    count += 1
    #Check if we are at the end of an octect
    if count == 8 or count == 16 or count == 24:
        netmask_bin += str(bit) + "."    
    else:
        netmask_bin += str(bit)
        
#Create an array with the binary subnetmask
subnet_mask_bin = netmask_bin.split(".")

#--------------------------------------------

#---------------- Network address ------------
network_add_bin=[]

#Loop to do the "add" in order to know the network address
for i in range (0,4):
    #we need to do the add with decimal numbers, so we nees convert it
    network_add_bin.append( (int(ip_dec[i])) & (int (subnet_mask_bin[i],2) ) )

#Define the network address
network_address =  str(network_add_bin[0]) + "." + str(network_add_bin[1]) + "." + str(network_add_bin[2]) + "." + str(network_add_bin[3]) 

print ("network address is:" + network_address + subnet_mask)
#---------------------------------------------

#---------------- Broadcast address ----------
#We need to invert the netmask
inv_mask_bin=''

#Var to save the broadcast add
broadcast_add_bin = []

#Set to 0 the aux var
count = 0;

#Loop to invert the bits
for bit in mask_bin:
    count += 1
    if bit == 0:
        inv_mask_bin += "1"
    else:
        inv_mask_bin += "0"
    #Check if we are at the end of an octect
    if count == 8 or count == 16 or count == 24:
        inv_mask_bin += "."
        
#Create an array with the binary subnetmask
inv_subnet_mask_bin = inv_mask_bin.split(".")

for i in range (0,4):
    #we need to do the add with decimal numbers, so we nees convert it
    broadcast_add_bin.append( (int(ip_dec[i])) | (int (inv_subnet_mask_bin[i],2) ) )
broadcast_add = str(broadcast_add_bin[0])+"."+str(broadcast_add_bin[1])+"."+str(broadcast_add_bin[2])+"."+str(broadcast_add_bin[3])

print ("broadcast address is:" + broadcast_add + subnet_mask)
#---------------------------------------------
