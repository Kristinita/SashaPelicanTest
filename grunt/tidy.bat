@REM @Author: Kristinita
@REM @Date:   2018-03-03 07:55:41
@REM @Last Modified by:   Kristinita
@REM Modified time: 2018-03-03 12:37:17
FOR /R %%i IN (*.html) DO tidy -mq -utf8 -config "../tidy-config.txt" %%i