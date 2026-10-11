# gonzalezasenjo2025 — Cost Allocation Methods and Their Properties in Energy Communities

- **File sorgente:** `Paper/Cost Allocation Methods and Their Properties in Energy Communities.pdf` (29 pagine, testo estraibile)
- **Tipo:** articolo su rivista (Energies, MDPI, open access); contributo **teorico/analitico**, nessun dato empirico ("Data Availability Statement: No data has been used in this paper", p. 13). Ripubblicato con una correzione minore non scientifica.
- **Lettura:** integrale (corpo pp. 1–13 e Appendici A–B con le dimostrazioni, pp. 14–28); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con "x of 29"). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
González-Asenjo, D.; Izquierdo, L. R.; Izquierdo, S. S. (2025). *Cost Allocation Methods and Their Properties in Energy Communities.* **Energies**, 18(23), 6236. https://doi.org/10.3390/en18236236. Ricevuto 30/9/2025; rivisto 20/11/2025; accettato 25/11/2025; pubblicato 27/11/2025. Universidad de Burgos; Instituto Tecnológico de Castilla y León; Universidad de Valladolid.

## 2. Obiettivo e research question
- **Obiettivo (autori, p. 2):** "providing a unified axiomatic characterization of cost allocation methods for energy communities": definire proprietà desiderabili (equità, "environmental friendliness", continuità) e valutare con esse otto CAM, con una tabella comparativa come contributo principale.
- **Gap dichiarato (p. 2, Sez. 1):** "to the best of our knowledge, there is currently no unified framework that allows researchers, practitioners, and policymakers to compare existing CAMs on a common basis" (p. 2); inoltre i termini "fairness", "stability", "equity" sono usati con significati diversi (p. 4).
- **RQ formulata come domanda?** Sì, in forma implicita: "How are these aggregate savings shared among the members of the community?" (p. 2).

## 3. Contesto
- **Paese / quadro normativo:** nessuno (modello stilizzato); riferimenti generali a RED II.
- **Tipo di CER:** comunità con unità di generazione condivisa; energia generata allocata ai membri con frazioni `α_a` arbitrarie (p. 5).
- **Membri:** n generici; distinzione fra Net Consumers (NC), Net Producers (NP) e N0 a seconda che il consumo superi o no l'energia allocata (p. 5).

## 4. Metodo
- **Modello (Sez. 2.1, p. 5):** un singolo slot temporale; prezzi di rete fissi `p_b > p_s > 0`; consumo/generazione noti e deterministici; costo totale `C = p_b[E_c − E_g]⁺ − p_s[E_g − E_c]⁺` (Eq. 1); risparmio da condivisione `(p_b − p_s)·E_Tr` con `E_Tr = min(E_NC, E_NP)` (Eq. 4); valore di coalizione `v(S) = (p_b − p_s)·min(Σ_{a∈S} e_a^NC, Σ_{a∈S} e_a^NP)` (p. 7).
- **Valutazione:** interamente analitica (proposizioni e controesempi, Appendici A–B), "without the need for simulations or empirical data" (p. 10).
- **Software / dati:** nessuno; `[NON SPECIFICATO]` il tipo di "extensive simulations" usate per la congettura sul nucleolo (p. 11).

## 5. Meccanismi di ripartizione analizzati (otto CAM, tre famiglie; Sez. 2.3)
- **Simple rules:** All Equal (AE); Bill Sharing (BS, equivale a prezzo di trasferimento zero).
- **Savings-based:** quote prestabilite `β_a`; proporzionale a `α_a`; **Shapley**; **nucleolus**.
- **Price-based:** Average Price (`p_tr = (p_b + p_s)/2`); Extreme Price (tutto il risparmio al lato scarso del mercato interno).

## 6. Metriche
**Sette proprietà assiomatiche (Sez. 2.4, pp. 9–10):** P1 parità fra eguali; P2 disparità fra diseguali; P3 partecipazione individuale vantaggiosa; P4 environmental friendliness (costo monotono crescente rispetto al consumo individuale, anche versione weak); P5 continuità; P6 correlazione di rango fra costo e consumo netto (anche weak); P7 partecipazione di gruppo vantaggiosa (appartenenza al core). Nessuna metrica numerica economica, ambientale, sociale o di engagement.

