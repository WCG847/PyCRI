from typing import Any

from svm import SVM_CallErr

adxerr_msg: list[int]
adxerr_func = None
adxerr_obj = None
def ADXERR_CallErrFunc1(msg: bytearray, obj: Any):
	global adxerr_msg
	adxerr_msg = [x for x in msg]
	if not adxerr_func:
		SVM_CallErr(adxerr_msg)

