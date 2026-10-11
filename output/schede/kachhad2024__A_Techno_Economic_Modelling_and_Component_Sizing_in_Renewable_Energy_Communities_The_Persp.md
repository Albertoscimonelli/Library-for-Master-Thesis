# kachhad2024 — A Techno-Economic Modelling and Component Sizing in Renewable Energy Communities: The Perspective of Technical Facilitators

- **File sorgente:** `Paper/A Techno-Economic Modelling and Component Sizing in Renewable Energy Communities_ The Perspective of Technical Facilitators.pdf` (6 pagine, testo estraibile)
- **Tipo:** conference paper (IEEE CASE 2024, Bari)
- **Lettura:** integrale (pp. 1–6); bibliografia non letta riga per riga. L'estrazione ha invertito l'ordine di abstract e introduzione (layout a due colonne): il contenuto è completo.
- **Convenzioni:** pagine = indici di pagina del PDF (numerazione stampata 329–334). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Kachhad, V.; Joshi, A.; Mariani, V.; Raffa, V.; Glielmo, L. (2024). *A Techno-Economic Modelling and Component Sizing in Renewable Energy Communities: The Perspective of Technical Facilitators.* 2024 IEEE 20th International Conference on Automation Science and Engineering (CASE), Bari, 28 Aug–1 Sep 2024. DOI 10.1109/CASE59546.2024.10711652. Università del Sannio; ENEA; Friendly Power Srl; Università di Napoli Federico II.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** modello matematico per dimensionare ottimamente PV e BESS in una REC con scambi di energia fra sistema PV+BESS e partecipanti, massimizzando il Net Profit (MINLP); in più, un "individual marginal contribution method to allocate incentives among REC participants equitably".
- **Gap dichiarato dagli autori (p. 1):** gli studi sul dimensionamento "still need to consider the NPV of the systems" e molti "focus only on single-day profiles, overlooking the critical aspect of an extended planning horizon (typically 25 years)".
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Italia; incentivo della Pubblica Amministrazione sull'energia condivisa e sul risparmio di costi di trasmissione (pp. 1, 3).
- **Tipo di CER:** modello con **Technical Facilitator (TF)** che possiede/finanzia PV e BESS (prestito bancario, contratto di locazione tetto/RLA), mentre i consumatori sono legati al TF da un accordo contrattuale di reward-sharing (Fig. 1, p. 2). Il TF decide quanta parte dell'incentivo ridistribuire.
- **Membri (caso studio):** Roseto Valfortore (Foggia, Puglia): 43 famiglie, domanda annua totale 36,5 MWh (p. 5).

## 4. Metodo
- **Modello:** MINLP che massimizza il Net Profit = NPV su 25 anni (Eq. 20–23) con PV, BESS (efficienze di carica/scarica, sostituzione a 12 anni), energia condivisa = min(immissione, domanda aggregata) (Eq. 14b), flussi di cassa (vendita, risparmi da scarica BESS, incentivo condiviso, acquisti). Approssimazione con **profili periodici** (4 settimane rappresentative, una per stagione, estratte col metodo L1; β = 13 settimane per stagione) per ridurre il carico computazionale (Sez. III-B).
- **Dati:** profili di domanda dei partecipanti forniti dal TF; irradianza e temperatura da dashboard online (rif. [25] = strumenti JRC/PVGIS); passo orario. Parametri (Tab. I, p. 5): pannello 0,43 kW, 1200 €/kW; BESS 5 kWh, 450 €/kWh, vita 12 anni, efficienza 90%; tariffa di condivisione C^E = 0,11 €/kWh, componente di trasmissione C^T = 0,00822 €/kWh; tariffe di acquisto/vendita come in un lavoro precedente degli stessi autori.
- **Software:** MATLAB con YALMIP e Gurobi (p. 4).

## 5. Meccanismi di ripartizione analizzati
- **Split TF vs partecipanti tramite il parametro δ:** il TF trattiene la quota δ dell'incentivo, distribuisce (1−δ) (Eq. 29). Valori testati: δ ∈ {0,4; 0,6; 0,8; 1}.
- **Ripartizione fra i partecipanti – "individual marginal contribution" (Sez. III-C):** fattore di riparto `ζ = d^n_t Δt / Σ_n d^n_t Δt` (Eq. 30), cioè proporzionale al consumo individuale orario; la bolletta del partecipante è `EB_REC,n = EB_IND,n − β Σ_t ζ^n_{x,t} R^sh_{x,t}` (Eq. 31).
- Nessun confronto con altre regole (Shapley, quote uguali, ecc.).

## 6. Metriche
- **Economiche:** NPV, Net Profit, payback, numero ottimo di PV/BESS, bolletta annuale di ciascun partecipante con/senza REC (Fig. 2–3).
- **Equità / sociali / ambientali / engagement:** nessuna metrica quantitativa (benefici sociali e ambientali citati solo a p. 1 come "triple benefit").

## 7. Risultati principali (dal testo, pp. 5–6)
- Con δ = 1 (il TF trattiene tutto) il numero ottimo di PV e BESS è maggiore che negli altri casi; la bolletta con REC non è significativamente diversa da quella senza REC.
- Con δ = 0,4 (60% ai partecipanti) la quantità ottima di PV è minore e il numero ottimo di BESS è **zero** "because of its higher investment cost to recover in the payback period"; le bollette dopo l'ingresso in REC sono "nearly 30% lower" rispetto a prima.
- Conclusione degli autori: la scelta di δ è nelle mani del TF e mostra "how important it is to balance participant profits and TF's efforts to recover their investment" (p. 6).

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata; nessuna limitazione dichiarata esplicitamente.

## 9. Future work dichiarati dagli autori
**Nessuno.** La Conclusione (p. 6) non contiene sviluppi futuri.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Il nome "individual marginal contribution" non corrisponde a un contributo marginale in senso Shapley: la formula è un riparto pro-rata sul consumo orario.
- `[INFERENZA]` Ambiguità nell'Eq. 20: il NPV del TF include i risparmi da scarica BESS (R^sav) e sottrae i costi di acquisto dalla rete (C^buy) che, nel testo, sono pagati dai partecipanti (p. 3). Non è chiaro se il Net Profit sia del TF o dell'intera comunità.
- `[INFERENZA]` Il risultato "δ vs dimensione ottima del sistema" è l'unico contributo sul trade-off investitore/membri: mostra che il meccanismo di ripartizione cambia la *decisione di investimento* (BESS = 0 per δ = 0,4). È un legame fra ripartizione e dimensionamento esplicitamente osservato dagli autori.
- `[INFERENZA]` Nessun confronto fra regole, nessuna misura di equità o di dispersione dei benefici fra le 43 famiglie.
