#!python3

import irsdk
import time
import codecs
import sys
import os
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M


class State:
	ir_connected = False
	newCorner = True
	is_trackIDFile_exists = -1
	trackFile_read = False
	cBegin = 0
	cEnd = 1
	cName = ''
	trackID = 0
	trackIDFile = ''
	f = ''
	
	

def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')

def loop():
	ir.freeze_var_buffer_latest()
	
	if state.trackFile_read == False:
		state.trackID = ir['WeekendInfo']

		state.trackID = str(state.trackID['TrackID'])
		state.trackIDFile = 'tracks/' + state.trackID + '/corners.txt'
		#print(trackIDFile)

		state.is_trackIDFile_exists = os.path.exists(state.trackIDFile)
		state.f = open(state.trackIDFile, 'r', encoding='utf-8')
		corner = state.f.readline()
		state.cBegin,state.cEnd,state.cName = corner.split(',')
		state.cBegin = int(state.cBegin)
		state.cEnd = int(state.cEnd)
		#print(state.cBegin,' ',state.cEnd,' ',state.cName)
		state.trackFile_read = True
	
	lapDist = round(ir['LapDist'],0)
	#print(lapDist)
	if lapDist > state.cBegin and lapDist < state.cEnd:
		if state.newCorner == True:
			fileName = 'C:\\Users\\sagam\\Documents\\GitHub\\iRCoDriver\\tracks\\' + state.trackID + '\\' + state.cName.strip() + '.mp3'
			#print(fileName)
			
			app=C.QCoreApplication(sys.argv)
			url= C.QUrl.fromLocalFile(fileName)
			content= M.QMediaContent(url)
			player = M.QMediaPlayer()
			player.setMedia(content)
			player.play()
			player.stateChanged.connect( app.quit )
			app.exec()
			
		#print(state.newCorner)
		state.newCorner = False
		os.system('cls')
		print(lapDist)
		print(state.cName.strip())
		
	else:
		state.newCorner = True
		corner = state.f.readline()
		state.cBegin,state.cEnd,state.cName = corner.split(',')
		state.cBegin = int(state.cBegin)
		state.cEnd = int(state.cEnd)
		if state.cName == 'EOF':
			state.trackFile_read = False
			state.f.close()
	
if __name__ == '__main__':
	ir = irsdk.IRSDK()
	state = State()
	whiletrue = True
	try:
		while whiletrue:
			check_iracing()
			if state.ir_connected and state.is_trackIDFile_exists:
				loop()
			elif state.is_trackIDFile_exists == False:
				print('Track File does not exist')
				whiletrue = False
			time.sleep(.1)
	except KeyboardInterrupt:
		pass