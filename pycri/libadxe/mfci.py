from typing import Any, Callable


mfci_vtbl: list[Callable] = [0] * 104
mfci_err_func: Callable = None
mfci_err_obj = None
def mfCiGetInterface():
	return mfci_vtbl

def mfCiEntryErrFunc(func: Callable, obj: Any):
	global mfci_err_func, mfci_err_obj
	mfci_err_func = func
	mfci_err_obj = obj



mfci_vtbl[1] = mfCiEntryErrFunc