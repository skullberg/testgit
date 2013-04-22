#!/usr/bin/python
import sys
from SOAPpy import SOAPProxy

server = SOAPProxy(proxy='http://fritz.box:49000/upnp/control/WANCommonIFC1',
	namespace ='urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1',
	soapaction='urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#GetCommonLinkProperties',
	noroot=True)
#	server.config.dumpSOAPOut = 1
#	server.config.dumpSOAPIn = 1
interface =  server.GetResponse()
#print interface
NewPhysicalLinkStatus = interface['NewPhysicalLinkStatus']
#warn,crit,min,max


if  NewPhysicalLinkStatus != 'Up':
    	print "Err - Link Down | UpLink=0;0;0;0;0 DownLink=0;0;0;0;0" 
    	sys.exit(2)
else:
	NewLayer1DownstreamMaxkBitRate = int(interface['NewLayer1DownstreamMaxBitRate'])/1000
	NewLayer1UpstreamMaxkBitRate = int(interface['NewLayer1UpstreamMaxBitRate'])/1000
	perfdata= "| "+ "UpLink=" + repr(NewLayer1UpstreamMaxkBitRate) + ";0;0;0;1000" + " DownLink=" + repr(NewLayer1DownstreamMaxkBitRate) + ";0;0;0;10000" 
    	print "OK - Link Up "+ repr(NewLayer1UpstreamMaxkBitRate) + "/" + repr(NewLayer1DownstreamMaxkBitRate) +" kbit" + perfdata
    	sys.exit(0)

sys.exit(0)

# TODO
# unknown state
# warning,critial level

