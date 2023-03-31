#include <X11/Xlib.h>
#include <assert.h>
#include <unistd.h>

#define NIL (0)

int main(){
  
  Display *dpy=XOpenDisplay(NIL);
  assert(dpy);
  int black=BlackPixel(dpy,DefaultScreen(dpy));
  int white=WhitePixel(dpy,DefaultScreen(dpy));
  
  Window w=XCreateSimpleWindow(dpy, DefaultRootWindow(dpy),0,0,200,100,0,black,black);
  XSelectInput(dpy,w,StructureNotifyMask);
  XMapWindow(dpy,w);
  GC gc = XCreateGC(dpy,w,0,NIL);
  XSetForeground(dpy,gc,white);
  for(;;) {
    XEvent e;
    XNextEvent(dpy,&e);
    if(e.type == MapNotify)
      break;
  }

  XDrawLine(dpy,w,gc,10,60,180,20);
  XFlush(dpy);
  sleep(10);

  return 0;
}
