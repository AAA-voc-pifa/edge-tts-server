from fastapi import FastAPI, Request
from service.edge_tts import voice_mng
from edge_tts.typing import VoicesManagerVoice

app = FastAPI()

@app.get('/voice')
async def all_voices(req: Request) -> list[VoicesManagerVoice]:
	return await voice_mng.find(
		**dict(req.query_params)
	)

# @app.get('/tts')
# async def tts(text: str, voice: str):
