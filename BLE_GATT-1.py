import BLE_GATT

# ubit_address = "CE, F7, 97, DA, 2E, 91, 4E, A4, A4, 24, F4, 50, 82, AC, 06, 82"

# ubit_address = "60:A4:23:C9:7E:4C"

my_device = BLE_GATT.Central("60:A4:23:C9:7E:4C")

# generic_services = '1800'

# ubit = BLE_GATT.Central(ubit_address)
# ubit.connect()

# print()

my_device.connect()

my_custom_uuid = '1800'
value = my_device.char_read(my_custom_uuid)
my_device.char_write(my_custom_uuid, [255, 255, 0, 123])