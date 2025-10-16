from cri_cvfs import cvFsEntryErrFunc, cvFsAddDev
from mfci import mfCiGetInterface
from adx_errs import ADXERR_CallErrFunc1
from htci import htCiGetInterface

def adxps2_err_host():
	ADXERR_CallErrFunc1()

def ADXPS2_SetupHostFs(sprm: memoryview = None):
	cvFsEntryErrFunc(adxps2_err_host, None)
	cvFsAddDev(b'HST\0', htCiGetInterface)
