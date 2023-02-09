# What is Pre-Amplifier?
A preamplifier, also known as a preamp, is an electronic amplifier that converts a weak electrical signal into an output signal strong enough to be noise-tolerant and strong enough for further processing, or for sending to apower amplifier and loud speaker.
An ideal preamp will be linear **(have a constant gain through its operating range)**, have high input impedance **(requiring only a minimal amount of current to sense the input signal)** and a low output impedance **(when current is drawn from the output there is minimal change in the output voltage)**.
# Circuit Diagram for the [Preamp1](https://github.com/IEEE-NITK/Digital-Stethoscope/blob/main/Hardware/preamp_5.asc):
![image](https://user-images.githubusercontent.com/96785457/217804933-3152c1b9-5be8-487b-9396-e3e77031851c.png)
### Calculation:
![git1](https://user-images.githubusercontent.com/96785457/217854871-38c850fd-844d-4f8b-b076-bee2ade8ba3a.jpg)

![git2](https://user-images.githubusercontent.com/96785457/217854383-270f58ec-007f-4fde-9e97-92b01498fb6b.jpg)

### Waveforms:

![WhatsApp Image 2023-02-09 at 20 36 43](https://user-images.githubusercontent.com/96785457/217852896-f297f102-7ec9-4e68-bd33-9d1ddcaffa69.jpg)

This waveform shows that the input signal has been shifted to 129 mV. So that your sampled signal has only positive values.

# Characteristics of the above circuit:
![image](https://user-images.githubusercontent.com/96785457/217806758-84c1ee36-9763-4b18-9f12-271d685dc743.png)
**Input**-V(n010)<br />
 **Output**-V(n003)<br />
**gain**=V(n003)/V(n010)<br />
The frequency Response for the circuit is:
![WhatsApp Image 2023-02-09 at 21 01 29](https://user-images.githubusercontent.com/96785457/217858074-7f83b79c-0c95-443e-ab19-29a5e2a652bb.jpg)

The circuit has a [butterworth filter](https://github.com/IEEE-NITK/Digital-Stethoscope/blob/main/Hardware/butterworth_filter/readMe.md) whose f<sub>c</sub> is 298 Hz.

