# eichelbeck2025 — Fair Cost Allocation in Energy Communities Under Forecast Uncertainty

- **File sorgente:** `Paper/Fair Cost Allocation in Energy Communities Under Forecast Uncertainty.pdf` (10 pagine; testo estraibile; Tab. 1–2 e Fig. 3–4 lette su immagine)
- **Tipo:** articolo su rivista (IEEE Open Access Journal of Power and Energy, CC BY 4.0)
- **Lettura:** integrale (corpo pp. 1–10); bibliografia (pp. 10–11) non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF; la numerazione stampata è di +1 (p. 1 del PDF = 2 stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Valute in EUR.

## 1. Riferimento bibliografico
Eichelbeck, M.; Althoff, M. (2025). *Fair Cost Allocation in Energy Communities Under Forecast Uncertainty.* **IEEE Open Access Journal of Power and Energy**, vol. 12 (2025). DOI 10.1109/OAJPE.2024.3520418. Ricevuto 9/8/2024; rivisto 31/10/2024; accettato 5/11/2024; pubblicato 19/12/2024; versione corrente 24/1/2025. Technical University of Munich. Finanziamento: German Research Foundation, grant AL1185/9-1. Intervallo di pagine stampate: `[NON SPECIFICATO]` nel PDF letto (numerazione 2–11).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** introdurre condizioni di equità per l'allocazione dei costi con conoscenza imperfetta (previsioni inaccurate), mostrare che formano un fronte di Pareto, dimostrare che il valore di Shapley applicato nativamente (*Shapley value mechanism*, SVM) "has unfavorable consequences for flexibility-providing community members and generally does not yield solutions on this Pareto front", e proporre un meccanismo che alloca con lo SVM il costo a conoscenza perfetta e il "costo dell'ignoranza" tramite un problema convesso multi-obiettivo risolvibile come LP o QP.
- **Gap dichiarato (abstract p. 1; Sez. I, p. 2):** "While many allocation mechanisms have been developed, existing literature does not account for the implications of inaccurate forecasts on the fairness of the allocation." E: "While the existing literature on cooperative cost allocation in ECs is highly sophisticated regarding game-theoretical robustness and computational efficiency, it does not define fairness in the presence of imperfect knowledge nor investigate the implications of inaccurate forecasts on individual members with different types of assets." (negative universali degli autori, cfr. B.3).
- **Contributi dichiarati (p. 2):** (i) condizioni di equità e prova di Pareto; (ii) dimostrazione che lo SVM nativo svantaggia chi fornisce flessibilità; (iii) programma ottimo convesso multi-obiettivo che garantisce soluzioni sul fronte.
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** nessun quadro normativo; dati SimBench (rete rurale tedesca 1-LV-rural2–1-sw) e prezzi spot danesi (Energidataservice) nel secondo caso (pp. 7–8). Il paper non considera incentivi.
- **Tipo di CER:** comunità con un *dispatch controller* centrale (democraticamente amministrato dai membri) che comanda accumuli, generatori dispatchabili e scambi con la rete, mentre carichi inflessibili e rinnovabili sono disturbi esogeni; il costo di un periodo di fatturazione è allocato ex post (p. 2). Modello "intentionally simple": nessun vincolo di flusso di potenza (p. 2).
- **Membri:** caso 1: tre famiglie (prosumer con PV, "storage provider" con ESS da 10 kWh, consumatore puro; carico totale 214,97 kWh, PV 88,89 kWh su 72 ore; prezzi 0,34 €/kWh acquisto e 0,08 €/kWh vendita) (p. 7–8); caso 2: rete Kerber a 27 bus/30 nodi con 14 famiglie e componenti assegnati a caso (carico 100%, batteria 50%, PV 75%), cinque realizzazioni su tre giorni del 2016 (p. 8).

## 4. Metodo
- **Costo e dispatch (Sez. II, pp. 2–3):** costo operativo `c(u_t, ψ_t)` convesso (mercato, generatori, usura ESS); dispatch come MPC a orizzonte mobile con previsioni (Eq. 2); costo totale `C(N)` (Eq. 3); scomposizione `C = C̃ + Č` (Eq. 4): costo a conoscenza perfetta `C̃` e *cost of ignorance* (CoI) `Č ≥ 0`, legato al valore dell'informazione ex post.
- **Gioco cooperativo (Sez. II-D, p. 3):** giocatori N, costo di coalizione `C(S)`, contributo marginale, costo stand-alone `φ^a_i`, **regret** `ε_i = φ_i − φ̃^a_i` (pagamento meno costo stand-alone a conoscenza perfetta; il regret è sovrastimato perché lo stand-alone è assunto a conoscenza perfetta, p. 3–4). Shapley `φ^SVM_i` (Eq. 5), con approssimazioni per campionamento e normalizzazione per l'efficienza (p. 4).
- **Condizioni (Sez. III, p. 4):** C1 *causation* (simmetria, linearità, giocatore nullo, a conoscenza perfetta); C2 efficienza `Σφ_i = C`; C3 *minimum divergence* `min ‖φ − φ̃‖_p`, `p ≥ 2`; C4 *minimum worst-case regret* `min max_i(φ_i − φ̃^a_i)`. Lemma 1: C1–C4 non possono essere soddisfatte insieme → fronte di Pareto.
- **Meccanismo proposto (Sez. IV-B, pp. 5–7):** `φ = φ̃ + γČ` con `Σγ_i = 1`, `γ_i ≥ 0` (Eq. 8–9); somma pesata normalizzata `min (1 − μ)J^R(z) + μJ^D(γ)` (Eq. 11), `μ ∈ [0,1]`; per `p = ∞` due LP, per `p = 2` un LP e un QP (Corollary 1).
- **Software:** libreria Python open source CommonPower [34], pandapower [36]; Shapley approssimato con il metodo di Castro et al. [14] nel caso 2 (p. 8–9).

## 5. Meccanismi di ripartizione analizzati
(a) **Shapley "nativo"** applicato al costo con conoscenza imperfetta; (b) **meccanismo proposto**: Shapley sul costo a conoscenza perfetta più allocazione del CoI con pesi `γ` ottenuti dal problema multi-obiettivo (divergenza minima vs. regret massimo minimo). Gli autori citano senza testarli: allocazioni proporzionali (consumo/produzione [11],[12]) e nucleolo [5],[7],[8]; il nucleolo è lasciato a lavori futuri.

## 6. Metriche
- **Economiche:** costo di coalizione, costo a conoscenza perfetta e CoI (€), pagamento per membro, quota di CoI per membro.
- **Equità (operazionalizzazione degli autori):** *causation* (simmetria, linearità, giocatore nullo), efficienza, **divergenza** (p-norma rispetto all'allocazione a conoscenza perfetta), **worst-case regret** (massimo regret fra i membri), funzioni obiettivo normalizzate `J^D` e `J^R` (Tab. 2). Il worst-case regret è un criterio *min-max* sul beneficio individuale.
- **Altre:** correlazioni di Pearson fra CoI, errore medio assoluto delle previsioni (MAE) e distanza dal fronte di Pareto (Tab. 1).
- **Sociali / ambientali / engagement:** non misurati. L'incentivo ad aderire è rappresentato dal regret ("members have the incentive to join the EC", p. 4) ma non garantito: "While we cannot guarantee that the regret of all members is negative, we aim to minimize the maximum regret across the EC."

## 7. Risultati principali (numeri dal paper)
- **Esempio 1 (pp. 4–5; Teorema 1):** due membri (carico inflessibile 1 kW; ESS 1 kW/1 kWh), 4 passi; prezzi previsti 1,0 → 2,0 → 0,5 €/kWh, reali 1,0 → 0,0 → 0,5 €/kWh. Costi: senza ESS 1,5 €; con previsioni perfette 1,0 €; con previsioni errate 2,0 € (CoI = 1,0 €). SVM: `φ_i = 0,5`, `φ_j = 1,5` (tutto il CoI al membro con ESS); regret `ε_i = 1,0`, `ε_j = 0`; divergenza 1,0; il punto di Pareto ripartisce il CoI a metà (`φ_i = 0,0`, `φ_j = 2,0`), con regret 0,5 e divergenza ≈ 0,71.
- **Caso 1, tre famiglie (p. 8; Fig. 2–4; CoI = 4,96 €):** lo SVM nativo assegna il CoI per il 32,53% al prosumer, il 60,90% al fornitore di accumulo e il 6,57% al consumatore. Con il meccanismo proposto, per `μ = 0` il 63,86% del CoI va al prosumer; per `μ = 1` il CoI è ripartito in modo uguale (con regret positivo per il consumatore); per `μ = 0,5` la divergenza massima è limitata a una quota di CoI del 43,22% "while all households maintain a comfortably negative regret". Il punto nativo è "significantly worse than any point on the Pareto front" (Fig. 4).
- **Correlazioni (Tab. 1; dieci simulazioni con previsioni a 1–10 settimane prima):** CoI–MAE 0,64; CoI–Dist 0,52; MAE–Dist 0,63 ("moderately strong positive correlation").
- **Caso 2, rete Kerber (Tab. 2, p. 9; medie su cinque realizzazioni; `p = 2`, `μ = 0,5`):** CoI 3,28 € (1/2/2016), 8,02 € (1/6/2016), 1,57 € (1/10/2016); `J^D` nativo/proposto 0,98/0,25, 1,43/0,35, 0,41/0,08; `J^R` nativo/proposto 1,33/0,01, 1,66/0,06, 0,76/0,00. Fig. 6 (1/6/2016): "the members owning an ESS are allocated more than the entire CoI, while the other members generally pay less than their perfect knowledge payments"; per l'approccio proposto con `μ = 10^−8` le allocazioni dei due gruppi sono "largely in balance".
- **Conclusione degli autori (p. 9):** il meccanismo nativo penalizza chi fornisce flessibilità; "the Pareto front is generally highly non-symmetric, which can make the choice of the weighting parameter µ challenging for practitioners".

## 8. Limitazioni dichiarate dagli autori
- p. 2: modello di sistema "intentionally simple" che non considera i vincoli di flusso di potenza.
- p. 3–4: lo stand-alone è assunto a conoscenza perfetta ("guaranteed overestimation of the regret").
- p. 4: "While we cannot guarantee that the regret of all members is negative".
- p. 5: "it is difficult to link forecast accuracy to total cost straightforwardly".
- p. 5 (nota 2): lo SVM "cannot guarantee stability in a context such as ours [7], [16]"; "previous numerical analysis has shown that the stability benefit of nucleolus-based approaches can be rather small [5], [7]".
- p. 9: la scelta del peso `μ` è "challenging for practitioners".

## 9. Future work dichiarati dagli autori (verbatim)
- Sez. I, p. 2: "As the central focus is on fairness, we limit our study to the SVM, leaving the investigation of nucleolus-based approaches for future work."
- Sez. V-B, p. 9: "However, further research would be beneficial for navigating the central trade-off." (fra divergenza minima e regret massimo minimo).
`[INFERENZA — test B.1]` Il primo è **self-referential** (estendere la propria costruzione al nucleolo), ma coincide con un tema segnalato anche in `cremers2023` (confrontare Shapley con nucleolo e least-core); i due paper indipendenti convergono su questa direzione. Il secondo è self-referential.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` L'incertezza di previsione riguarda il *dispatch* di accumuli e generatori. Nel regime CACER l'incentivo sull'energia condivisa è calcolato ex post su misure orarie (minimo fra immissione e prelievo), quindi il CoI non si presenta nella ripartizione dell'incentivo, salvo che la comunità gestisca asset flessibili con previsioni: il paper è contestuale, non trasferibile direttamente.
- `[INFERENZA — esempio 1]` Anche l'allocazione proposta non garantisce la razionalità individuale: nell'esempio il membro senza flessibilità paga 2,0 contro 1,5 stand-alone (regret +0,5); anche lo SVM (regret +1,0 per il membro con ESS) viola la stessa condizione. Il criterio scelto è quindi la minimizzazione del peggiore regret, non l'assenza di regret positivi.
- `[INFERENZA]` La proposta sposta sui membri senza flessibilità (che non hanno causato l'errore) una parte del CoI: è coerente con la scelta di "minimum divergence" ma contraddice, nello stesso esempio, il principio di causazione che gli autori usano come proxy di equità (p. 4). La scelta di `μ` determina il compromesso, e il paper non fornisce una regola per sceglierlo.
- `[INFERENZA — aritmetica sulla Tab. 2]` Il rapporto fra PV e carico nei tre giorni è 0,34 (1/2), 1,24 (1/6) e 1,16 (1/10) mentre il CoI è 3,28, 8,02 e 1,57 €: la tesi che "CoI being larger when more energy is generated relative to power demand" (p. 9) è sostenuta dal giorno 1/6 ma non è monotona (1/10 ha rapporto più alto di 1/2 e CoI più basso). Con soli tre giorni e cinque realizzazioni per giorno non c'è evidenza statistica.
- `[INFERENZA]` Lo SVM è calcolato in modo approssimato (Castro et al. [14]) nel caso 2: i confronti con il meccanismo proposto includono l'errore di campionamento, non quantificato (`[NON SPECIFICATO]`). Il paper cita `cremers2023` solo nella versione di conferenza ACM e-Energy 2022 [19].
- `[INFERENZA]` Per la tesi: introduce *regret* (rispetto allo stand-alone), *divergenza* dall'allocazione di riferimento e *worst-case regret* come criteri di equità calcolabili con un modello numerico; sono applicabili in Matlab a una `v(S)` di CER purché sia definito il costo/beneficio stand-alone.
