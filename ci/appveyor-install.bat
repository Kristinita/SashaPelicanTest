@REM @Author: Kristinita
@REM @Date:   2018-02-28 19:42:16
@REM @Last Modified by:   Kristinita
@REM Modified time: 2018-03-04 17:12:45
@REM Parallel pip and npm commands.
@REM Use REM comments:
@REM https://stackoverflow.com/a/12407934/5951529
@REM Hide REM lines from showing, use @ symbol:
@REM https://www.computerhope.com/issues/ch001313.htm
@REM https://jpsoft.com/help/rem.htm
@REM CMD command /C option run another console; without /C option command doesn't work:
@REM https://ss64.com/nt/cmd.html
@REM START command /B option, that output from another consoles move to head console
@REM https://ss64.com/nt/start.html
@REM [WARNING] Use -ignoredependencies for HTML Tidy installation to AppVeyor
@REM https://github.com/majkinetor/au-packages/issues/75
@REM https://ci.appveyor.com/project/Kristinita/sashatidydebugging/build/1.0.12
START /B CMD /C "choco install html-tidy -y -ignoredependencies"
START /B CMD /C "pip install --upgrade pip & pip install pipenv & pipenv install --dev"
START /B CMD /C "choco install nodejs -y & npm install -g grunt-cli & npm install"
