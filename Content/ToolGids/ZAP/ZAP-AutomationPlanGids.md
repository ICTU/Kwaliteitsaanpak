# ZAP Automation-plan-gids
## Automation Plan met quality gate
Een compleet plan dat **verkenning, scanning, rapportage en quality gates** combineert:

```yaml
env:
  parameters:
    base_url: "https://test.example.org"
contexts:
  - name: app
    urls: ["${base_url}"]
    includePaths: ["${base_url}.*"]

jobs:
  - type: passiveScan-config
    parameters:
      maxAlertsPerRule: 1000

  - type: activeScan-config
    parameters:
      maxScanDurationInMins: 30
      maxRuleDurationInMins: 5
      threadPerHost: 2

  - type: openapi
    parameters:
      context: app
      targetUrl: "${base_url}"
      apiUrl: "${base_url}/v3/api-docs"

  - type: spider
    parameters:
      context: app
      url: "${base_url}"
      maxDuration: 5

  - type: ajaxSpider
    parameters:
      context: app
      url: "${base_url}"
      maxDuration: 5

  - type: activeScan
    parameters:
      context: app

  - type: report
    name: html
    parameters:
      template: traditional-html
      reportDir: /zap/wd/reports
      reportTitle: "ZAP Scan"

  - type: report
    name: xml
    parameters:
      template: traditional-xml
      reportDir: /zap/wd/reports

  - type: exitStatus
    parameters:
      warnLevel: Low
      errorLevel: Medium
```

## Runnen in Docker:
```bash
docker run --rm -t -u zap   -v "$PWD":/zap/wd   ghcr.io/zaproxy/zap-stable:latest   zap.sh -cmd -autorun /zap/wd/af-plan.yaml
```
