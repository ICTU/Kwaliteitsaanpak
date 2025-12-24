# Functional suitability

Capability of a product to provide functions that meet stated and implied needs of intended users when it is used under specified conditions.

Opmerking: functional suitability gaat alleen over of, en in welke mate, expliciete en impliciete behoeften worden afgedekt en betreft niet de functionele eisen zelf.

## Functional completeness

Capability of a product to provide a set of functions that covers all the specified tasks and intended users’ objectives.

#include "Content/Templates/NFE/Eisentabel.md"

## Functional correctness

Capability of a product to provide accurate results when used by intended users.

#include "Content/Templates/NFE/Eisentabel.md"

## Functional appropriateness

Capability of a product to provide functions that facilitate the accomplishment of specified tasks and objectives.

#include "Content/Templates/NFE/Eisentabel.md"

# Performance-efficiency

Capability of a product to perform its functions within specified time and throughput parameters and be efficient in the use of resources under specified conditions.

## Time behavior

Capability of a product to perform its specified function under specified conditions so that the response time and throughput rates meet the requirements.

#include "Content/Templates/NFE/Eisentabel.md"

## Resource utilization

Capability of a product to use no more than the specified amount of resources to perform its function under specified conditions.

#include "Content/Templates/NFE/Eisentabel.md"

## Capacity

Capability of a product to meet requirements for the maximum limits of a product parameter.

#include "Content/Templates/NFE/Eisentabel.md"

# Compatibility

Capability of a product to exchange information with other products, and/or to perform its required functions while sharing the same common environment and resources.

## Co-existence

Capability of a product to perform its required functions efficiently while sharing a common environment and resources with other products, without detrimental impact on any other product.

#include "Content/Templates/NFE/Eisentabel.md"

## Interoperability

Capability of a product to exchange information with other products and mutually use the information that has been exchanged.

#include "Content/Templates/NFE/Eisentabel.md"

# Interaction capability

Capability of a product to be interacted with by specified users to exchange information between a user and a system via the user interface to complete the intended task.

## Appropriateness recognizability

Capability of a product to be recognized by users as appropriate for their needs.

#include "Content/Templates/NFE/Eisentabel.md"

## Learnability

Capability of a product to have specified users learn to use specified product functions within a specified amount of time.

#include "Content/Templates/NFE/Eisentabel.md"

## Operability

Capability of a product to have functions and attributes that it easy to operate and control.

#include "Content/Templates/NFE/Eisentabel.md"

## User error protection

Capability of a product to prevent operation errors.

#include "Content/Templates/NFE/Eisentabel.md"

## User engagement

Capability of a product to present functions and information in an inviting and motivating manner encouraging continued interaction.

#include "Content/Templates/NFE/Eisentabel.md"

## Inclusivity

Capability of a product to be utilised by people of various backgrounds.

