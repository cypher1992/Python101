import random
import sys
import socket
import hashlib
from datetime import datetime

def make_node():

	# The RFC4122 spec says that if it's not possible to get the MAC addresses of the host
	# one option is to take as many information that identify this node and hash them together.
	# The IP address of the node is useful for this purpouse.
	ip_address = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
			
	hash = md5_hash(ip_address)
	node = 0
	for i in range(min(6, len(hash))):
		if type(hash[i]) is int:
			node |= (0x00000000000000ff & hash[i]) << (5 - i) * 8
		else:
			node |= (0x00000000000000ff & ord(hash[i])) << (5 - i) * 8

	# As we don't use the mac address, the multicast bit must be 1
	return node | 0x0000010000000000
	
def md5_hash(ip_address):
	hash = hashlib.md5()
	hash.update(ip_address.encode('utf-8'))		
	return hash.digest()	
	
def digits(value, bytes_nr):
    return value & digits_masks[bytes_nr]
	
def datetime_to_nanos(dt):
	delta = dt - epoch
	return (delta.days * 86400 + delta.seconds) * 10000000 + (delta.microseconds * 10)
	
def get_time_based_blocks(dt, nanos_to_add):

	# Convert millis to nanos
	nanos = datetime_to_nanos(dt)
    
	# Add random nanoseconds
	if (nanos_to_add > 0):
		nanos += nanos_to_add
		
	return digits(nanos >> 32, 8), digits(nanos >> 16, 4), digits(nanos, 4)

def get_clock_seq_and_node():

	clock = random.randint(0, sys.maxsize)	
	clock_seq_and_node = 0
	clock_seq_and_node |= 0x8000000000000000 # Variant
	clock_seq_and_node |= (clock & 0x0000000000003FFF) << 48
	clock_seq_and_node |= _node

	return digits(clock_seq_and_node >> 56, 2), digits(clock_seq_and_node >> 48, 2), digits(clock_seq_and_node, 12)
	
_node = make_node()
epoch = datetime(1970, 1, 1)
digits_masks = { 2: 0xFF, 4: 0xFFFF, 8: 0xFFFFFFFF, 12: 0xFFFFFFFFFFFF }