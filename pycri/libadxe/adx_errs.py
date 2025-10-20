adxerr_func = None
adxerr_obj = None
from svm import SVM_CallErr

def ADXERR_CallErrFunc1(msg: str):
	adxerr_msg = msg[:256]
	if not adxerr_func:
		SVM_CallErr(adxerr_msg)
	raise ValueError(msg)