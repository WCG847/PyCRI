from cri_cvfs import cvFsEntryErrFunc, cvFsAddDev
from mfci import mfCiGetInterface
from adx_errs import ADXERR_CallErrFunc1

def adxps2_err_mem(obj, msg: bytearray):
	ADXERR_CallErrFunc1(msg, obj)


def ADXPS2_SetupMemFs():
	cvFsEntryErrFunc(adxps2_err_mem, None)
	cvFsAddDev(b'MFS\0', mfCiGetInterface)

