# volpato2024 — A stochastic optimization procedure to design the fair aggregation of energy users in a Renewable Energy Community

- **File sorgente:** `Paper/A stochastic optimization procedure to design the fair aggregation of energy users in a Renewable Energy Community.pdf` (17 pagine, testo estraibile)
- **Tipo:** articolo su rivista (Renewable Energy, Elsevier, open access)
- **Lettura:** integrale (corpo e Appendice, pp. 1–15); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Volpato, G.; Carraro, G.; De Giovanni, L.; Dal Cin, E.; Danieli, P.; Bregolin, E.; Lazzaretto, A. (2024). *A stochastic optimization procedure to design the fair aggregation of energy users in a Renewable Energy Community.* **Renewable Energy**, 237, 121580. DOI 10.1016/j.renene.2024.121580. Ricevuto 14/2/2024; rivisto 7/10/2024; accettato 9/10/2024; online 11/10/2024. Università di Padova.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1; Sez. 1.2, p. 3):** (i) individuare il "best" set di scenari stocastici di irradianza e consumi elettrici; (ii) valutare l'accuratezza delle "stochastic forecasts" di costo totale e taglie rispetto alle "perfect forecasts". In più, i costi ottimi sono ripartiti con lo Shapley value.
- **Gap dichiarati (p. 3, Sez. 1.2):** (1) "validation and successive test of the optimization models under uncertainty" (gli scenari si scelgono a priori); (2) assenza di un caso di studio completo in cui il peso delle diverse incertezze sia quantificato nell'ottimizzazione design-operation e considerando anche la ripartizione equa dei costi fra i membri.
- **RQ formulata come domanda?** No; due obiettivi.

## 3. Contesto
- **Paese / quadro normativo:** Italia (Padova); membri sotto la stessa cabina primaria con autoconsumo virtuale collettivo; energia condivisa = minimo orario fra prelievo e immissione, al netto dell'autoconsumo fisico individuale (p. 4); incentivo REC 0,12 €/kWh (p. 8).
- **Tipo di CER:** REC con sistema multi-energia (PV, pompe di calore, accumuli elettrico e termico, caldaie a gas) e demand response price-based (RTP).
- **Membri:** 4: residenziale (prosumer), pubblico (prosumer), terziario e commerciale (consumatori) (Fig. 2, pp. 3–4).

## 4. Metodo
- **Modello:** MILP con conoscenza perfetta degli input (365 giorni, orario) e programmazione stocastica a due stadi (SP) con giorni tipici da K-means (2–30 cluster) come scenari; addestramento 2005–2014, test 2015–2020; selezione del set con minimo RMSE fra costo "stochastic" e "historical" (Sez. 2.2–3.2, pp. 3–8). Il set migliore ha 29 scenari (anno 2014, residuo 1,26 k€, 0,33%).
- **Ripartizione:** Shapley value applicato ex-post; il valore di coalizione v(S) è il costo ottimo di ciclo di vita ottenuto risolvendo l'SP con i soli membri di S (16 coalizioni; Eq. 2, p. 6).
- **Dati:** PVGIS (Padova), profili elettrici e termici da un rif. [92]; prezzo di vendita = metà del prezzo day-ahead italiano, acquisto = vendita + 0,2 €/kWh; gas 0,098 €/kWh; tasso 5%, vita 20 anni; frazione di carico spostabile 0,1 (p. 8).
- **Software:** Gurobi (gap di ottimalità 2%); i9-12900K, 64 GB RAM. La soluzione MILP a conoscenza perfetta richiede in media 32 h per anno di test, l'SP pochi minuti (p. 12).

## 5. Meccanismi di ripartizione analizzati
- **Shapley value** (unico meccanismo applicato). Nucleolus e Nash bargaining sono discussi nella letteratura (p. 3) e per il confronto fra i tre approcci l'articolo rimanda a un lavoro precedente (rif. [71]); qui la scelta è motivata perché lo Shapley "does not require an optimization problem dedicated to the cost allocation" (p. 3).

