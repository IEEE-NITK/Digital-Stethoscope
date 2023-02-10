*Butterworth filter*

A Butterworth filter is a type of signal processing filter designed to have a frequency response as flat as possible in the passband. Hence the Butterworth filter is also known as “maximally flat magnitude filter”. In Butterworth filter, mathematically it is possible to get flat frequency response from 0 Hz to the cut-off frequency at -3dB with no ripple. If the frequency is more than the cut-off frequency, it will roll-off towards zero with the rate of -20 dB/decade for the first-order filter.If you increase the order of the filter, the rate of a roll-off period is also increased. And for second-order, it is -40 dB/decade.However, one main
disadvantage of the Butterworth filter is that it achieves this pass band flatness at the expense
of a wide transition band as the filter changes from the pass band to the stop band.

**Why Butterworth?**

The aim is the frequencies that are supposed to pass do pass entirely due to the flat response. So that we hear everything we are supposed to hear from audio samples.
When amplitude accuracy is important, the Butterworth is mostly a good choice.

**Circuit Diagram**

![2 -Second-Order-Low-Pass-Butterworth-Filter](https://user-images.githubusercontent.com/97295669/217611291-8e3fc637-3fcd-463e-b266-1b164169cabb.jpg)

**Ideal Frequency Response of Butterworth Filter**

![4 -Ideal-Frequency-Response-of-the-Butterworth-Filter](https://user-images.githubusercontent.com/97295669/217613571-c362d534-d20c-403c-9e47-9842d118a1f4.jpg)

In this second order filter, the cut-off frequency value depends on the resistor and capacitor values of two RC sections. The cut-off frequency is calculated using the below formula.

fc = 1 / (2π√R^2C^2)

The gain rolls off at a rate of 40dB/decade and this response is shown in slope -40dB/decade. The transfer function of the filter can be given as

Vout / Vin = Amax / √{1 + (f/fc)4}

The standard form of transfer function of the second order filter is given as

Vout / Vin = Amax /s^2 + 2ε ωn s + ωn^2

Where ωn = natural frequency of oscillations = 1/R^2C^2

ε = Damping factor = (3 – Amax ) / 2

For second order Butterworth filter, the middle term required is sqrt(2) = 1.414, from the normalized Butterworth polynomial is

3 – Amax = √2 = 1.414

In order to have secured output filter response, it is necessary that the gain Amax is 1.586.

