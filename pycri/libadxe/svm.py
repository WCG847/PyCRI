from io import BytesIO
from typing import Any


svmerr_msg: BytesIO = BytesIO(b'\x00' * 128)
svmerr_func = None

def SVM_CallErr(msg: list[int], obj: Any = None):
	global svmerr_msg
	print(bytearray(msg), file=svmerr_msg)
	if svmerr_func:
		svmerr_func(obj)

