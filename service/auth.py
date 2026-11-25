import os
from typing import Annotated
from fastapi import Depends, Header, status, HTTPException

def make_verify():
	pw = os.getenv('AUTHENTICATION')
	if pw is None or pw == '':
		raise ValueError('（环境变量）未设置 AUTHENTICATION')

	def verify(authentication: Annotated[str, Header(alias='Authentication')]):
		if authentication != pw:
			raise HTTPException(
				status_code=status.HTTP_403_FORBIDDEN,
				detail='密码错误',
			)
	return Depends(verify)
