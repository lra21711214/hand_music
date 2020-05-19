# coding=utf-8
import subprocess
import shlex
import json


# Control iTunes
class Control():
	# Make sure iTunes is running, if it isn't, launch iTunes.
	check_startup = 'osascript -e \'if application "Music" is not running then\ntell application "Music" to activate\nend if \''
	subprocess.Popen(shlex.split(check_startup),stdout=subprocess.PIPE,universal_newlines=True)
	# Pause music
	def pause():
		Script_execution.run('pause')
	# Play music
	def play():
		Script_execution.run('play')
	# Play playlist
	def play_list(playlist_name):
		script = f'play playlist "{playlist_name}"'
		Script_execution.run(script)
	# If the music is playing, stop the music and if the music is stopped, play the music.
	def playpause():
		Script_execution.run('playpause')
	# Stop music
	def stop():
		Script_execution.run('stop')
	# Play next track
	def next_track():
		Script_execution.run('next track')
	# Play from the beginning.
	def back_track():
		Script_execution.run('back track')
	# Play previous track
	def previous_track():
		Script_execution.run('previous track')
# Get iTunes data and return data
class Get_data():
	# Get current track name
	def current_track():
		script = 'osascript -e \'tell application "Music"\nreturn name of current track\nend tell\''
		return(Script_execution.get(script))
	# Get current track artist name
	def current_track_artist():
		script = 'osascript -e \'tell application "Music"\nreturn artist of current track\nend tell\''
		return(Script_execution.get(script))
	# Get current track album name
	def current_track_album():
		script = 'osascript -e \'tell application "Music"\nreturn album of current track\nend tell\''
		return(Script_execution.get(script))
	# Get current track data(track name, artist name, album name) and return json
	def current_all():
		track = Get_data.current_track()
		artist = Get_data.current_track_artist()
		album = Get_data.current_track_album()
		return(json.dumps({'track':track,'artist':artist,'album':album},ensure_ascii=False))
class Script_execution():
	# Run osascript
	def run(script_to_execute):
		script = f'osascript -e \'tell application "Music"\n{script_to_execute}\nend tell\''
		subprocess.Popen(shlex.split(script),stdout=subprocess.PIPE,universal_newlines=True)
	# Run osascript and return itune data to function
	def get(script):
		acquisition_data,_ = subprocess.Popen(shlex.split(script),stdout=subprocess.PIPE,universal_newlines=True).communicate()
		return(acquisition_data.strip())


