#!/usr/bin/env python
""" Pygame BlueSky start script """
from __future__ import print_function
import pygame as pg
import bluesky as bs
from bluesky.ui.pygame import splash
from bluesky import cmdargs
from pprint import pprint


def PDEBUG(msg, obj=None):
    print("\033[0;34m[DEBUG] " + msg)
    if obj is not None:
        pprint(obj)
    print("\033[0m", end='')

def main():
    # HACK: Parse BlueSky Pygame arguments using BlueSky QtGL cmdargs
    args = cmdargs.parse()
    args['gui'] = 'pygame'
    args['mode'] = 'sim'
    PDEBUG("Program arguments", args)

    """ Start the mainloop (and possible other threads) """
    splash.show()
    bs.init(**args)
    # bs.sim.op()
    bs.scr.init()
    PDEBUG("Screen is initialized", bs.scr)

    if args['scenfile'] is not None:
        # Disable first time Keyboard.update()
        #
        # The first time Keyboard.update() would emit an empty 'IC' command
        # to reset the simulation with a Screen.show_file_dialog().
        # Simulation.init() already has scheduled an f'IC {scenfile}' command
        # so there is no need to Screen.show_file_dialog().
        bs.scr.keyb.firstx = False
    PDEBUG("Keyboard.firstx", bs.scr.keyb.firstx)

    # Main loop for BlueSky
    while not bs.sim.state == bs.END:
        bs.sim.update()   # Update sim
        bs.scr.update()   # GUI update

    bs.sim.quit()
    pg.quit()

    print('BlueSky normal end.')


if __name__ == '__main__':
    print("   *****   BlueSky Open ATM simulator *****")
    print("Distributed under GNU General Public License v3")
    # Run mainloop if BlueSky_pygame is called directly
    main()
