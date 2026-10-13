# goncalves2024b — Towards Fair Energy Communities: Integrating Storage, Sharing and Pricing Strategies

- **File sorgente:** `Paper/Towards Fair Energy Communities_Integrating Storage_ Sharing and Pricing Strategies.pdf` (6 pagine; il livello di testo del PDF ripete più volte la prima pagina e restituisce le formule in modo imperfetto, quindi le ho controllate sui rendering)
- **Tipo:** conference paper (IFAC PapersOnLine 58-13, 2024, pp. 320–325, open access CC BY-NC-ND). Il nome della conferenza non compare nel testo `[NON SPECIFICATO]`. È un lavoro gemello di `goncalves2024a` (stesso gruppo e stesso caso di studio).
- **Lettura:** integrale (pp. 1–6; bibliografia letta come elenco; dopo la bibliografia non c'è altro contenuto, verifica della coda eseguita). Eq. (1)–(28) verificate sull'immagine (pp. 2–3); Tab. 1–2 e Fig. 1–5 verificate come immagine (Fig. 2 ingrandita).
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con le pagine 320–325 stampate: PDF p. 1 = p. 320). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Le virgolette riportano il testo degli autori.

## 1. Riferimento bibliografico
Goncalves, C.; Lezama, F.; Vale, Z. (2024). *Towards Fair Energy Communities: Integrating Storage, Sharing and Pricing Strategies.* **IFAC PapersOnLine**, 58(13), 320–325. DOI 10.1016/j.ifacol.2024.07.502. GECAD, LASI – Polytechnic of Porto, Portogallo. Sviluppato nell'ambito dell'Innovation Pact "NGS – New Generation Storage" (C644936001-00000045), cofinanziato da NextGenerationEU tramite il PRR portoghese (p. 6).

## 2. Obiettivo e research question
- **Obiettivo (abstract p. 1; Sez. 1, p. 1):** "optimize energy transactions in an energy community", promuovere lo scambio con transazioni di rete e P2P con sistemi di accumulo e integrare "fairness metrics to evaluate economic equity"; "we study key dynamics between energy sharing, pricing strategies, and fairness metrics".
- **Gap dichiarato:** nessun gap rispetto alla letteratura è formulato. Il paper presenta come risultato che "there exists a disparity in potential savings among members with different power acquisition capacities within the same community" (p. 1).
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Portogallo (edificio GECAD "Building N" a Porto, p. 3; tariffa triplice del fornitore, FiT 0,045 €/kWh, potenze contrattuali 3,45 / 6,9 / 10,35 kW, p. 4). Nessun incentivo sull'energia condivisa e nessun riferimento al quadro portoghese delle CER.
- **Tipo di CER:** community con scambio P2P di surplus; "a community manager (CM) can apply two distinct pricing strategies" (p. 3); è un mercato locale (LEM) più che un regime di incentivo.
- **Membri:** 10 famiglie in un'area suburbana: 6 prosumer con PV e batteria di capacità bassa / media / alta (famiglie 1–2, 3–4, 5–6) e 4 consumatori senza PV né batteria (famiglie 7–10). La diversità di PV è usata per "simulate diverse income levels within the community" (p. 3).

## 4. Metodo
- **Modello:** MILP di ottimizzazione dei flussi (proposto in Dynge et al. 2023 e Faia et al. 2021, p. 2). Funzione obiettivo (Eq. 1): minimizzare la somma delle bollette `Σ_h Σ_t (C^R_{t,h}·P^buyG_{t,h} − C^FiT_{t,h}·P^sellG_{t,h})·1/Δt`, quindi **solo flussi con la rete**; vincoli: transazioni peer-to-peer simmetriche (Eq. 2–4), bilancio per famiglia (Eq. 5), binari anti-simultaneità e limiti (Eq. 6–11), batterie con vincoli di potenza, stato di carica ed efficienza (Eq. 12–18).
- **Prezzi delle transazioni peer** (Sez. 2.3, p. 3): *MMR* (mid-market rate, `C^MMR = (C^R + C^FiT)/2`, Eq. 21); *SDR* (supply–demand ratio, `SDR_t = Σ_h(P^sellG + P^sellEC)/Σ_h(P^buyG + P^buyEC)`, Eq. 22, e `C^SDR = SDR_t·C^FiT + (1 − SDR_t)·C^R`, Eq. 23).
- **Dati:** un solo giorno a passi di 15 minuti (96 punti) con generazione e consumi dai dataset GECAD (Goncalves et al. 2022), profili dei sei prosumer derivati da un profilo base con piccole variazioni casuali, PV di picco ≈ 4 kW (famiglie 1–2), ≈ 8 kW (3–4), ≈ 12 kW (5–6); batterie da Faia et al. 2023 (Tab. 1: capacità 6,4–6,6 / 9,3–9,6 / 12,9 e 17,2 kWh; potenza di carica e scarica 2–3,5 / 5 / 6,5 e 8,5 kW; efficienza 0,945–0,975) (pp. 3–4).
- **Baseline BAU** (p. 4): bolletta di ciascun membro con la propria domanda e produzione "without any energy sharing mechanism", import a tariffa triplice ed export a FiT 0,045 €/kWh, "without any optimization".
- **Software:** Python (Spyder), libreria Python-MIP con solver CBC, Intel i5-8250U, 20 GB (p. 4).

