
import curses
import sys

def main(argv):
  stdscr = curses.initscr()
  curses.noecho()
  curses.cbreak()
  curses.curs_set(False)
  if curses.has_colors():
    curses.start_color()
  # Optional - Enable the keypad. This also decodes multi-byte key sequences
  # stdscr.keypad(True)
  caughtExceptions = ""

  try:
    # Coordinates start from top left, in the format of y, x.
    stdscr.addstr(0, 0, "Hello, world!")
    screenDetailText = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
    startingXPos = int ( (curses.COLS - len(screenDetailText))/2 )
    stdscr.addstr(curses.LINES//2 - 2, startingXPos, screenDetailText)
    stdscr.addstr(curses.LINES//2, (curses.COLS - len("Press a key to quit."))//2, "Press a key to quit.")
    stdscr.refresh()
    stdscr.getch()
  except Exception as err:
   caughtExceptions = str(err)
  curses.nocbreak()
  curses.echo()
  curses.curs_set(True)
  # stdscr.keypad(False)
  curses.endwin()
  if "" != caughtExceptions:
   print ("Got error(s) [" + caughtExceptions + "]")

# if __name__ == "__main__":
#   main(sys.argv[1:])
main("")