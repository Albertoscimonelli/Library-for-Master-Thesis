# trevisan2024 — A Cooperative Game Theory Framework for Revenues Redistribution in Renewable Energy Communities

- **File sorgente:** `Paper/A cooperative game theory framework for revenues redistribution in renewable energy communities.pdf` (4 pagine, testo estraibile)
- **Tipo:** conference paper (CIRED 2024 Vienna Workshop, Paper 0453)
- **Lettura:** integrale (pp. 1–4, Conclusioni comprese: nell'estrazione compaiono dopo la bibliografia, le ho verificate con un'estrazione `-raw` della p. 4); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Trevisan, R.; Ghiani, E.; Pilo, F. (2024). *A Cooperative Game Theory Framework for Revenues Redistribution in Renewable Energy Communities.* CIRED 2024 Vienna Workshop, 19–20 June 2024, Paper 0453. DOI 10.1049/icp.2024.1913. Università di Cagliari, Dip. di Ingegneria Elettrica ed Elettronica. Supportato dal PRIN2022 "SCORET".

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** applicare lo Shapley value alla ripartizione equa dei benefici economici fra i membri di una CER, con un modello "meritocratic revenue sharing".
- **Novità dichiarata (p. 2):** identificare il contributo marginale di ciascun utente da due prospettive: capacità di generare incentivo *immettendo* e capacità di aumentare l'energia condivisa *prelevando*.
- **RQ formulata come domanda?** No. È dichiarato un confronto con la ripartizione proporzionale (p. 2).

## 3. Contesto
- **Paese / quadro normativo:** Italia; incentivo tariffario (TIP) sull'energia condivisa, funzione del prezzo di mercato e della potenza dell'impianto, con valore massimo e base definiti nelle Regole Operative GSE (rif. [10], p. 2).
- **Tipo di CER:** caso-studio costruito *ad hoc* (Fig. 1).
- **Membri:** 5 utenti: User 1 consumatore; User 2 produttore con PV 20 kWp; Users 3–5 prosumer con PV 20 kWp ciascuno (p. 3). Orizzonte 24 ore, prezzo costante 100 €/MWh.

## 4. Metodo
- **Modello:** gioco cooperativo con Shapley value calcolato per enumerazione di tutte le permutazioni/coalizioni. (1.1) valore di coalizione = energia condivisa e TIP risultanti dall'immissione; (1.2) valore = energia condivisa legata al prelievo (limitata dal minore fra prelievi totali ed energia condivisa). I valori sono normalizzati in una "percentage of importance" (pp. 2–3).
- **Dati:** profili orari sintetici/di esempio (Fig. 2); `[NON SPECIFICATO]` origine dei profili.
- **Software:** codice proprio ("the code iterates through every possible coalition", p. 3); linguaggio `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati
- **Shapley value** (doppia prospettiva: injection / withdrawal).
- **Ripartizione proporzionale** a iniezione e prelievo, come benchmark "streamlined" (Tab. 2, p. 4).
- `[NON SPECIFICATO]` come le due prospettive (immissione e prelievo) si combinino in un unico riparto monetario né quanta parte del beneficio vada alla componente produzione e quanta ai consumi.

## 6. Metriche
- **Economiche:** nessuna metrica monetaria; coefficienti normalizzati (somma = 1).
- **Equità:** confronto qualitativo fra coefficienti Shapley e proporzionali; nessun indice (Gini ecc.).
- **Sociali / ambientali / engagement:** solo menzionati come motivazione (p. 1–2: politiche di coinvolgimento degli utenti); nessuna misura.

## 7. Risultati principali (Tab. 1–2, pp. 3–4)
- **Shapley (iniezione):** U1 0,000; U2 0,272; U3 0,255; U4 0,274; U5 0,199. **Shapley (prelievo):** U1 0,530; U2 0,000; U3 0,130; U4 0,210; U5 0,130.
- **Proporzionale (iniezione):** U1 0,000; U2 0,354; U3 0,231; U4 0,241; U5 0,173. **Proporzionale (prelievo):** U1 0,606; U2 0,000; U3 0,110; U4 0,175; U5 0,108.
- Tesi degli autori (p. 4): la ripartizione proporzionale "diminishes the actual contribution of some users to the configuration, in favor of other users", favorendo gli utenti 1 e 2 a scapito dei prosumer 3–5. Il software calcola lo Shapley per ogni ora, e ciò permette "advices" per aumentare il contributo degli utenti.
- Conclusione: lo Shapley fornisce una distribuzione "more nuanced and equitable" di quella proporzionale.

## 8. Limitazioni dichiarate dagli autori
Nessuna dichiarata.

## 9. Future work dichiarati dagli autori
- p. 4 (Sez. 5, Conclusions): "Future developments are aimed towards the standardization of the code, creating a less experimental version of it to facilitate its testing also in an operative environment."

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Validazione molto debole: 5 utenti, 24 ore, prezzo costante, nessuna analisi di sensibilità; "equo" è stabilito per confronto qualitativo, senza criterio esterno.
- `[INFERENZA]` Il riparto proporzionale usato come benchmark è solo una delle regole semplici possibili (non include quote uguali, né regole basate sul solo surplus).
- `[INFERENZA]` Non è definito come i due Shapley (injection/withdrawal) diventino pagamenti: manca il collegamento con la struttura reale dell'incentivo (TIP e restituzione componenti tariffarie).
- `[INFERENZA]` Future work *self-referential* (standardizzazione del proprio codice).
