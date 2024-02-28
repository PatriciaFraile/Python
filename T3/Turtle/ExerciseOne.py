from turtle import *
title('Exercise')

log = 300
an = 170

begin_fill
while True:
    forward(log)
    right(an)
    if abs (pos())<1:
        break
end_fill
mainloop()