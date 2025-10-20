from typing import Callable
from ctypes import c_char, c_ubyte, cast

cvfs_errfn = None

cvfs_errobj = None
cvfs_build = "\nCVFS/PS2EE Ver.2.39 Build:Feb  8 2005 17:53:47\n"
cvfs_tbl = []
cvfs_defdevice = []
def cvFsCallUsrErrFn():...
def addDevice(name: bytearray, fn):
	toUpperStr(name)
	IF_TBL: list[Callable] = fn()
	dev = getDevice(name)
	if not dev:
		global cvfs_tbl
		cvfs_tbl.append((IF_TBL, name))
	return IF_TBL


def getDevice(name: bytearray):
	length = len(name)
	try:
		for vtable, device in cvfs_tbl:
			if device == name:
				return (vtable, device)
	except Exception:
		return 0
	return 0


def toUpperStr(name: bytearray):
	length = len(name)
	if length != 0:
		for i in range(length):
			letter = name[i] & 0xFF
			v1 = (letter - 32) & 0xFF
			v0 = (letter - 97) & 0xFF
			if v0 < 26:
				name[i] = (-v1) & 0xFF


def cvFsEntryErrFunc(fn: Callable, obj):
	global cvfs_errfn, cvfs_errobj
	if fn:
		cvfs_errfn = fn
		cvfs_errobj = obj


def cvFsError(msg: str):
	global cvfs_errfn, cvfs_errobj
	cvFsCallUsrErrFn(msg)


def cvFsCallUsrErrFn(msg: str):
	if cvfs_errfn:
		cvfs_errfn(cvfs_errobj, msg)


def cvFsAddDev(name: bytearray, fn: Callable):
	global cvfs_build
	if not name:
		cvFsError("cvFsAddDev #1:illegal device name")
	elif not fn:
		cvFsError("cvFsAddDev #2:illegal I/F func name")
	interface = addDevice(name, fn)
	if interface:
		if interface[1]:
			interface[1](cvFsEntryErrFunc, None)

def isExistDev(name, length):
	for interface, device in cvfs_tbl:
		if device == name:
			return 1
	return 0

def cvFsSetDefDev(name: bytearray):
	if not name:
		cvFsError('cvFsSetDefDev #1:illegal device name')
	if len(name) != 0:
		toUpperStr(name)
		ok = isExistDev(name, name.__len__())
		if not ok:
			cvFsError("cvFsSetDefDev #2:unknown device name")
		global cvfs_defdevice
		cvfs_defdevice.append(name)