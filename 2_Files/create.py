from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile(type=0)
track = MidiTrack()
mid.tracks.append(track)

track.append(MetaMessage('key_signature', key='C#'))
track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))

mid.save('new_song.mid')