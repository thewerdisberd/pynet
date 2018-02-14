# Pynet
Network clients written in python, used to view the raw data sent by servers to clients.

# Features

* Basic HTTP GET and POST Requests
* UDP and TCP Clients
* DNS Client

# Usage:
Pynet is intended to be imported into other programs as a class. However support has been added to run pynet as a standalone program.

pynet.py -c client type -h host -p port [-u uri -d data]
* When using dns clients, use the -h argument for the query

Available Client Types:

tcp_client, udp_client, http_get, http_post, fdns_client, rdns_client

# TODO

* Support for TCP and UDP servers
* Ability to add extra headers to HTTP Requests
* Have except statements raise errors so they can be handled outside of the class
