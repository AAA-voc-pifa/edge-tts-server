import logging
from typing import Annotated, Literal
from fastapi import FastAPI, Query, status
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from service.edge_tts import voice_mng, tts_stream
from edge_tts.typing import VoicesManagerVoice
from service.auth import make_verify

log = logging.getLogger('uvicorn.error')
verify = make_verify()

app = FastAPI(
	title='edge-tts-server',
	description='微软 Edge 在线语音合成 HTTP API。受保护接口需在请求头携带 `Authentication`。',
)
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=False,
	allow_methods=['*'],
	allow_headers=['*'],
)

@app.get(
	'/ready',
	status_code=status.HTTP_200_OK,
	summary='就绪检查',
	description='始终返回 200，无需鉴权。',
)
async def ready() -> None:
	return None

@app.post(
	'/auth',
	status_code=status.HTTP_204_NO_CONTENT,
	summary='验证密码',
	description='仅校验请求头 `Authentication`，成功无响应体。',
	dependencies=[verify],
)
async def auth() -> None:
	return None

@app.get(
	'/voice',
	summary='查询音色',
	description='可按 gender、locale、language 过滤。',
	dependencies=[verify],
)
async def all_voices(
	gender: Annotated[Literal['Female', 'Male'] | None, Query(description='性别：Female / Male')] = None,
	locale: Annotated[str | None, Query(description='地区，如 zh-CN、en-US')] = None,
	language: Annotated[str | None, Query(description='语言，如 zh、en')] = None,
) -> list[VoicesManagerVoice]:
	filters = {}
	if gender is not None:
		filters['Gender'] = gender
	if locale is not None:
		filters['Locale'] = locale
	if language is not None:
		filters['Language'] = language
	return await voice_mng.find(**filters)

class AudioMpegResponse(StreamingResponse):
	media_type = 'audio/mpeg'

@app.get(
	'/tts',
	response_class=AudioMpegResponse,
	summary='文本转语音',
	description='流式返回 MP3（audio/mpeg）。',
	dependencies=[verify],
)
async def tts(
	text: Annotated[str, Query(description='要合成的文本')],
	voice: Annotated[str, Query(description='音色 ShortName，见 /voice')],
	rate: Annotated[str, Query(
		description='语速，格式如 +0%、+50%、-20%',
		pattern=r'^[+-]\d+%$',
	)] = '+0%',
):
	log.info('合成: %s', text)
	return AudioMpegResponse(
		tts_stream(text, voice, rate),
		headers={
			'Cache-Control': 'public, max-age=86400',
		},
	)
