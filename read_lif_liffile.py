


# %%
#
# liffile is also made by Christoph Gohlke from Phasorpy
# it explicitly mentions that it doesn't support reading "non-image data such as FLIM/TCSPC"
# https://github.com/cgohlke/liffile


# Run this in `2026_FLIM` environment.

from liffile import LifFile

testfilepath = "/Users/m.wehrens/Data_notbacked/2026_testdata_lifptu/2026-testmw.lif"
lif = LifFile(testfilepath)

for image in lif.images:
    _ = image.name
    
image = lif.images['Fast Flim']  # by name
assert image.dtype == 'float16'
assert image.sizes == {'Y': 1024, 'X': 1024}
lifetimes = image.asxarray()

lifetimes




