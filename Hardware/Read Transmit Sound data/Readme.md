<h1>Code description</h1>

The code is used to collect sound data using an ESP32  from an electret microphone at a rate of 44.1kHz and then transmit it to a device using a Websocket connection.
The following header files are used to enable communication and web server on the ESP32 .<br>

WiFi<br>
AsyncTCP<br>
ESPAsyncWebServer

**WiFi**: This allows the ESP32 to connect to Wi-Fi networks and create a Wi-Fi access point.

**AsyncTCP**: This provides an asynchronous TCP/IP stack implementation for the ESP32. It enables non-blocking communication over TCP/IP sockets, which can improve the responsiveness and efficiency of the ESP32's network communication.

**ESPAsyncWebServer**: This provides a web server implementation for the ESP32 that can handle HTTP requests and serve web pages. It enables the ESP32 to function as a web server, allowing it to serve dynamic content and respond to requests from other devices on the network. It is built on top of the AsyncTCP library to enable non-blocking communication.

```const char* ssid = "Galaxy M325522";
const char* password = "zkkt3170";
```

The  **ssid** variable contains the name of a Wi-Fi network that the ESP32 will connect to, while the **password** variable contains the password for that network.

```
String a="";
int value;
int i = 0;
volatile int interruptCounter;
```
The variables are defined. interruptCounter is declared as volatile int, volatile indicates that its value can be changed by an interrupt service routine (ISR).
```
AsyncWebServer server(80);
AsyncWebSocket ws("/ws");
```
The first line initializes the server object of AsyncWebserver class and sets it up to listen for incoming HTTP requests on port 80.
Then the ws object is initialized and is set up to listen for incoming WebSocket connections on the "/ws" path.

The next part of the code provides a basic web interface for an ESP WebSocket Server and uses a WebSocket client in JavaScript to communicate with a server. A constant character array named index_html using the PROGMEM macro. This macro is used to indicate that the array should be stored in the program memory instead of SRAM. This helps to conserve SRAM.<br>

The index_html array contains the HTML, CSS, and JavaScript code for a web page that serves as an interface for an ESP WebSocket Server. This web page is designed to be viewed on a web browser.<br>

The HTML code includes a <!DOCTYPE> declaration and several tags for defining the structure and content of the web page. The <head> section includes a title for the web page, a viewport meta tag for controlling the viewport settings on mobile devices, and a link to an empty favicon (used to show a small icon in the browser tab).
The HTML code also includes several CSS styles defined in the <style> section. These styles are applied to different elements of the web page, including the font family, font size, color, background color, and alignment.<br>

The <body> section contains the main content of the web page, including a header with the title "ESP WebSocket Server" and a div with a class content that contains a heading "Digital Stethoscope".<br>

The JavaScript code defines a WebSocket client that connects to a WebSocket server running on the same host as the web page (using the hostname from the window.location object). The WebSocket client is created using the WebSocket constructor and the ws:// protocol. Once the WebSocket connection is established, the client sends and receives messages using the onmessage event handler.<br>

The JavaScript code defines four functions: initWebSocket, onOpen, onClose, and onMessage.<br>The **initWebSocket** function creates a WebSocket object and assigns the onopen, onclose, and onmessage event handlers to the corresponding functions.<br> The **onOpen** function logs a message to the console when the WebSocket connection is opened.<br> The **onClose** function logs a message to the console when the connection is closed and attempts to reopen the connection after a delay of 2 seconds.<br> The **onMessage** function logs the received message data to the console.<br>  The **onLoad** function is called when the web page is loaded and calls initWebSocket to establish the WebSocket connection.
  
```
hw_timer_t * timer = NULL;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;
```
hw_timer_t * timer = NULL; declares a pointer variable timer of type hw_timer_t, which is a structure that represents a hardware timer on the ESP32 microcontroller.
 
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED; declares a mutex variable timerMux of type portMUX_TYPE, which is a custom type defined in the ESP32 SDK for creating mutexes. A mutex is a synchronization primitive that helps to prevent multiple threads or tasks from accessing shared resources simultaneously, which could lead to race conditions and other issues.

Then ***voidnotifyClients*** is used to send a message in text format to all clients connected to a WebSocket server.<br>
***OnEvent*** function is used as a callback for events that occur on an instance of the AsyncWebSocket class.<br>
Function ***initWebSocket*** that initializes a WebSocket server by setting up an event handler and adding it to a server object.<br>
***IRAM_ATTR onTimer*** is the timer interrupt function. It is incrementing the interrupt counter by one everytime interrupt occurs.<br>
 
In the void setup connection to a WiFi network using the SSID and password is attempted, once connection is made the IP address of ESP32 is printed.
Then WebSocket server is initialized by calling the initWebSocket() function. HTTP server is started and it starts listening for requests. Pin 34 is set as input pin.<br>
Timer0 of ESP32 is setup. The timer is set to trigger an interrupt every 22.7microseconds.<br>

  ```
   if (interruptCounter > 0) {
    portENTER_CRITICAL(&timerMux);
    interruptCounter--;
    value = analogRead(34);
    portEXIT_CRITICAL(&timerMux);
    // Read analog input value from pin 34
    a += String(value);
    a +=" ";
    i += 1;
    if(i==500){
      notifyClients();
      i = 0;
      a += "";
    }
}
  ws.cleanupClients();
}
  ```
In the void loop we check if the interruptCounter variable is greater than 0, which indicates that a timer interrupt has occurred. If so, it enters a critical section to prevent other interrupts from modifying interruptCounter. Analog input is read at pin34 and appended to String a and everytime i is increased by one. When String a has 500 values ***notifyClients()*** function is called to send the value to clients. After sending the data, i is reset to 0, and a is cleared.The ws.cleanupClients() function is used to remove disconnected clients from the WebSocket server's list of clients.
  

  
  
