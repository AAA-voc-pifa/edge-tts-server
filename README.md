# PPz's edge-tts server

把 [edge-tts](https://github.com/rany2/edge-tts)（微软 Edge 在线语音合成）包成 **HTTP API**。

## Docs

1. 启动测试服务器
2. 浏览器打开 http://localhost:8000/docs

``` bash
git clone git@github.com:AAA-voc-pifa/edge-tts-server.git
cd edge-tts-server
export password=123456
uv sync
source .venv/bin/activate
fastapi dev
```

## Docker

``` bash
docker build -t edge-tts-server .
docker run --rm \
	-p 60001:8000 \
	-e password=123456 \
	edge-tts-server
```
