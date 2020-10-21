@ECHO OFF

set a=1
set b=1
set n=%1

set i=0
:loop
if %i% equ %n% goto:endloop
	set /a a=%b%*%a%
	set /a b+=1
	set /a i+=1
	goto:loop
:endloop
echo %a%