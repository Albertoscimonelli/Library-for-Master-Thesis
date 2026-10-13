# cavalcante2025 — Strategies for Fair Distribution of Collective Benefits in Renewable Energy Communities

- **File sorgente:** `Paper/Strategies for Fair Distribution of Collective Benefits in Renewable Energy Communities.pdf` (6 pagine, testo estraibile ma con equazioni illeggibili: lette sulle immagini)
- **Tipo:** articolo di conferenza (IEEE EEM 2025, 21st International Conference on the European Energy Market)
- **Lettura:** integrale (pp. 1–6); Eq. (1)–(17), Tab. I e Fig. 1–3 lette sulle immagini delle pagine 1–5; bibliografia (p. 6) letta come elenco. Verifiche aritmetiche mie.
- **Convenzioni:** pagine = indici di pagina del PDF (p. 1 = prima pagina). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Le virgolette riportano il testo degli autori.

## 1. Riferimento bibliografico
Cavalcante, L.; Lucas, A.; Villar, J.; Doménech Martínez, S. (2025). *Strategies for Fair Distribution of Collective Benefits in Renewable Energy Communities.* In: **2025 21st International Conference on the European Energy Market (EEM)**. DOI 10.1109/EEM64765.2025.11050342. INESC TEC, Porto. Finanziamento: PNRR/Recovery and Resilience Plan (Componente 5), NextGenerationEU, progetto ATE, rif. 56 (p. 6).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** valutare "three approaches for benefit-sharing based on the Shapley value, direct marginal contributions, and system marginal cost", confrontandoli "in terms of practicality, fairness, and impact on financial returns"; inoltre "proves that settling local transactions using system marginal costs ensures that all REC participants incur equal or lower costs compared to operating independently".
- **Gap dichiarati (p. 1):** "fair benefit allocation among members remains a challenge [3], [4]"; il Shapley "offers a cooperative game-theoretic benchmark, its complexity limits practical application [5]".
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Portogallo; riferimento alla Direttiva 2018/2001 (rif. [2]); prezzi di mercato reali per acquisto, vendita e tariffa di accesso alla rete per l'autoconsumo (λ^grid) di una giornata di fine settembre (caso di controllo); regole nazionali e modalità di ripartizione regolatorie `[NON SPECIFICATO]`.
- **Tipo di CER:** REC con un aggregatore a cui i membri vendono il surplus e un fornitore (retailer) da cui comprano; i membri possono anche acquistare energia da altri membri pagando la tariffa di accesso per autoconsumo (p. 1).
- **Membri:** (a) caso di controllo con 5 profili sintetici: max_ben (alto consumo e generazione), control (consumo e generazione simili: contributo neutro), unfav (solo consumo notturno senza generazione), reg1 (famiglia con figli, consumo pomeridiano e serale), reg2 (professionista single con attività diurna) (p. 3); (b) caso reale: Caxias Living Lab (Lisbona), 9 membri, tutti con PV e (tranne uno) con batterie simili: 6 residenziali (membri 0–5; il membro 1 senza batteria), un centro comunitario (6), una scuola (7), un mercato municipale (8) (pp. 3–4). Finestra reale: seconda settimana di luglio (10–16), ottobre (9–15) e dicembre (11–17) 2023 (p. 4).

