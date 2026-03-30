

# Installation

### Environment 1, for readlif, ptufile, liffile

```bash
# Create & activate environment with conda
conda create -n 2026_FLIM
conda activate 2026_FLIM

# install "readlif" (conda-forge)
conda install -c conda-forge readlif 

# Install ptu file
# https://pypi.org/project/ptufile/
python -m pip install -U "ptufile[all]"

# Install liffile
pip install liffile
```

### Second environment, that handles bioformats

This cannot be combined with readlif..

Note: `python-javabridge` requires a JDK installed that matches your system
architecture. On macOS Apple Silicon, make sure you have an **arm64** JDK
(not x86_64). You can install one via Homebrew (`brew install openjdk@11`)
or download an arm64 JDK from Oracle. Then set `JAVA_HOME` before installing.

Also note: `python-javabridge` does not yet support Python 3.13+, so pin
Python to 3.11 or 3.12 when creating the environment.

```bash
conda create -n 2026_bioformats python=3.11
conda activate 2026_bioformats

# Set JAVA_HOME to an arm64 JDK (adjust version as needed)
export JAVA_HOME=$(/usr/libexec/java_home -a arm64)

# Install bioformats (requires javabridge, which requires a JDK)
pip install python-javabridge python-bioformats

# Install ipykernel support if desired
pip install ipykernel
```

# Remarks

We wanted to access the raw photon arrival information from `.lif` files.

After manually exporting `.ptu` files from LAS X, this information is easily available,
see `read_ptu.py`. (To export in LAS X, use the FLIM/FCS package, and there opt for
right top menu, file > export raw data.)

However, neither `liffile`, `bioformats` or `readlif` can access time trace 
information for every pixel, ie (t, c, x, y) array format (t=time bin, c=channel,
x,y = pixel location in plane).
See the files:

- `read_lif_bioformats.py`
- `read_lif_readlif.py`
- `read_lif_liffile.py`

In Jan 2025, Christoph Gohlke also commented that this information is 
explicitly not available due to a pending pattent:

>"FWIW, the compression scheme in which photon arrival times are stored in LIF files (in the MemBlock referenced by the “FLIM Compressed” element of the XML metadata) is apparently patent pending, which makes it impossible for open source software to implement a decoder unless given permission by Leica (I’ll ask them)."
-- Christoph Gohlke

See: [https://forum.image.sc/t/leica-stellaris-to-flimj/106989/3](https://forum.image.sc/t/leica-stellaris-to-flimj/106989/3).

I think the pattent is now granted. 

Not sure this means the data is now accessible.