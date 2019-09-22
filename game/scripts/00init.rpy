'''This is the initialization for our watercress VN codenamed Citrus'''

#characters go here
define lim = Character("Lime", color="#66B649", callback=speaker("lim"))
define lem = Character("Lemon", color="#FBD98A", callback=speaker("lem"))

init python:
    # define the BGs
    DefineImages('cgs')
    DefineImages('bgs', prepend='bg')
    DefineImages('mainmenu', prepend='mm')

    # define the sprites with manual layer ordering
    #layerorder = None
    layerorder = ['base','mouth','eyes', 'brow']
    DefineImages("sprites", composite=True, overrideLayerOrder=layerorder)

    # manually create shortcuts to more complex expressions
    MapEmote('lim speak',  'lim m_default')
    MapEmote('lem speak',  'lem m_default')

transform centerleft:
    xalign 0.2

transform centerright:
    xalign 0.8

#CGs go here

#Backgroudns go here
