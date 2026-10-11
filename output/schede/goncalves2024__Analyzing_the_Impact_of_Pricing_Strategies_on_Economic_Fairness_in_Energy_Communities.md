# goncalves2024 — Analyzing the Impact of Pricing Strategies on Economic Fairness in Energy Communities

- **File sorgente:** `Paper/Analyzing the Impact of Pricing Strategies on Economic Fairness in Energy Communities.pdf` (5 pagine, testo estraibile; le formule sono estratte in modo imperfetto)
- **Tipo:** conference paper (IEEE PES General Meeting 2024)
- **Lettura:** integrale (pp. 1–5); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Goncalves, C.; Lezama, F.; Vale, Z. (2024). *Analyzing the Impact of Pricing Strategies on Economic Fairness in Energy Communities.* 2024 IEEE Power & Energy Society General Meeting (PESGM). DOI 10.1109/PESGM51994.2024.10689031. GECAD, LASI – Polytechnic of Porto, Portogallo. Sviluppato nell'ambito del patto di innovazione "NGS – New Generation Storage" (PRR).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** un framework che comprende ottimizzazione dello scambio di energia, schemi di prezzo per le transazioni e metriche di equità "to validate the profit distribution of members in an energy community"; si studia l'impatto di quattro meccanismi di prezzo sull'equità economica.
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Portogallo (dati dell'edificio GECAD a Porto; potenze contrattuali 3,45/6,9/10,35 kW; tariffa retail triplice e FiT 0,045 €/kWh). Nessun riferimento alle regole italiane.
- **Tipo di CER:** energy community con scambio peer-to-peer di surplus, gestita da un *Community Manager* (p. 2).
- **Membri:** 10 famiglie in area suburbana: 6 prosumer con PV (picchi ≈ 4 kW per H1–H2, ≈ 8 kW per H3–H4, ≈ 12 kW per H5–H6, con PV "aggiuntivo" ipotizzato) e 4 consumatori (H7–H10). Le potenze PV diverse sono usate come proxy "indicative of income levels" (p. 3).

## 4. Metodo
- **Modello:** MILP di market clearing che minimizza le bollette (acquisti/vendite verso rete e peer; vincoli di bilancio, binari anti-simultaneità e limiti; Eq. 1–11, p. 2). I prezzi delle transazioni fra peer sono applicati *dopo* l'ottimizzazione (ex-post pricing).
- **Dati:** un solo giorno a passi di 15 minuti (96 punti); profili PV da un dataset GECAD, profili di consumo da famiglie europee (rif. [10]); i profili dei 6 prosumer derivano da un profilo base con piccole variazioni casuali (p. 3). Baseline "Business as Usual" (BAU): bolletta con autoconsumo, import a tariffa retail ed export a FiT.
- **Software:** Python (Spyder/Anaconda), libreria MIP con solver CBC; Intel i5-8250U, 20 GB RAM (p. 4).

## 5. Meccanismi di ripartizione analizzati
Quattro **meccanismi di prezzo per le transazioni peer** (p. 2–3), che di fatto redistribuiscono il surplus fra venditori e acquirenti:
1. `C^EC = C^R` (prezzo retail): favorisce i venditori.
2. `C^EC = C^FiT`: favorisce gli acquirenti.
3. `C^MMR` (mid-market rate): media fra FiT e prezzo retail.
4. `C^SDR` (supply-demand ratio): `C^SDR = SDR·C^FiT + (1 − SDR)·C^R`, con `SDR = (vendite alla rete + vendite peer)/(acquisti dalla rete + acquisti peer)` (Eq. 12–13).
Nessuna regola di ripartizione del tipo quote uguali/proporzionali/Shapley.

## 6. Metriche
- **Economiche:** bolletta per famiglia e media per gruppo (Low PV, Mid PV, High PV, No PV) rispetto al BAU (Tab. II).
- **Equità:** **QoE** `= 1 − σ_t/σ_t^max`, con σ_t deviazione standard dei prezzi percepiti `EB_h/(D − P_PV)` (Eq. 15–17); **mMF** `= min_h(EB_h)/max_h(EB_h)` (Eq. 19) (p. 3).
- **Sociali / ambientali / engagement:** nessuna misura (citate solo nell'introduzione).

## 7. Risultati principali (Tab. II, p. 5; valori medi della bolletta del giorno, unità `[NON SPECIFICATO]`)
- BAU: Low PV 5,95; Mid-PV 2,12; High PV 2,12; No PV 3,72.
- Variazioni percentuali rispetto al BAU: **C^R**: −4,87% (Low), −15,09% (Mid), −86,32% (High), 0% (No PV). **C^FiT**: −24,37%, −7,08%, −5,66%, −9,95%. **C^MMR**: −14,62%, −10,85%, −45,75%, −5,11%. **C^SDR**: −18,49%, −6,60%, −24,53%, −9,41%.
- Gli autori: la sostituzione di `C^EC` con uno qualunque dei quattro metodi dà bollette uguali o inferiori al BAU; la famiglia 6, con C^R o C^MMR, ottiene bolletta negativa (p. 5).
- Equità (Fig. 5–6, p. 5): fuori dalle ore PV i valori sono ≈ 1; nelle ore di scambio `C^SDR` risulta "more equitable" di `C^FiT`, "approaching a fairness metric value of 1 in both QoE and mMF" (solo nelle figure, nessun numero nel testo).

## 8. Limitazioni dichiarate dagli autori
Nessuna esplicita (nessuna sezione dedicata).

## 9. Future work dichiarati dagli autori
- p. 5 (Sez. V): "Future work will explore larger communities, scalability, dynamic pricing methods, and additional fairness metrics to further enhance the effectiveness of pricing strategies."
`[INFERENZA — test B.1]` **Misto**: "additional fairness metrics" è una richiesta di più indicatori di equità (portata più generale), ma la frase è formulata come estensione del proprio studio sui prezzi.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Orizzonte di **un solo giorno** e 10 membri: nessun effetto stagionale né di scala; qualunque conclusione sull'equità è su un singolo profilo.
- `[INFERENZA]` Il contesto è un mercato locale P2P con prezzi liberi, non un regime di incentivo sull'energia condivisa come quello italiano: i risultati non sono trasferibili senza riformulare la funzione di valore.
- `[INFERENZA]` `mMF` confronta bollette assolute di famiglie con consumi molto diversi: un valore vicino a 1 non indica equità rispetto al contributo; `QoE` normalizza sul fabbisogno netto ma non sul contributo alla generazione.
- `[INFERENZA]` Nel Tab. II il BAU delle famiglie Mid-PV e High-PV è lo stesso (2,12), a fronte della frase "as PV generation rises ... BAU bills experience a reduction" (p. 4). Le percentuali sono coerenti con questo valore, quindi non è un errore di calcolo, ma il confronto Mid/High è poco informativo.
- `[INFERENZA]` Dal punto di vista della "ripartizione" il meccanismo che massimizza i guadagni dei prosumer (C^R) è quello che lascia i consumatori senza beneficio (0%): evidenzia un trade-off venditori/acquirenti, non risolto da un criterio di equità esplicito.
