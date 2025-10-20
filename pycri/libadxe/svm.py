svm_err_func = None
svm_err_obj = None
import logging
logging.basicConfig(filename='svm_err.txt')

def SVM_CallErr(msg: str):
	logging.error(msg)
	if svm_err_func:
		svm_err_func(svm_err_obj)
