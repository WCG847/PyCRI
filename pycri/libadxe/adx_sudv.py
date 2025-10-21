adxps2_rt_ver0_ver4 = "\nADXRT  Ver.3020"
adxps2_rt_ver5 = " Build:Feb  8 2005 17:53:38\n"
from adx_errs import ADXERR_CallErrFunc1
from cri_cvfs import cvFsEntryErrFunc, cvFsAddDev, cvFsSetDefDev
from mfci import mfCiGetInterface
from htci import htCiGetInterface, htCiSetFileSystem64, htCiSetLockHost, htCiSetOpenMode, htCiSetRootDir
from dvci import dvCiSetRdMode, dvCiSetRootDir

def adxps2_err_dvd(obj, msg: str):
	ADXERR_CallErrFunc1(msg)


def ADXPS2_SetupDvdFs(system_param: list):
	global adxps2_rt_ver0_ver4, adxps2_rt_ver5
	cvFsEntryErrFunc(adxps2_err_dvd, None)
	cvFsAddDev(bytearray(b'MFS'), mfCiGetInterface)
	cvFsEntryErrFunc(adxps2_err_dvd, None)
	cvFsAddDev(bytearray(b'CDV'), mfCiGetInterface)
	cvFsSetDefDev(bytearray(b'CDV'))
	if system_param:
		dvCiSetRdMode(system_param[2], system_param[3], system_param[4], system_param[5])
		dvCiSetRootDir(system_param[0])