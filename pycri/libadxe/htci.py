from cri_srd import SRD_SetFilesystem64, SRD_SetLockHost
from typing import Callable


htci_vtbl: list[Callable] = [0] * 26
htci_err_func = None
htci_err_obj = None
htg_ci_root_dir = None
htg_ci_head_name = None
htg_ci_open_mode = 0x8001

def htCiSetRootDir(dir: bytes = None):
	global htg_ci_root_dir
	if not dir:
		htg_ci_root_dir = 0
		return
	if dir in {b'/', b'\\'}:
		htg_ci_root_dir = dir
	else:
		htg_ci_root_dir = b'/'

def htCiSetFileSystem64(mode: int = 1): SRD_SetFilesystem64(mode)
def htCiSetAccessName(access: bytes = None):
	global htg_ci_head_name
	if not access:
		htg_ci_head_name = b'host:'

def htCiSetOpenMode(unk):
	global htg_ci_open_mode
	if not unk:
		htg_ci_open_mode = 0x8001

def htCiSetLockHost(mode=0):
	SRD_SetLockHost(mode)


def htCiGetInterface():
	htCiSetRootDir()
	htCiSetAccessName()
	return htci_vtbl

def htCiEntryErrFunc(fn: Callable, obj = None):
	global htci_err_func, htci_err_obj
	htci_err_func = fn; htci_err_obj = obj

htci_vtbl[1] = htCiEntryErrFunc