# PPz's edge-tts server

把 [edge-tts](https://github.com/rany2/edge-tts)（微软 Edge 在线语音合成）包成 **HTTP API**。

接口请求头携带 `Authentication`。
就绪检查：`GET /ready`（无需鉴权）。

## DEV

``` bash
uv sync
source .venv/bin/activate
export AUTHENTICATION=123456
fastapi dev
```

文档: 浏览器打开 http://127.0.0.1:60001/docs

## Deploy with docker
```sh
docker build -t edge-tts-server .
docker run --rm \
	-p 60001:80 \
	-e AUTHENTICATION=123456 \
	edge-tts-server
```
