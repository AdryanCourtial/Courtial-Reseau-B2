const url = "ws://10.1.1.11:13337";


const exampleSocket = new WebSocket(
  url,  "protocolOne"
);


exampleSocket.onopen = () => {
  console.log("Tu es CO");
}

exampleSocket.send('Hello|Something About Me');