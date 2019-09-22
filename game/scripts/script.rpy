
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lim at centerright
    show lem at centerleft

    # These display lines of dialogue.

    show lim speak

    lim "You've created a new Ren'Py game."

    show lem speak
    show lim default

    lem "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
