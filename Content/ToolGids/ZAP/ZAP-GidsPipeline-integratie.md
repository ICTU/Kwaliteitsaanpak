# ZAP-Gids Pipeline-integratie
## Portabiliteit en omgevingsvariabelen
Bij het werken met ZAP Automation Plans is het belangrijk om rekening te houden met portabiliteit. Scripts die lokaal goed functioneren, kunnen in een CI/CD-omgeving onverwachte problemen opleveren. Dit komt voornamelijk doordat omgevingsvariabelen (environment variables) anders zijn ingericht op een ontwikkelmachine dan in een pipeline-omgeving.

## Omgevingsvariabelen in YAML

Het ZAP Automation Framework interpreteert **géén** omgevingsvariabelen automatisch in YAML-velden zoals `urls` of `includePaths`. In tegenstelling tot bijvoorbeeld shellscripts of Docker Compose, wordt een waarde als `${RELEASE_NAME}` door ZAP beschouwd als een letterlijke string, tenzij je deze gebruikt in:

- een Zest-script, of
- een expliciet ondersteund veld zoals `env.parameters`

Houd hier dus rekening mee bij het verplaatsen of hergebruiken van automation plans tussen verschillende omgevingen.

⚠️ Variabelen in sequence worden niet overgenomen uit automation plan.

Je moet daarom een shell-script maken met `envsubst`
  
![Screenshot van terminal](Images/Pasted%20image%2020250728160826.png "Screenshot van terminal")

## ZAP-scan in GitLab CI/CD

De ZAP-scan is geïntegreerd in de GitLab CI/CD-pipeline als een job in het bestand `.gitlab-ci.yml`. Deze taak doet het volgende:

1. Draait in de *zap*-stage van de pipeline.  
2. Gebruikt het Docker-image `zaproxy/zaproxy:stable`.  
3. Wordt uitgevoerd voor zowel merge requests als de main-branch.  
4. Stelt omgevingsvariabelen in op basis van de context (merge request of main-branch).  
5. Vervangt variabelen in de configuratiebestanden.  
6. Start de ZAP-scan met het commando `zap.sh` en het automation plan `zap-scan.yaml`.  
7. Slaat de rapporten op als artefacten, die toegankelijk zijn via de GitLab-UI.  

## Lokaal uitvoeren van de ZAP-scan met run-zap-scan.sh
De `run-zap-scan.sh` wordt gebruikt om ZAP-scans lokaal uit te voeren.

```bash
  ./run-zap-scan.sh -r mr155
```

De volgende acties worden uitgevoerd:
1. Maakt een tijdelijke directorystructuur aan voor ZAP-scanresultaten.
2. Stelt omgevingsvariabelen in (RELEASE_NAME, ZEST_SCRIPT, ENCODING_SCRIPT).
3. Vervangt omgevingsvariabelen in configuratiebestanden.
4. Voert de ZAP-scan uit met behulp van Docker met de zaproxy/zap-stable-image.
5. Slaat de scanresultaten op in de tijdelijke directory.
## Gebruik
Om de ZAP-scan lokaal uit te voeren,  gebruik het onderstaande commando.
```bash
  ./run-zap-scan.sh -r mr155
```

Na het uitvoeren van het script zijn de scanrapporten te vinden in de map `./zap-temp/reports`.
## Debuggen
Het script bevat uitgecommentarieerde code voor debuggingdoeleinden. Om de ZAP-container te openen voor debugging: 
1. Verwijder de opmerkingen uit het debugginggedeelte in het script
2. Voer het script uit
3. Je komt terecht in een shell binnen de ZAP-container
