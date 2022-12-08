Сборка и запуска образа

``` 
docker build -t mtu .
docker run -i -t mtu
```

Запуск скрипта
``` 
python3 mtu.py HOST
```
Параметры скрипта можно посмотреть через 
```
$python3 mtu.py -h
usage: mtu.py [-h] [-c C] host

PMTUD

positional arguments:
  host        discovery host

options:
  -h, --help  show this help message and exit
  -c C        count of ping by one discovery, by default 1
```