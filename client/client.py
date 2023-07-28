import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
sock = context.socket(zmq.REQ)
sock.connect("tcp://localhost:5555")

for request in range(3):
    print(f"Sending request {request} …")
    sock.send(b"Hello")

    #  Get the reply.
    message = sock.recv()
    print(f"Received reply {request} [ {message} ]")
