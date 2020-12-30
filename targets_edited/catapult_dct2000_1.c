if (*length > 0 && linebuff[*length-1] == '\n')	{ linebuff[*length-1] = '\0';*length = *length - 1;}

CWE-124
Write the null terminator at the proper place inside the buffer