def on_on_chat():
    builder.move(LEFT, 5)
    builder.mark()
    builder.move(UP, 6)
    builder.move(LEFT, 6)
    builder.move(DOWN, 6)
    builder.move(RIGHT, 6)
    builder.trace_path(OBSIDIAN)
    player.say("Put Flint and Steel into the Obsidian frame")
player.on_chat("enterIntoNewDimension", on_on_chat)
