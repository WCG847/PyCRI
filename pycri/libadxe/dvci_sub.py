dvg_rbuf = []
dvg_fpath = []
dvg_flist_tbl = []
def load_flist(name, buf):
	if name.upper() != 'HST':
		global dvg_fpath
		dvg_fpath = [0] * 32


def dvci_init_flist():
	global dvg_flist_tbl
	dvg_flist_tbl = [0] * 4
