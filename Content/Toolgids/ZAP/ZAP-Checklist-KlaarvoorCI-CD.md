# ZAP-Checklist klaar voor CI/CD
Voordat je de scripts die je lokaal hebt opgebouwd kunt deployen in de pipeline, is het goed om onderstaande punten na te lopen.

- Context juist ingericht (auth, include/exclude)  
- Variabelen consistent gebruikt (`${base_url}` etc.)  
- Sequence (.zst) opgenomen en getest  
- Scanlimieten ingesteld  
- Rapporten schrijven naar `reports/`  
- `exitStatus` ingesteld (fail op Medium, of anders waar nodig.)  
- Rapporten geüpload als artefact  

![Screenshot van menu](Images/Context_aanmaken.png "Screenshot van menu")
