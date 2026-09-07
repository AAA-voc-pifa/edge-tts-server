import asyncio
from pprint import pprint
from edge_tts import VoicesManager

async def m():
	voices = await VoicesManager.create()
	all_v = voices.find(Language='en')
	print(f'en 语音共 {len(all_v)}个, 结构如下:')
	pprint(all_v[0])

	language = [item['Language'] for item in all_v]
	print(set(language))



asyncio.run(m())
