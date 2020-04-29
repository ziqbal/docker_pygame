

import os
import sys
import time
import datetime
import random
from threading import Thread

import pygame





def pygame_helloworld_events_update( ) :

    for event in pygame.event.get( ) :

        if event.type == pygame.QUIT :

            return( False )

        elif event.type == pygame.KEYUP :

            if event.key == pygame.K_ESCAPE :

                return( False )

    return( True )



pygame.init( )

pygame_helloworld_screen_width = 256
pygame_helloworld_screen_height = 256

pygame_helloworld_screen_surface = pygame.display.set_mode( ( pygame_helloworld_screen_width , pygame_helloworld_screen_height ) )

pygame.display.set_caption( "Hello World!" )



def pygame_helloworld_task_tick( tid ) :
    #print("pygame_helloworld_task_tick tid = " + str( tid ) )
    time.sleep( 1 )




pygame_helloworld_thread_running = False

#####################################################


def pygame_helloworld_thread_proc( tid ) :

    print( "pygame_helloworld_thread_ starting " + str( tid ) )

    while( pygame_helloworld_thread_running == True ) :

        pygame_helloworld_task_tick( tid )

        time.sleep( 0.1 )

    print( "pygame_helloworld_thread_ stopping" )

#####################################################

pygame_helloworld_thread_obj1 = Thread( target = pygame_helloworld_thread_proc , args = ( 1 , ) )
pygame_helloworld_thread_obj2 = Thread( target = pygame_helloworld_thread_proc , args = ( 2 , ) )

#####################################################

def pygame_helloworld_thread_start( ) :

    global pygame_helloworld_thread_running

    pygame_helloworld_thread_running = True

    pygame_helloworld_thread_obj1.start( )
    pygame_helloworld_thread_obj2.start( )

#####################################################

def pygame_helloworld_thread_stop( ) :

    global pygame_helloworld_thread_running

    pygame_helloworld_thread_running = False



def pygame_helloworld_loop_step( ) :

    pygame_helloworld_screen_surface.fill( ( 0,0,0 ) )


    x1=random.randint( 0 , pygame_helloworld_screen_width )
    y1=random.randint( 0 , pygame_helloworld_screen_height)
    x2=random.randint( 0 , pygame_helloworld_screen_width )
    y2=random.randint( 0 , pygame_helloworld_screen_height)

    pygame.draw.line( pygame_helloworld_screen_surface,(0,255,0),(x1,y1),(x2,y2));


    pygame.display.update( )

    time.sleep( 0.1 )




pygame_helloworld_screen_surface.fill( ( 0 , 0 , 0 ) )

######################################################################

trigger_start = 0
trigger_delay = 42

pygame_helloworld_thread_start( )

######################################################################

pygame_helloworld_gamemaster_running = True

while pygame_helloworld_gamemaster_running :

    if( not pygame_helloworld_events_update( ) ) :
        pygame_helloworld_thread_stop( )
        pygame_helloworld_gamemaster_running = False

    trigger_current = int( round( time.time( ) * 1000 ) )

    if( ( trigger_current - trigger_start ) >= trigger_delay ) :

        pygame_helloworld_loop_step( )

        #pygame.display.update( )

        trigger_start = trigger_current

    time.sleep( 0.01 )

######################################################################

pygame_helloworld_thread_stop( )

pygame.quit( )


