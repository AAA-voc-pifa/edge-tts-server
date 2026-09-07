import asyncio
from pprint import pprint
from edge_tts import VoicesManager
from service.util import perf

async def m():
	perf()
	voices = await VoicesManager.create()
	perf()
	all_v = voices.find()
	print(f'en 语音共 {len(all_v)}个, 结构如下:')
	pprint(all_v[0])

	language = [item['Language'] for item in all_v]
	print(set(language))
	perf()



asyncio.run(m())
