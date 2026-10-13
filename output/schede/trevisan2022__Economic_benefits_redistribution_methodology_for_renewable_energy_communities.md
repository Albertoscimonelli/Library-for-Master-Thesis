# trevisan2022 — Economic Benefits Redistribution Methodology for Renewable Energy Communities

- **File sorgente:** `Paper/Economic_benefits_redistribution_methodology_for_renewable_energy_communities.pdf` (6 pagine, testo estraibile; le formule (1)–(10) sono quasi tutte perse nell'estrazione, ricostruite dalle descrizioni)
- **Tipo:** conference paper. Il PDF non riporta in chiaro il nome della conferenza nel testo estratto; dal rif. [4] di `trevisan2024` risulta *13th Mediterranean Conference on Power Generation, Transmission, Distribution and Energy Conversion (MEDPOWER 2022), pp. 213–218* (`[NON SPECIFICATO nel PDF]`).
- **Lettura:** integrale (pp. 1–5); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Trevisan, R.; Ghiani, E.; Pilo, F. (2022). *Economic Benefits Redistribution Methodology for Renewable Energy Communities.* Dept. of Electrical and Electronic Engineering, University of Cagliari. Conferenza: MEDPOWER 2022 (da citazione in `trevisan2024`).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** proporre, con riferimento al quadro legislativo italiano, un modello di distribuzione dei benefici legati alla produzione e condivisione di energia in una REC, secondo principi di equità e proporzionalità ("meritocratic redistribution"); categorizzazione dei membri in produttori, prosumer e consumatori.
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Italia, fase sperimentale (L. 8/2020, D.Lgs. 199/2021 citati; p. 1); incentivo sull'energia condivisa e ritiro dedicato (RID) del GSE per l'energia immessa (p. 2).
- **Tipo di CER:** REC con soggetto giuridico che riceve il pagamento e ha uno statuto/regolamento interno per ripartirlo (p. 1).
- **Membri (caso 2021, centro Italia, Tab. 1, p. 4):** 5 utenti sotto la stessa cabina MV/LV: User 1 produttore (PV 7 kWp, autoconsumo trascurabile); User 2 prosumer (3 kWp; 3.309 kWh/anno); User 3 consumatore (3.159 kWh); User 4 prosumer (3 kWp; 4.727 kWh); User 5 consumatore (2.352 kWh).

## 4. Metodo
- **Modello (Sez. 2):** decomposizione "top-down" dell'incentivo annuo sull'energia condivisa in un **albero di categorie** (profondità 5, 9 nodi, 5 foglie). Ogni arco ha una percentuale (decisione di progetto) con vincolo `Σ pesi dallo stesso nodo ≤ 1`. Foglie: **riserve** (non redistribuite, per altri progetti della comunità); **quota fissa** (uguale per tutti); **prelievi** (quota ∝ energia prelevata `w_i`); **immissioni di produttori e prosumer** (∝ energia immessa `i_i`); **immissioni dei soli prosumer** (∝ energia immessa fra i prosumer `ip_i`) (pp. 2–3).
- **Ottimizzazione:** il vettore dei pesi è scelto risolvendo problemi di ottimizzazione scritti in MiniZinc (linguaggio open-source di modellazione dei vincoli) con vincoli sulla riduzione minima di costo `z_i` per utente e diversi obiettivi (Sez. 3, Tab. 3).
- **Dati:** profili di carico generati con Load Profile Generator, PV da PVGIS, prezzi mensili RID dal GSE; anno 2021 (p. 4).
- **Ipotesi chiave (p. 2):** viene redistribuito solo l'incentivo sull'energia condivisa; il RID resta al proprietario dell'impianto perché "those benefiting from the RID have incurred an investment for the construction of the plant, so they require a higher income to return on that investment".

## 5. Meccanismi di ripartizione analizzati
**Schema ibrido a categorie** (quota fissa uguale + proporzionale ai prelievi + proporzionale alle immissioni, con categoria separata per i prosumer "to prevent dominance actions by producers", p. 3 + riserve), con pesi calcolati per ottimizzazione. Non ci sono confronti con Shapley o altre regole.

## 6. Metriche
- **Economiche:** incentivo ripartito per categoria (€), percentuale di riduzione dei costi `z_i` per utente (costo di rata dell'impianto per il produttore, bolletta per gli altri; Tab. 5).
- **Equità / sociali / ambientali / engagement:** nessun indice; solo il vincolo di riduzione minima di costo per utente.

## 7. Risultati principali (Tab. 2–5, pp. 4–5)
- Incentivo totale annuo da ripartire: **309,45 €**. RID per utente: 465,0 € (U1), 117,9 € (U2), 0 (U3), 102,5 € (U4), 0 (U5). Costi da ridurre: 1.344 € (rata annua produttore) e 446,6; 764,8; 727,51; 564,34 € (bollette) (Tab. 2). Riduzione minima già garantita dal solo RID: 34,61% (U1), 26,42% (U2), 14,09% (U4).
- **Cinque simulazioni** (Tab. 3): (1) `max(I_alloc)`, z ≥ 0,10; (2) `max(I_alloc − q1)`, z ≥ 0,10; (3) `min(I_alloc)`, z ≥ 0,05; (4) `max(z2+z4)`, z ≥ 0,10; (5) `max(z1)`, z ≥ 0,08.
- **Riduzioni di costo % (Tab. 5):** Sim 1: U1 34,61; U2 37,44; U3 12,93; U4 25,60; U5 12,96. Sim 3: 34,61; 31,23; 5,18; 18,71; 5,20. Sim 4: 34,61; 43,44; 10,37; 27,20; 10,40. Sim 5: 40,26; 38,37; 8,27; 23,71; 8,29.
- Gli autori (p. 5): la categoria "Withdrawals" basta a raggiungere i target imposti; i membri con impianti ottengono riduzioni maggiori grazie alla valorizzazione dell'energia immessa oltre all'autoconsumo.

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata. Il lavoro è dichiarato "a first step in the development of a more complex system" (p. 2).

## 9. Future work dichiarati dagli autori
- p. 5 (Sez. 4): "The developed distribution scheme, including its constraints, could be supplemented by further data on the investment parameters related to the construction of the production plants. Future developments could concern the definition of a dedicated algorithm to overcome the use of the optimization software used in this study, as well as the expansion of the model with additional parameters that consider a broader community context or redistribution metrics based on other KPIs that consider other beneficial contributions to the energy community."
`[INFERENZA — test B.1]` **Self-referential**.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` La riduzione di costo del produttore (34,61%) deriva interamente dal RID (465/1344 €) e non dall'incentivo condiviso (U1 riceve 0 € di incentivo in Sim 1): l'incentivo ridistribuito è piccolo (309 €/anno) rispetto agli altri flussi.
- `[INFERENZA]` Nel testo la Tab. 4 è descritta come "of L2" (foglie *esclusa* la riserva) ma riporta cinque colonne (q2, q4, q6, q8, q9), una delle quali (q2) corrisponde alla riserva; incoerenza di etichettatura.
- `[INFERENZA]` I pesi dell'albero sono scelti per rispettare un vincolo di *riduzione minima di costo* per utente: è un approccio di tipo "target di convenienza", diverso dal criterio di contributo (Shapley) o dal proporzionale puro.
- `[INFERENZA]` La separazione fra RID (al proprietario) e incentivo (condiviso) è una scelta di governance dichiarata: è un buon esempio di come la regola italiana lasci libertà di ripartizione interna.
