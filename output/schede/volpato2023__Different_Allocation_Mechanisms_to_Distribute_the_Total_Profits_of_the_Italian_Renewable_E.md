# volpato2023 — Different allocation mechanisms to distribute the total profits of the Italian Renewable Energy Community

- **File sorgente:** `Paper/Different Allocation Mechanisms to Distribute the Total Profits of the Italian Renewable Energy Community.pdf` (11 pagine, testo estraibile; la Tab. 2 dei parametri è estratta con codifica dei font alterata ma decifrabile)
- **Tipo:** conference paper (ECOS 2023, 36th International Conference on Efficiency, Cost, Optimization, Simulation and Environmental Impact of Energy Systems, Las Palmas, 25–30 giugno 2023)
- **Lettura:** integrale (pp. 1–10); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (la numerazione stampata va da 3386 a 3396). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Volpato, G.; Carraro, G. (2023). *Different allocation mechanisms to distribute the total profits of the Italian Renewable Energy Community.* Proceedings of ECOS 2023, Las Palmas de Gran Canaria, 25–30 June 2023. DOI 10.52202/069564-0304. Dipartimento di Ingegneria Industriale, Università di Padova.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** valutare e confrontare due meccanismi di allocazione del profitto: lo **Shapley value** (cooperativo) e lo **Uniform pricing** (prezzo uniforme indipendente dalla cooperazione), su una REC italiana con condivisione virtuale.
- **Gap dichiarato (p. 2):** gli studi applicano un solo criterio e/o non confrontano allocazioni cooperative con altre non cooperative; "To the best of authors' knowledge, the application of different allocation criteria for the economic benefit of a REC, according to the Italian framework, represents a first gap in the literature. Moreover, as highlighted in [14], the literature lacks of more in-depth discussions about the fairness of the cost/profit distribution within ECs and, in particular, within RECs." Il rif. [14] è Cremers et al. (presente nel corpus).
- **RQ formulata come domanda?** No; due contributi dichiarati (p. 3).

## 3. Contesto
- **Paese / quadro normativo:** Italia; REC "centralizzata" con condivisione virtuale; energia condivisa = minimo orario fra prelievo e immissione; incentivo REC 0,12 €/kWh (somma di premio e tariffa legata alle perdite di rete evitate) (pp. 5–6, Tab. 2).
- **Tipo di CER:** MINLP di una REC con demand shifting e batteria; località Padova.
- **Membri (3):** consumatore terziario (Ter); prosumer residenziale (Res, solo PV, 60 m²); prosumer commerciale (Com, PV 250 m² + batteria 50 kWh) (p. 4, 10).

## 4. Metodo
- **Modello:** MINLP che massimizza il profitto giornaliero della REC (Eq. 20): ricavi/costi di scambio con la rete + incentivo × energia condivisa; il valore della grande coalizione coincide con l'ottimo (p. 6). Eq. 5–19: PV, batteria, carichi spostabili (fino al 10%), limite di scambio con la rete.
- **Allocazione:** Shapley (Eq. 2) con valore di ogni coalizione ottenuto risolvendo il modello con i soli membri di S; Uniform pricing `c_u = TC/ΣΣE_{i,t}` (Eq. 3).
- **Dati:** irradianza PVGIS (Padova, giornata tipo di primavera), prezzi GME, profili di domanda dei tre settori da un dataset **OpenEI del Dipartimento dell'Energia USA** (rif. [28]); efficienza PV 0,17, area PV, e altri parametri "assumed" (Tab. 2, p. 7).
- **Software:** Gurobi.

## 5. Meccanismi di ripartizione analizzati
- **Shapley value** (cooperativo).
- **Uniform pricing** (payoff proporzionale alla domanda: profitto totale / domanda totale × domanda del membro). Citati ma non applicati: time-of-use pricing e segmented pricing (p. 4).

## 6. Metriche
- **Economiche:** profitto/costo giornaliero allocato a ciascun membro (€/giorno); efficienza e razionalità individuale (p. 4, 9).
- **Equità:** discussa qualitativamente ("fairer towards prosumers"); nessun indice.
- **Sociali / ambientali / engagement:** nessuna.

## 7. Risultati principali (Tab. 3–4, pp. 8–9)
- Profitto giornaliero ottimo della REC: **8,35 €**.
- **Valori di coalizione (Tab. 3):** {Ter} −12,85; {Res} −1,03; {Com} −22,20; {Ter,Res} −6,95; {Ter,Com} 2,70; {Res,Com} 20,09; {Ter,Res,Com} 8,35 €.
- **Payoff (Tab. 4):** Shapley: Ter −5,03; Res 9,57; Com 3,81. Uniform pricing: Ter 1,95; Res 0,69; Com 5,71. Entrambi sono efficienti e individualmente razionali (ciascuno sta meglio che da solo).
- Gli autori: l'Uniform pricing dà payoff "più omogenei" (tutti in profitto), lo Shapley è "fairer towards prosumers" perché premia chi contribuisce di più al profitto (p. 9–10).

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata. Il caso è una sola giornata tipo con tre membri (descrizione, p. 6).

## 9. Future work dichiarati dagli autori
- p. 10 (Sez. 5): "A future research direction of this work could cover the analysis of the economic stability of the REC, strictly dependent on the costs/profits distributed by the implemented allocation mechanisms, to avoid the case of members willing to exit from the REC."
`[INFERENZA — test B.1]` Self-referential ma pertinente: chiede un'analisi di stabilità della ripartizione (uscita dei membri).

## 10. Note del lettore (inferenze mie)
- `[INFERENZA — verificato aritmeticamente]` Dai valori della Tab. 3 ho ricalcolato lo Shapley (−5,03; 9,57; 3,81: coincidono). Il valore della coalizione {Res,Com} (20,09 €) è **maggiore** di quello della grande coalizione (8,35 €) e della somma dei payoff dei due membri sia con Shapley (9,57 + 3,81 = 13,38 €) sia con Uniform pricing (0,69 + 5,71 = 6,40 €): nessuna delle due allocazioni sta nel core, cioè Res e Com avrebbero convenienza a uscire e formare una coalizione senza Ter. Il paper verifica solo la razionalità *individuale*, non quella *di gruppo*, e non commenta il fatto che la grande coalizione valga meno di una sua sottocoalizione.
- `[INFERENZA]` Un'osservazione collegata: il membro Ter ha contributi marginali negativi in diverse coalizioni (es. −11,74 € alla coalizione {Res,Com}), per cui lo Shapley gli attribuisce un costo; in un regime volontario e aperto questo solleva il tema dell'esclusione/ingresso dei membri.
- `[INFERENZA]` Profili di domanda statunitensi, una sola giornata, tre membri: nessuna generalizzabilità; i valori in € (<10 €/giorno) sono molto piccoli.
- `[INFERENZA]` Citazione secondaria: l'affermazione che Cremers et al. "highlighted the need to further investigate different allocation criteria, other than Shapley" va verificata nel testo di `cremers2022` (scheda dedicata) prima di essere usata.
