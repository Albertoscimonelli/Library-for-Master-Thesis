# chatel2026 — Designing energy sharing in energy communities: Review of coordination mechanisms and internal tariff structures

- **File sorgente:** `Paper/Designing_energy_sharing_in_energy_communities__Review_of_coordination_mechanisms_and_internal_tariff_structures.pdf` (23 pagine; testo estraibile; Fig. 3 e Tab. 1 letti su immagine, la Tab. 1 non riga per riga; Tab. 2 e Eq. 1–38 letti dal testo)
- **Tipo:** rassegna su rivista (RSER); «structured analytical review», dichiaratamente non una revisione PRISMA né uno studio bibliometrico (p. 5). Nessun dato.
- **Lettura:** integrale (corpo pp. 1–21, con le Appendici assenti); bibliografia (pp. 21–23) letta come elenco, non riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione della rivista). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente. Le virgolette riportano il testo degli autori.

## 1. Riferimento bibliografico
Chatel, A.; Notton, G.; Faggianelli, G. A.; Voyant, C. (2026). *Designing energy sharing in energy communities: Review of coordination mechanisms and internal tariff structures.* **Renewable and Sustainable Energy Reviews**, 239, 117139. https://doi.org/10.1016/j.rser.2026.117139. Ricevuto 3/3/2026; rivisto 6/5/2026; accettato 22/5/2026; online 28/5/2026. Università di Corsica Pasquale Paoli (UMR CNRS 6134) e Mines Paris-PSL (OIE). Finanziamenti: `[NON SPECIFICATO]` (nessuna sezione). Dati: «No data was used» (p. 21).

## 2. Obiettivo e research question
- **Obiettivo (abstract p. 1; p. 8):** un esame «structured and unified» dello scambio di energia nelle EC: regole di allocazione, coordinamento basato su ottimizzazione, algoritmi distribuiti, paradigmi di mercato, progettazione delle tariffe interne; confronto sistematico dei paradigmi per «allocative efficiency, incentive compatibility, scalability, fairness integration, and regulatory embedding».
- **Posizionamento (review of reviews, pp. 5–8):** 58 rassegne degli ultimi cinque anni (Tab. 1); «Only 9 reviews address at least one of the topics covered in our article» (p. 5). La più vicina è Basaran et al. [86], che però «provide only a concise treatment of optimization methods and their effectiveness» (p. 8). Gasca et al. [85] «explain the principles of profit redistribution comprehensively, incorporating the notion of fairness, but they disregard the optimization of energy flows within ECs» (p. 8).
- **Gap dichiarati (Sez. 4.1, pp. 19–20):** vedi §8 sotto.
- **RQ formulata come domanda?** No; contributi in forma affermativa.

## 3. Contesto
- **Paese / quadro normativo:** nessun paese; quadro europeo. Solo EC elettriche (p. 4); i meccanismi trattati «are not limited to currently implemented regulatory arrangements» (p. 9). Distingue fra aspetti fisici ed economici: «In the CSCs context, energy injected into the network, or energy withdrawn from the network refers to the SC at the contractual accounting level rather than the physical reality» (p. 4).
- **Definizione di energia condivisa (p. 4):** `SE = min(GRID→CSC, PV_CSC→grid)` (Eq. 5), da Branchetti et al.; indici SCR e SSR estesi al CSC (Eq. 6–7).
- **Scelta della chiave:** «The choice of a distribution key [29] is flexible and has a significant impact on the economic outcome for a given physical configuration» (p. 4).

