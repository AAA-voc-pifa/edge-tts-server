# PPz's edge-tts server

把 [edge-tts](https://github.com/rany2/edge-tts)（微软 Edge 在线语音合成）包成 **HTTP API**。

## Start up

``` bash
git clone git@github.com:AAA-voc-pifa/edge-tts-server.git
cd edge-tts-server

docker build -t edge-tts-server .
docker run --rm \
	-p 60001:80 \
	-e password=123456 \
	edge-tts-server
```

文档: 浏览器打开 http://127.0.0.1:60001/docs
