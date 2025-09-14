import msg_packed.msgpack as msgpack
with open("challenge.mp", "rb") as data_file:
    byte_data = data_file.read()
print(msgpack.unpackb(byte_data))