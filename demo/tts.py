import asyncio
from edge_tts import Communicate

voice = 'Microsoft Server Speech Text to Speech Voice (en-AU, WilliamMultilingualNeural)'
text = 'hello, world!'

async def m():
	communicate = Communicate(text, voice)
	await communicate.save('output.mp3')

asyncio.run(m())