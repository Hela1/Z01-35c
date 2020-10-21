@ECHO OFF

set a=1
set b=1
set n=%1

set i=0
:loop
if %i% equ %n% goto:endloop
	echo %a%
	set /a tmp=%a%+%b%
	set /a a=%b%
	set /a b=%tmp% 
	set /a i+=1
	goto:loop
:endloop