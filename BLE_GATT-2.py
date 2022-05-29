import pygatt

# The BGAPI backend will attempt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.
# adapter = pygatt.BGAPIBackend()
adapter = pygatt.backends.GATTToolBackend()
try:
    adapter.start()
    device = adapter.connect('60:A4:23:C9:7E:4C')
    value = device.char_read("1800")
    print(value)
finally:
    adapter.stop()