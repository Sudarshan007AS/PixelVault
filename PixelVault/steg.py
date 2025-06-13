from PIL import Image

def encode_text_into_image(image_path, secret_text):
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    pixels = img.load()

    binary_text = ''.join(format(ord(char), '08b') for char in secret_text)
    text_length = len(secret_text)
    binary_length = format(text_length, '032b')  # 32 bits for message length
    full_binary = binary_length + binary_text
    total_bits = len(full_binary)

    if total_bits > width * height * 3:
        raise ValueError("Message too long to encode in image.")

    idx = 0
    for y in range(height):
        for x in range(width):
            if idx >= total_bits:
                break
            r, g, b = pixels[x, y]
            rgb = [r, g, b]
            for i in range(3):
                if idx < total_bits:
                    rgb[i] = (rgb[i] & ~1) | int(full_binary[idx])
                    idx += 1
            pixels[x, y] = tuple(rgb)
        if idx >= total_bits:
            break

    output_path = 'static/encoded_image.png'
    img.save(output_path)
    return output_path


def decode_text_from_image(image_path):
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    pixels = img.load()

    total_pixels = width * height
    total_bits = total_pixels * 3

    all_bits = ''
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            all_bits += str(r & 1)
            all_bits += str(g & 1)
            all_bits += str(b & 1)

    # Extract the first 32 bits for length
    msg_length_bits = all_bits[:32]
    msg_length = int(msg_length_bits, 2)

    message_bits = all_bits[32:32 + msg_length * 8]
    if len(message_bits) < msg_length * 8:
        raise ValueError("Encoded message is corrupted or incomplete.")

    byte_data = bytearray()
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i+8]
        byte_data.append(int(byte, 2))

    try:
        return byte_data.decode('utf-8')
    except UnicodeDecodeError:
        return "[Error] Could not decode message. Possibly corrupted or non-UTF8 text."
