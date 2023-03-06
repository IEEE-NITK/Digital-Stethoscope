# Heart Model

## Libraries Used 
- Librosa 
- Tensorflow keras
- Matplotlib
- Numpy
- Pandas 
- sklearn

## Data 
The dataset is split into two sources, A and B:
- set_a.csv - Labels and metadata for heart beats collected from the general public via an iPhone app
- nset_a_timing.csv - contains gold-standard timing information for the "normal" recordings from Set A.
- set_b.csv - Labels and metadata for heart beats collected from a clinical trial in hospitals using a digital stethoscope
- audio files - Varying lengths, between 1 second and 30 seconds. (some have been clipped to reduce excessive noise and provide the salient fragment of the sound).

## Data Augmentation / Processing 
 - Combined both the data set to make a more uniform classified data
 - Extracted features of MFCC - in some cases 30 and other 40 [ for experimentation ] 
 
## Model

Tried couple of architecture but one given here is as :
|Layer (type) |               Output Shape|              Param #   |
|---------------|----------------------------|--------------------------|
| LSTM     |        (None, 40, 128)   |    66560    | 
| LSTM     |        (None, 64)   |     49408     | 
| Dense | (None,3) | 195 |


## Results
This gave accuracies of : 
- model train data score       :  71 %
- model test data score        :  69 %
- model validation data score  :  79 %
- model unlabeled data score   :  79 %
Loss Function came to 0.56247

## Observations 
The loss functions for various parameter changes comes consistently between 0.533 to 0.56, which seems to be very inefficient. 