| Nr.  | Eis  | Rationale | Realisatie door | Verificatie |
| :--- | :--- | :-------- | :-------------- | :---------- |
| 1   | De applicatie voldoet aan de [WCAG2.2](https://www.w3.org/Translations/WCAG22-nl/) succescriteria, niveau A en AA | [WCAG2.1](https://www.w3.org/Translations/WCAG21-nl/) is een wettelijke verplichting volgend uit [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf). [WCAG2.2 voegt negen criteria toe ten opzichte van versie 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) ten opzichte van versie 2.1  en wordt [aangeraden](https://www.digitaleoverheid.nl/nieuws/nieuwe-aanbevolen-standaard-digitale-toegankelijkheid/) door het platform Digitale Overheid van het Ministerie van BZK voor nieuwe websites en applicaties. Zie de bijlage "WCAG2.2 successcriteria" voor een tabel met de succescriteria. Per succescriterium is aangegeven of Axe-core, en zo ja met welke regels, het criterium geautomatiseerd kan controleren. {Geef aan of de succescriteria die Axe-core niet geautomatiseerd kan controleren wel of niet met de hand zullen worden gecontroleerd.} | ICTU | Axe-core rapportage {en handmatige rapportage} |

## User assistance

Capability of a product to be used by people with the widest range of characteristics and capabilities to achieve specified goals in a specified context of use.

#include "Content/Templates/NFE/Eisentabel.md"

## Self-descriptiveness

Capability of a product to present appropriate information, where needed by the user, to make its capabilities and use immediately obvious to the user without excessive interactions with a product or other resources.

#include "Content/Templates/NFE/Eisentabel.md"

## Taal en leesbaarheid

Naast de aan NEN-ISO/IEC 25010:2023 ontleende hoofdeigenschap bruikbaarheid zijn voor de gebruikskwaliteit van {het product} van belang:

* Taal: welke talen dienen te worden ondersteund.
* Leesbaarheid: teksten moeten makkelijk te lezen zijn. Korte zinnen hebben de voorkeur. Hoe gemakkelijker de zin en de woorden, hoe beter de leesbaarheid.

| Nr.  | Eis  | Rationale | Realisatie door | Verificatie |
| :--- | :--- | :-------- | :-------------- | :---------- |
| 1    | De applicatie gebruikt maximaal taalniveau B1 | [Aanbevolen richtlijn](https://www.communicatierijk.nl/vakkennis/rijkswebsites/aanbevolen-richtlijnen/taalniveau-b1) | {opdrachtgever} | {verificatie} |
| 2    | De applicatie ondersteunt {ondersteunde talen} | {rationale} | ICTU | {verificatie} |

# Reliability

Capability of a product to perform specified functions under specified conditions for a specified period of time without interruptions and failures.

## Faultlessness

Capability of a product to perform specified functions without fault under normal operation.

#include "Content/Templates/NFE/Eisentabel.md"

## Availability

Capability of a product to be operational and accessible when required for use.

#include "Content/Templates/NFE/Eisentabel.md"

## Fault tolerance

Capability of a product to operate as intended despite the presence of hardware or software faults.

#include "Content/Templates/NFE/Eisentabel.md"

## Recoverability

Capability of a product in the event of an interruption or a failure to recover the data directly affected and re-establish the desired state of the system.

#include "Content/Templates/NFE/Eisentabel.md"

# Security

Capability of a product to protect information and data so that persons or other products have the degree of data access appropriate to their types and levels of authorization, and to defend against attack patterns by malicious actors.

| Nr.  | Eis   | Rationale   | Realisatie door | Verificatie   |
|:-----|:------|:------------|:----------------|:--------------|
| 1    | Voldoen aan de BIO- en SDD-maatregelen ten aanzien van informatiebeveiliging | BIO en SSD bevatten een aantal maatregelen ten aanzien van software en/of de infrastructurele componenten waar de software gebruik van maakt. Zie de bijlage "BIO- en SDD-maatregelen". | ICTU | {penetratietest en/of een secure code review}, te organiseren door {ICTU of opdrachtgever} |
| {nr} | {eis} | {rationale} | {partij}        | {verificatie} |

## Confidentiality

Capability of a product to ensure that data are accessible only to those authorized to have access.

#include "Content/Templates/NFE/Eisentabel.md"

## Integrity

Capability of a product to ensure that the state of its system and data are protected from unauthorized modification or deletion either by malicious action or computer error.

#include "Content/Templates/NFE/Eisentabel.md"

## Non-repudiation

Capability of a product to prove that actions or events have taken place, so that the events or actions cannot be repudiated later.

#include "Content/Templates/NFE/Eisentabel.md"

## Accountability

Capability of a product to enable actions of an entity to be traced uniquely to the entity.

#include "Content/Templates/NFE/Eisentabel.md"

## Authenticity

Capability of a product to prove that the identity of a subject or resource is the one claimed.

#include "Content/Templates/NFE/Eisentabel.md"

## Resistance

Capability of a product to sustain operations while under attack from a malicious actor.

#include "Content/Templates/NFE/Eisentabel.md"

# Maintainability

Capability of a product to be modified by the intended maintainers with effectiveness and efficiency.

## Modularity

Capability of a product to limit changes to one component from affecting other components.

#include "Content/Templates/NFE/Eisentabel.md"

## Reusability

Capability of a product to be used as assets in more than one system, or in building other assets.

#include "Content/Templates/NFE/Eisentabel.md"

## Analysability

Capability of a product to be effectively and efficiently assessed regarding the impact of an intended change to one or more of its parts, to diagnose it for deficiencies or causes of failures, or to identify parts to be modified.

#include "Content/Templates/NFE/Eisentabel.md"

## Modifiability

Capability of a product to be effectively and efficiently modified without introducing defects or degrading existing product quality.

#include "Content/Templates/NFE/Eisentabel.md"

## Testability

Capability of a product to enable an objective and feasible test to be designed and performed to determine whether a requirement is met.

#include "Content/Templates/NFE/Eisentabel.md"

# Flexibility

Capability of a product to be adapted to changes in its requirements, contexts of use, or system environment.

## Adaptability

Capability of a product to be effectively and efficiently adapted for or transferred to different hardware, software or other operational or usage environments.

#include "Content/Templates/NFE/Eisentabel.md"

## Scalability

Capability of a product to handle growing or shrinking workloads or to adapt its capacity to handle variability.

#include "Content/Templates/NFE/Eisentabel.md"

## Installability

Capability of a product to be effectively and efficiently installed successfully and/or uninstalled in a specified environment.

#include "Content/Templates/NFE/Eisentabel.md"

## Replaceability

Capability of a product to replace another specified product for the same purpose in the same environment.

#include "Content/Templates/NFE/Eisentabel.md"

# Safety

Capability of a product under defined conditions to avoid a state in which human life, health, property, or the environment is endangered.

## Operational constraint

Capability of a product to constrain its operation to within safe parameters or states when encountering operational hazard.

#include "Content/Templates/NFE/Eisentabel.md"

## Risk identification

Capability of a product to identify a course of events or operations that can expose life, property or environment to unacceptable risk.

#include "Content/Templates/NFE/Eisentabel.md"

## Fail safe

Capability of a product to automatically place itself in a safe operating mode, or to revert to a safe condition in the event of a failure.

#include "Content/Templates/NFE/Eisentabel.md"

## Hazard warning

Capability of a product to provide warnings of unacceptable risks to operations or internal controls so that they can react in sufficient time to sustain safe operations.

#include "Content/Templates/NFE/Eisentabel.md"

## Safe integration

Capability of a product to maintain safety during and after integration with one or more components.

#include "Content/Templates/NFE/Eisentabel.md"
