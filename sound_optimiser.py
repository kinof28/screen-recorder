from maad.util import plot2d, power2dB
from maad.sound import (load, spectrogram,
                        remove_background, median_equalizer,
                        remove_background_morpho,
                        remove_background_along_axis, sharpness)
import numpy as np

from timeit import default_timer as timer

import matplotlib.pyplot as plt

s, fs = load('./outputs/recording.wav')
Sxx, tn, fn, ext = spectrogram(s, fs, fcrop=[0, 20000], tcrop=[0, 60])
Sxx_dB = power2dB(Sxx, db_range=96) + 96
plot2d(Sxx_dB, extent=ext, title='original',
       vmin=np.median(Sxx_dB), vmax=np.median(Sxx_dB)+40)

print("Original sharpness : %2.3f" % sharpness(Sxx_dB))
