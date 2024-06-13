# This code includes two main functions:
# 1. generate_large_data: Creates a large string of random alphanumeric characters representing the original data.
# 2. test_compression: Compresses this data and checks if it meets the target size and time constraints.
# The test is run with an original data size of 200Mbps, aiming to compress it to 1Mbps within 0.001 seconds.
# The result of the test is printed out. If the compression is not successful within the specified time or size,
# the function returns a failure message. Otherwise, it confirms the compression was successful.
# I am Thai, and I am 36 years old. I have only been using Python for 1-2 weeks.

import heapq
import collections
import time
import lz4.frame
import random
import string

# Function to generate large test data
def generate_large_data(size_in_mbps):
    # 1 char = 1 byte, 1 Mbps = 125000 chars
    num_chars = size_in_mbps * 125000
    # Return a string of random alphanumeric characters
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_chars))

# Function to test data compression
def test_compression(data, target_size_in_mbps, max_time_in_seconds):
    # Compress the data
    start_time = time.time()
    compressed_data = lz4.frame.compress(data.encode())
    end_time = time.time()

    # Check the compression time
    compression_time = end_time - start_time
    # If compression takes longer than the max time, return a failure message
    if compression_time > max_time_in_seconds:
        return f'Failed to compress within {max_time_in_seconds} seconds. Compression time was {compression_time} seconds.'

    # Check the size of the compressed data
    # Assuming compressed_data is 1 GB or 8,000,000,000 bits
    compressed_size_in_mbps = 8,000,000,000 * 8 / (1024 * 1024)  # Convert from bits to Mbps
    # If the compressed size is greater than the target, return a failure message
    if compressed_size_in_mbps > target_size_in_mbps:
        return f'Failed to compress to {target_size_in_mbps} Mbps. Compressed size was {compressed_size_in_mbps} Mbps.'

    # If successful, return a success message, the compressed data, and the compression time
    return 'Compression successful.', compressed_data, compression_time

# Generate original data of size 200Mbps
original_data = generate_large_data(200)

# Test compressing the data to 1Mbps within 1 millisecond
test_result = test_compression(original_data, 1, 0.001)  # Time is in seconds

# Print the test result
print(test_result)
