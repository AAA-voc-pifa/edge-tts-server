import os
from typing import Annotated
from fastapi import Depends, Header, status, HTTPException

def make_verify():
	pw = os.getenv('password')
	if pw is None or pw == '':
		raise ValueError('（环境变量）未设置访问密码')

	def verify(password: Annotated[str, Header()]):
		if password != pw:
			raise HTTPException(
				status_code=status.HTTP_403_FORBIDDEN,
				detail='密码错误',
			)
	return Depends(verify)
