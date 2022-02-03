#ifndef SLIDE_LINE
#define SLIDE_LINE
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#define SLIDE_RIGHT 1 // 0 or 1 to indicate direction
#define SLIDE_LEFT 0 // 0 or 1 to indicate direction

int slide_line(int *line, size_t size, int direction);

#endif // SLIDE_LINE