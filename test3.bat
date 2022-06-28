@echo off
set file=data/cameras.txt
set /A i=0

for /F "usebackq delims=" %%a in ("%file%") do (
set /A i+=1
call echo %%i%%
call set array[%%i%%]=%%a
call set n=%%i%%
)

for /L %%i in (1,1,%n%) do call echo %%array[%%i]%%

PAUSE