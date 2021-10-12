# Record .wav audio file and perform FFT

> A small task of my *Theory and Design for Mechanical Measurement* class.

## Environment

- Python `3.8.10`
- NumPy `1.20.3`
- Matplotlib `3.3.4`
- SciPy `1.7.1`

## Usage

Record an `.wav` file(length and filename decided by yourself) and perform ***fast fourier transform*** on it.

## How to use

In the console:

```bash
python3 main.py audio_length filename
```

Attension:

- `audio_length` should be an interger `<= 1`
- `filename` should not with the `.wav` file format

For example:

```bash
python3 main.py 3 test_audio  # record a 3-second-long named test_audio.wav file
```

## Effection

The following example shows the output of the time and frequency domain of a recording file of "dou" sound.

![time](/images/Figure_1.png)

![freq](/images/Figure_2.png)

## References

- [Fourier Transforms With scipy.fft: Python Signal Processing](https://realpython.com/python-scipy-fft/)
- [Playing and Recording Sound in Python](https://realpython.com/playing-and-recording-sound-python/)
