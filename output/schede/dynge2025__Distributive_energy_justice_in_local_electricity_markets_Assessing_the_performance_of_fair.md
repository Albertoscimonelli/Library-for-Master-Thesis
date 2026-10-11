# dynge2025 — Distributive energy justice in local electricity markets: Assessing the performance of fairness indicators

- **File sorgente:** `Paper/Distributive energy justice in local electricity markets_ Assessing the performance of fairness indicators.pdf` (13 pagine, testo estraibile; i risultati numerici sono in gran parte nelle figure)
- **Tipo:** articolo su rivista (Applied Energy, Elsevier, open access)
- **Lettura:** integrale (corpo pp. 1–12); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Dynge, M. F.; Cali, U. (2025). *Distributive energy justice in local electricity markets: Assessing the performance of fairness indicators.* **Applied Energy**, 384, 125463. DOI 10.1016/j.apenergy.2025.125463. Ricevuto 15/4/2024; rivisto 12/1/2025; accettato 27/1/2025; online 8/2/2025. NTNU (Trondheim) e University of York.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** definire formalmente la *distributive energy justice* nel contesto dei local electricity markets (LEM) e valutare come gli indicatori di equità più diffusi la rappresentano; proporre adattamenti degli indicatori.
- **Domande esplicite (p. 2):** "What fairness indicators should be used in further studies on local electricity markets?", "How is fairness addressed in the current literature on local electricity markets?", "How can distributive energy justice be defined in a local electricity market context?", "How do the currently used fairness indicators capture fairness in local electricity markets?" (la prima compare come punto in testa all'elenco; le altre sono elencate subito sotto).
- **Gap dichiarato (pp. 2–3):** "No research has been found addressing or comparing the performance of these indicators"; "their relevance to the local electricity market setting has never been explicitly discussed" (negative universali degli autori, cfr. B.3).

## 3. Contesto
- **Paese / quadro normativo:** Norvegia (dati di 10 famiglie di Oslo, prezzi NordPool NO1 2021, FiT = prezzo spot, tariffa di rete 4,48 c€/kWh; p. 7). Non è un contesto di CER con incentivo sull'energia condivisa.
- **Tipo di CER:** *local electricity market* di peer trading, esteso oltre la comunità; gli asset sono individuali; mercato centralmente compensato a basso costo totale con prezzi interni *supply–demand ratio* (pp. 4–5).
- **Membri:** 10 famiglie; 9 casi con 1/5/10 proprietari di PV (5 o 10 kWp) e 0/1/5 batterie (6 kWh/3 kW, efficienza 90%) (Tab. 2–3, p. 7). Consumi 5–32 MWh/anno.

## 4. Metodo
- **Modello:** LP di market clearing (Eq. 1–8) con prezzi ex-post SDR `λ_t = s_t·C^FiT + (1 − s_t)(C^spot + C^g)` (Eq. 9–10). Gli indicatori sono calcolati ex-post come medie mensili (allocazione) e annuali (costi).
- **Dati:** consumi reali norvegesi ott. 2020–mar. 2022; PV da PVGIS (irradianza 2020); nessun PV reale nelle case.
- **Software:** `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati
Non si confrontano regole di ripartizione di un incentivo. Si analizza l'esito di un mercato (LP + prezzo SDR) con quattro indicatori di equità e tre loro varianti (p. 4–6):
- **Definizione proposta (p. 4):** "Distributive energy justice in a local electricity market can be formally defined as the state in which all market participants benefit from participating in the local market compared to other alternatives. This state is achieved when prosumers and flexibility providers receive rewards that are proportional to their respective contributions to the energy balance within the local electricity market. Simultaneously, it ensures that consumers benefit from an equal distribution of resources." (equità ai prosumer, uguaglianza ai consumatori).

## 6. Metriche
- **Indicatori originali:** MinMax (rapporto min/max degli import dalla rete all'ingrosso, Eq. 11), QoS (indice di Jain sui volumi scambiati, Eq. 12), QoE (1 − σ dei prezzi percepiti/σ_max, Eq. 13–14), Equality Index (variante Gini sui risparmi di costo, Eq. 15).
- **Indicatori proposti:** MinMax separati per prosumer (quote di surplus venduto) e consumatori (volumi acquistati) (Eq. 16–17); QoS_new (Jain su quote per i prosumer e su volumi per i consumatori, pesato per ρ e μ; Eq. 18); EI_new (risparmio *percentuale* per i prosumer e *monetario* per i consumatori; Eq. 19).
- **Sociali / ambientali / engagement:** non misurati; la giustizia procedurale e di riconoscimento è esclusa (p. 2–4).

## 7. Risultati principali
- Tutti i partecipanti risparmiano rispetto al solo mercato all'ingrosso in tutti i nove casi; le batterie aumentano i risparmi di tutti (p. 9).
- MinMax originale: valori quasi uguali in tutti i casi (poco informativo). MinMax prosumer ≈ 1; MinMax consumatori anche molto basso (es. 0,11 con 1 PV e 1 batteria: 10,5 vs 93 kWh/mese) (p. 8).
- QoS: con l'originale 4 partecipanti su 10 (40%) risultano "equi", con il nuovo 8 (80%) (p. 9). QoE sempre alto per la piccola differenza tra i limiti di prezzo (p. 9–10); EI originale giudica "meno equi" i casi con un solo prosumer, giudizio che gli autori mettono in discussione (p. 10).
- Conclusione (p. 12): "the current definitions of MinMax, QoS and EI do not align with the definition of distributive justice in this article, and are more suitable where strict equality is desired"; il QoE richiede ulteriori prove con altri meccanismi di prezzo.

## 8. Limitazioni dichiarate dagli autori
- p. 4: il mercato è "a pure transactional market model and does not consider any grid impacts"; i punti di vista da legami sociali di comunità e quelli degli operatori sono ignorati.
- p. 10: "It is, however, challenging to determine whether the indicator is suitable as a fairness measure overall or if the reason for the suboptimal behaviour is due to the pricing mechanism used in this article. Specific alterations are thus not proposed at this stage. Further investigation should be made using pricing mechanisms with differential prices for the participants, such as auction mechanisms or distributed optimisation mechanisms."
- pp. 10–11: il QoE dipende da σ_max (costante in questo caso) e l'EI "can reach the same value for two very different distributions of cost savings".

## 9. Future work dichiarati dagli autori (Sez. 8, p. 12, verbatim)
"Future studies should engage in interdisciplinary dialogues to comprehensively grasp the societal acceptance criteria for these market structures. This will allow for a more theoretically grounded definition of distributive energy justice in local electricity markets. Furthermore, additional investigation is needed to refine fairness indicators, ensuring their effectiveness across diverse market models. Potential barriers to their implications, such as data privacy considerations, should also be further investigated. More concrete evaluation criteria could also be derived to perform a more generalisable and comprehensive evaluation of multiple fairness indicators. When these fundamental concepts are adequately investigated, one can consider the need to develop entirely new, specific indicators for a local electricity market context."
- Sez. 7.1 (p. 11): la scelta degli indicatori dipende dall'obiettivo del mercato (servizi di rete, investimenti in DER, democrazia energetica/povertà energetica).
`[INFERENZA — test B.1]` Il contributo del paper **è già un confronto multi-indicatore** (4 indicatori × 9 casi): la sua richiesta di raffinare e valutare in modo più generalizzabile "multiple fairness indicators" è del tipo **"generale"** (forte), con la cautela che il contesto è il LEM P2P, non la CER italiana.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` È il paper del corpus che formalizza meglio la distinzione **equity** (ricompensa proporzionale al contributo) vs **equality** (stessa ricompensa a prescindere dal contributo) e discute quale indicatore le rappresenti (nota p. 2). Utile per definire le metriche di equità nella tesi.
- `[INFERENZA]` Le famiglie hanno consumi e PV molto diversi, ma il campione è di 10 membri e senza regole di ripartizione dell'incentivo: i risultati non si trasferiscono direttamente al regime CACER.
- `[INFERENZA]` L'EI proposto confronta risparmi % per i prosumer e € per i consumatori (due metriche diverse nello stesso indice): scelta normativa discutibile, non validata.
- `[INFERENZA]` Le affermazioni "no research has been found" sono negative universali e non vanno riprese così in un gap.
