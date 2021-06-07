import threading as thread
import multiprocessing as multiproc

def thread_do(function):
	thread.Thread(target=function).start()

def multi_do(function):
	multiproc.process(target=function).start()

async def asnyc_do(function):
	await function()