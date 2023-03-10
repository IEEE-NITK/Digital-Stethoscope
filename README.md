# Digital-Stethescope

<br>
<details>
  <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#introduction">Introduction</a>
            <ul>
                <li><a href="#technologies-used">Technologies Used</a></li>
            </ul>
        </li>
        <li>
          <a href="#Objectives">Getting Started</a>
        </li>
        <li>
            <a href="#literature-survey">Literature Survey</a>
            <ul>
                <li><a href="#ESP32">MicroController</a></li>
                <li><a href="#Deep-Learning-Model">Detection Model</a></li>
            </ul>
        </li>
        <li>
          <a href="#Deep Learning">Deep learning</a>
        </li>
        <li>
            <a href="#references">References</a> 
        </li>
        <li>
            <a href="#project-mentors">Project Mentors</a></li>
        </li>
        <li>
            <a href="#project-members">Project Members</a></li>
        </li>   
    </ol>
</details>

<hr>

## Introduction

Digital Stethoscope aims at producing an electronics based amplifying stethoscope, which can store/ transmit the sound waveform captured to another device. Some of the advantages and motivation to switch from mechanically to electronically based amplifying are :
- Better amplification, and a more flexible range of amplification
- Noise reduction capabilities 
- Ability to store and transmit sound captures in order to analyse them on a later date 

### Technologies Used
We have used the following technologies and software for our project
- Python
- TensorFlow
- LTSpice
- AVR C
- ESP32

## Objectives 
The main goals we have set out for this project are 
- Make a microphone - amplification module that can detect frequencies from 50Hz to 20kHz 
- Transmit the sound clip to an associated laptop wirelessly 
- Be able to detect the disease by using an associated Deep Learning model <hr>

<!--- Microcontroller description starts --->

<h2>ESP32</h2>
<img src="https://cdn.shopify.com/s/files/1/0609/6011/2892/files/doc-esp32-pinout-reference-wroom-devkit.png?width=1384" alt="ESP32 Pinout"
  width="700"
  height="500"
  align="middle"
>
<p>The microcontroller that we are using in our project is the ESP32.
The ESP32 is a high-performance microcontroller board that is widely used in Internet of Things (IoT) applications.
Espressif Systems manufactures it, and it is the successor to the ESP8266. The ESP32 is built around a dual-core 
Tensilica LX6 processor that operates at up to 240 MHz, providing plenty of processing power for IoT applications.
</p>

The ESP32 microcontroller board has the following key features:
<ol>
<li>
    <em>Wi-Fi and Bluetooth connectivity:</em> The ESP32 includes Wi-Fi and Bluetooth connectivity, making it simple to connect to the internet and other devices.
</li>
<li>
    <em> Low power consumption:</em> The ESP32 is energy-efficient, with multiple power modes that allow it to operate on very little power.
</li>
<li>
    <em> Large Memory:</em> The ESP32 comes up with up to 520 KB of SRAM and 4MB of flash memory, which is enough to run complex applications.
</li>
<li>
    <em>GPIO pins:</em> The ESP32 has a large number of GPIO pins, which makes it easy to interface with other devices and sensors.
</li>
<li>
    <em>Development tools:</em> There are many development tools available for it including Arduino IDE, ESP-IDF, and MicroPython.
</li>
</ol>
<p>
Overall, the ESP32 is a powerful and versatile microcontroller board that is well-suited for a wide range of IoT applications. Its built-in Wi-Fi and Bluetooth capabilities, low power consumption, and large memory make it a popular choice among developers.

In this project, the esp32 is used to transmit the data collected from the microphone to the ML model over the in-built Wi-Fi.
</p> <hr>


<!--- Microcontroller description ends --->
<h3>Deep Learning</h3>
RNN

<p>Recurrent Neural Network is a generalization of feedforward neural network that has an internal memory. RNN is recurrent in nature as it performs the same function for every input of data while the output of the current input depends on the past one computation. After producing the output, it is copied and sent back into the recurrent network. For making a decision, it considers the current input and the output that it has learned from the previous input.
Unlike feedforward neural networks, RNNs can use their internal state (memory) to process sequences of inputs. This makes them applicable to tasks such as unsegmented, connected handwriting recognition or speech recognition. In other neural networks, all the inputs are independent of each other. But in RNN, all the inputs are related to each other.
</p>
<img width="669" alt="Screenshot 2023-03-10 at 9 38 11 AM" src="https://www.simplilearn.com/ice9/free_resources_article_thumb/Simple_Recurrent_Neural_Network.png">

LSTM
<p>Long Short-Term Memory (LSTM) networks are a modified version of recurrent neural networks, which makes it easier to remember past data in memory. The vanishing gradient problem of RNN is resolved here. LSTM is well-suited to classify, process and predict time series given time lags of unknown duration. It trains the model by using back-propagation. In an LSTM network, three gates are present:
Input gate — discover which value from input should be used to modify the memory. Sigmoid function decides which values to let through 0,1. and tanh function gives weightage to the values which are passed deciding their level of importance ranging from-1 to 1.
Forget gate — discover what details to be discarded from the block. It is decided by the sigmoid function. it looks at the previous state(ht-1) and the content input(Xt) and outputs a number between 0(omit this)and 1(keep this)for each number in the cell state.
Output gate— the input and the memory of the block is used to decide the output. Sigmoid function decides which values to let through 0,1. and tanh function gives weightage to the values which are passed deciding their level of importance ranging from-1 to 1 and multiplied with output of Sigmoid
There were multiple architectures used that are explained in detail in the Heart-Model folder
</p>
<img width="669" alt="Screenshot 2023-03-10 at 9 38 11 AM" src="https://user-images.githubusercontent.com/119749228/224388357-968e1a6b-347e-49fd-b49e-97095111a611.png">

## Model

Tried couple of architecture but one given here is as :
|Layer (type) |               Output Shape|              Param #   |
|---------------|----------------------------|--------------------------|
| LSTM     |        (None, 30, 256)   |    264192    | 
| LSTM     |        (None, 30,128)   |     197120     | 
| LSTM     |        (None, 64)        |    49408      |  
| Dense    | (None,3) | 195 |


## Results
This gave accuracies of : 
- model train data score       :  74 %
- model test data score        :  76 %
- model validation data score  :  79 %
- model unlabeled data score   :  74 %


## Project Mentors

1. [Dharaneedaran K S](https://github.com/DharaneedaranKS)
2. [Hrishikesh Kulkarni](https://github.com/HrishiCoolkarni)

## Project Members

1. [Aditya Rajesh](https://github.com/Adityarajesh001)
2. [Aman Raj](https://github.com/amanrajNitk)
3. [Chandan Padmashali](https://github.com/CHANDAN-2003)
4. [Gagan Mahotiliya](https://github.com/gagan20003)
