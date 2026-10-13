# giudice2026 — A performance-based incentive sharing mechanism for communities of residential end users leveraging an ontology-driven approach

- **File sorgente:** `Paper/A performance-based incentive sharing mechanism for communities of residential end users leveraging an ontology-driven approach.pdf` (21 pagine, testo estraibile)
- **Tipo:** articolo su rivista (Building and Environment, Elsevier, open access; numero speciale "Climate Change Impacts for Buildings")
- **Lettura:** integrale (corpo pp. 1–19, compresa la parte finale delle Conclusioni che nell'estrazione compare dopo "References"); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Giudice, R.; Piscitelli, M. S.; Capozzoli, A. (2026). *A performance-based incentive sharing mechanism for communities of residential end users leveraging an ontology-driven approach.* **Building and Environment**, 287, 113786. DOI 10.1016/j.buildenv.2025.113786. Ricevuto 28/2/2025; rivisto 18/9/2025; accettato 29/9/2025; online 15/10/2025. TEBE Research Group / BAEDA Lab, Politecnico di Torino.

## 2. Obiettivo e research question
- **Obiettivo (autori):** meccanismo di condivisione degli incentivi basato sulla performance (capacità dell'utente di spostare i consumi sulle ore di surplus), con baseline dinamica di consumo e modello di metadati basato su ontologie (SAREF, S4BLDG, S4ENER) (abstract, p. 1).
- **Research question esplicite (p. 2):**
  1. "Can individual consumption baselines be effectively used to identify and reward virtuous user behavior within RECs and CSC groups?"
  2. "Does a hybrid redistribution mechanism based on consumption performance improve fairness compared to standard allocation rules?"
  3. "Can an ontology-based data structure support scalable and automated deployment of such mechanisms across heterogeneous community configurations?"
- **Gap dichiarato (p. 2):** "Further research is needed to develop allocation mechanisms that explicitly consider virtuous/unvirtuous behavior of individual members towards the achievement of objectives at community level and that could help maintain member engagement".

## 3. Contesto
- **Paese / quadro normativo:** Italia; incentivo sull'energia condivisa "in the range between 80 and 120 €/MWh" (p. 2); energia condivisa = minimo orario fra immissione e prelievi (p. 2).
- **Tipo di CER:** autoconsumo collettivo (CSC) con **impianto PV centralizzato** (che alimenta parti comuni, una pompa di calore centralizzata e un piccolo BESS); il condominio funge da prosumer, i 13 appartamenti da consumatori; condivisione virtuale (p. 5). Gli utenti non stanno realmente nello stesso edificio: il setup *modella* appartamenti di un condominio (p. 5).
- **Membri:** 13 utenze residenziali in Italia; dati reali a 15 minuti dal 1/1/2023 al 31/7/2023 (7 mesi, p. 5).

## 4. Metodo
- **Ripartizione prosumer/consumer:** quote α e β dell'energia condivisa (Eq. 1–2, p. 3).
- **Meccanismo proposto (Sez. 5.1, pp. 7–8):** nelle ore di surplus, quota di energia condivisa del consumatore `SE_c^t = (1 − SS_add)·E_c,cons^t + SS_add·(E_c,cons^t + a_c^t − d_c^t)` (Eq. 6), dove `a` (aggiunta, comportamento "virtuoso" = consumo sopra la baseline) e `d` (detrazione, consumo sotto la baseline) sono ripartite proporzionalmente a partire da `A_t = min(ΔE⁺, |ΔE⁻|)` (Eq. 7–12). Il peso della componente performance è l'indicatore **SS_add = SS_pot − SS** (autosufficienza aggiuntiva potenziale): se il surplus è già pienamente sfruttato (SS_add = 0) si applica il metodo *progressive*.
- **Baseline:** 8 modelli candidati (7 aritmetici High X of Y / Medium X of Y + XGBoost con riaddestramento settimanale); selezione giornaliera del modello con minimo RMSE_adj (permutazione ±1 h nelle ore di surplus) sui 5 giorni precedenti (Sez. 5.2, pp. 8–9).
- **Ontologie:** grafo RDF, query SPARQL, moduli Python (Sez. 5.3, 6.1).
- **Software:** Python (p. 12); `[NON SPECIFICATO]` solver o librerie oltre a XGBoost/SPARQL.

## 5. Meccanismi di ripartizione analizzati
- **Progressive** (water-filling a partire dal membro con minor consumo; rif. [13] del paper): usato come riferimento "standard".
- **Proportional** (sulla quota di consumo; α/β con soglia minima di [14]) e **ownership-based**: descritti in Sez. 2.1 (pp. 2–3), non simulati.
- **Hybrid progressive/performance-based** (proposto).
- Rassegna di Sez. 2.1: cita Queiroz et al. (Portogallo), Eisner et al. (proporzionale statico/dinamico/ibrido/progressivo) e un lavoro con chiavi dinamiche (Pearson/trend).

## 6. Metriche
- **Economiche:** variazione dell'incentivo giornaliero rispetto al metodo progressive (±40%), quote di energia condivisa aggiunta/detratta per membro (Fig. 14–18). Esempio numerico con tariffa ipotetica 109 €/MWh (p. 15).
- **Tecniche:** SS, SS_pot, SS_add (Eq. 3–5); RMSE_adj per l'accuratezza delle baseline (Fig. 10–13).
- **Equità:** nessun indice quantitativo; la "fairness" è argomentata (p. 16).
- **Sociali / ambientali:** nessuna.
- **Engagement:** non misurato; l'impatto sul coinvolgimento è rimandato a lavori futuri.

## 7. Risultati principali
- Baseline migliori: Medium 4 of 8, Medium 6 of 8 e XGBoost; per i membri 5, 9, 10 la differenza di RMSE_adj fra miglior e peggior modello è 40–50%; per il membro 10 XGBoost è scelto in oltre l'80% dei giorni (p. 12–13). Tutti i membri usano da 3 a 8 modelli diversi nel periodo. Variazione della finestra di selezione (3/5/7 giorni): differenza di scelta < 5% (p. 13).
- Su 7 mesi, saldo a−d positivo per i membri 1, 5, 6, 9, 12, 13; negativo per 10 e 11; neutro per 2, 3, 4, 7 (p. 15).
- Il membro con comportamento adeguato aumenta (o riduce) l'incentivo giornaliero "by up to 40%" rispetto al metodo progressive (p. 16; abstract).
- Il meccanismo è più efficace con contratti a prezzo fisso; con tariffe dinamiche/ToU lo spostamento di carico è più complesso (p. 16).
- Estensione a REC: es. 80% dell'incentivo ai consumatori e 20% ai prosumer, quest'ultima quota ripartita per proprietà o energia scambiata (p. 16).

## 8. Limitazioni dichiarate dagli autori
- p. 16 (Sez. 6.3): "This 40% variation should not be interpreted as a generalized outcome, but rather as an observation of possible redistributions of shared energy quotas arising from the interplay between individual and collective behaviors. Moreover, this result does not account for how uncertainties in baseline estimation may propagate through the redistribution logic and affect the final incentive allocations, particularly for users with high load variability."
- p. 17 (Sez. 7): "While the proposed mechanism demonstrates encouraging results within the studied CSC group, several limitations may affect its generalizability to broader contexts. First, user behavior in residential settings is inherently variable and context-dependent. This variability may compromise the robustness of baseline estimations, particularly in communities with markedly different socio-demographic profiles, occupancy patterns, or access to flexible loads. Second, the framework presupposes a degree of regulatory flexibility in defining and allocating economic incentives among participants. However, in jurisdictions governed by rigid or centrally regulated schemes, such customization may not be feasible, limiting the practical implementation of the approach. Third, the economic viability of the proposed incentive mechanism is highly sensitive to local tariff structures. When electricity prices during peak periods outweigh the perceived benefits of the incentive the financial incentive would be insufficient to justify behavioral changes."
- p. 4 (Sez. 2.2): la stima di baseline per singole utenze residenziali è "particularly challenging" (variabilità dei consumi individuali).

## 9. Future work dichiarati dagli autori
- p. 17 (Sez. 7): "Future work could explore integrating a predictive approach into this envisioned decision support system for community energy management, allowing members to take informed decisions. This requires advanced forecasting capabilities to predict aggregated energy production and consumption within the community..."
- pp. 17–18 (Sez. 7): "future work will pursue several complementary directions. Sensitivity analyses will be conducted on critical design and operational parameters, such as the size and orientation of PV systems, the number and composition of community members, and their level of end-use electrification, in order to assess the framework performance across a variety of technical and organizational configurations. [...] Finally, the long-term impacts of the incentive mechanism on both individual consumption patterns and collective engagement dynamics will be systematically evaluated. This includes investigating whether the mechanism promotes permanent behavioral change, fosters a stronger sense of participation within the community, and remains effective under evolving market, regulatory, and social conditions."
- p. 19 (Sez. 8): integrazione di capacità real-time e, possibilmente, LLM per raccomandazioni agli utenti; estensione ai contesti REC con quota ai prosumer (pp. 16, 18).
`[INFERENZA — test B.1]` **Self-referential**: tutti gli sviluppi sono estensioni del *proprio* meccanismo. Il punto sulla "number and composition of community members" è però una richiesta di analisi di sensibilità su composizione/dimensione, che è un tema generale.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` La RQ2 ("improve fairness compared to standard allocation rules") non è verificata con un indicatore di equità né con più regole: il confronto è solo con il *progressive*.
- `[INFERENZA]` Il caso è un CSC con un unico impianto centralizzato e 13 consumatori puri: manca il caso con prosumer multipli (estensione solo descritta, p. 16).
- `[INFERENZA]` Il meccanismo richiede serie storiche individuali (baseline) e misure disaggregate per utente: coerente con le difficoltà di dati dichiarate dagli stessi autori.
- `[INFERENZA]` Il paper è molto recente (online ottobre 2025): ottimo candidato come "paper recente" per l'ancora di un gap, ma le future work sono tutte estensioni del proprio metodo.
