# WeIO Minima

Minimal WeIO Platform

## Install

```bash
git clone https://github.com/nodesign/weioMinima
cd weioMinima
```

## Usage

First start the server:

```
python weio.py
```

Then send MQTT commands from remote client:
```
mosquitto_pub -t weio/api/cmd -m '{"jsonrpc": "2.0", "method": "start"}'
```

or

```
mosquitto_pub -t weio/api/cmd -m '{"jsonrpc": "2.0", "method": "stop"}'
```

## License 
[BSD](https://opensource.org/licenses/BSD-3-Clause)
