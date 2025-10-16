import array
from typing import Callable

htg_ci_root_dir = array.array('b', [0] * 257)
htg_ci_head_name = array.array('b', [0] * 33)
htci_vtbl: list[Callable] = [0] * 104

def htCiSetRootDir(sprm):
	global htg_ci_root_dir
	if not sprm:
		htg_ci_root_dir[0] = 0

def htCiSetAccessName(sprm):
	global htg_ci_head_name
	htg_ci_head_name[:5] = b'host:'


def htCiGetInterface():
	htCiSetRootDir(None)
	return htci_vtbl