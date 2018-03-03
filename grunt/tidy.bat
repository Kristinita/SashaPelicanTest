@REM @Author: Kristinita
@REM @Date:   2018-03-03 07:55:41
@REM @Last Modified by:   Kristinita
@REM Modified time: 2018-03-03 07:57:19
FOR /R %%i IN (*.html) DO tidy -mq -config "../tidy-config.txt" %%i