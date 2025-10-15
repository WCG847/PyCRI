from typing import Any, Callable

cvfs_errfn = None
cvfs_errobj = None
cvfs_tbl = [0] * 512

def toUpperStr(name: bytearray):
	name = memoryview(name)
	size = len(name)
	for i, c in enumerate(name):
		v1 = (c - 0x20) & 0xFFFFFFFF
		c = (c - 0x61) & 0xFFFFFFFF
		if c < 0x1A:
			name[i] = v1


def addDevice(device_name: bytearray, fn: Callable):
	toUpperStr(device_name)
	result = fn()
	ok = getDevice(device_name)
	if not ok: 
		unk = cvfs_tbl[4]
		if unk == 0:
			cvfs_tbl[0] = result
			size = len(device_name)
			cvfs_tbl[4:size] = device_name
			return result

def getDevice(device_name: bytearray):
	size = len(device_name)
	for i in range(32):
		if device_name != cvfs_tbl[size+16:i+size]:
			continue
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



def cvFsError(msg: bytearray):
	cvFsCallUsrErrFn(cvfs_errobj, msg)

def cvFsCallUsrErrFn(obj: Any, msg: bytearray):
	if cvfs_errfn:
		cvfs_errfn(obj, msg)