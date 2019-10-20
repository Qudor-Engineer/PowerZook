#!/usr/bin/env python3
'''
 This software is to retrieve the values of current (AMP) and power (watt)
 from Jacarta powerZook meter (https://www.jacarta.com/powerzook/)
 through network using SNMP protocol.
 This software is developed by: Khudhur Alfarhan   Qudoren@gmail.com
                         and: Dr. Ammar Zakaria
 This software is developed by Ideria company and lisenced under GPL 3.0
 October 2019
'''
from easysnmp import snmp_walk
from time import sleep

hostIP = '192.168.1.200'
# List of powerZook OIDs the first one is of electrical current OIDs second one is of power value
oids = ['.1.3.6.1.4.1.19011.1.3.5.1.3.1', '.1.3.6.1.4.1.19011.1.3.5.1.3.2']


# retrieve the values from the Jacarta powerZook meter using SNMP protocol
def retrieve_measurements(_oid):
    # Perform an SNMP walk
    return snmp_walk(oids=_oid, hostname=hostIP, community='public', version=1, timeout=3,
                  retries=5, remote_port=161, use_long_names=True, retry_no_such=True, abort_on_nonexistent=True)


if __name__ == "__main__":
    print("Retrieve the measurements from Jacarta powerZook meter")
    while True:
        values = retrieve_measurements(oids) # get electrical current and power value from powerZook
        current = int(values[0].value) / 1000
        power = values[1].value
        print("Current = {} (Amp)".format(current))
        print("Power = {} (Watt)".format(power))
        print("===========================================")
        sleep(2)
