# ZAP-Gids Zest
## Wat is Zest?

**Zest** is een scripttaal ontwikkeld door Mozilla, specifiek voor security testing. Het is ontworpen om eenvoudig leesbare en herbruikbare scripts te maken die het gedrag van een gebruiker of aanvaller simuleren binnen ZAP. De doorontwikkeling van Zest wordt momenteel gedaan in de ZAP-repo en inmiddels niet meer in de repo van Mozilla.

Zest-scripts zijn:
- **Menselijk leesbaar** en gebaseerd op JSON-structuur
- **Herhaalbaar** en dus goed inzetbaar voor regressietests
- **Geïntegreerd** met ZAP: je kunt ze opnemen in automation plans, aanpassen via de ZAP-GUI en uitvoeren als onderdeel van scans

Zest wordt vaak gebruikt voor:
- Het automatisch uitvoeren van testscenario’s
- Het aanroepen van specifieke URL's met aangepaste headers of cookies
- Het controleren van verwachte responses en statuscodes
- Het vastleggen van testlogica op een declaratieve manier

Zest ondersteunt conditionele logica (zoals if-statements), logging, loops, en integratie met andere ZAP-functies zoals scan rules en contexten.

## Sequences opnemen (Zest)
Voor **stateful flows** (login, checkout, transacties) die spiders vaak missen.

1. **Opnemen**: *Scripts → Sequences → Record Sequence*. Doorloop scenario → stop → sla `.zst`.  
2. **Requests toevoegen**: via *Add to Script from History*.  
3. **Variabiliseren**: vervang vaste URL’s door `${base_url}`.  
4. **Debug**: voeg *Action → Print* toe; output zichtbaar in GUI.  
5. **Integreren in plan**:
```yaml
- type: script
  parameters:
    engine: Zest
    name: login-flow
    type: sequence
    file: "/zap/wd/sequences/login-flow.zst"
```
