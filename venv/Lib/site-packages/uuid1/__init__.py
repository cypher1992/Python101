from .utils import *
from datetime import datetime
import random
import uuid
	
def uuid1():
	return from_dt(datetime.utcnow())
	
def from_dt(dt):

	# Generate the time based part of the UUID
	time_low, time_mid, time_hi_version = utils.get_time_based_blocks(dt, random.randint(0, 10000))
	
	# Get the clock seq and node value
	clock_seq_hi_variant, clock_seq_low, node = utils.get_clock_seq_and_node()
	
	return uuid.UUID(fields=(time_low, time_mid, time_hi_version, clock_seq_hi_variant, clock_seq_low, node))

def max(dt):

	# Generate the time based part of the UUID
	time_low, time_mid, time_hi_version = utils.get_time_based_blocks(dt, 9999)
	
	return uuid.UUID(fields=(time_low, time_mid, time_hi_version, 0xFF, 0xFF, 0xFFFFFFFFFFFF))
	
def min(dt):

	# Generate the time based part of the UUID
	time_low, time_mid, time_hi_version = utils.get_time_based_blocks(dt, 0)
	
	return uuid.UUID(fields=(time_low, time_mid, time_hi_version, 0x00, 0x00, 0x000000000000))
