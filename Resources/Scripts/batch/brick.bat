FOR /F "delims=" %%i IN ('type "Z:\Applications\Mac Hill.app\Contents\Resources\server.txt"') DO set server=%%i
"C:\users\Wineskin\AppData\Roaming\Brick Hill\Player.exe" %server%
