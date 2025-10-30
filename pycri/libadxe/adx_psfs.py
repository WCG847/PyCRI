adxps2_debug_level = 0
import warnings
def ADXPS2_PrintfWarn(msg: str):
	if adxps2_debug_level:
		return
	print(msg)
	warnings.warn(msg, ResourceWarning)
