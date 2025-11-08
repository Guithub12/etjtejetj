@echo off
setlocal

set WEBHOOKURL=https://discord.com/api/webhooks/1436701879651270838/LpU0hzJ3uGOmZDDRiVuuYeYhKlQshjQctG2DCe9ktoRy0FZXFc02wN5zWoO77C9dsD18

set MESSAGE=Persistance funktional!

curl -H "Content-Type: application/json" -X POST -d "{\"content\": \"%MESSAGE%\"}" %WEBHOOKURL%

