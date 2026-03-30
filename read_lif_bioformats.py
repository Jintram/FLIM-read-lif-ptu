

# %% 

# Run this in `2026_bioformats` environment.

# %% 

import os
os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/jdk-26.jdk/Contents/Home"

import javabridge
import bioformats
import numpy as np

# %% 

# Can read in files, but 
# "SizeT=1, SizeC=4, SizeZ=1, SizeX=512, SizeY=512"
# So don't have access to time-binned data.

javabridge.start_vm(class_path=bioformats.JARS)

testfilepath = "/Users/m.wehrens/Data_notbacked/2026_testdata_lifptu/2026-testmw.lif"

metadata = bioformats.get_omexml_metadata(testfilepath)
# Parse metadata to find FLIM dimensions (SizeC, SizeT, etc.)

img = bioformats.load_image(testfilepath, series=0, rescale=False)
# For multi-dimensional data, use ImageReader for more control:

with bioformats.ImageReader(testfilepath) as reader:
    # Read individual planes (c=channel, z=z-slice, t=time-bin)
    plane = reader.read(c=0, z=0, t=0, series=0, rescale=False)
    

# Parse metadata to find dimensions for the series of interest
ome = bioformats.OMEXML(metadata)
series_index = 0
pixels = ome.image(series_index).Pixels
size_t = pixels.SizeT  # often holds FLIM time bins
size_c = pixels.SizeC  # sometimes time bins are stored here instead
size_z = pixels.SizeZ
print(f"SizeT={size_t}, SizeC={size_c}, SizeZ={size_z}, SizeX={pixels.SizeX}, SizeY={pixels.SizeY}")

# Read all time bins (adjust dimension depending on where FLIM bins are stored)
# If time bins are in T dimension:
with bioformats.ImageReader(testfilepath) as reader:
    planes_t = np.stack([
        reader.read(c=0, z=0, t=t, series=series_index, rescale=False)
        for t in range(size_t)
    ])
    print(f"Shape (from T): {planes_t.shape}")  # (n_timebins, Y, X) or (n_timebins, Y, X, C)

# If time bins are in C dimension instead (common in some Leica FLIM files):
# with bioformats.ImageReader(testfilepath) as reader:
#     planes_c = np.stack([
#         reader.read(c=c, z=0, t=0, series=series_index, rescale=False)
#         for c in range(size_c)
#     ])
#     print(f"Shape (from C): {planes_c.shape}")

javabridge.kill_vm()