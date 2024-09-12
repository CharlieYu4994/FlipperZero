import os

hex_values_256 = [os.urandom(32).hex() for _ in range(11)]

formatted_hex_values_c = []
formatted_hex_values_py = []
for hex_value in hex_values_256:
    formatted_hex_value_c = ', '.join(f'0x{hex_value[i:i+2]}' for i in range(0, len(hex_value), 2))
    formatted_hex_values_c.append(f"{{{formatted_hex_value_c}}}")
    formatted_hex_value_py = ', '.join(f'0x{hex_value[i:i+2]}' for i in range(0, len(hex_value), 2))
    formatted_hex_values_py.append(f"[{formatted_hex_value_c}]")

formatted_output_c = ',\n    '.join(formatted_hex_values_c)
formatted_output_py = ',\n    '.join(formatted_hex_values_py)
print(formatted_output_c)
print('-----------py-----------')
print(formatted_output_py)
