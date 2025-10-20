from cri_cvfs import cvFsEntryErrFunc, cvFsAddDev
from mfci import mfCiGetInterface
from adx_errs import ADXERR_CallErrFunc1

def adxps2_err_mem(obj, msg: str):
	ADXERR_CallErrFunc1(msg)


def ADXPS2_SetupMemFs():
	cvFsEntryErrFunc(adxps2_err_mem, None)
	cvFsAddDev(bytearray(b'MFS'), mfCiGetInterface)