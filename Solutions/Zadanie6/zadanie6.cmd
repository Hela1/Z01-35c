@ECHO OFF
SETLOCAL

if [%1]==[] goto:here
cd %1
:here

call:funkcyjka 0
goto:eof

:funkcyjka
set n=%~1
set /a nn=n+1
for /D %%s in (.\*) do (
	call:wciecie %n%
	echo %%s
	cd %%s
	call:funkcyjka %nn%
	cd ..\
)
EXIT /B


:wciecie
for /l %%i in (1,1,%~1) do (
	echo|set /p="------"
)
EXIT /B
