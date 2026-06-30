# ZAP Installatiegids
## Download en installatie voor desktop

Een OS-specifieke variant van de ZAP Desktop Tool kan worden opgehaald van:
[https://www.zaproxy.org/download/](https://www.zaproxy.org/download/)
Voor het opstarten van de tool is Java JRE versie 11 of hoger nodig (geen JDK). Anders verschijnt de volgende melding:

![zie je dit](ToolGids/Images/jre.png "hoi")

## Installatie en gebruik via Docker

```bash
docker run --rm -it   -u zap   -p 8090:8090 -p 8091:8091   -v "$PWD":/zap/wd   ghcr.io/zaproxy/zap-stable:latest sh
```
- Poort **8090** = proxy  
- Poort **8091** = API
