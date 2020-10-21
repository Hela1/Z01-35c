@ECHO OFF

net session >nul 2>&1
if %ERRORLEVEL% == 0 (
	echo JEST ADMINISTRATOREM
) else (
	echo NIE MA UPRAWNIEN ADMINISTRATORA
)