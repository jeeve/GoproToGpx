mkdir .\exports
if [%1]==[] goto :eof
:loop
.\bin\ffmpeg -i "%~1" > output.txt 2>&1
for /F "delims=" %%a in ('FINDSTR "gpmd" output.txt') do set line=%%a
echo "%line%"
set stream= %line:~12,3%
echo "%stream%"
START /WAIT .\bin\ffmpeg -y -i "%~1" -codec copy -map "%stream%" -f rawvideo "%~n1".bin
START /WAIT .\bin\gpmd2csv -i "%~n1".bin -o exports/"%~n1".csv
START /WAIT .\bin\gopro2gpx -i "%~n1".bin -o exports/"%~n1".gpx
START /WAIT .\bin\gopro2json -i "%~n1".bin -o exports/"%~n1".json
START /WAIT .\bin\gps2kml -i "%~n1".bin -o exports/"%~n1".kml
DEL "%~n1".bin
DEL output.txt
shift
if not [%1]==[] goto loop
