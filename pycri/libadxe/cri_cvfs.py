from typing import Any, Callable

cvfs_errfn = None
cvfs_errobj = None
cvfs_tbl: list[tuple[list[Callable], bytearray]] = []

def toUpperStr(name: bytearray):
	name = memoryview(name).cast('b')
	size = len(name)
	for i, c in enumerate(name):
		v1 = (c - 0x20)
		c = (c - 0x61)
		if c < 0x1A:
			name[i] = v1


def addDevice(device_name: bytearray, fn: Callable):
	toUpperStr(device_name)
	result = fn()
	ok = getDevice(device_name)
	if not ok: 
		if not any(dev_name == device_name for _, dev_name in cvfs_tbl):
			cvfs_tbl.append((result, device_name))
			return result
def getDevice(device_name: bytearray):
	for vtable, dev_name in cvfs_tbl:
		if dev_name == device_name:
			return device_name

	return 0



def cvFsEntryErrFunc(fn: Callable, obj: Any):
	global cvfs_errfn, cvfs_errobj
	if fn:
		cvfs_errfn = fn
		cvfs_errobj = obj

def cvFsAddDev(device_name: bytearray, fn: Callable):
	if not device_name:
		cvFsError(b'cvFsAddDev #1:illegal device name\0')
	elif not fn:
		cvFsError(b'cvFsAddDev #2:illegal I/F func name\0')
	vtable = addDevice(device_name, fn)
	if not vtable:
		cvFsError(b'cvFsAddDev #3:failed added a device\0')
	got = vtable[1]
	got()


def cvFsSetDefDev(device_name: bytearray):
	if not device_name:
		cvFsError(b'cvFsSetDefDev #1:illegal device name\0')

	elif len(device_name) != 0:
		toUpperStr(device_name)

def isExistDev(device_name: bytearray):



def cvFsError(msg: bytearray):
	cvFsCallUsrErrFn(cvfs_errobj, msg)

def cvFsCallUsrErrFn(obj: Any, msg: bytearray):
	if cvfs_errfn:
		cvfs_errfn(obj, msg)