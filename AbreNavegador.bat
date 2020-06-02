@echo off

echo 'Iniciando servidor, Aguarde!'
ping 127.0.0.1 -n 5 >null

start "Chrome" chrome --app=http://127.0.0.1:8000/ 

exit