## 6. Metriche
- **Economiche:** costo di ciclo di vita (k€), errore relativo stochastic vs perfect (%), RMSE (k€), costo allocato a ciascun membro, risparmio annuo per membro rispetto all'operatività indipendente e quota sul risparmio totale (Fig. 9–10, Tab. 4).
- **Tecniche:** errori relativi sulle taglie (Tab. 2).
- **Equità:** definita come "weighted average marginal contribution" (Shapley); nessun indice di equità aggiuntivo.
- **Ambientali / sociali / engagement:** nessuna metrica (citate solo in letteratura, p. 1).

## 7. Risultati principali
- **Accuratezza (pp. 10–12):** RMSE 36 k€ (training, 29 scenari) vs 7 k€ (test, −81%); errore medio sul costo 1,63% (max 2,77% nel 2015, min 0,27% nel 2016); errori di taglia 3–13% per PV e HP, 0% per GB, 38% (residenziale) e 23% (pubblico) per il TES.
- **Costi allocati con Shapley (Tab. 4a, p. 15):** residenziale 18–20 k€/anno; terziario 16–18 k€; commerciale 53–54 k€; pubblico 288–294 k€ (costo totale REC ≈ 376–383 k€).
- **Risparmi rispetto all'operare da soli (Tab. 4b):** totale REC 6,03–11,33 k€/anno; quote sul totale: commerciale 41–57% (media 48,41%), pubblico 21–34% (26,2%), terziario 10–20% (14,14%), residenziale 3–15% (11,25%). Gli autori leggono questo esito come equo perché lo Shapley "supports these investments by fairly distributing higher annual cost savings to the commercial and public users" (p. 12).

## 8. Limitazioni dichiarate dagli autori
- p. 13 (Sez. 4.3): "a limitation of the proposed procedure is that it disregards the temporal relationship between consecutive typical days used as stochastic scenarios in the SP model" (errori TES 38% e 23%); l'incertezza sulla temperatura ambiente non è considerata.
- p. 13 (Sez. 4.3): "given a REC with a higher number of members (e.g., tens or hundreds), greater computational resources would be required to solve the MILP model with perfect knowledge and to fairly allocate the optimal predicted life cycle cost to the REC members using the Shapley value. In fact, for large RECs, the number of user coalitions increases dramatically and so does the computational time to solve the SP model for each coalition".
- p. 13 (Conclusioni): "The implicit assumption is that the representation of uncertainties in the "future" will remain the same as in the "past"."

## 9. Future work dichiarati dagli autori
- p. 14 (Sez. 5): "Further research could analyse the impact of changing the temporal position of the "present moment" on the "stochastic forecasts", which would require larger training and testing datasets. Other directions of future work could focus on considering other uncertainties (e.g., ambient temperature, heating demands, prices of technologies and energy-related costs, etc.) and further investigating the temporal relationship between consecutive typical days used as stochastic scenarios in the SP model."
- p. 13 (Sez. 4.3): tecniche alternative di generazione degli scenari (K-medoids, clustering gerarchico, reti neurali).
`[INFERENZA — test B.1]` **Self-referential e non pertinenti all'allocazione**: riguardano la procedura stocastica, non i meccanismi di ripartizione.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Il paper è utile soprattutto come esempio di *interazione fra design ottimo e ripartizione*, ma non confronta più regole di ripartizione.
- `[INFERENZA]` La quota di risparmio più alta va al commerciale (media 48,41%), che è un consumatore puro con GB di taglia fissata dal fabbisogno termico (p. 6): l'argomentazione degli autori ("bear more expensive investments", p. 12) non è dimostrata nel testo per questo membro; la quota potrebbe riflettere l'elevato assorbimento di energia condivisa. Il paper non lo verifica.
- `[INFERENZA]` Il risparmio totale della REC (6–11 k€) è circa 1,6–3% del costo totale (~380 k€): il "beneficio da ripartire" è piccolo rispetto alla scala dei costi dei membri (quattro utenze di taglie molto diverse).
- `[INFERENZA]` La scalabilità dello Shapley (4 membri, 16 coalizioni, risoluzione di un SP per coalizione) è un vincolo dichiarato dagli autori.
