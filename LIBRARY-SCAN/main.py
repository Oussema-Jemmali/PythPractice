from My_Library_Scan import (get_target,get_port_list,port_scanner)
ip=get_target()
list=get_port_list()
port_scanner(ip, list)