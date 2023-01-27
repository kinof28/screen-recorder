import sounddevice
from scipy.io.wavfile import write

# declare frame per seconds / frequency
frame_per_second = 44100

# declare length of record / duration
duration = 5

# recording

record = sounddevice.rec(int(frame_per_second*duration), frame_per_second, 2)

sounddevice.wait()

write("./outputs/recording.wav", frame_per_second, record)
