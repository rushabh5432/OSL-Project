#!/usr/bin/perl
#tcpclient.pl

use IO::Socket::INET;

# flush after every write
$| = 1;

my ($socket,$client_socket);

# creating object interface of IO::Socket::INET modules which internally creates 
# socket, binds and connects to the TCP server running on the specific port.
$socket = new IO::Socket::INET (
PeerHost => '127.0.0.1',
PeerPort => '5000',
Proto => 'tcp',
) or die "ERROR in Socket Creation : $!\n";

print "TCP Connection Success.\n";

# read the socket data sent by server.
# we can also read from socket through recv()  in IO::Socket::INET
# $socket->recv($data,1024);

# write on the socket to server.
# we can also send the data through IO::Socket::INET module,
while(1) {
	print "\nClient :  ";
	$temp = <>;
    $socket->send($temp);
	sleep (1);
	$socket->recv($data,1024);
	print "\nServer : $data ";		
}
$socket->close();
