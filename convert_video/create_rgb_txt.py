#!/usr/bin/env python3

import sys
from glob import glob

if len(sys.argv) < 4:
    print(
        "./create_rgb_txt <input image sequence> <output rgb.txt path> <fps> [image file extension]"
    )
    sys.exit()

input_path = sys.argv[1]
output_path = sys.argv[2]
fps = int(sys.argv[3])
extension = sys.argv[4] or "jpg"
time_delta = 1 / fps
start_time = 0

lines = []
for i, path in enumerate(glob(f"{input_path}/*.{extension}")):
    lines.append(f"{start_time + time_delta * i} {path}")

with open(output_path, "w") as f:
    for line in lines:
        f.write(f"{line}\n")

print(f"Successfully wrote to '{output_path}'")
