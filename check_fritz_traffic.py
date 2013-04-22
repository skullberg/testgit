#!/usr/bin/python
import sys
from SOAPpy import SOAPProxy

server = SOAPProxy(proxy='http://fritz.box:49000/upnp/control/WANCommonIFC1',
	namespace ='urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1',
	soapaction='urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#GetAddonInfos',
	noroot=True)
#	server.config.dumpSOAPOut = 1
#	server.config.dumpSOAPIn = 1
traffic =  server.GetResponse()
#warn,crit,min,max


if traffic == None:		#dummy
    	print "Err - traffic " 
    	sys.exit(2)
else:
	ByteSendRate=traffic['NewByteSendRate']
	TotalBytesSent=traffic['NewTotalBytesSent']
	ByteReceiveRate=traffic['NewByteReceiveRate']
	PacketReceiveRate=traffic['NewPacketReceiveRate']
	TotalBytesReceived=traffic['NewTotalBytesReceived']
	PacketSendRate=traffic['NewPacketSendRate']

	perfdata= "| "+ "ByteSendRate=" + ByteSendRate + "B;0;0;0;633000" + " ByteReceiveRate=" + ByteReceiveRate + "B;0;0;0;6780000"
	perfdata+= " PacketSendRate=" + PacketSendRate + ";0;0;0;1000" + " PacketReceiveRate=" + PacketReceiveRate + ";0;0;0;1000"
	perfdata+= " TotalBytesSent=" + TotalBytesSent + "c;0;0;0;0" + " TotalBytesReceived=" + TotalBytesReceived + "c;0;0;0;0"
    	print "OK - Traffic: " + repr(int(ByteSendRate)/1000)+ "/" + repr(int(ByteReceiveRate)/1000) + " kByte/s" + perfdata
    	sys.exit(0)

sys.exit(0)

# TODO
# unknown state
# warning,critial level