## 5. Meccanismi di ripartizione analizzati
Due **prezzi per le transazioni peer**, che ripartiscono il valore dello scambio fra venditori e acquirenti: MMR (media fra prezzo retail e FiT) e SDR (prezzo che scende dal retail al FiT al crescere dell'offerta rispetto alla domanda locale). Non ci sono regole di ripartizione dei benefici di tipo quote uguali, proporzionali, teoria dei giochi o altro, né un trasferimento esplicito fra membri.

## 6. Metriche
- **Economiche:** bolletta giornaliera media per segmento di famiglie (EUR/giorno) e miglioramento percentuale rispetto al BAU (Tab. 2), valori negativi della bolletta = ricavo netto; volumi di scambio P2P (Fig. 1); stati di carica e cicli di carica delle batterie (Fig. 2–3).
- **Equità (Sez. 2.4, p. 3):** `EB_h = (C^R·P^buyG − C^FiT·P^sellG + C^EC·(P^buyEC − P^sellEC))/Δt` (Eq. 24); **QoE_t** `= 1 − σ_t/σ_t^max` con `σ_t` deviazione standard fra le famiglie del "prezzo percepito" `EB_h/(D_{t,h} − P^PV_{t,h})` e `σ_t^max = C^R − C^FiT` (Eq. 25–27); **mMF_t** `= min_h(EB_h)/max_h(EB_h)` (Eq. 28). Valori calcolati per ogni periodo di 15 minuti (Fig. 5).
- **Sociali / ambientali / engagement:** nessuna metrica.

## 7. Risultati principali (dal paper)
- **Scambi P2P (Sez. 4.1, p. 4; Fig. 1):** il volume maggiore è fra le famiglie 2 e 6 (42,41 kWh nel giorno), poi 1–6 (15,79 kWh) e 2–5 (14,88 kWh); "on average, each prosumer in the P2P market transacted approximately 5.88 kWh during the day"; le famiglie 7–10 non vendono.
- **Batterie (Sez. 4.2, pp. 4–5; Fig. 2–3):** tutti i prosumer usano la batteria durante la giornata e sfruttano la tariffa triplice ("buying energy in periods of low prices to use that energy in later times").
- **Bollette (Tab. 2, p. 5; verificata sull'immagine e ricalcolata):**

| Segmento | BAU (EUR) | MMR (EUR) | Migl. MMR | SDR (EUR) | Migl. SDR |
|---|---|---|---|---|---|
| 1 e 2 (Low PV e batteria) | 5,95 | 2,45 | 58,82% | 2,01 | 66,22% |
| 3 e 4 (Mid) | 2,12 | −0,72 | 133,96% | −0,51 | 124,06% |
| 5 e 6 (High) | 2,12 | −1,78 | 183,96% | −1,06 | 150,00% |
| 7–10 (senza PV né batteria) | 3,72 | 3,23 | 13,17% | 2,98 | 19,89% |

  Testo (p. 5): "high PV-battery households obtain on average an improvement of 183% with the MMR strategy, and 150% with the SDR"; "only 13% and 19% of savings for households without PV and battery systems"; "a large disparity of cost savings depending on the capacity for equipment acquisition".
- **Equità (Sez. 4.4, p. 5; Fig. 5, solo grafici):** QoE migliora con entrambi i prezzi rispetto alla tariffa triplice; MMR è migliore dove manca il PV, SDR dove c'è PV; "the mMF metric is null in periods with absence of PV generation, making evident that this metric requires energy sharing to provide a sense of fairness"; nei periodi con PV SDR supera MMR in entrambe le metriche.
- **Conclusioni (p. 6):** risparmi per tutti i membri; disparità "directly tied to the capacity of PV and battery systems"; "The nuanced performance of these metrics underscores the context-dependent nature of fairness assessments"; "the need for tailored solutions considering both economic and social dimensions".

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione di limitazioni né dichiarazioni esplicite. `[INFERENZA]` Non dichiarati: orizzonte di un solo giorno e 10 famiglie; PV e batteria usati come proxy del reddito senza dati di reddito; fonti dei profili dei consumatori "from diverse European households" (p. 4), non portoghesi; nessuna analisi di sensibilità né di scala; nessuna regola di ripartizione oltre al prezzo.

## 9. Future work dichiarati dagli autori
Elenco completo (Sez. 5, p. 6): 1. "Future research must further analyze social aspects in EC, focusing not only on the monetary advantages of member participants but also on the interactions of households with different income levels."
`[INFERENZA — test B.1]` Indicazione generale, non autoreferenziale, ma vaga e non operazionalizzata (B.5: "social aspects" e "interactions" non sono grandezze calcolabili senza ulteriori definizioni).

## 10. Note del lettore (inferenze mie)
- **Rapporto con `goncalves2024a`.** Stesso gruppo, stesso caso di studio e stessi valori di BAU (5,95 / 2,12 / 2,12 / 3,72), ma qui con le batterie e due soli prezzi (MMR, SDR). Con MMR i miglioramenti passano da −14,62 / −10,85 / −45,75 / −5,11% (senza batterie, `goncalves2024a`) a 58,82 / 133,96 / 183,96 / 13,17% (con batterie). Poiché il BAU coincide con quello senza batterie, i miglioramenti percentuali di questo paper sommano l'effetto delle batterie (arbitraggio sulla tariffa triplice e uso del proprio PV), dello scambio P2P e del prezzo, e non si possono attribuire al solo schema di condivisione `[INFERENZA]`.
- **La disparità non è effetto della regola di prezzo.** I prezzi MMR e SDR sono uguali per tutti i membri: la differenza di risparmio fra 13–20% (senza PV) e 150–184% (High PV) nasce dal possesso degli impianti, e nessuna regola testata può ridurla se non trasferendo valore dai prosumer ai consumatori; il paper la osserva senza mettere alla prova un meccanismo correttivo `[INFERENZA]`. Per l'obiettivo del progetto è un buon esempio del fatto che i benefici ai membri senza asset richiedono una regola esplicita di ripartizione.
- **Il dispacciamento non dipende dal prezzo locale.** L'Eq. (1) contiene solo i flussi con la rete: `C^EC` entra solo nella bolletta `EB_h` (Eq. 24) e nel calcolo di `SDR_t` dai flussi ottimizzati, quindi il prezzo è un trasferimento ex post che non cambia il dispacciamento. Il testo parla di "two ex-ante pricing methods" (p. 1), formula che non corrisponde alla struttura del modello `[INFERENZA]`. L'Eq. (23) non include un tetto per `SDR_t ≥ 1`, mentre il testo dice che in presenza di surplus il prezzo vale il FiT (p. 3): senza `min(SDR_t, 1)` il prezzo scenderebbe sotto il FiT `[INFERENZA]`.
- **Metriche di equità poco informative.** `mMF_t` confronta bollette assolute di famiglie con consumi molto diversi e vale 0 non appena un membro ha bolletta nulla (ad esempio una famiglia con batteria che copre il carico di notte); lo "0 in assenza di PV" è quindi un artefatto della metrica, non la prova che "this metric requires energy sharing" (p. 5). `QoE_t` divide per `D_{t,h} − P^PV_{t,h}`, che può annullarsi o diventare negativo per gli esportatori, e non è definito per i periodi senza consumo netto. Le metriche sono calcolate per ogni periodo di 15 minuti e non c'è un valore giornaliero per schema; nessuna misura confronta il beneficio con il contributo del membro `[INFERENZA]`.
- **Incoerenze interne.** (a) Il testo dice che le famiglie 5 e 6 raggiungono "full battery charge (with 6.5 kWh and 8.5 kWh)" (p. 4), ma le capacità in Tab. 1 sono 12,9 e 17,2 kWh; 6,5 e 8,5 sono invece le potenze di carica in kW. (b) Fig. 2: lo stato di carica iniziale e finale delle famiglie 5 e 6 è, letto sul grafico, circa 0,5 / 0,6 kWh (famiglia 5) e circa 3,8 / 3,8 kWh (famiglia 6), mentre Tab. 1 riporta Initial/Final SoC di 6,45 e 8,6 kWh. (c) In Fig. 2 la famiglia 6 passa da 0 a circa 8,5 kWh in un solo passo di 15 minuti (circa 34 kW), contro un limite di carica di 8,5 kW (Tab. 1) e una carica di circa 1 kWh nello stesso periodo in Fig. 3. (d) La media di "5.88 kWh" per prosumer non è compatibile con le tre coppie citate, che da sole sommano 73,08 kWh (6 × 5,88 = 35,3 kWh). Sono letture di grafico o dichiarazioni non spiegate (`[INFERENZA — lettura di figura]` per (b) e (c)).
- **Collegamenti nel corpus:** cita `minuto2022` (Minuto & Lanzini, 2022). Gli indici QoE e MinMax (qui "mMF") e il prezzo SDR provengono da Dynge et al. 2023 (*Local electricity market pricing mechanisms' impact on welfare distribution, privacy and transparency*, non nel corpus); il lavoro successivo di Dynge e Cali, `dynge2025`, valuta criticamente QoE, QoS, MinMax ed EI e propone adattamenti, quindi è il riferimento per le debolezze degli indici elencate sopra; gli stessi indici compaiono in `gasca2025`. Per il prezzo MMR cita Gjorgievski et al. 2022 (*Virtual net-billing*, non nel corpus).
