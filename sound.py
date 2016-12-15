import pygame
import os

_SOUNDS = []

pygame.mixer.pre_init( 44100, -16, 2 ,2048)

def get_sound_path(sound_name):
	sound_name = sound_name.replace(":","/")
	path = os.path.realpath( os.path.join("Sound", sound_name) )
	if os.path.isfile(path):
		return path
	return None

_ID_ =0 
	
def play_effect( name, volume=1.0, pitch=1.0):

	global _ID_
	global _SOUNDS
	
	if not pygame.mixer.get_init():
		IOError("No mixer modules")

	path = get_sound_path( name )

	if not path:
		return

	sound = pygame.mixer.Sound( path )
	sound.set_volume( volume )
	sound.play()
	id = _ID_
	_ID_ += 1
	_SOUNDS.append( sound )
	
	return id
	
def stop_effect( id ):

	if not _SOUNDS[id]:
		pass
	else:
		_SOUNDS[id].stop()
		_SOUNDS[id] = None
		
def set_volume( vol ):
	#Not yet done, let's figure out if we want to do channel or sound
	pass