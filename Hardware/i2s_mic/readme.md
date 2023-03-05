<h1>Introduction</h1><br>
The code uses the ESP32's I2S peripheral to read audio data from a microphone and output it to the serial port. The configuration of the I2S peripheral is defined using the <b>i2s_config_t</b> and <b>i2s_pin_config_t</b> structures, which specify settings such as the sample rate, bits per sample, and pins to use for the clock and data lines.

The <b>setup()</b> function initializes the serial port for output and sets up the I2S peripheral using <b>i2s_driver_install()</b> and <b>i2s_set_pin()</b>.

The <b>loop()</b> function reads audio samples from the I2S peripheral using <b>i2s_read()</b>, and then outputs the samples to the serial port using Serial.printf(). The number of samples to read is specified by SAMPLE_BUFFER_SIZE, and the size of each sample is defined by sizeof(int32_t).<hr>

<h2>Code Description</h2><br>

```
#include <driver/i2s.h>
#define SAMPLE_BUFFER_SIZE 512
#define SAMPLE_RATE 44100
```
The first line includes the <b>i2s.h</b> header file which contains the definitions for the <b>I2S</b> (Inter-IC Sound) driver.
The second and third lines define constants for the sample buffer size and sample rate of the audio signal.

```
#define I2S_MIC_CHANNEL I2S_CHANNEL_FMT_ONLY_LEFT
```
This line defines the I2S channel format. In this case, only the left channel is used.

```
#define I2S_MIC_SERIAL_CLOCK GPIO_NUM_32      //sck
#define I2S_MIC_LEFT_RIGHT_CLOCK GPIO_NUM_25 //ws
#define I2S_MIC_SERIAL_DATA GPIO_NUM_33     //sd
```
These lines define the GPIO pins used for the I2S serial clock, left/right clock, and serial data.

```
i2s_config_t i2s_config = {
    .mode = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX),
    .sample_rate = SAMPLE_RATE,
    .bits_per_sample = I2S_BITS_PER_SAMPLE_32BIT,
    .channel_format = I2S_CHANNEL_FMT_ONLY_LEFT,
    .communication_format = I2S_COMM_FORMAT_I2S,
    .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1,
    .dma_buf_count = 4,
    .dma_buf_len = 1024,
    .use_apll = false,
    .tx_desc_auto_clear = false,
    .fixed_mclk = 0};
```
This code block initializes an i2s_config_t struct, which contains the configuration settings for the I2S peripheral interface. 
These settings include the operating mode, sample rate, bits per sample, channel format, communication format, interrupt allocation flags, 
DMA buffer count and length, and various other settings related to clock synchronization and auto-clearing of transmit descriptors.

Specifically, the I2S_MODE_MASTER and I2S_MODE_RX flags are set to enable the I2S peripheral as a master receiver. The sample rate
is set to SAMPLE_RATE, which in this case is 44100 Hz. The bits per sample are set to 32 bits, and the channel format is set to 
I2S_CHANNEL_FMT_ONLY_LEFT, which indicates that only the left channel will be used for input. The communication format is set to 
I2S_COMM_FORMAT_I2S, which uses the I2S standard communication protocol. Finally, various other settings such as interrupt flags, 
DMA buffer count and length, and clock synchronization are configured.

```
i2s_pin_config_t i2s_mic_pins = {
    .bck_io_num = I2S_MIC_SERIAL_CLOCK,
    .ws_io_num = I2S_MIC_LEFT_RIGHT_CLOCK,
    .data_out_num = I2S_PIN_NO_CHANGE,
    .data_in_num = I2S_MIC_SERIAL_DATA};
```
This block of code defines an i2s_pin_config_t struct called i2s_mic_pins which contains the GPIO pin settings for the I2S driver.

```
void setup()
{
  Serial.begin(115200);
  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  i2s_set_pin(I2S_NUM_0, &i2s_mic_pins);
}
```
This function is called once at the start of the program and sets up the serial communication and the I2S driver. Serial.begin() initializes the serial communication at a baud rate of 115200. i2s_driver_install() installs the I2S driver for the given I2S port number and configuration settings, and i2s_set_pin() sets the GPIO pins for the I2S driver.

```
int32_t raw_samples[SAMPLE_BUFFER_SIZE];
```
This line declares an array of 32-bit signed integers called raw_samples with a size of SAMPLE_BUFFER_SIZE.

```
void loop()
{
  // read from the I2S device
  size_t bytes_read = 0;
  i2s_read(I2S_NUM_0, raw_samples, sizeof(int32_t) * SAMPLE_BUFFER_SIZE, &bytes_read, portMAX_DELAY);
  int samples_read = bytes_read / sizeof(int32_t);
  // dump the samples out to the serial channel.
  for (int i = 0; i < samples_read; i++)
  {
    Serial.printf("%ld\n", raw_samples[i]);
  }
}
```
This is the main loop of the program, which continuously reads audio samples from the I2S device and prints them to the serial monitor.

The loop starts by initializing a variable bytes_read to 0, which will be used to keep track of the number of bytes read from the I2S device. 
Then, it calls the i2s_read() function, which reads audio samples from the I2S device and stores them in the raw_samples buffer.
The i2s_read() function takes the following arguments:

I2S_NUM_0: The I2S device number to read from (in this case, I2S device 0).
raw_samples: The buffer to store the samples in.
sizeof(int32_t) * SAMPLE_BUFFER_SIZE: The maximum number of bytes to read from the I2S device. sizeof(int32_t) gives the number of bytes in an int32_t data type, and SAMPLE_BUFFER_SIZE is the number of samples that can be stored in the raw_samples buffer.
&bytes_read: A pointer to a variable to store the number of bytes actually read from the I2S device.
portMAX_DELAY: The maximum amount of time to wait for data to be available on the I2S device.
The i2s_read() function returns when either the requested number of bytes have been read or when the portMAX_DELAY time has elapsed.

After reading the samples, the code calculates the number of samples actually read (samples_read) by dividing bytes_read by the size of a single sample (sizeof(int32_t)).

Finally, the loop iterates over each sample in the raw_samples buffer that was read from the I2S device and prints its value to the serial monitor using Serial.printf(). The %ld format specifier is used to print a long integer, which matches the size of the int32_t data type.
