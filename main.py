
#!/usr/bin/env python
import numpy as np
import sys
import cv2

data = sys.stdin.buffer.read()
image = np.frombuffer(data, dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow('stdin Image', image)
cv2.waitKey()