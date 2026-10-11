# li2024 — Decentralized Equitable Energy Access in Energy Communities

- **File sorgente:** `Paper/Decentralized Equitable Energy Access.pdf` (4 pagine, testo estraibile)
- **Tipo:** preprint arXiv (2410.04300v1, eess.SY, 5/10/2024), destinato agli atti dell'Allerton Conference 2024 (estensione di 4 pagine; la derivazione completa è rimandata a un "working paper" non disponibile, rif. [8])
- **Lettura:** integrale (pp. 1–4); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Li, S.; Mount, T. D.; Tong, L. (2024). *Decentralized Equitable Energy Access in Energy Communities.* arXiv:2410.04300v1 [eess.SY], 5 Oct 2024; Proceedings of the 2024 60th Annual Allerton Conference on Communication, Control, and Computing (in corso di pubblicazione). Cornell University. Supportato dalla NSF (Grants 2218110 e 2412776).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** equità di accesso all'energia in una comunità con membri di reddito e capacità di accesso alle DER diversi; formulare **Equity-regarding Welfare Maximization (EqWM)** e una versione decentralizzata **D-EqWM** a due livelli, in cui un operatore non-profit definisce una politica di prezzi comunitari e i membri ottimizzano il proprio consumo.
- **Gap dichiarato (abstract, p. 1):** "While optimal energy consumption scheduling is well-studied, integrating equity into decentralized real-time energy access remains under-explored."
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** non esplicito; tariffa di net energy metering (NEM) regolata dall'utility, prezzi in dollari (acquisto 0,4 $/kWh, vendita 0,2 $/kWh) e dati EIA 2020 delle famiglie del Sud degli USA (p. 3). Nessun riferimento alla normativa europea/italiana sulle CER.
- **Tipo di CER:** comunità gestita da un operatore non-profit/aggregatore che compra e vende alla utility sotto NEM; alcuni membri sono prosumer (PV, storage), altri no (p. 1).
- **Membri:** N = 100 (75 con PV su tetto), carichi flessibili, utilità quadratiche crescenti (p. 3).

## 4. Metodo
- **Modello (Sez. III, p. 2):** problema centralizzato EqWM (massimizzare il surplus totale con vincoli di razionalità individuale, adeguatezza dei ricavi dell'operatore, vincolo di equità `min_i Ũ(d_i) ≥ ω`, Eq. 5) e problema decentralizzato D-EqWM (livello superiore: prezzi `Π_i(z) = θ_i + θ_0·z` con prezzo volumetrico uniforme θ_0 e quota fissa discriminante θ_i; livello inferiore: massimizzazione del surplus con vincolo di budget `x_i`; Eq. 8–10).
- **Equità:** funzione di benessere sociale **Rawlsiana** (utilità del membro peggiore), con riferimento al principio di Pigou–Dalton e alle curve di Lorenz (Sez. II, pp. 1–2).
- **Dati:** distribuzione dei budget energetici dai dati EIA 2020; 100 realizzazioni di budget × 100 scenari di generazione (previsione PV + errore gaussiano); orizzonte di 1 ora (p. 3).
- **Software:** `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati
Non si tratta di ripartizione di un incentivo ma di **politica di prezzo comunitaria discriminante** (quote fisse θ_i dipendenti dal budget) che realizza un trasferimento di Pigou–Dalton. Confronto fra tre regimi (p. 3): (1) utente standalone sotto NEM; (2) membro EC con prezzi NEM; (3) membro EC con D-EqWM.

## 6. Metriche
- **Economiche:** surplus di consumo per membro (Fig. 4); efficienza (benessere totale); frontiera di Pareto efficienza–equità (Fig. 2).
- **Equità / sociali:** funzione di benessere Rawlsiana; **curve di Lorenz** della distribuzione dei consumi attesi (Fig. 3); budget energetico legato al reddito.
- **Ambientali / engagement:** nessuna.

## 7. Risultati principali (p. 3–4)
- Proprietà (p. 3): D-EqWM raggiunge il benessere del problema centralizzato; garantisce che ogni membro abbia surplus non inferiore a quello fuori dalla comunità; la frontiera efficienza–equità è concava e ogni punto è raggiungibile.
- Esempio numerico: senza prezzi discriminanti "the equity of the expected energy consumption distribution does not improve significantly after households join the EC"; con D-EqWM i consumi attesi sono più concentrati (curva di Lorenz più vicina all'uguaglianza); i membri con budget limitato hanno il miglioramento di surplus più marcato (p. 4).
- Conclusione (p. 4): "while the widespread adoption of rooftop solar tends to exacerbate energy inequalities, an energy community can benefit all members—rich and poor alike—by improving equitable access to distributed energy resources."

## 8. Limitazioni dichiarate dagli autori
Nessuna dichiarata. La derivazione teorica è rimandata a un working paper.

## 9. Future work dichiarati dagli autori
**Nessuno** (la Conclusione non contiene sviluppi futuri).

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Contesto non trasferibile in modo diretto alle CER italiane: i membri pagano un prezzo comunitario discriminante (quote fisse in funzione del budget), non ricevono la quota di un incentivo sull'energia condivisa.
- `[INFERENZA]` Orizzonte di un'ora, sistema statico: nessuna evoluzione temporale né dati reali di CER.
- `[INFERENZA]` Utile come riferimento per un criterio di equità fondato sul **reddito/budget** (Rawls, Pigou–Dalton, Lorenz) — l'unico del corpus finora che lo formalizza con un vincolo di ottimizzazione.
- `[INFERENZA]` Essendo una versione estesa breve di un preprint, la verificabilità è limitata (risultati solo in figura).
