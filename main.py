from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from service.edge_tts import voice_mng, tts_stream
from edge_tts.typing import VoicesManagerVoice
from service.auth import make_verify

app = FastAPI(
	dependencies=[
		make_verify(),
	],
)
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

@app.get('/voice')
async def all_voices(req: Request) -> list[VoicesManagerVoice]:
	return await voice_mng.find(
		**dict(req.query_params)
	)

class AudioMpegResponse(StreamingResponse):
	media_type = 'audio/mpeg'

@app.get('/tts', response_class=AudioMpegResponse)
async def tts(text: str, voice: str):
	return AudioMpegResponse(
		tts_stream(text, voice),
		headers={
			'Cache-Control': 'public, max-age=86400',
		},
	)
