from adx_errs import ADXERR_CallErrFunc1
from cri_cvfs import cvFsEntryErrFunc, cvFsAddDev
from mfci import mfCiGetInterface
from htci import htCiGetInterface, htCiSetFileSystem64, htCiSetLockHost, htCiSetOpenMode, htCiSetRootDir

def adxps2_err_host(obj, msg: str):
	ADXERR_CallErrFunc1(msg)


def ADXPS2_SetupHostFs(system_param: list):
	cvFsEntryErrFunc(adxps2_err_host, None)
	cvFsAddDev(bytearray(b'MFS'), mfCiGetInterface)
	cvFsEntryErrFunc(adxps2_err_host, None)
	cvFsAddDev(bytearray(b'HST'), htCiGetInterface)
	if system_param:
		htCiSetOpenMode(system_param[1])
		htCiSetRootDir(system_param[0])
		if not system_param[2]:
			htCiSetFileSystem64(1)
		if not system_param[3]:
			htCiSetLockHost(0)