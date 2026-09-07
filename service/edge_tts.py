from edge_tts import VoicesManager

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
