from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from service.edge_tts import voice_mng, tts_stream
from edge_tts.typing import VoicesManagerVoice
from service.auth import make_verify

app = FastAPI(
	dependencies=[
		make_verify(),
	]
)

@app.get('/voice')
async def all_voices(req: Request) -> list[VoicesManagerVoice]:
	return await voice_mng.find(
		**dict(req.query_params)
	)

@app.get('/tts')
async def tts(text: str, voice: str):
	return StreamingResponse(
		tts_stream(text, voice),
		media_type='audio/mpeg',
		headers={
			'Cache-Control': 'public, max-age=86400',
		},
	)
