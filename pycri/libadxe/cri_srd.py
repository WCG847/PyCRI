srd_filesystem64 = 0

def SRD_SetFilesystem64(mode: int):
	global srd_filesystem64
	if mode == 1:
		print('SRD: 64bit Host filesystem.', end='\r\n')
	srd_filesystem64 = mode

def SRD_SetLockHost(mode: int):
