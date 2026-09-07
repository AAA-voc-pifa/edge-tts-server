import time

__start = time.perf_counter()
def perf():
	print(f'执行时间: {(time.perf_counter() - __start):.3f}s')
