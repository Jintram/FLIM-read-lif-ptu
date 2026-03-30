



# %% Trying with readlif

# Run this in `2026_FLIM` environment.

# Seems to work somewhat, but 
# (a) there doesn't appear to be data with correct dimensions
# (b) there seems to be a bug when using `lif.get_image(1)` -- lif.get_image(1) did work


from readlif.reader import LifFile
import numpy as np

import matplotlib.pyplot as plt

testfilepath = "/Users/m.wehrens/Data_notbacked/2026_testdata_lifptu/2026-testmw.lif"

lif = LifFile(testfilepath)

# List all image series in the file
for i, image in enumerate(lif.get_iter_image()):
    print(f"Series {i}: {image.name}, dims: {image.dims}")
    # dims is a named tuple with x, y, z, t, m (channels), etc.

# Get a specific series
img = lif.get_image(1)

# Read frames into numpy — FLIM time bins often appear along the t or m axis
frames = [np.array(frame) for frame in img.get_iter_t()]  # or get_iter_c()
stack = np.stack(frames)

plt.imshow(stack)