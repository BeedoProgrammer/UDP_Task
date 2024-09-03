Implementing a Reliable UDP Communication
Objective: Develop both a server and a client to ensure reliable data transfer over UDP, including handling simulated connection losses.

Steps:

Initialize: Both the server and the client should start with an initial packet number set to 0, representing the last packet received.
Client Request: The client should request the next packet by sending the current packet number to the server.
Server Response: Upon receiving the request, the server should send the packet corresponding to the requested number.
Client Processing: When the client receives the packet, it should increment the packet number and continue the process in a loop.
Connection Loss Simulation: Introduce a mechanism to simulate packet loss or connection drops. The client should be able to detect when a packet is lost and re-request the same packet until it is successfully received. Hint : choose rondomly yo send the packet or not.
Goal: Ensure that each packet is reliably received and acknowledged in the correct sequence, even in the presence of simulated connection losses.
