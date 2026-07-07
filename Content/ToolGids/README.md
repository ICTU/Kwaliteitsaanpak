# Bijdragen
De inhoud van de toolgidsen staat in `Content/ToolGids`. Hierin staat per tool een map. Voor het toevoegen van een toolgids voor een tool die nu nog niet beschreven is, moet er eerst een [DocumentDefinition](../../README.md#Documentdefinities) worden gemaakt.

- Werk altijd vanuit een issue op de backlog, maak eerst een branch in GitHub
- Check de branch lokaal uit
- Doe de wijzigingen in de contentbestanden
- Test het lokaal met 
```bash
uv run src/convert.py --log INFO DocumentDefinitions/tool-gids-dt.json
```

of wanneer je de ZAP-toolgids hebt aangepast:
```bash
uv run src/convert.py --log INFO DocumentDefinitions/tool-gids-zap.json
```



# Gebruikmaken van het Diátaxis-raamwerk
Om de informatie goed te structureren, is gebruikgemaakt van het Diátaxis-raamwerk.
De tabel hieronder kan helpen bij het bepalen welke informatie waar thuishoort.

| Als de inhoud…                             | …en het ondersteunt de gebruiker bij… | …dan hoort het thuis in een…                                                              |
| ------------------------------------------ | ------------------------------------- | ----------------------------------------------------------------------------------------- |
| informeert over een actie (praktisch/doen) | het aanleren van een vaardigheid      | tutorial / stap-voor-stap                                                                 |
| informeert over een actie (praktisch/doen) | het toepassen van een vaardigheid     | how-to gids / praktische gids / oplossingen (wanneer doe je X? / Wat moet je doen als Y?) |
| begrip te vergroten                        | het toepassen van een vaardigheid     | naslagwerk (Referenties en Links)                                                         |
| begrip te vergroten                        | het aanleren van een vaardigheid      | uitleg (begrijpen)                                                                        |

Meer info op de [Diátaxis-website](https://diataxis.fr/compass/).