#Import the RegEx library
import re
# Template for the interface type

access_template = ['switchport mode access',

'switchport access vlan {}',

'switchport nonegotiate',

'spanning-tree portfast',

'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

'switchport mode trunk',

'switchport trunk allowed vlan {}']


int_type_pattern = re.compile(r'(Fa|Gi|Po|Se)(\d)((/)(\d){1,2}){1,2}')

#Loop to request information
while (1):
    
    interface_mode = input ("Enter interface mode(access/trunk)");
    #Check that the mode is the correct
    if ((interface_mode == "access") or (interface_mode == "trunk")):
        
        #Loop to the interface type and number
        while (1):
            #Request the information
            interface_type = input ("Enter interface type and number:")
            interface_type_check = int_type_pattern.search(interface_type)
            
            #If the interface type is correct...
            if interface_type_check:
                
                #Check if the mode is access
                if (interface_mode == "access"):
                    #Loop to request the VLAN id
                    while (1):
                        vlan_id = input("Enter VLAN number:")
                        #Check if the VLAN id is correct
                        if (int(vlan_id) > 0 and int(vlan_id)<=4096):
                            access_template[1] = access_template[1].format(str(vlan_id)) 
                            
                            #Loop to print the results
                            print ("Interface " + interface_type)
                            for element in access_template:
                                print (element)
                            break
                        else:
                            print ("Invalid VLAN number")
                            continue
                    
                #If the mode is trunk...
                else:
                    #Request the VLANs allowed group
                    vlan_group = input ("Enter allowed VLANs")
                    trunk_template[2] = trunk_template[2].format (vlan_group)
                          
                    print ("Interface " + interface_type)
                    #Loop to print the results
                    for element in trunk_template:
                        print (element)
                break
            else:
                print ("Invalid interface type or number")
                continue
        break
    else:
        print ("Invalid interface mode")
        continue