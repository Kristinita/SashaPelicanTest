@REM @Author: Kristinita
@REM @Date:   2018-03-03 07:55:41
@REM @Last Modified by:   Kristinita
@REM Modified time: 2018-03-03 19:21:28
rem Disable echo command and cwd in output:
rem https://serverfault.com/a/187358/351829
@echo off
cd output
FOR /R %%i IN (*.html) DO echo %%i & tidy -mq --wrap 0 %%i