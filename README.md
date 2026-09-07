# PPz's edge-tts server

把 [edge-tts](https://github.com/rany2/edge-tts)（微软 Edge 在线语音合成）包成 **HTTP API**。

> **许可说明：** 本项目代码可自由使用；依赖库 [edge-tts](https://github.com/rany2/edge-tts) 采用 **GPL-3.0**。若你分发或商用集成该库，请注意 GPL 合规要求。

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
