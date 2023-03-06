# Deep Learning Models 

Developing a reliable sound detection and recognition system offers many benefits and has many useful applications in different industries. There have been many efforts made in the process of developing these reliable sound detection systems. These efforts include the incorporation of machine learning and neural networks using deep learning. The main motive of the deep learning model that being used here is to identify and perform a classification of different heart and sound diseases. 

There are two seperate model being built here, namely 
- **Lung Model**: Uses CNN to perform multiclass classifciation 
- **Heart Model** : Uses RNN + LSTM to perform classification between 3 sets of diseases 

## Lung Model 

### CNN 
A Convolutional neural network (CNN) is a neural network that has one or more convolutional layers and are used mainly for image processing, classification, segmentation and also for other auto correlated data.
A convolution is essentially sliding a filter over the input. One helpful way to think about convolutions is this quote from Dr Prasad Samarakoon: “A convolution can be thought as “looking at a function’s surroundings to make better/accurate predictions of its outcome.”
The archecture of the model used here is as follows :
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 39, 861, 16)       80        
                                                                 
 max_pooling2d (MaxPooling2D  (None, 19, 430, 16)      0         
 )                                                               
                                                                 
 dropout (Dropout)           (None, 19, 430, 16)       0         
                                                                 
 conv2d_1 (Conv2D)           (None, 18, 429, 32)       2080      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 9, 214, 32)       0         
 2D)                                                             
                                                                 
 dropout_1 (Dropout)         (None, 9, 214, 32)        0         
                                                                 
 conv2d_2 (Conv2D)           (None, 8, 213, 64)        8256      
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 4, 106, 64)       0         
 2D)                                                             
                                                                 
 dropout_2 (Dropout)         (None, 4, 106, 64)        0         
                                                                 
 conv2d_3 (Conv2D)           (None, 3, 105, 128)       32896     
                                                                 
 max_pooling2d_3 (MaxPooling  (None, 1, 52, 128)       0         
 2D)                                                             
                                                                 
 dropout_3 (Dropout)         (None, 1, 52, 128)        0         
                                                                 
 global_average_pooling2d (G  (None, 128)              0         
 lobalAveragePooling2D)                                          
                                                                 
 dense (Dense)               (None, 6)                 774       
                                                                 
## Heart Model

### RNN 
Recurrent Neural Network is a generalization of feedforward neural network that has an internal memory. RNN is recurrent in nature as it performs the same function for every input of data while the output of the current input depends on the past one computation. After producing the output, it is copied and sent back into the recurrent network. For making a decision, it considers the current input and the output that it has learned from the previous input.

Unlike feedforward neural networks, RNNs can use their internal state (memory) to process sequences of inputs. This makes them applicable to tasks such as unsegmented, connected handwriting recognition or speech recognition. In other neural networks, all the inputs are independent of each other. But in RNN, all the inputs are related to each other.

### LSTM
Long Short-Term Memory (LSTM) networks are a modified version of recurrent neural networks, which makes it easier to remember past data in memory. The vanishing gradient problem of RNN is resolved here. LSTM is well-suited to classify, process and predict time series given time lags of unknown duration. It trains the model by using back-propagation. In an LSTM network, three gates are present:
- **Input gate** — discover which value from input should be used to modify the memory. Sigmoid function decides which values to let through 0,1. and tanh function gives weightage to the values which are passed deciding their level of importance ranging from-1 to 1.
- **Forget gate** — discover what details to be discarded from the block. It is decided by the sigmoid function. it looks at the previous state(ht-1) and the content input(Xt) and outputs a number between 0(omit this)and 1(keep this)for each number in the cell state.
- **Output gate**— the input and the memory of the block is used to decide the output. Sigmoid function decides which values to let through 0,1. and tanh function gives weightage to the values which are passed deciding their level of importance ranging from-1 to 1 and multiplied with output of Sigmoid

There were multiple architectures used that are explained in detail in the Heart-Model folder
