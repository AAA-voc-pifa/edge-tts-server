from edge_tts import VoicesManager, Communicate

class VoiceMNG:
	def __init__(self):
		self.__manager: None | VoicesManager = None
	async def m(self) -> VoicesManager:
		if self.__manager is None:
			self.__manager = await VoicesManager.create()
		return self.__manager

	async def find(self, **kwargs):
		return (await self.m()).find(**kwargs)

voice_mng = VoiceMNG()

async def tts_stream(text: str, voice: str) -> bytes:
	async for chunk in Communicate(text, voice).stream():
		if chunk['type'] == 'audio':
			yield chunk['data']
