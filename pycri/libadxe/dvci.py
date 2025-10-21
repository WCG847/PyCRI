from typing import Callable
from dvci_sub import dvg_rbuf


dvg_ci_root_dir = None
dvci_vtbl: list[Callable] = [0] * 26
def dvCiSetRootDir(dir: bytes = None):
	global dvg_ci_root_dir
	if not dir:
		dvg_ci_root_dir = 0
		return
	if dir in {b'/', b'\\'}:
		htg_ci_root_dir = dir
	else:
		htg_ci_root_dir = b'/'

def dvCiGetInterface():
	dvCiSetRootDir()
	return dvci_vtbl

dvg_ci_rdmode = 0
dvg_ci_cdrmode = 0
dvg_flist_tbl = [0] * 4

def dvCiSetRdMode(unk, unk2, unk3, rdmode):
	global dvg_ci_rdmode
	dvg_ci_rdmode = rdmode
	dvg_ci_cdrmode = unk3 << 16 | unk2 << 8 | unk

def dvCiLoadFcache(unk, unk2, unk3, unk4):
	global dvg_flist_tbl
	if not dvg_flist_tbl[0]:
		if unk:
			if unk2:
				if unk3:
					load_flist(unk, dvg_rbuf)

def load_flist(name, buf):
