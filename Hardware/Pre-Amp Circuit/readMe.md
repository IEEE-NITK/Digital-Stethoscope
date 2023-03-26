# What is Pre-Amplifier?
A preamplifier, also known as a preamp, is an electronic amplifier that converts a weak electrical signal into an output signal strong enough to be noise-tolerant and strong enough for further processing, or for sending to a power amplifier and loud speaker.
An ideal preamp will be linear **(have a constant gain through its operating range)**, have high input impedance **(requiring only a minimal amount of current to sense the input signal)** and a low output impedance **(when current is drawn from the output there is minimal change in the output voltage)**.
# Circuit Diagram for the [Preamp](https://github.com/gagan20003/Digital-Stethoscope/blob/main/Hardware/Pre-Amp%20Circuit/preamp_9.asc):

![WhatsApp Image 2023-03-23 at 19 40 16](https://user-images.githubusercontent.com/96785457/227601324-fc54864a-a1f2-4eaa-b858-ac07d4a24ab0.jpg)



<h3>Working </h3>
<p>
The signal source (V_in) is connected to the non-inverting input of the op-amp (U2). The voltage at this input is compared to the voltage at the inverting input (which is held at virtual ground due to negative feedback), and the op-amp amplifies the difference between the two inputs. The gain of the amplifier is determined by the ratio of the feedback resistor (R3) to the input resistor (R4), according to the formula:

Gain = $1 + \frac{R_3}{R_4}$

In this circuit, the gain is set to 57 ( $1 + \frac{56k}{1k}$).

The output of the first stage is fed to a second non-inverting op-amp amplifier (U1), which provides additional gain. The gain of this amplifier is determined by the ratio of the feedback resistor (R1) to the input resistor (R2), according to the formula given earlier. In this circuit, the gain is set to 
21 ( $1 + \frac{20k}{1k}$).

The capacitors C1 and C3 are used to filter out any DC offset present in the input signal, preventing it from being amplified by the op-amps. The capacitor C2 is used to filter out high-frequency noise that may be present in the signal.
The resistors R6, and R7 form a voltage divider to bias the non-inverting input of U2 at half the supply voltage. This ensures that the output voltage swing of the second stage is centered around half the supply voltage, allowing maximum output swing without clipping.

Total Gain of the preamp = gain of first stage * gain of second stage = 57*21 = 1197.
</p>

<h3>Waveforms</h3>
<h4>Input $V_{in}$</h4>
<img src="https://github.com/gagan20003/Digital-Stethoscope/blob/main/resources/input.jpg" alt="input Vin">
<h4>$V_{out}$</h4>
<img src ="https://github.com/CHANDAN-2003/Digital-Stethoscope/blob/main/resources/Output.jpeg" alt ="output img">

$V_{n004} = Output\ of \ stage 2$

$V_{n002} = Output\ of\ stage 1$

<h4>Frequency Response</h4>

![image](https://user-images.githubusercontent.com/97295669/227711224-cc5aef8a-42e8-495e-966c-b35f55364e36.png)