## 7. Risultati principali (Tab. 1, p. 11; dimostrazioni in Appendice)
| CAM | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|---|---|---|---|---|---|---|---|
| All Equal | Y | N | N | Y | Y | Y (weak) | N |
| Bill Sharing | Y | N | N | Y (weak) | Y | Y (weak) | N |
| Quote β_a | N | N | Y | Y | Y | N | N |
| Prop. α_a | N | N | Y | Y | Y | N | N |
| Shapley | Y | Y | Y | Y | Y | Y | **N** |
| Nucleolus | Y | ? | Y | ? | Y | ? | Y |
| Average Price | Y | Y | Y | Y | Y | Y | **N** |
| Extreme Price | Y | Y | Y | **N** | **N** | Y | Y |
- **Average Price** soddisfa le stesse proprietà dello Shapley ed è computazionalmente banale (p. 11). **Extreme Price** è l'unico metodo price-based che soddisfa P7, ma viola P4 e P5; Proposizioni 2 e 3: nessun CAM price-based può soddisfare insieme P4 e P7, né P5 e P7 (p. 12).
- **Nucleolo:** soddisfa P1, P3, P5, P7; per P2, P4, P6 "we have not been able to prove (or disprove) compliance"; "Based on extensive simulations and intuition, we conjecture that the nucleolus does, in fact, satisfy all seven properties" (p. 11).
- **Posizione sullo Shapley (p. 8):** "a minimum requirement for a CAM to be considered fair is to provide an allocation which is in the core [...] Since the Shapley value does not fulfill this requirement, we would not qualify it as fair." Controesempio tramite "glove game" (App. A, Prop. A35).
- Sintesi (p. 2): "no computationally efficient CAM satisfies all desirable properties simultaneously".

## 8. Limitazioni dichiarate dagli autori
- p. 5 (Sez. 2.1): "The EC model used here is intentionally minimal, reflecting the most common structure in the literature. It assumes known and deterministic consumption and generation within each time slot, fixed grid prices, and no marginal cost of internal transfers. This abstraction allows us to focus purely on the theoretical properties of ex-post CAMs (those which distribute savings after the time slot has ended), without conflating them with operational or regulatory variations. More complex settings like dynamic pricing, storage, or network constraints can be analyzed within the same axiomatic framework, but are beyond the scope of this paper."
- p. 11 (Sez. 3.2): proprietà P2, P4, P6 del nucleolo non dimostrate (vedi sopra).
- p. 12 (Sez. 3.3): il nucleolo ha un onere computazionale che "limits its practical applicability unless more efficient EC-specific algorithms are developed".
- p. 13: nessun dato usato.

## 9. Future work dichiarati dagli autori (Sez. 4, p. 13: elenco numerato, verbatim)
1. "Formal characterization of the nucleolus. A central open question is whether the nucleolus indeed satisfies all seven desirable properties. Proving or disproving this conjecture would significantly advance the theoretical foundations of EC cost allocation and clarify whether a "gold standard" CAM exists."
2. "Design of computationally efficient algorithms for the nucleolus. Given the nucleolus's strong theoretical appeal, identifying algorithms that exploit the structural features of the coalitional game that characterizes energy sharing could dramatically expand its practical applicability."
3. "Extending the axiomatic framework to more complex EC settings. Future work could consider settings with dynamic pricing, storage, network constraints, household flexibility, or multi-period coupling. Extending the framework to such contexts would help evaluate the robustness of CAM properties under more realistic conditions."
4. "Empirical validation using real-world EC data. Applying the framework to real consumption-generation patterns from operational energy communities would help assess how theoretical properties translate into practical outcomes and user perceptions."

`[INFERENZA — test B.1]` Il contributo del paper **è già un confronto multi-metodo** (8 CAM × 7 proprietà): quindi le sue richieste di estendere il confronto a contesti più complessi (#3) e di validarlo su dati reali (#4) sono del tipo **"generale"** (forte). I punti #1 e #2 riguardano specificamente il nucleolo e **non sono compatibili** con un inquadramento che non usi il nucleolo: ai fini di un gap vanno citati solo #3 e #4 dichiarando esplicitamente che #1–#2 esistono (regola B.2 delle istruzioni). Verificato nel PDF: l'elenco ha esattamente quattro punti, con #1–#2 sul nucleolo e #3–#4 sulle estensioni/validazione empirica.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` È un lavoro puramente teorico a un solo slot temporale: non include né una serie temporale oraria, né storage, né vincoli normativi, né dati. Le sue stesse future work #3–#4 chiedono proprio questo.
- `[INFERENZA]` La formula `v(S) = (valore unitario) × min(Σ prelievi, Σ immissioni)` ha la stessa struttura dell'energia condivisa orario-per-orario con valore unitario costante: potrebbe rappresentare il caso italiano se `(p_b − p_s)` fosse sostituito dal valore unitario dell'energia condivisa. `[da verificare con la normativa: non letta, come da tua istruzione]`.
- `[INFERENZA]` La posizione "Shapley non è equo perché non sta nel core" contraddice l'uso di molti altri paper del corpus che lo definiscono "the most fair" (es. `moncecchi2020`): è un punto di **contraddizione** da riportare nella sintesi.
- `[INFERENZA]` L'affermazione "no unified framework" è una negativa universale degli autori (cfr. regola B.3): non va ripresa tale e quale in un gap.
- `[INFERENZA]` P4–P6 sono proprietà di *incentivo* (monotonia e rango del costo rispetto al consumo): potrebbero essere collegate alla "forza incentivante" della regola (regola B.5), ma il paper non le misura numericamente.
