#Import the library for RegEx
import re
#Library to know the commons elements
import collections

#Open the file
file = open ("ShowIpRoute.txt", "r")

#Create the RegEx
route_pattern = re.compile (r'(?P<Pr>\D.*) (?P<Pre>\b\d[\d|\.]+\d\b) (?P<AD>.*) via (?P<Nhop>\b\d[\d|\.]+\d\b).* (?P<LU>\b\d[\d|\:]+\d\b), (?P<Oint>.*)')

#Dictionary with the dynamic routes
dict_protocol ={'R':'RIP', 'M':'mobile', 'B':'BGP','D':'EIGRP', 'EX':'EIGRP external', 'O':'OSPF', 'IA':'OSPF inter area',      
               'N1':'OSPF NSSA external type 1', 'N2':'OSPF NSSA external type 2', 'E1':'OSPF external type 1', 
               'E2':'OSPF external type 2', 'i':'IS-IS', 'su':'IS-IS summary', 'L1':'IS-IS level-1','L2':'IS-IS level-2',
       'ia':'IS-IS inter area', 'H':'NHRP'}


route_info_pattern = []
routes_info = []

for line in file:
        
        #Dictionary to save the routes
        routes_info_dict = {}
        #Looking for the RegEx
        route_info_pattern = route_pattern.search(line)      
        
        if route_info_pattern:
            #Save the data in the dictionary
            routes_info_dict['protocol'] = route_info_pattern.group(1)
            routes_info_dict['prefix'] = route_info_pattern.group(2)
            routes_info_dict['metric-ad'] = route_info_pattern.group(3)
            routes_info_dict['next-hop'] = route_info_pattern.group(4)
            routes_info_dict['updates'] = route_info_pattern.group(5)
            routes_info_dict['intf'] = route_info_pattern.group(6)
        else:
            continue
        #Save the dictionary into a table
        routes_info.append(routes_info_dict)
#Close the file
file.close()

protocol_section = []
protocol = []
index = []
#Loop to split the protocols
for protoc in routes_info:
    protocol_section.append(protoc['protocol'].split())

#Loop to convert the protocol
j=0
for sect,row in zip(protocol_section, routes_info):
    i=0
    for row in sect:
        if row in dict_protocol:
            #Convert the protocol with the dictionary
            protocol_section[j][i] = dict_protocol[row] 
            index.append(j)
        i += 1
    j += 1

index_s = []

#Looking for the duplicates entries
for indx, count in collections.Counter(index).items():
    if count >= 1:
        index_s.append(int(indx))
#Loop to print the dynaminc routes
for j in index_s:
        
        print ('-----------------------------------------------')
        print ('Protocol:', end='')
        
        for  i in range(0, len(protocol_section[j])):
            print ('{0:>18}'.format(protocol_section[j][i]) + "\t", end='')
        
        print ("\n")

        print ('Prefix: {0:>24}'.format(routes_info[j]['prefix']), end='')
        print ("\n")
        print ('AD/Metric: {0:>18}'.format(routes_info[j]['metric-ad']))
        print ('Next-Hop: {0:>24}'.format(routes_info[j]['next-hop']))
        print ('Last Update: {0:>16}'.format(routes_info[j]['updates']))
        print ('Outbound interface: {0:>12}'.format(routes_info[j]['intf']))
       
        print ('-----------------------------------------------')
        print("\n")