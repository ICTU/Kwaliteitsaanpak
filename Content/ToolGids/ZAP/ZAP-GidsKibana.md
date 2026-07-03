# ZAP in combinatie met Kibana
Wanneer je ZAP gebruikt voor het scannen van een applicatie in een testomgeving, is het vaak wenselijk om het ZAP-verkeer te onderscheiden van normaal verkeer. Door een specifieke **User-Agent**-header in te stellen in ZAP, kun je dit verkeer eenvoudig terugvinden en filteren in logsystemen zoals **Kibana** (op basis van bijvoorbeeld Elasticsearch-logs).

## Waarom wordt deze combinatie geadviseerd?
ZAP genereert veel verkeer en kan foutmeldingen of ongebruikelijke requests veroorzaken. Om analyses zuiver te houden en false positives in dashboards te vermijden, is het aan te raden ZAP-verkeer te markeren (met een tag) en uit te sluiten of juist te volgen in Kibana.

---

## Stap 1 – Stel de User-Agent in binnen ZAP
De User-Agent kan op meerdere manieren worden ingesteld, afhankelijk van hoe je ZAP gebruikt.

### Via de GUI
1. Open ZAP.
2. Ga naar **Tools** → **Options**.
3. Navigeer naar **HTTP Sessions** of **Connection** → **User-Agent**.
4. Voeg een custom User-Agent toe, bijvoorbeeld:  

### In een Automation Plan (YAML)

Je kunt ook een custom header instellen via een script of een request policy. Bijvoorbeeld via een script dat wordt opgenomen in je automation plan:

```yaml
jobs:
- type: requestor
 parameters:
   requests:
     - url: "https://example.org"
       method: "GET"
       headers:
         User-Agent: "ZAP-Scanner/1.0"



```


## Stap 2 – Filter ZAP-verkeer in Kibana
Zodra de requests zijn gelogd met deze specifieke User-Agent, kun je in Kibana eenvoudig filteren op dit verkeer om bijvoorbeeld foutanalyses of dashboards zuiver te houden.

### Voorbeelden van Kibana-queries

**Alle verkeer afkomstig van ZAP:**

```kql
user_agent.keyword: "ZAP-Scanner/1.0"

```

**Verkeer uitsluiten in visualisaties of zoekopdrachten:**
```kql
NOT user_agent.keyword: "ZAP-Scanner/1.0"
```

Let op: de exacte veldnaam kan variëren, afhankelijk van de ingest pipeline of logstructuur in jouw Elasticsearch-configuratie. Veelvoorkomende velden zijn `user_agent`, `http.user_agent` of `user_agent.keyword`.

## Best practices

- Gebruik een unieke en herkenbare User-Agent zoals `ZAP-Scanner/1.0` zodat je deze eenvoudig kunt terugvinden in logs.
    
- Leg in je testdocumentatie of Automation Plan vast welke User-Agent wordt gebruikt.
    
- Filter ZAP-verkeer standaard uit in je productiedashboards om verwarring of onterechte alerts te voorkomen.
    
- Overweeg om aparte dashboards of waarschuwingen op te zetten voor ZAP-verkeer, zodat je gestructureerd inzicht hebt in bevindingen uit penetratietests.
    
- Combineer de User-Agent met andere metadata (zoals IP-adres van je CI-runner) om verkeer nog betrouwbaarder te onderscheiden.