## 4. Metodo
- **Modello (Sez. II-A, pp. 1–2, Eq. 1–3):** minimizzazione del costo operativo totale della REC (versione "normalized and simplified ... without batteries"): Σ_t Σ_n (E^SUP λ^buy − E^SUR λ^sell + E^PUR λ^grid), con bilanci Σ_n E^SALE − Σ_n E^PUR = 0 (duale λ^BAL = System Marginal Cost, SMC) e bilancio al contatore per ogni membro (duale λ^nBAL). "As this is an overall cost-minimization problem, settlement of each member's local sales and purchases within the REC do not appear in (1)" (p. 1).
- **Valore di coalizione (Eq. 5):** v*(S) = Σ_{j∈S} c({j}) − c(S), cioè il risparmio di costo della cooperazione rispetto ai comportamenti individuali.
- **Indicatori (Sez. II-B, p. 2):** (1) SV-IV: Shapley sul valore incrementale v* (Eq. 6); (2) DMC-IV: contributo marginale diretto DMC_i = v*(N) − v*(N\{i}) (Eq. 7), "computationally efficient" ma "does not account for all interactions between members"; (3) SMC: prezzo ombra λ^BAL come prezzo di regolazione degli scambi interni; i risparmi sono il confronto fra il costo con regolazione a SMC e il costo isolato (p. 2).
- **Dimostrazione (pp. 2–3, Eq. 8–17):** dal problema duale si ha λ^sell ≤ λ^nBAL ≤ λ^buy (Eq. 13); per un contatore che acquista localmente λ^sell ≤ λ^BAL + λ^grid ≤ λ^buy (Eq. 16), per uno che vende localmente λ^sell ≤ λ^BAL ≤ λ^buy (Eq. 17): chi compra in REC paga non più che dal retailer e chi vende riceve non meno che dall'aggregatore. "This proof can be generalized for more complex versions of the model (e.g., adding batteries or generators with positive variable cost), but that generalization remains for future works" (p. 3).
- **Software:** Python con PuLP e solver CPLEX (p. 3). Tempi di calcolo `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati
- **Shapley Value for Incremental Value (SV-IV):** media dei contributi marginali su tutte le coalizioni; per gli autori "robust methodology for fairly distributing costs or benefits", ma "computationally intensive for larger communities and can be difficult to explain and interpret" (p. 2).
- **Direct Marginal Contribution for Incremental Value (DMC-IV):** v*(N) − v*(N\{i}), "members with higher DMC-IV values are assigned a larger share of the savings" (p. 2); nessuna normalizzazione a un monte totale è descritta `[NON SPECIFICATO]`.
- **System Marginal Cost (SMC):** regolazione degli scambi interni al prezzo ombra del bilancio energetico; è un meccanismo di prezzo, non un'allocazione cooperativa (Eq. 14–17).
- Non analizzati: regole semplici (uguale, proporzionale), Nucleolo, Nash bargaining.

## 6. Metriche
- **Economiche:** contributo (€) di ciascun membro per SV-IV e DMC-IV; risparmio (€) per membro con SMC; tutti i valori "expressed in euros" (p. 4).
- **Equità/consistenza:** confronto qualitativo delle graduatorie fra indicatori; nessuna correlazione di rango, indice di Gini/Jain o misura di stabilità calcolati `[INFERENZA]`. "Fairness, computational efficiency, and their ability to engage REC members" sono dichiarati a p. 1 come criteri di valutazione ma efficienza computazionale ed engagement non compaiono fra i risultati.
- **Sociali / ambientali:** nessuna.

## 7. Risultati principali (numeri dal paper)
- **Caso di controllo (Tab. I, p. 4):** SV-IV: max_ben 0,0528; control 0,0000; unfav 0,0000; reg1 0,0294; reg2 0,0164. DMC-IV: 0,0986; 0,0000; 0,0000; 0,0519; 0,0260. SMC: 0,11; 0,02; 0,00; 0,04; 0,02. Gli autori: max_ben ha il contributo più alto con tutti i metodi; control e unfav hanno contributi trascurabili, ma control "still achieves slight savings under the SMC approach, likely due to favorable transactional conditions" (p. 4).
- **Caso reale, SV-IV (Fig. 1, p. 4):** a luglio il membro 6 (centro comunitario) domina, seguito da 0, 5, 8; a ottobre il membro 6 resta più alto con trend decrescente; a dicembre i contributi sono uniformi con un picco in un giorno per i membri 8 e 6 (lettura grafica: valori di ordine 0,05–4 € al giorno).
- **Caso reale, DMC-IV (Fig. 2, p. 4–5):** graduatorie "closely align" con SV-IV ma valori "consistently higher" e più variabili (lettura: fino a ≈ 6 €).
- **Caso reale, SMC (Fig. 3, p. 5):** i risparmi variano molto fra i membri, maggiori a luglio e ottobre che a dicembre; a luglio i migliori sono 0, 5, 6, 8 (coerenti con SV-IV); a ottobre il membro 6 (e 8); a dicembre i membri 3 e 8 "achieve the highest savings, despite Member 6 maintaining a notable SV-IV contribution. This discrepancy may stem from lower solar availability and shifts in energy usage patterns" (p. 5). Valori medi settimanali dalla Fig. 3: SV-IV medio fino a ≈ 2 €, risparmio medio fino a ≈ 2,2 € (membro 6, ottobre) `[INFERENZA, lettura grafica]`.
- **Conclusioni (p. 5):** "strong consistency between all three methods, as they generally produce similar member rankings"; DMC-IV "aligns closely with SV-IV but is more transparent and computationally efficient, making it preferable for large RECs"; SMC "also reflects cooperative contributions, but its applicability extends beyond fairness considerations, as it directly influences financial impact"; "Seasonal variations significantly impact member benefits, reinforcing the need for temporal granularity in benefit allocation".

## 8. Limitazioni dichiarate dagli autori
- p. 3: la dimostrazione di non-perdita con SMC vale per il modello senza batterie e senza generatori a costo variabile positivo; la generalizzazione è rimandata.
- p. 2: DMC-IV non considera tutte le interazioni (meno completo di SV-IV); SV-IV costoso e difficile da spiegare.
- p. 4: la finestra reale è la seconda settimana di tre mesi (luglio, ottobre, dicembre 2023), scelta per evitare periodi festivi o atipici.
- Nessuna sezione di limitazioni.

## 9. Future work dichiarati dagli autori
Elenco completo (verifica B.2):
1. p. 5: "Future work should explore scalability to larger RECs, predictive models for evaluating new members, and the role of community-scale storage in benefit allocation."
2. p. 3: generalizzazione della dimostrazione (batterie, generatori con costo variabile positivo) "remains for future works".

Classificazione `[INFERENZA — test B.1]`: 1 è generale e non autoreferenziale (scalabilità a REC più grandi, valutazione di nuovi membri, ruolo dello stoccaggio comunitario nell'allocazione); la 2 è autoreferenziale (estensione della propria dimostrazione).

## 10. Note del lettore (inferenze mie)
- **Incoerenza dei totali in Tab. I (verifica mia).** Σ SV-IV = 0,0528 + 0,0294 + 0,0164 = 0,0986 = v*(N) (efficienza di Shapley, e coincide con DMC-IV di max_ben: v*(N\{max_ben}) = 0, cioè tutto il valore dipende da un solo membro). Con regolazione a SMC i trasferimenti interni si annullano (Eq. 2), quindi la somma dei risparmi dei membri dovrebbe coincidere con v*(N) = 0,0986; la riga SMC somma invece 0,11 + 0,02 + 0,00 + 0,04 + 0,02 = 0,19 (anche con arrotondamenti di ±0,005 per cella il totale sarebbe ≤ 0,215). Il testo non spiega la differenza. `[INFERENZA]`
- **DMC-IV non è un'allocazione.** Σ DMC-IV = 0,0986 + 0,0519 + 0,0260 = 0,1765 ≠ v*(N): non ripartisce un monte totale; la descrizione "assigned a larger share of the savings" richiede una normalizzazione non indicata. `[INFERENZA]`
- **Contributi non negativi per costruzione.** Poiché ogni membro può sempre operare come isolato e la funzione v* è monotona, i contributi marginali non sono mai negativi (gli autori lo riconoscono per "unfav", p. 3); gli indicatori non possono rilevare esternalità negative. `[INFERENZA]`
- **Proof di non-perdita ristretta.** I membri reali hanno batterie (8 su 9), mentre le Eq. (1)–(17) sono "without batteries"; il risultato "all participants incur equal or lower costs" dell'abstract vale quindi per il modello semplificato (p. 3), non per il caso reale. La dimostrazione (Eq. 13–17) è una proprietà standard del prezzo duale di un mercato con prezzi esogeni retail/aggregatore. `[INFERENZA]`
- **Prove di "scalabilità ed engagement" assenti.** L'introduzione annuncia valutazioni di efficienza computazionale e "ability to engage REC members" e un framework "designed for scalability" (p. 1), ma nessun tempo di calcolo o misura di engagement è riportato e la scalabilità è rimandata a lavoro futuro (p. 5); con 9 membri l'enumerazione di Shapley è banale (2^9 coalizioni). `[INFERENZA]`
- **Conclusione di consistenza non quantificata.** "Strong consistency" e "strong correlation" fra graduatorie sono giudizi a vista; a dicembre SMC e SV-IV indicano membri diversi (3 e 8 contro 6); nessuna correlazione di rango è calcolata. `[INFERENZA]`
- **Importi molto piccoli.** I valori sono di ordine decimi–pochi euro per membro al giorno (Tab. I: 0,02–0,11 € nel caso di controllo); la rilevanza distributiva è limitata e dipende da prezzi e giornata scelta. `[INFERENZA]`
- **Relazione col mio tema:** utile per (i) il confronto fra Shapley, contributo marginale diretto e regolazione a prezzo marginale con proprietà di razionalità individuale dimostrata (nel caso senza batterie); (ii) il legame con `norbu2021a/b` (contributo marginale) e `silva2023` (meccanismi di prezzo); (iii) il tema della granularità temporale (allocazione giornaliera, variazione stagionale). Limiti: pochi membri, settimane campione, nessun indice. Il contesto portoghese è un caso di studio (B.4).
- **Collegamenti nel corpus:** `kulmala2021` ([3]), `volpato2024b` ([4]), `cremers2023` ([5]), `norbu2021a` ([8]), `norbu2021b` ([9]), `silva2023` ([10]); [12] e [13] (Saraiva et al.; Rocha et al., Energies 2023) non sono fra i paper del corpus.
