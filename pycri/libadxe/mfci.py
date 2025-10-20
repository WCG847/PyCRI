
from typing import Callable


mfci_vtbl: list[Callable] = [0] * 26
mfci_err_func = None
mfci_err_obj = None

def mfCiGetInterface():
	return mfci_vtbl

def mfCiEntryErrFunc(fn: Callable, obj = None):
	global mfci_err_func, mfci_err_obj
	mfci_err_func = fn; mfci_err_obj = obj

mfci_vtbl[1] = mfCiEntryErrFunc