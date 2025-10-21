srd_filesystem64 = 0
srd_hst_exec_locked = 0
srd_host_lock = 0
def SRD_SetFilesystem64(mode: int):
	global srd_filesystem64
	if mode == 1:
		print('SRD: 64bit Host filesystem.', end='\r\n')
	srd_filesystem64 = mode

def SRD_SetLockHost(mode: int):
	unk = mode * 0x40000
	global srd_hst_exec_locked
	srd_hst_exec_locked = mode
	global srd_host_lock
	srd_host_lock = srd_hst_exec_locked
	if srd_hst_exec_locked == 1:
		print('SRD: Enable HostLock', end='\r\n')