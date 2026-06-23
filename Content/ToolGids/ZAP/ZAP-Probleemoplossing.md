## Probleemoplossing

- **Browser start niet bij opname**: start Firefox handmatig; ZAP snuffelt via proxy.  
- **Geen output bij sequence headless**: gebruik GUI *Output-tab*.  
- **Context mismatch**: Automation-context ≠ GUI-context → plan opnieuw genereren.  
- **SAML-token faalt in CI**: token elke run vernieuwen via sequence of regex.  
- **Regex lastig**: gebruik add-on *Regular Expression Tester*.  
- **Scans lopen eindeloos**: altijd `maxScanDurationInMins` instellen + `exitStatus`.  
![[Pasted image 20251003102208.png]]

# Bekende beperkingen
## HTTP Request methods

Naast HTTP GET, HTTP POST en HTTP PUT zijn er nog meer [request methods](https://en.wikipedia.org/wiki/HTTP#Request_methods) zoals HTTP PATCH. ZAP ondersteunt dit nog (in 2025) niet.

Wanneer je PATCH in een sequence probeert te gebruiken, stopt de sequence bij de overview. Als je PATCH via een andere route probeert te implementeren, krijg je de volgende foutmelding:

```java
java.lang.IllegalArgumentException: Method not supported: PATCH
```

# Loggen in Zest-scripts

Zest-scripts bieden geen directe ondersteuning voor logging naar `stdout`, zeker niet in headless modus. Wil je toch logberichten gebruiken binnen een Zest-script, dan zijn er enkele alternatieve werkwijzen:

- Gebruik de `ZestActionPrint` om een waarde op te slaan in een variabele.
- Log deze variabele via een secundair mechanisme, zoals:
  - een custom scan rule
  - een apart script dat de uitvoer verwerkt

Let op: standaard logging vanuit Zest werkt niet zoals je wellicht gewend bent bij andere scriptalen. Test dit goed bij gebruik in een pipeline.
# Redirects (HTTP 303) handmatig afhandelen

In tegenstelling tot een normale webbrowser volgt ZAP een **HTTP 303-redirect** niet automatisch. Dit kan ertoe leiden dat een testscript stopt of faalt nadat een POST-verzoek een `303 See Other` statuscode teruggeeft. Om dit gedrag te corrigeren, moet je de redirect handmatig afhandelen binnen je script of automation plan.
## Oplossing: handmatig de `Location`-header verwerken

De HTTP 303-redirect bevat in de response-header een `Location`-veld met de URL waarheen het verzoek doorgestuurd moet worden. Om deze waarde te extraheren en te gebruiken in een volgend verzoek, volg je onderstaande stappen:

1. **Maak een variabele aan via `Edit Assignment`**  
   Voeg in je script een `Edit: Set Variable` stap toe.

![](img/zap-demo-10.png)

3. **Lees de `Location`-header uit de response**  
   Gebruik de optie om een variabele te vullen met de waarde van een specifieke header.

4. **Gebruik regex voor prefix en postfix**  
   Stel een prefix-regex in (bijvoorbeeld `Location: `) en een postfix-regex (zoals een newline of einde van de regel) om alleen de URL uit de header te isoleren.

5. **Gebruik de variabele in een volgend request**  
   Je kunt de nieuwe URL uit de `Location`-header vervolgens gebruiken in een opvolgend `Request`-object of stap binnen je Zest-script of automation plan.

![](img/zap-demo-11.png)

## ⚠️ Let op
- Deze aanpak vereist dat je werkt met Zest of met aangepaste scripting binnen je automation plan.
    
- Test dit goed, want een fout in je regex kan ertoe leiden dat je een onvolledige of ongeldige URL gebruikt.