## 4. Metodo
- **Quadro unificato (Sez. 2.1–2.3, pp. 9–11):** tutti i meccanismi condividono lo stesso spazio fisico ammissibile (bilancio nodale, dinamica dello storage, scambi con la rete; Eq. 8–11); si differenziano per autorità decisionale, informazione, formazione dei prezzi e fairness. Benchmark del social planner (Eq. 12) come riferimento normativo, «not necessarily as a governance prescription» (p. 10).
- **Tre nozioni di efficienza (Sez. 2.3, p. 11):** tecnica (SCR, SSR, importazioni), allocativa (surplus aggregato, Eq. 13) e economica individuale (`ΔC_i = C_i^baseline − C_i^community`, Eq. 14). Indice SCR/SSR/SCL: Eq. 1–3 (p. 3; lette sull'immagine, corrette).
- **Paradigmi (Sez. 2.4–2.8, pp. 11–17):** rule-based (coefficienti `α_i(t)`, Eq. 15–17; Virtual Net Billing, Eq. 18; coefficienti dinamici o ottimizzati, Eq. 21), allocation-based centralizzata (Eq. 24) e distribuita (ADMM), market-based (equilibri GNE/VI, aste), ibridi (allocation-first, market-first, divergenza fra prezzo duale ed equilibrio, Eq. 32–38). Tab. 2 (p. 17) confronta cinque paradigmi su otto dimensioni.
- **Tariffe interne (Sez. 2.9, pp. 17–19):** rassegna di studi (bill sharing, mid-market rate, intermediate-market rate, supply–demand ratio, post-delivery pool-based da [133]; sei assiomi di [139]: individual rationality, profit-neutrality, equity, monotonicity, cost-causation penalty, cost-mitigation reward).
- **Software / dati:** nessuno.

## 5. Meccanismi di ripartizione analizzati
Rassegna, non confronto: regole a coefficienti statici/dinamici (VNB; Gianaroli et al. [106], Villalonga Palou et al. [107], Madrigal et al. [104], Jorquera-Bravo et al. [109] con equità esplicita), Shapley (Eq. 23) e nucleolo come benchmark cooperativi, envy-freeness, ottimizzazione vincolata dalla fairness `min ΣC_i + γΦ(S_1..S_N)` (Eq. 26), pricing con vincoli di distanza di Wasserstein (Irusta e Morales [130]). Nessuna regola è implementata.

## 6. Metriche
Discussione concettuale: SCR, SSR, SCL; welfare aggregato `W = ΣU_i − C_grid` (Eq. 13); risparmio individuale (Eq. 14); indicatori di fairness citati da altri (Jain, fairness index, massima eccedenza in [93]); «Price of Anarchy» per i mercati (p. 16). Nessun calcolo numerico.

## 7. Risultati principali (affermazioni degli autori)
- **Tab. 2 (p. 17), confronto qualitativo dei cinque paradigmi.** Riga «Fairness integration»: *Implicit via coefficients* (RB), *Can be embedded* (centralizzata e distribuita), *Rare/constrained* (mercato), *Multi-layer* (ibrida). Riga «Welfare optimality»: *No guarantee* (RB); *Yes (under convexity)* (centralizzata, distribuita); *Only under ideal assumptions* (mercato); *Context-dependent* (ibrida).
- **RB (p. 13):** «Consequently, RB CSC mechanisms do not inherently guarantee coalition stability, envy-freeness, or proportional fairness. Their distributive properties are entirely determined by the chosen coefficient rule, which may reflect regulatory simplicity rather than equity optimization.» Con `W(x_RB) ≤ W(x*)` e disuguaglianza stretta in presenza di eterogeneità (Eq. 20, p. 12).
- **Tariffe interne (p. 19):** le tariffe interne devono stare fra prezzo di acquisto e di vendita al dettaglio; «the selection of contracts and the treatment of grid costs for shared energy strongly influence both indi­vidual bills and community-level outcomes, sometimes more than the internal pricing rule itself» (p. 19).
- **Discussione (Sez. 3, p. 19):** «The appropriate design is therefore context-dependent and should be selected according to community size, data availability, regulatory environment, flexibility resources, and distributive objectives.»
- **Conclusioni (Sez. 5.1, pp. 20–21):** «Third, efficiency, fairness, scalability, and regulatory embedding are not orthogonal dimensions. Improving one dimension often weakens another.» (p. 20).

## 8. Limitazioni dichiarate dagli autori
- **Perimetro (p. 4):** solo EC elettriche; coupling di settore e EC termiche escluse. Studi di soli aspetti legali, accettazione sociale, business model generici o EC non elettriche non entrano nel quadro analitico (pp. 4–5).
- **Metodo (p. 5):** non PRISMA e non bibliometrico; selezione dei lavori per rilevanza rispetto alle dimensioni analitiche.
- **Gap della letteratura dichiarati (Sez. 4.1, pp. 19–20), citazioni testuali:**
  1. «A first limitation concerns the lack of conceptual alignment between performance metrics. Technical indicators such as CSC or self-sufficiency are frequently used alongside welfare-based objectives without a systematic articulation of how these criteria interact or conflict.» (p. 19)
  2. «Centralized and distributed allocation frameworks typically presume cooperative participation and truthful parameter revelation, thereby sidestepping incentive compatibility issues.» (p. 19)
  3. «Equity considerations are introduced either through ex post redistribution, cooperative benchmarks, or additional constraints in optimization problems. However, fairness is rarely embedded simultaneously across dispatch decisions, pricing rules, and regulatory conditions.» (p. 19)
  4. «The gap between theoretical optimality and regulatory feasibility further constrains the external validity of many contributions. Optimization-based studies often abstract from legal constraints governing tariffs, grid fees, and settlement mechanisms. […] The divergence between shadow-price optimality and legally admissible arrangements remains insufficiently examined» (pp. 19–20).
  5. Nonconvessità, scalabilità, privacy, validazione empirica su comunità eterogenee (p. 20).
- Sez. 2.8.5 (p. 17): «Many optimization-based models treat regulation as an exogenous constraint rather than an endogenous design parameter, limiting implementation realism.»

## 9. Future work dichiarati dagli autori
Elenco completo (Sez. 4.2 «Future trends», p. 20; verifica B.2):
1. *Integrated mechanism design*: progettare insieme regole di dispatch e di prezzo per efficienza, incentive compatibility e fairness con strutture informative realistiche.
2. *Hybrid multi-layer architectures*: analisi formale della divergenza duale-equilibrio, dell'ammissibilità regolatoria e dei vincoli di fairness fra livelli.
3. *Dynamic and adaptive allocation rules*: oltre i coefficienti statici, con previsione, apprendimento e ottimizzazione, «while maintaining regulatory simplicity».
4. *Distributionally robust and equity-aware formulations*: «Embedding inequality metrics or fairness-oriented constraints directly into equilibrium, distributed, or hybrid coordination models offers a pathway to reconcile social justice objectives with economic efficiency in energy communities.»

`[INFERENZA — test B.1]` Il documento è una rassegna e non un confronto di regole: le sue richieste sono di natura generale e non autoreferenziale. Nessuna di esse è un'ancora diretta su «quanto diversi indicatori concordano sugli stessi meccanismi», ma i gap 1, 3 e 4 sopra (§8) e la conclusione «not orthogonal dimensions» sono **dichiarazioni di stato dell'arte** utilizzabili come ancora di una rassegna recente e autorevole (RSER, maggio 2026). Sono qualitative (la Tab. 2 usa giudizi verbali) e non misurano i compromessi.

## 10. Note del lettore (inferenze mie)
- **Ancora utilizzabile per tre temi diversi:** (a) *compromessi*: la frase «not orthogonal dimensions» è la versione qualitativa, da rassegna, dell'impossibilità assiomatica di `gonzalezasenjo2025`; (b) *misura*: il gap 1 (nessuna articolazione di come i criteri interagiscono o confliggono) sostiene il tema dell'allineamento degli indicatori (`dynge2025`, `gasca2025`); (c) *regolazione*: il gap 4 e la frase sulla regolazione «exogenous constraint rather than an endogenous design parameter» sostengono il tema della regolazione come parte del problema. Il terzo è un'ancora più concettuale della frase generica di `gonzalezasenjo2026` sui «regulatory constraints».
- **Nel tuo modello la regolazione entra nel gioco.** Con il fattore di riduzione F e le categorie esenti il valore di coalizione dipende dalla composizione per categoria e non è monotono (README del progetto, §7.5, esempio 1,00 € contro 0,75 €): è un caso concreto di regolazione «endogena» al gioco, che questa rassegna dichiara non esaminato in generale. Questa lettura è mia; la rassegna non cita il caso italiano.
- **Nessuna evidenza nuova.** La rassegna non ripartisce un incentivo regolato e non confronta regole su dati: ciò che afferma sul RB (p. 13) e sul welfare (Eq. 20) è argomento analitico, senza test.
- **La tripartizione dell'efficienza (p. 11)** — tecnica, allocativa, economica individuale — è utile per etichettare gli indicatori della tesi; con un incentivo ex post a energia fisica fissata la prima (SCR, SSR) non dipende dalla regola (README §7.2, `contendibleShare`), la seconda coincide con `v(N)` ed è identica per tutte le regole, e solo la terza discrimina `[INFERENZA]`.
- **Citazioni incrociate nel corpus:** `gasca2025` ([85]), `fina2024` ([97]), `gianaroli2024` ([106]) e `gjorgievski2023` ([142]: «regulated charges in Europe may reduce households' savings from about 62.3% to 18.6% of the monthly electricity bill», p. 18). Non sono nel corpus e sono citati nel testo: Couraud et al. 2025 ([113], arXiv:2508.16819), usato per «a detailed pricing model to compare the fairness of various energy distribution algorithms» (p. 19); Irusta e Morales ([130], arXiv:2501.09713); Gjorgievski et al. 2022 ([93], Virtual net-billing); Li, Hakvoort, Lukszo 2021 ([80]); Fina 2023 ([110]).
