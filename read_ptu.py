

# %%

import numpy as np
import matplotlib.pyplot as plt

import ptufile as pf
import functions.wrappers as funwrap

# %%

# Run this in `2026_FLIM` environment.

# Location of testfile
testfile = "/Users/m.wehrens/Data_notbacked/2026_testdata_lifptu/2026-testmw.ptu"

# Load the testfile, and extract some properties
ptu = pf.PtuFile(testfile)
signal_properties = funwrap.get_signal_properties_from_ptu(ptu)
# Slightly different output with dtime option
ptu = pf.imread(testfile, dtime=0)
    # dtime=0 makes sure that the bins match the measurement window

# Now obtain and show intensity image
thechannel=0
img_intensity = np.sum(ptu[0, :, :, thechannel, :], axis=2)
plt.imshow(img_intensity)

# Now obtain and show trace of whole image
trace_time  = signal_properties['dt'] * np.arange(ptu.shape[4])
trace_decay = np.sum(ptu[0, :, :, thechannel, :], axis=(0, 1))
plt.plot(trace_time,trace_decay)
