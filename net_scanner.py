import scapy.all as scapy
import optparse
#Arp request
def get_user_input():
	parse_object=optparse.OptionParser()
	parse_object.add_option("-i","--ip",dest="ip_address",help="use -i for write your ip.")
	(user_input,arguments) = parse_object.parse_args()
	if not user_input.ip_address:
		print("Enter ip address")
	return user_input
def search_ip(ip):
	arp_request_packet  = scapy.ARP(pdst=ip)
	brodcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	combined_packet = brodcast_packet/arp_request_packet
	(answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
	answered_list.summary()
user_ip_address = get_user_input()
search_ip(user_ip_address.ip_address)
