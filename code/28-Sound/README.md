## Prompt
> Use sound.

## Idea
- Record something
- Create spectrum
- `plingo spectrum`
- Spectrum to sound (not clear if this works)

## Implementation Idea 1
`scipy`'s toolchain seems to provide something like this
* https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.istft.html
* https://dsp.stackexchange.com/questions/55540/how-to-go-from-wav-file-to-spectrogram-back-to-wav-file-in-python

So the code could work like this
```
data =  scipy.io.wavfile.read("input.wav")
img_data = convert_to_rgb(data)
cv2.imwrite(img_data, "output.png")

# plingo output.png

img_data = cv2.imread("output.png_out.png")
sound_data = invert_convert_to_rgb(img_data)
scipy.io.wavfile.write(sound_data, "output.wav")
```
