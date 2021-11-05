

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

while True:
    for i in range(0, 180, 1):
        kit.servo[0].angle = i
        time.sleep(.05)

    for i in range(180,0 , -1):
        kit.servo[0].angle = i
        time.sleep(0.05)
