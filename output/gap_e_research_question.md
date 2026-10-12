# Fase 3 — Gap, verifica online e research question candidate

**Stato:** bozza per il **CHECKPOINT**. Nessuna scelta è stata presa. Non ho scritto né l'articolo né il piano del modello Matlab (Fase 4): aspetto la tua decisione (§7).
**Data della verifica online:** 12/10/2026.
**Lingua:** italiano; termini tecnici e titoli dei paper in inglese (B.6).
**File collegati:** `output/schede/` (56 schede), `output/sintesi.md` (Fase 2), `output/gap_registro_fw.md` (registro dei future work, 56 righe), `output/supporto_fase3/` (due controlli numerici giocattolo in Python, vedi Appendice B).

---

## 0. In sintesi

1. **Base di future work.** Dei 56 documenti, 7 hanno future work di tipo *generale* (test B.1): `dynge2025`, `gasca2025`, `gonzalezasenjo2025` (#3 e #4), `gonzalezasenjo2026`, `volpato2024b`, `cremers2023` (#4), `cavalcante2025`. 34 sono autoreferenziali, 9 non hanno future work utilizzabile (registro completo in `gap_registro_fw.md`).
2. **Gap.** Ho individuato otto gap candidati (G1–G8, §3). Tre sono utilizzabili come base di una research question, con forza diversa: **G1** (nozioni e indicatori di fairness non confrontabili fra le regole: ancore forti ma tema già occupato), **G2** (forza incentivante della regola, ciò che dell'«engagement» resta calcolabile da un modello: ancore adiacenti, tema attivo), **G4** (quota ai produttori e composizione: ancore deboli, utile come asse di scenario o sotto-domanda). G3 (stabilità delle regole semplici) è più un KPI che un gap; G5–G8 sono già occupati o non reggono (§3.5).
3. **Verifica online.** Ho potuto usare solo `WebSearch`: arXiv e tutti gli altri host accademici provati sono bloccati dalla policy di rete dell'ambiente (§1.3). Di ogni lavoro nuovo ho quindi solo il riassunto del motore di ricerca, non il testo. Il quadro 2025–2026 fuori dal corpus è **denso**: nessuno dei tre gap è «vuoto». Per ciascuno resta uno spazio delimitabile, descritto in §3.
4. **Tre research question candidate (§4):** RQ-1 (dipendenza del ranking delle regole dalla nozione di fairness), RQ-2 (trade-off fra forza incentivante ed equità distributiva), RQ-3 (quota ai produttori e composizione). **Raccomando RQ-2**, con RQ-1 come base di confronto e la composizione come asse di scenario (§5).
5. **Cose da dire senza attenuazioni (§6):** le ancore «facili» sul nucleolo e sul least core non reggono più; l'«engagement» non è misurabile da un modello e va dichiarato; con dispacciamento fisso il KPI ambientale è identico per tutte le regole; il protocollo Scopus del Cap. 2 va verificato/aggiornato sul 2025–2026.
6. **Mi serve la tua scelta** (§7). Dopo non faccio nulla finché non rispondi.

---

## 1. Metodo, convenzioni e limiti

### 1.1 Etichette
- `[PAPER]` = ciò che dicono gli autori (sezione/pagina come nelle schede).
- `[INFERENZA]` = mia deduzione o classificazione.
- `[WEB]` = trovato con la ricerca online; riportato **come lo riassume il motore di ricerca**, senza aver letto il testo.
- `[TOY]` = calcolo mio su un esempio giocattolo (Appendice B): illustra una struttura, **non è un risultato**.

### 1.2 Verifica verbatim (B.2)
Tutte le 39 citazioni letterali (tra virgolette «“…”») di questo documento sono state ricontrollate parola per parola sul testo estratto dei PDF, con uno script che le cerca nel testo del paper citato; in più ho letto il paragrafo che le contiene. Tutte presenti (alcune solo dopo aver tolto artefatti di a-capo dell'estrazione come «highenergy» o «pro sumers»). Le citazioni tra virgolette «…» a caporale sono termini o parafrasi, non brani verbatim. Per tre paper con layout a due colonne ho guardato l'immagine della pagina per stabilire in quale sezione cadono le frasi:
- `cremers2023`: il paragrafo di future work è in **Sez. 6 «Conclusions & further work»**, p. 13 (colonna destra; l'ordine del testo estratto lo faceva sembrare in Sez. 5.3), come già riportato nella scheda.
- `bilardo2025`: la frase sul *need-based allocation* è a fine **Sez. 5.4**, p. 12, prima delle Conclusioni, e non nella Sez. 6.1 «Future perspectives» sotto cui la scheda elenca gli altri punti.
- `minuto2022`: le due frasi sulla composizione sono a chiusura di **Sez. 4.3**, p. 15, subito prima della Sez. 5.

### 1.3 Verifica online: cosa ho potuto e non potuto fare
- Gli accessi diretti falliscono perché il proxy di rete dell'ambiente rifiuta la connessione (`CONNECT` fallito; per `arxiv.org` il proxy registra `403`, policy di rete) per `arxiv.org`, `doaj.org`, `hal.science`, `hal.archives-ouvertes.fr`, `api.crossref.org`, `api.openalex.org`, `api.semanticscholar.org`, `iris.polito.it`, `www.boa.unimib.it`, `researchportal.hw.ac.uk`, `www.mdpi.com`, `www.sciencedirect.com`, `ieeexplore.ieee.org`. Non ho aggirato la policy.
- Restano utilizzabili solo i riassunti di `WebSearch` (30 ricerche, Appendice A). Per i lavori nuovi **non ho letto né abstract né testo originali**: ho il riassunto del motore. Dove scrivo «non trovato» intendo «non emerso in queste ricerche», non «non esiste» (B.3).
- Non ho potuto interrogare Scopus o Web of Science. Verifica se il protocollo del Cap. 2 (628 → 163 → 55 paper) copre il 2025–2026: molti dei lavori trovati qui sono del 2026 e non sono nel corpus di 56 documenti.
- Se vuoi la lettura integrale dei lavori della Appendice C, serve sbloccare i domini nelle impostazioni di rete dell'ambiente (Network access) oppure caricare i PDF in `Paper/`.

### 1.4 File mancante
`Paper/ISTRUZIONI_E_CONTESTO.md` rimanda a `HANDOFF_SESSIONE_GAP.md` per «stato di avanzamento e citazioni già verificate». **Il file non esiste nel repository.** Non ho quindi potuto riusare le citazioni verificate nelle sessioni precedenti: ho rifatto da capo la verifica B.2 su tutte le ancore qui usate.

### 1.5 Regole applicate
B.1 (autoreferenziale vs generale) su ogni ancora; B.2 (verbatim + lista completa dei future work dello stesso paper, dichiarando i punti non usati); B.3 (formulazioni positive, controesempi segnalati subito, §6 punto 8); B.4 (il contesto italiano è caso studio, non gap); B.5 (ogni termine delle RQ deve essere calcolabile); B.6 (italiano per le bozze).

---

## 2. Come ho costruito l'elenco dei gap

1. **Dichiarati:** sezione 9 di tutte le 56 schede (elenco completo dei future work, trascritto dal PDF). Classificazione B.1 in `gap_registro_fw.md`.
2. **Impliciti:** limitazioni dichiarate (sezione 8 delle schede) e convergenze/contraddizioni della sintesi (`C1–C11`, `K1–K11`, `output/sintesi.md` §5–§7). Un gap implicito da solo **non** basta (Parte A §2): lo uso solo come supporto di un'ancora esplicita.
3. **Per ogni gap:** descrizione; evidenza con sezione/pagina e citazione verificata; classificazione B.1; rilevanza e originalità; fattibilità con un modello Matlab e dati disponibili; rischio di copertura (ricerca online).
4. **Mappa verso la tesi:** G1 ↔ §2.3 (fairness metrics e quadri assiomatici); G2 ↔ §2.4 (impatti ambientali, comportamentali e sociali); G4 ↔ §2.5 (ruolo della composizione). Il contesto normativo (quota eccedentaria, fattore F, categorie utente) entra come specifica nel Cap. 3 e come equazione nel Cap. 4, non in §2.6 (B.4).

---

## 3. Gap candidati

### 3.1 G1 — Nozioni di fairness e indicatori non confrontabili fra le regole

**Descrizione (formulazione positiva).** Nel corpus le regole di ripartizione sono valutate con indicatori che misurano obiettivi diversi: uguaglianza dei compensi assoluti (Gini, Equality Index, MinMax, QoE), proporzionalità al contributo (Fairness Index di Casalicchio, distanza dallo Shapley), stabilità (appartenenza al core, θ). Due paper che sono già confronti multi-metodo o multi-indicatore (`volpato2024b`, `dynge2025`) chiedono parametri o criteri quantitativi più concreti per confrontare le nozioni di fairness e valutare più indicatori; `gasca2025` chiede ulteriori confronti nello stesso framework, in particolare con metriche non economiche; `cremers2023` chiede di confrontare altri concetti di fairness con lo Shapley.

**Evidenza esplicita `[PAPER]`**

| Paper | Dove | Citazione (verificata sul PDF) | Tipo B.1 |
|---|---|---|---|
| `volpato2024b` | Sez. 4, p. 22 | “Another interesting direction of future work will be to identify parameters that can quantitatively compare the different benefit distributions based on the "individual", "collective" and "proportional" fairness.” | Generale: il paper confronta già SW, NB, Shapley e nucleolo |
| `dynge2025` | Sez. 8, p. 12 | “Furthermore, additional investigation is needed to refine fairness indicators, ensuring their effectiveness across diverse market models.” e “More concrete evaluation criteria could also be derived to perform a more generalisable and comprehensive evaluation of multiple fairness indicators.” | Generale (4 indicatori × 9 casi), ma contesto LEM P2P, non CER |
| `gasca2025` | Sez. 3.5, p. 12 | “Nevertheless, additional types of comparisons could also be explored within the same framework, for instance, contrasting market-based and KoR within centralized frameworks, particularly for evaluating metrics beyond economic metrics.” | Generale |
| `cremers2023` | Sez. 6, p. 13 | “Finally, while this paper focuses on the key topic of Shapley value computation, there are many other fairness concepts that could be explored in energy applications, and it would be relevant to compare their outcome to Shapley values.” | Generale: il paper confronta approssimazioni *dello stesso* concetto, la richiesta esce dal suo perimetro |

Nota B.2/B.3: `volpato2023` (p. 2) parafrasa `cremers2023` in modo più forte («the literature lacks of more in-depth discussions about the fairness»): nell'originale non c'è. Va citata la formulazione originale.

**Completezza B.2 (lista intera).** `volpato2024b` ha due punti, il primo (più membri e storage) è autoreferenziale e non contraddice. `dynge2025` include anche il dialogo interdisciplinare sull'accettabilità sociale, le barriere (privacy) e nuovi indicatori specifici del mercato locale: nessuno contraddice. `gasca2025` ha sette punti: uso solo #1, #2, #6, #7 (§3.2) e dichiaro che #3–#5 riguardano il lato mercato. `cremers2023` ha quattro punti: #1–#3 (rete, costi, blockchain) autoreferenziali e non usati.

**Evidenza implicita `[INFERENZA]` (sintesi).** K5: «equity», «equality» e «fairness» indicano obiettivi opposti a seconda del paper (`gasca2025`: equity = allocazione uguale «regardless of their contribution»; `dynge2025`: proporzionalità al contributo per i prosumer e uguaglianza per i consumatori; `fina2024`: stessa variazione percentuale). C8: gli indici disponibili misurano uguaglianza, non proporzionalità al contributo. K1: lo Shapley è «il più equo» oppure non è né stabile né equo, a seconda della nozione. `gonzalezasenjo2025` (p. 4) nota che «fairness», «stability» ed «equity» sono usati con significati diversi.

**Rilevanza e originalità.** Rilevanza alta (cuore del Cap. 2.3). Originalità **medio-bassa**: il confronto fra regole è un tema occupato (sotto).

**Fattibilità (Matlab, dati).** Alta. Regole in forma chiusa o con LP/approssimazioni; Shapley esatto per N ≲ 16 (2^N coalizioni, calcolo a blocchi su 8760 ore), Monte Carlo per N maggiori (`cremers2023`: errore sotto l'1% per N > 100); least core/nucleolo con `linprog` per N ≲ 14. Dati: profili di carico del corpus (Thames Valley Vision in `norbu2021a/b` e `cremers2023`; LoadProfileGenerator in `alonsopedrero2024` e `casalicchio2022a/b`; dati e tariffe ARERA citati in 16 schede) e produzione da PVGIS (citato in 16 schede).

**Rischio di copertura `[WEB]`.**
- Couraud et al., *Fairness of Energy Distribution Mechanisms in Collective Self-Consumption Schemes* (arXiv:2508.16819, 2025): simulazioni su 250 comunità residenziali generate casualmente (20 famiglie) per confrontare meccanismi di distribuzione, con un nuovo indicatore di fairness meritocratica; secondo il riassunto, «glass-filling with prioritization» è il migliore su misure egalitarie e min-max, mentre «double auction» e «pro rata» sono i migliori sulla meritocrazia. Dal riassunto i meccanismi confrontati riguardano la distribuzione dell'energia (glass-filling, double auction, pro rata); non risultano regole game-theoretic `[INFERENZA dal riassunto]`.
- Limmer, *Empirical Study of Stability and Fairness of Schemes for Benefit Distribution in Local Energy Communities* (Energies 16(4):1756, 2023): Shapley stabile in circa il 90% dei casi, nucleolo equo in circa il 75%, dati reali australiani.
- `gonzalezasenjo2025/2026` (nel corpus): otto metodi × sette proprietà in un modello a singolo slot; poi un framework data-driven a cinque metodi.
- Bigi, Fioriti, Frangioni, Passacantando, Poli (arXiv:2511.05291, 2025) e Fioriti et al., *Fair Least Core* (IEEE Trans. Energy Markets, Policy and Regulation, 2025): il least core è stato sviluppato. Perciò la richiesta di `cremers2023` su least-core e nucleolo («explored much less in energy applications») **non regge più come gap** (§6, punto 1).
- Rassegne: Wangen & Clastres (IAEE Energy Forum, 2024) e una rassegna RSER 2026 sui meccanismi di coordinamento e le tariffe interne (valuta incentive compatibility e fairness).

**Esito.** Gap reale ma già occupato. Un contributo distintivo non può essere «confrontare le regole». Ciò che nei riassunti **non è emerso** è un confronto che (a) metta nello stesso banco di prova regole semplici di tipo italiano (percentuali fisse per categoria, progressiva/Layered, pro-rata orario) e regole game-theoretic, e (b) verifichi esplicitamente se il ranking dipende dalla nozione di fairness. Uso G1 come **base di confronto** (backbone), non come contributo distintivo.

---

### 3.2 G2 — Forza incentivante delle regole (l'«engagement» operazionalizzato, B.5)

**Descrizione (formulazione positiva).** Nelle simulazioni del corpus i profili di carico sono fissi e la ripartizione è applicata a posteriori (C2, K8): l'effetto della regola sul comportamento dei membri non entra nei risultati. L'unico test di sensibilità al comportamento nei 56 paper riguarda **una sola regola** (`zatti2021`, Shapley, Tab. 9–10; sintesi C9). Due confronti multi-metodo del 2025–2026 dichiarano di astrarre dalla flessibilità delle famiglie e dai fattori comportamentali e indicano questi aspetti come sviluppo. Tre paper sul caso italiano propongono regole che «premiano» il comportamento virtuoso (`bilardo2025`, `giudice2026`, `gianaroli2024`); due di essi (`giudice2026`, `bilardo2025`) indicano il coinvolgimento come sviluppo futuro.

**Evidenza esplicita `[PAPER]`**

| Paper | Dove | Citazione (verificata sul PDF) | Tipo B.1 |
|---|---|---|---|
| `gonzalezasenjo2025` #3 | Sez. 4, p. 13 | “Extending the axiomatic framework to more complex EC settings. Future work could consider settings with dynamic pricing, storage, network constraints, household flexibility, or multi-period coupling. Extending the framework to such contexts would help evaluate the robustness of CAM properties under more realistic conditions.” | Generale (8 CAM × 7 proprietà) |
| `gonzalezasenjo2025` #4 | Sez. 4, p. 13 | “Applying the framework to real consumption-generation patterns from operational energy communities would help assess how theoretical properties translate into practical outcomes and user perceptions.” | Generale; uso solo la parte «dati realistici», non «user perceptions» (non calcolabile, B.5) |
| `gonzalezasenjo2026` | Sez. 5, p. 35 | “the analysis focuses on ex post allocation methods and operational costs, abstracting from investment decisions, network constraints, and subjective behavioural factors” […] “Addressing these aspects represents a natural direction for future research.” | Generale (limite dichiarato di un confronto multi-metodo, codice pubblico) |
| `basilico2025` | Sez. 6.6, p. 16 | “further empirical research into the social dimensions of RECs (e.g., citizen engagement, community participation)” e (Sez. 6.3, p. 15) “understanding the social motivations that drive prosumers and consumers to engage with RECs will be essential for fostering participation and long-term success” | Generale ma vago, e di natura **empirico-sociale**: non è risolvibile con un modello (B.5) |
| `gasca2025` | Sez. 3.5, p. 12 | “However, for local energy markets, it is essential to consider the active involvement of users in the market—engaging with their preferences and trading with others.” | Generale ma lato mercato |
| `giudice2026` | Sez. 7, p. 18 | “Finally, the long-term impacts of the incentive mechanism on both individual consumption patterns and collective engagement dynamics will be systematically evaluated.” | Autoreferenziale (supporto) |
| `bilardo2025` | Sez. 6.1, p. 13 | “In addition, the integration of such an incentive mechanism with energy forecasting tools could also support community engagement, optimizing its energy and economic benefits.” | Autoreferenziale (supporto) |
| `alonsopedrero2024` | Sez. 7.5, p. 13 (limitazione dichiarata, non future work) | “the distribution of costs post-operations may limit end users' ability to adapt to more favourable economic outcomes on time” e “its mathematical complexity can hinder understandability, potentially affecting residents' trust in the method” | Limitazione autoreferenziale al Nested Shapley; il punto sull'allocazione ex post è però generale |

**Dichiarazione B.2.** Di `gonzalezasenjo2025` uso solo #3 e #4. Esistono anche #1 («Formal characterization of the nucleolus») e #2 («Design of computationally efficient algorithms for the nucleolus»): riguardano il nucleolo e **non sostengono** un inquadramento che non lo metta al centro. Di `basilico2025` esistono sei punti (altre fonti rinnovabili, PDM ibrido, redditi): nessuno contraddice.

**Cautela sull'ancora principale `[INFERENZA]`.** `gonzalezasenjo2025` #3 chiede di estendere **il quadro assiomatico** (proprietà) a contesti più complessi; il loro modello è a **singolo slot** (Sez. 2.1, p. 5: «intentionally minimal», consumo e generazione deterministici «within each time slot»). Per costruzione il sincronismo con il surplus non può comparire in un modello a singolo slot: «multi-period coupling» e «household flexibility» sono proprio gli assi in cui entra. La mia RQ risponde a #3 solo su quest'asse e con una misura diversa (forza incentivante, non proprietà assiomatiche): **non rimpiazza** #3 né ne copre gli altri assi (dynamic pricing, storage, rete).

**Evidenza implicita `[PAPER]`/`[INFERENZA]`.**
- `zatti2021` (Sez. 4.2, p. 12; Eq. 9; Tab. 9–10): modello semplice di spostamento del carico applicato a una sola regola. Conclusioni (p. 15): “the use of Shapley value-based income distribution is effective in pushing final users to shift their electricity consumption in periods of high PV generation”; a p. 12 osservano la “competition generated by the distribution rule”. È la metodologia di partenza più vicina nel corpus.
- `minuto2022` (p. 10) osserva che una delle sue regole “does not promote a virtuous energy consumption”.
- `gonzalezasenjo2026` (Sez. 3.1.1, pp. 13–14, scheda §4): scenari sintetici con due profili di domanda a **pari consumo giornaliero ma sfasati** (allineato e anti-allineato alla produzione PV) in cinque mix: un disegno vicino a «stessa energia annua, diverso sincronismo». Valutano però la ripartizione fra Net Consumer e Net Producer, non una misura di forza incentivante.
- Sintesi C9: l'engagement è invocato ovunque e non è mai misurato; K8: la regola influenza il design solo in quattro paper.

**Che cosa si può e non si può calcolare (B.5).**
- *Non calcolabile da un modello:* motivazione, soddisfazione, fiducia e comprensibilità della regola (`alonsopedrero2024`), percezione di equità (`basilico2025` #3/#5; `gonzalezasenjo2025` #4 «user perceptions»). La forza incentivante è una **condizione necessaria, non sufficiente**, dell'engagement: va detto nella tesi.
- *Calcolabile senza modello comportamentale (misure rule-intrinseche, definizioni mie `[INFERENZA]`).* Sia `R_i^ρ` il compenso del membro `i` con la regola `ρ` e `B` il valore totale da ripartire.
  - **(a) Dispersione a parità di energia annua:** `D_ρ` = rapporto (o coefficiente di variazione) fra i compensi di membri con la stessa energia annua e diverso sincronismo con il surplus. Per regole basate su quantità annue vale 1 per costruzione.
  - **(b) Quota del guadagno marginale trattenuta:** `ι_i^ρ = [R_i^ρ(dopo lo spostamento) − R_i^ρ(prima)] / [B(dopo) − B(prima)]`, per un piccolo spostamento di carico del membro `i` da un'ora senza surplus a un'ora con surplus.
  - **(c) Sensibilità al consumo aggiuntivo nelle ore vincolate dalla produzione:** `λ_i^ρ = ΔR_i^ρ / Δc_i` quando `ΔB = 0`. Un valore positivo indica un incentivo a consumare di più per sottrarre quota agli altri.
- *Calcolabile con un'ipotesi di flessibilità (strato di risposta):* una quota `φ` del carico sposta in risposta a `ι_i`; si misurano energia condivisa, € e, solo se si hanno fattori di emissione orari, CO2. Il risultato dipende da `φ`: va presentato come analisi di scenario, non come risultato.

**Rilevanza e originalità.** Rilevanza alta per il tuo macro-tema (impatto della regola su benefici e coinvolgimento). Originalità **media**: il tema è attivo (sotto), ma una misura rule-intrinseca confrontata fra famiglie di regole non è emersa nei riassunti.

**Fattibilità.** Alta per (a)–(c) (perturbazioni di profili con regole in forma chiusa/LP; nessun dato comportamentale). Media per lo strato di risposta (ipotesi su `φ` e sulla risposta). Dati: come in G1. Per l'ambientale, nel corpus `ceglia2022` (p. 15) usa fattori di emissione orari e mostra che la media annua (316,8 gCO2/kWh) sovrastima le emissioni fino al 50,3% a mezzogiorno di un giorno di luglio, mentre `cutore2023` (p. 15) usa il valore medio nazionale ISPRA (276,3 gCO2/kWh); la fonte della serie oraria di `ceglia2022` non è riportata nella scheda `[da verificare]`.

**Rischio di copertura `[WEB]`.**
- **Rodrigues, Villar, Lucas, Sousa, *Loyalty and tier-based benefit allocation frameworks for renewable energy communities* (Utilities Policy 102, ott. 2026, art. 102277).** Secondo il riassunto: framework di ottimizzazione multi-stadio con punteggi di fedeltà (partecipazione di lungo periodo, flessibilità, coinvolgimento sociale e commerciale); quattro meccanismi (cascade stretto e ibrido con rete di sicurezza che agiscono sui coefficienti di allocazione dell'energia; due meccanismi a trasferimento diretto); simulazione a 50 membri; **«trade-off tra forza incentivante meritocratica ed equità sociale»**. È il lavoro più vicino per l'idea centrale di RQ-2: **la mia RQ non può dire di essere la prima a trattare il trade-off incentivo/equità** (§6, punto 8).
- Shooshtari, Pepiciello, Domínguez-García: *Grid-informed Sharing Coefficients in RECs* (arXiv:2509.12847, 2025) e *Sharing Coefficient-Based Price Signals for Demand Response in RECs* (arXiv:2607.09357, lug. 2026): coefficienti di ripartizione usati come segnali di prezzo per la risposta della domanda (quindi accoppiamento fra regola e comportamento), con focus sulla rete.
- Conte, Silvestro, Vinci, Di Fazio (arXiv:2301.06452): REC italiana con elettrodomestici smart e una politica di ripartizione dello sconto, con controllo predittivo.
- Rollo et al. (Energies 18(4):872, 2025); Bianchini, Casini, Gholami (Energies 18:4904, 2025); Stai et al. (IEEE Access, 2024; gioco non cooperativo su allocazione proporzionale vs uguale); uno studio basato su equilibrio di Nash segnala che l'esito egalitario è «less incentivizing» (fra i risultati compare arXiv:2010.05544; attribuzione non verificata); PMC10777070 (quota fissa uguale a ogni membro con la regola EQ; Shapley simile al contributo marginale).
- Un'altra ricerca mirata («does the allocation rule reward flexibility…») ha dato questo esito: **nessuna** misura formale di sensibilità del compenso allo spostamento di carico confrontata fra regole nei riassunti; PMC10777070 è il più vicino ma usa € e profili specifici.

**Esito.** Gap difendibile solo se delimitato: **misura rule-intrinseca e comparabile della forza incentivante fra famiglie di regole, con il suo rapporto con più nozioni di fairness**, non «primo studio su incentivi e allocazione».

---

### 3.3 G3 — Stabilità, razionalità individuale e uscita delle regole semplici

**Descrizione.** Nel corpus la razionalità individuale è «garantita per costruzione» per le regole nel core o nel least core e **non verificata** per la maggior parte delle regole semplici italiane (K6: `cecini_tesi`, `marrasso2025`, `basilico2025`, `trevisan2024`; nessun controfattuale «fuori dalla CER»).

**Evidenza esplicita `[PAPER]`**

| Paper | Dove | Citazione (verificata) | Tipo B.1 |
|---|---|---|---|
| `volpato2023` | Sez. 5, p. 10 | “A future research direction of this work could cover the analysis of the economic stability of the REC, strictly dependent on the costs/profits distributed by the implemented allocation mechanisms, to avoid the case of members willing to exit from the REC.” | Autoreferenziale ma pertinente |
| `gianaroli2024` | Sez. 4, p. 12 | “Furthermore, as members of a REC or CSC can voluntarily enter or exit the established legal entity, future studies will need to evaluate indicators of potential expansion or decline of community members with the same production plants.” | Misto |
| `cavalcante2025` | Sez. V, p. 5 | “Future work should explore scalability to larger RECs, predictive models for evaluating new members, and the role of community-scale storage in benefit allocation.” | Generale (punto 1); il punto 2 (p. 3) è autoreferenziale |
| `casalicchio2022a` | p. 9 (Sez. 2.5) | “In the future, when assessing the opportunity for new members to join the ECs, a truthful assessment could be extremely important. It would be even more useful if a personalized fee for community participation were applied.” | Autoreferenziale |

**Rilevanza e originalità.** Rilevanza media. Originalità **bassa-media**: la stabilità delle regole game-theoretic è ben coperta.

**Rischio di copertura `[WEB]`.** Limmer 2023 (stabilità empirica); Bigi et al. 2025 (proprietà del gioco con veto player, fino a 200 utenti sintetici: **controesempio parziale** a K2 della sintesi, che va letta come «nel corpus»); *Incentivising community self-consumption in energy markets: Stable coalition formation using cooperative game theory* (Applied Energy, 2025); arXiv:2311.18792 (giochi di condivisione bilanciati, core non vuoto); HAL-02520203 (core non vuoto, algoritmo distribuito). Per le **regole semplici** un'analisi di stabilità non è emersa nei riassunti.

**Esito.** Non è una RQ autonoma: lo uso come **KPI** (margine rispetto al core, eccesso massimo delle coalizioni bloccanti, quota di membri sotto l'opzione di uscita) dentro G1/G2/G4.

---

### 3.4 G4 — Quota ai produttori e composizione della comunità

**Descrizione.** La quota dell'incentivo attribuita ai produttori (proprietari degli impianti) non ha un valore condiviso nel corpus e i valori usati sono scelti dagli autori (K7, C10): 50% o 20% in `cecini_tesi`, α = 0,75 / β = 0,25 in `candela2022`, 54,2% al condominio proprietario in `zatti2021`, ecc. L'effetto della composizione sulla *ripartizione* (non sul valore totale) è poco studiato (C11).

**Evidenza esplicita `[PAPER]`**

| Paper | Dove | Citazione (verificata) | Tipo B.1 |
|---|---|---|---|
| `minuto2022` | Sez. 4.3, p. 15 | “Furthermore, another important research question we consider worthy of being addressed is: what is the best balance between owner and non-owner members within an energy community supplied by fluctuating RES?” e “Other important aspects that deserve further investigation concern how the different EC compositions (number of members in the UT groups) and/or a different EC self-sufficiency level impact the results presented here.” | Autoreferenziale (la domanda è però generale) |
| `marrasso2025` | Abstract, p. 1 | “the used algorithm should incorporate specific parameters that account for the different operating conditions, such as the presence of third-party producers, prosumers, and high-energy consumers, as well as solidarity-based objectives, such as addressing energy poverty” | Generale ma non operazionalizzato (necessità, non future work) |
| `gianaroli2024` | Sez. 4, p. 12 | “an energy community require the implementation of allocation mechanisms that consider the different types of users who contribute to energy sharing” | Misto |
| `cecini_tesi` | Sez. 5.2, p. 97 (stampa tesi) | “a valid future analysis could seek to identify an identifying value for the allocations just described” | Autoreferenziale |

**Evidenza implicita `[INFERENZA]`.** C4: con le regole basate sul contributo marginale il lato che limita lo scambio ottiene la quota maggiore (`fioriti2021`, `gonzalezasenjo2026`, `campagna2024`). K7: nessun valore condiviso della quota produttori. C10: parametri scelti dall'autore, non stimati da comportamenti osservati (nel corpus).
`[TOY]` (Appendice B): in un gioco con un produttore e sei consumatori la quota Shapley del produttore va da 0,73 (PV/carico = 0,2) a 0,50 (PV/carico ≥ 4): il «riferimento contributivo» per la quota produttori **dipende dalla scarsità relativa**, mentre le percentuali fisse no.

**B.1 onesta.** Le quattro ancore sono autoreferenziali o non operazionalizzate. Convergono su un tema, ma **da sole non reggono** un gap secondo la Parte A: G4 va usato come asse di scenario o sotto-domanda, non come ancora principale.

**Fattibilità.** Alta: la quota produttori è un parametro `π`; il riferimento si calcola con Shapley esatto e nucleolo/least core per N ≲ 14; la composizione è una griglia (rapporto PV/carico, numero di produttori, quota di non proprietari, quota di persone fisiche vs grandi consumatori).

**Rischio di copertura `[WEB]`.** Non è emerso un lavoro che derivi la quota produttori da un criterio contributivo. Il più vicino per struttura è Awerkin, Falbo, Vargiolu, *Optimal Investment and Fair Sharing Rules of the Incentives for REC* (arXiv:2311.12055, rev. mar. 2025; un'inserzione di Annals of Operations Research ago. 2026 con titolo simile, non confermata come stessa opera): compensazione per ogni MWh prodotto e consumato nella stessa ora, regola di ripartizione scelta dall'amministratore (leader-follower), decisioni di investimento. Collegato: progetto PRIN 2022 «Compensation Rules Among Members of Heterogeneous Energy Communities» (Brescia/Torino; modellazione + esperimenti e sondaggi; durata ottobre 2023–marzo 2026; pubblicazioni non ancora elencate nelle ricerche). Magni, Bricca, Familiari (JSDEWES, 2025): scenari sul D.M. 414/2024; secondo il riassunto, al crescere del prezzo di vendita il nuovo schema può favorire solo i membri investitori.

**Esito.** Gap plausibile e utile per la pratica italiana, ma debole in B.1: lo uso come **asse di scenario** di RQ-2 oppure come RQ-3.

---

### 3.5 G5–G8: gap scartati o assorbiti

Stessa struttura di G1–G4, in forma compatta.

#### G5 — Pesi sociali e povertà energetica
- **Descrizione.** Quattro paper integrano un criterio sociale nella regola (`campagna2024`, `marrasso2025`, `fina2024`, `basilico2025`) con indicatori diversi e non confrontabili (LIHC, ISEE, reddito dichiarato, costo unitario; sintesi §6.6); `cecini_tesi` lo lascia da parte per motivi di privacy.
- **Evidenza `[PAPER]`.** `bilardo2025` (Sez. 5.4, p. 12): “To further explore the concept mechanism of "fairness", possible extension of this work might try to incorporate need-based allocation method that are linked to users' socio-economic conditions.” `gianaroli2024` (Sez. 4, p. 12): “other studies could consider vulnerable users in energy poverty through the development of social indicators.” `cecini_tesi` (Sez. 6.4, p. 103, stampa tesi): “the issue of how to include support for vulnerable users and those in energy poverty has been partially sidelined”. `goncalves2024b` (Sez. 5, p. 6): “Future research must further analyze social aspects in EC, focusing not only on the monetary advantages of member participants but also on the interactions of households with different income levels.” `fina2024` (Sez. 6, p. 15): “However, it would be possible to introduce weighting factors to combine even contradictory or conflicting objectives when it comes to redistribution.” Tipo B.1: autoreferenziali o generali ma vaghe; B.5: «social aspects» e «interactions» non sono grandezze calcolabili senza definire un indicatore e i dati.
- **Rilevanza e originalità.** Rilevanza alta per il macro-tema sociale; originalità bassa-media.
- **Fattibilità.** Media-bassa: gli indicatori di povertà energetica richiedono dati (ISEE, reddito) che `marrasso2025` e `cecini_tesi` segnalano difficili da ottenere; una vulnerabilità sintetica con analisi di sensibilità è possibile ma resta un'ipotesi del modello.
- **Copertura `[WEB]`.** Il titolo di un lavoro 2026 («…differentiated pricing and incentive allocation», Appendice C) indica che il lato progettuale è già trattato (contenuto non letto).
- **Verdetto.** KPI (quota ai membri vulnerabili e alle persone fisiche) e scenario, non RQ.

#### G6 — Dimensione ambientale della ripartizione
- **Descrizione.** Gli indicatori ambientali sono assenti o non differenziano le regole.
- **Evidenza `[PAPER]`.** `casalicchio2022a` (p. 17): “It is possible to develop further the described method by focusing both on other technical details and by dedicating more space to environmental and emissions-related aspects.” `cutore2023` (p. 15): “This last remark demonstrates that environmental and social performances are at odds, and further analysis is required to determine how these two factors interact.” `gasca2025` #2 (§3.1). Tipo B.1: i primi due autoreferenziali; `gasca2025` generale.
- **Rilevanza e originalità.** Rilevanza media; originalità bassa.
- **Fattibilità.** Alta per energia condivisa e autoconsumo; per la CO2 servono fattori di emissione (dati in `ceglia2022` e `cutore2023`, vedi §3.2).
- **Copertura `[WEB]`.** Non ricercata separatamente: il gap è assorbito.
- **Verdetto.** `[INFERENZA]` Con dispacciamento fisso gli indicatori ambientali sono **identici per tutte le regole**: la ripartizione non cambia i flussi fisici. Può differenziarle solo l'accoppiamento comportamentale, che è G2.

#### G7 — Scalabilità e approssimazioni del calcolo
- **Descrizione.** Costo esponenziale dello Shapley e approssimazioni (C6, K2).
- **Evidenza `[PAPER]`.** `norbu2021b` (Sez. V, p. 21): “Finally, on the more theoretical side, development of other redistribution schemes that closely resemble or approximate the Shapley value solution concept, but are computationally tractable to compute, forms another exciting area of research.” `cavalcante2025` (Sez. V, p. 5, §3.3). `gasca2025` (Sez. 3.5, p. 12): “[…] crucial to identify simple and practical cost allocation methods, as testing a wide range of repartition keys (KoR) can be practically infinite. This includes using Shapley value approximations and other complex repartition keys.” Tipo B.1: `norbu2021b` autoreferenziale con un punto generale; `cavalcante2025` e `gasca2025` generali.
- **Rilevanza e originalità.** Rilevanza media; originalità bassa.
- **Fattibilità.** Alta (Monte Carlo, row generation).
- **Copertura.** Nel corpus: `alonsopedrero2024`, `cremers2023`, `ferrucci2025`. `[WEB]` Fair Least Core 2025 e Bigi et al. 2025 (10–200 utenti sintetici).
- **Verdetto.** Già sviluppato: non è un gap aperto. Le approssimazioni servono solo come strumento per N grandi.

#### G8 — Investimento e ripartizione accoppiati
- **Descrizione.** La ripartizione è trattata ex post, con l'investimento fuori dal modello; solo quattro paper accoppiano la regola al design (K8).
- **Evidenza `[PAPER]`.** `gasca2025` (Sez. 3.5, p. 12): “Furthermore, this work dealt with operational frameworks, future work may include investment decisions to consider within the fairness assessment.” `gonzalezasenjo2026` (Sez. 5, p. 35; §3.2). `berg2024` (Sez. III-C, p. 5): “The fairness evaluation here is a good starting point for considering the distribution of investment costs and revenues when introducing shared assets within a CSC scheme.” Tipo B.1: generale per i primi due; accenno per `berg2024`.
- **Rilevanza e originalità.** Rilevanza media-alta; originalità bassa (tema occupato).
- **Fattibilità.** Bassa-media: richiede ottimizzazione degli investimenti, fuori dal perimetro di un modello operativo di ripartizione.
- **Copertura.** Nel corpus: `fioriti2021`, `ferrucci2025`, `casalicchio2022a`. `[WEB]` Awerkin–Falbo–Vargiolu e Energies 18(8):1920 («Optimal Investment and Sharing Decisions in RECs with Multiple Investing Members»).
- **Verdetto.** Fuori perimetro.

---

## 4. Tre research question candidate

Convenzioni comuni: la ripartizione riguarda un incentivo calcolato sull'energia condivisa **oraria** `min(immissione, prelievo)`; il caso italiano (tariffa premio, quota eccedentaria, fattore F, categorie utente) entra come caso studio nel Cap. 3–4 (B.4); le sei famiglie sono quelle del Cap. 2.2 della tesi.

### RQ-1 — Dipendenza del ranking dalla nozione di fairness

**Formulazione.** *In una CER che ripartisce un incentivo calcolato sull'energia condivisa oraria, il ranking delle regole di ripartizione delle sei famiglie cambia al variare della nozione di fairness (uguaglianza, proporzionalità al contributo, stabilità) e della composizione della comunità? Quale insieme minimo di indicatori basta a discriminarle?*

**Termini calcolabili (B.5).** Ranking = ordinamento delle regole per indicatore; concordanza = Kendall τ fra ordinamenti; composizione = parametri (N, quota produttori, rapporto PV/carico, quota persone fisiche); indicatori = Gini, Jain, MinMax, Price of Fairness, indice di proporzionalità al contributo (correlazione fra compenso e contributo marginale), margine di stabilità e di razionalità individuale.

**Ancore (B.1).** `volpato2024b`, `dynge2025`, `gasca2025`, `cremers2023` #4: tutte di tipo generale.

**Contributo atteso.** Una mappa «quale regola per quale nozione di fairness e quale composizione» e una riduzione degli indicatori.

**Metodo.** Motore Matlab con le regole delle sei famiglie, indicatori comuni sullo stesso valore da ripartire, griglia di composizioni, profili sintetici e semi-reali; coefficienti di concordanza e analisi di sensibilità.

**Novità (formulazione positiva).** Un confronto che riunisce nello stesso banco di prova regole semplici di tipo italiano e regole game-theoretic, su un incentivo orario, e testa la dipendenza del ranking dalla nozione di fairness.

**Rischi.** (1) Rischio **alto** di «me-too» rispetto a Couraud et al. 2025, Limmer 2023, `gonzalezasenjo2025/2026` e alle rassegne 2024–2026. (2) Indicatori circolari se basati sullo Shapley (K1). (3) Risultati dipendenti dai profili sintetici. (4) **Controesempio interno al corpus (B.3):** `campagna2024`, `fioriti2023`, `volpato2023`, `volpato2024b` e `trevisan2024` confrontano già più regole, semplici e game-theoretic, su casi italiani (sintesi K9): la novità si riduce al test esplicito di dipendenza del ranking dalla nozione di fairness e a un insieme comune di indicatori.

**Impegno stimato (tesi magistrale).** Basso-medio.

---

### RQ-2 — Trade-off fra forza incentivante ed equità distributiva

**Formulazione.** *In una CER con incentivo sull'energia condivisa oraria, quanta forza incentivante forniscono le regole delle sei famiglie — misurata come (a) dispersione dei compensi a parità di energia annua e diverso sincronismo con il surplus, (b) quota del guadagno marginale di sincronizzazione trattenuta dal membro, (c) sensibilità al consumo aggiuntivo nelle ore vincolate dalla produzione — e come cambia il suo trade-off con l'equità distributiva a seconda della nozione di fairness adottata e della composizione della comunità?*
*Sotto-domanda:* quanta energia condivisa e quanti € aggiuntivi (e, se i dati lo permettono, CO2 evitata) si generano se una quota `φ` del carico è flessibile e risponde all'incentivo, e il guadagno compensa il costo in equità?

**Termini calcolabili (B.5).** (a), (b), (c) come in §3.2; equità = Gini, Jain, Price of Fairness (nozione di uguaglianza) e indice di proporzionalità al contributo (nozione contributiva); composizione come in RQ-1; `φ` è un parametro di scenario. L'«engagement» in senso sociologico **non** è nella RQ.

**Ancore (B.1).** Principali: `gonzalezasenjo2025` #3 (household flexibility, multi-period coupling) e `gonzalezasenjo2026` (p. 35: metodi ex post, fattori comportamentali), entrambe di tipo generale; #4 per l'uso di dati realistici. Supporto: `basilico2025` (3, 5), `gasca2025` (#7), `giudice2026`, `bilardo2025`, `gianaroli2024`, più l'esperimento di `zatti2021`. **Dichiaro:** #1–#2 di `gonzalezasenjo2025` (nucleolo) non sono usati; RQ-2 risponde a #3 solo sull'asse flessibilità/multi-periodo.

**Ipotesi da testare (non sono risultati; H1–H3 hanno un riscontro nell'esempio giocattolo `[TOY]` dell'Appendice B, H4 no).**
- H1: le regole basate su quantità annue (parti uguali, proporzionale al consumo annuo) hanno dispersione = 1 per costruzione; le regole orarie o contributive hanno dispersione > 1 (nel toy 2,2–2,7).
- H2: con quota produttori fissa `π`, la quota di guadagno trattenuta dal membro nelle regole orarie è limitata da `1 − π` (nel toy 0,5 con `π` = 0,5): `π` è anche un parametro incentivante, quindi RQ-2 e RQ-3 sono collegate.
- H3: le regole proporzionali al consumo (annuo o orario), la progressiva e lo Shapley premiano il consumo aggiuntivo nelle ore vincolate dalla produzione senza aumentare `B`; parti uguali e contributo marginale no.
- H4: il trade-off con l'equità **esiste solo per le nozioni di uguaglianza**; con una nozione contributiva le regole più incentivanti risultano anche più eque. Se H4 regge, il trade-off dipende dalla nozione di fairness: è il punto in cui RQ-2 incorpora RQ-1.

**Contributo atteso.** (i) Una misura calcolabile e comparabile della forza incentivante per le sei famiglie; (ii) la frontiera incentivo–equità per più nozioni di fairness e composizioni; (iii) la quantificazione, sotto ipotesi esplicite di flessibilità, del beneficio aggiuntivo economico e ambientale che la regola può attivare.

**Metodo.** Matlab: (1) regole in forma chiusa o LP; (2) misure (a)–(c) per perturbazione dei profili (coppie di membri con la stessa energia annua e diverso sincronismo, in stile `gonzalezasenjo2026` Sez. 3.1.1; spostamenti piccoli di carico); (3) famiglia parametrica di regole `ρ_λ` (combinazione convessa fra una regola neutra e una contributiva, come l'ibrido 50/50 equità–contributo marginale di arXiv:2606.30359 `[WEB]`) per tracciare la frontiera; (4) strato di risposta opzionale con `φ`; (5) KPI economici, sociali (quota a persone fisiche/vulnerabili), stabilità.

**Novità (formulazione positiva).** Misure rule-intrinseche della forza incentivante confrontate fra famiglie di regole (incluse regole game-theoretic), sull'incentivo orario, con dipendenza dalla nozione di fairness e dalla composizione; il lavoro risponde al limite «ex post / fattori comportamentali» dichiarato da `gonzalezasenjo2026` e all'asse «household flexibility, multi-period coupling» di `gonzalezasenjo2025`.

**Rischi.** (1) Rodrigues et al. 2026 trattano già il trade-off incentivo/equità per schemi basati sulla fedeltà: va letto per intero e la differenza dichiarata (§3.2). (2) Le misure (a)–(c) sono definizioni mie: vanno motivate rispetto alla letteratura di mechanism design (lo dichiaro come `[INFERENZA]`). (3) Il KPI ambientale dipende interamente da `φ` e dai fattori di emissione. (4) Perimetro ampio: va ridotto (§6, punto 5). (5) Una regola molto incentivante ma poco comprensibile può non produrre coinvolgimento: `alonsopedrero2024` (Sez. 7.5, p. 13) segnala comprensibilità, fiducia e ripartizione ex post come barriere; la forza incentivante non le cattura.

**Impegno stimato.** Medio.

---

### RQ-3 — Quota ai produttori e composizione

**Formulazione.** *Come dipende dalla composizione di una CER (rapporto produzione/consumo, numero di produttori, presenza di non proprietari e di persone fisiche) la quota dell'incentivo ai produttori che è coerente con il contributo di ciascun lato (Shapley) e stabile (margine rispetto all'uscita), e di quanto se ne discostano le percentuali fisse usate nella pratica?*

**Termini calcolabili (B.5).** Quota produttori di riferimento `π*(composizione)` = quota Shapley del lato produttori; scostamento `π − π*`; margine di stabilità = eccesso massimo delle coalizioni bloccanti (LP del least core); composizione = griglia di parametri.

**Ancore (B.1).** `minuto2022`, `marrasso2025`, `gianaroli2024`, `cecini_tesi`: tutte autoreferenziali o non operazionalizzate; convergono sul tema ma **non reggono da sole** (§3.4).

**Contributo atteso.** Un riferimento contributivo per un parametro oggi scelto arbitrariamente e un test di quanto le percentuali fisse se ne discostino al variare della composizione.

**Metodo.** Matlab: Shapley esatto (N ≲ 14–16) e least core/nucleolo con LP; griglia di composizioni; confronto con le percentuali fisse della pratica (`cecini_tesi` 50%/20%; `candela2022` 25%).

**Novità (formulazione positiva).** Quota produttori derivata da un criterio contributivo come funzione della composizione.

**Rischi.** (1) Ancore deboli. (2) Lo Shapley *non è nel core* in generale (`gonzalezasenjo2025`, p. 8: «we would not qualify it as fair»): il riferimento è normativo, non «la» quota giusta. (3) Rischio di sovrapposizione con Awerkin–Falbo–Vargiolu e con il progetto PRIN `[WEB]`. (4) Il gioco del solo incentivo ignora l'opzione esterna del produttore (vendita, autoconsumo).

**Impegno stimato.** Medio.

---

## 5. Confronto e raccomandazione

| Criterio | RQ-1 | RQ-2 | RQ-3 |
|---|---|---|---|
| Forza delle ancore (B.1) | Forte (4 paper di tipo G) | Medio-forte (2 di tipo G + supporti) | Debole-media (autoreferenziali convergenti) |
| Rischio di copertura `[WEB]` | Alto | Medio-alto (Rodrigues 2026) | Medio |
| Novità (positiva) | Bassa-media | Media | Media-alta |
| Calcolabilità (B.5) | Piena | Piena per (a)–(c); parziale per lo strato di risposta | Piena |
| Copertura del macro-tema (economico, sociale, ambientale, engagement) | Economico + equità | Tutti, con ambientale solo via risposta e engagement solo come forza incentivante | Economico + composizione |
| Sezione della tesi | §2.3 | §2.3 e §2.4 | §2.5 |
| Impegno | Basso-medio | Medio | Medio |

**Raccomandazione: RQ-2**, costruita sul confronto di RQ-1 e con la composizione di RQ-3 come asse di scenario. Motivi:
1. È l'unica che dà un significato calcolabile all'«engagement» del tuo macro-tema (B.5) e produce una dimensione ambientale, seppur condizionata.
2. Si aggancia a due future work generali e recenti (`gonzalezasenjo2025` #3, `gonzalezasenjo2026` p. 35), in linea con la struttura logica della Parte A: paper recente e autorevole → future work chiaro → gap → il lavoro risponde. Le ancore sono però **adiacenti, non esatte**: #3 chiede di estendere il quadro assiomatico e p. 35 elenca i «fattori comportamentali soggettivi» fra i limiti (§3.2, cautela).
3. Contiene RQ-1 (la dipendenza dalla nozione di fairness è condizione di H4) e quindi non si perde l'ancora più solida.
4. Il rischio principale (Rodrigues 2026) è **verificabile**: leggerlo per intero decide se la differenza (misura rule-intrinseca cross-famiglia, regole game-theoretic incluse, dipendenza dalla nozione di fairness) regge.
5. Le misure si calcolano senza dati comportamentali che non hai; l'unica ipotesi esterna (`φ`) è confinata a una sotto-domanda.

**Cosa mi farebbe cambiare idea.** Se la lettura di Rodrigues et al. 2026 mostra che coprono già una misura cross-famiglia e rule-intrinseca: passerei a RQ-3, riposizionando l'incentivo come asse di scenario. Se preferisci l'ancoraggio più forte e il minimo rischio di perimetro: RQ-1, accettando una novità più bassa.

---

## 6. Feedback diretto (Parte A)

1. **Le ancore «facili» non reggono più.** La richiesta di `cremers2023` su least-core e nucleolo, quella di `eichelbeck2025` e i punti #1–#2 di `gonzalezasenjo2025` riguardano un tema che nel 2025 ha già lavori dedicati (Limmer 2023, Bigi et al. 2025, Fair Least Core 2025 `[WEB]`). Non fondare un gap su «least-core e nucleolo poco esplorati».
2. **«Engagement» non è misurabile da un modello.** La forza incentivante è una condizione necessaria, non sufficiente. `basilico2025` (3, 5) chiede ricerca empirica sociale: non è la tua RQ e non va presentata come tale.
3. **Il KPI ambientale non discrimina le regole a dispacciamento fisso `[INFERENZA]`.** La ripartizione non cambia i flussi fisici: l'impatto ambientale della regola esiste solo se i membri rispondono (strato `φ`). Un risultato ambientale della tesi sarebbe un artefatto delle ipotesi di flessibilità e va presentato come scenario.
4. **Il caso italiano non è il gap (B.4).** La struttura «ripartizione di un valore calcolato sulla sovrapposizione oraria fra produzione e consumo» non è solo italiana: nel corpus ci sono casi di collective self-consumption fuori dall'Italia (`berg2024`) e il caso portoghese di `santos2025`. Formula il gap in termini generali.
5. **Perimetro.** Sei famiglie × più nozioni di fairness × composizioni × strato di risposta è troppo per una tesi magistrale. Proposta: una regola rappresentativa per famiglia (6–8 regole in tutto), tre composizioni, N = 12 come caso base con Shapley esatto, e N maggiore solo con approssimazione; lo strato di risposta come analisi di sensibilità su `φ`.
6. **Lo Shapley non è «la» quota giusta.** `gonzalezasenjo2025` (p. 8) non lo qualifica come equo perché fuori dal core; usarlo come riferimento nella RQ-3 e nelle regole di confronto va dichiarato come scelta normativa.
7. **Dati.** Dati reali di membri di CER italiane non sono nel corpus (sintesi §6.1); la «validazione su dati reali» di `gonzalezasenjo2025` #4 si realizza con profili misurati pubblici (Thames Valley Vision, ecc.) e questo va detto: non è una validazione su CER italiane operative.
8. **Controesempi emersi dalla ricerca online (B.3), da tenere presenti:** (i) Rodrigues et al. 2026 contraddicono ogni formulazione del tipo «nessuno ha studiato il trade-off incentivo/equità»; (ii) la mia sintesi (K2) diceva che nessun paper testa approssimazioni su un gioco a molti membri con l'incentivo italiano: va letta come «nel corpus», perché Bigi et al. 2025 testano il least core fino a 200 utenti sintetici; (iii) C9 («engagement mai misurato») vale per il corpus: Rodrigues et al. includono punteggi di coinvolgimento come *input* di allocazione.
9. **Aggiornamento bibliografico.** Nell'Appendice C ci sono oltre 10 lavori del 2025–2026 che non sono nel corpus di 56 documenti: verifica se rientrano nel tuo protocollo Scopus (628 → 163 → 55) e, se la data della ricerca è precedente, aggiornalo.

---

## 7. Decisione richiesta (CHECKPOINT)

Mi serve da te:
1. **Quale RQ (1, 2 o 3) o quale combinazione** vuoi sviluppare nella Fase 4. La mia raccomandazione è RQ-2 (§5).
2. **Conferma dell'uso di `gonzalezasenjo2025` #3/#4** con la dichiarazione B.2 sui punti #1–#2 (nucleolo).
3. **Accesso ai lavori trovati online:** vuoi sbloccare i domini nelle impostazioni di rete dell'ambiente (menu dell'ambiente cloud → Edit → Network access; passi in https://code.claude.com/docs/en/cloud-environments#network-access) oppure caricare in `Paper/` i PDF che ti indico (almeno Rodrigues et al. 2026 e Couraud et al. 2025), in modo che li legga integralmente prima di fissare il gap?
4. **Lingua** della Fase 4 (outline IMRaD e piano del modello): italiano per la bozza (B.6) salvo diversa indicazione.

Non scrivo l'articolo né il piano del modello finché non confermi.

---

## Appendice A — Log delle ricerche online

Tutte con `WebSearch`; «S» = modalità standard, «E» = extended. Esiti come riportati dal motore di ricerca.

| # | Oggetto della ricerca | Mod. | Esito principale |
|---|---|---|---|
| 1 | Confronto di regole (Shapley, nucleolo, proporzionale) con indicatori Gini/Jain | S | Limmer 2023; `cremers2023`; Fair Least Core 2025; nessun risultato su Gini/Jain |
| 2 | Incentive compatibility delle regole di ripartizione | S | Politecnico di Torino 2026 (`giudice2026`, già nel corpus); trial australiano sul load shifting; nessuna analisi diretta di incentive compatibility |
| 3 | Gioco cooperativo con core e glove game | S | arXiv:2311.18792; arXiv:2511.05291; HAL-02520203; il termine «glove game» non compare |
| 4 | Parametri di ripartizione e composizione, CER italiane | S | Materiale pratico; caso Villanovaforru (fonte non accademica, non usata come evidenza) |
| 5 | Effetto della regola su engagement e partecipazione | S | arXiv:2508.16819; Limmer 2023; il riassunto cita un «sharing game» con partecipanti reali (non ritrovato nelle ricerche successive); nessuna misura diretta di engagement |
| 6 | Couraud et al. 2025 | S | Dettagli su 250 comunità e indicatore meritocratico |
| 7 | *Least cores in energy community games* | S | Proprietà del gioco con veto player, 10–200 utenti sintetici |
| 8 | Limmer 2023 | S | Esiti 90%/75% |
| 9 | Gioco sperimentale sul comportamento dei partecipanti | S | Studio sperimentale 2016 (Frontiers in Energy Research: gioco online con soglia di consumo di gruppo, non allocazione di generazione); Stai et al. 2024; il «conference paper» del punto 5 non è stato ritrovato |
| 10 | Strategy-proof / incentive-compatible per l'incentivo condiviso | E | Nessuna dimostrazione diretta; lavori sull'allocazione proporzionale/progressiva e sul load shifting |
| 11 | Glove game, forma chiusa dello Shapley per min(immissione, prelievo) | E | Nessuna forma chiusa trovata |
| 12 | *Explicit Reward Mechanisms for Local Flexibility in RECs* | S | arXiv:2601.05756 (solo l'inizio dell'abstract) |
| 13 | Rollo et al. 2025 | S | Energies 18(4):872; dettagli sull'allocazione non emersi |
| 14 | *Grid-informed Sharing Coefficients* | S | arXiv:2509.12847 (equo, proporzionale, rank-based; feeder-aware) |
| 15 | Trade-off fra equità e incentivo ad allineare il consumo | E | arXiv:2607.09357; Energies 16(18):6564; arXiv:2606.30359; arXiv:2508.16819 |
| 16 | *Sharing Coefficient-Based Price Signals for DR* | S | arXiv:2607.09357 (luglio 2026) |
| 17 | Tesi PoliMi 2026 su CER | S | Nessuna tesi «Ullo» identificata; tesi CER.ca.MI Solidale e altre |
| 18 | Price of fairness e free-riding | S | arXiv:2010.05544; arXiv:2309.05363; Fair Least Core |
| 19 | Wangen & Clastres 2024 | S | Rassegna IAEE; `gasca2025` |
| 20 | Quota ai proprietari e consumatori non proprietari | E | Nessun «optimal ratio» trovato; framework Shapley e Stackelberg |
| 21 | Statuti reali di CER italiane | S | JSDEWES 2025; PRIN 2022; due tesi |
| 22 | Rassegne sistematiche sui meccanismi di ripartizione | E | RSER 2026; Energies 2025/2026; Utilities Policy 2026; Applied Energy 2026 |
| 23 | Progetto PRIN 2022 (Brescia/Torino) | S | Pubblicazioni «in sviluppo»; un lavoro su investimento e regole di ripartizione presentato 2025–2026 |
| 24 | *Loyalty and tier-based benefit allocation frameworks* | E | Utilities Policy 102 (ott. 2026) |
| 25 | *Optimal Investment and Fair Sharing Rules for Incentives in Virtual RECs* | E | arXiv:2311.12055; inserzione Annals OR ago. 2026 |
| 26 | Dettagli su Rodrigues et al. | E | Quattro meccanismi, trade-off incentivo/equità (solo abstract/highlights) |
| 27 | Sensibilità del compenso al load shifting per regola | E | Nessuna misura formale trovata; PMC10777070 il più vicino |
| 28 | Regole in Italia con premi per il comportamento, simulazione | E | Nessun confronto proporzionale/progressivo/Shapley con premio al load shifting trovato |
| 29 | Coefficienti statici vs dinamici e risposta dei membri | E | Evidenza su coefficienti dinamici; nessun modello di risposta |
| 30 | arXiv:2301.06452 | S | Conte et al.: REC con elettrodomestici smart |

(30 ricerche in totale. I tentativi di `WebFetch` e `curl` su arXiv e sugli altri host sono falliti per la policy di rete, §1.3.)

---

## Appendice B — Controllo numerico giocattolo `[TOY]`

**Non è un risultato.** Script in `output/supporto_fase3/` (`toy_game.py`, `toy_incentive.py`; Python con numpy/scipy; output salvati in `toy_game_output.txt`, `toy_incentive_output.txt`). Un solo giorno rappresentativo ripetuto, **un produttore e sei consumatori** con profili inventati (tre famiglie con picco serale, tre utenti diurni); energia condivisa oraria `min(PV, carico totale)` con valore unitario; PV da 10 kWp salvo dove indicato; quota produttori fissa `π` = 0,5 per le regole semplici e per il contributo marginale; per lo Shapley la quota del produttore è quella che esce dal gioco.

**B.1 — Quota Shapley del produttore e core, al variare di PV/carico.**

| PV/carico | 0,20 | 0,50 | 1,00 | 2,01 | 4,02 | 8,03 |
|---|---|---|---|---|---|---|
| Quota Shapley del produttore | 0,733 | 0,585 | 0,525 | 0,509 | 0,500 | 0,500 |
| `ε*` del least core | −0,0000 | −0,0000 | −0,7033 | −1,0769 | −1,2501 | −1,2527 |

`ε* ≤ 0` in tutti i casi (core non vuoto); `ε* = 0` per PV/carico ≤ 0,5 (nessuna allocazione strettamente interna al core). Il punto di least core restituito dall'LP non è unico e non è riportato.

**B.2 — Tre misure di forza incentivante.** Membri 0–2 con la stessa energia (6 kWh nel giorno rappresentativo ripetuto, quindi stessa energia annua) e diverso sincronismo (sera, piatto, diurno).

| Regola (quota consumatori) | Compenso sincrono / asincrono | Quota del guadagno marginale trattenuta `ι` (spostamento di 0,4 kWh dalle 19 alle 12) | Variazione del compenso per +0,4 kWh in un'ora vincolata (PV 3 kWp) |
|---|---|---|---|
| Parti uguali | 1,00 | 0,083 | 0,000 |
| Proporzionale al consumo annuo | 1,00 | 0,042 | +0,053 |
| Proporzionale al consumo orario | 2,38 | 0,500 | +0,093 |
| Progressiva (water-filling orario) | 2,23 | 0,500 | +0,073 |
| Contributo marginale (normalizzato) | 2,67 | 0,594 | 0,000 |
| Shapley (produttore incluso) | 2,46 | 0,500 | +0,063 |

Lettura `[INFERENZA]`: le tre misure discriminano le regole; nelle regole orarie con `π` fisso il valore di `ι` è `1 − π` quando l'ora di arrivo è in surplus; le regole proporzionali, la progressiva e lo Shapley premiano il consumo aggiuntivo in ore vincolate senza aumentare il valore totale. Valori e ordini di grandezza dipendono dai profili inventati: la tesi deve ricalcolarli con dati orari reali.

---

## Appendice C — Lavori trovati online e **non letti**

Riassunti del motore di ricerca; nessun testo originale letto. Da recuperare per intero prima di fissare il gap (priorità alle prime tre righe).

| Lavoro | Riferimento come riportato | Perché conta |
|---|---|---|
| Rodrigues, Villar, Lucas, Sousa — *Loyalty and tier-based benefit allocation frameworks for renewable energy communities* | Utilities Policy 102, art. 102277 (ott. 2026). https://www.sciencedirect.com/science/article/pii/S0957178726001360 | Trade-off incentivo/equità in schemi basati sulla fedeltà (RQ-2) |
| Couraud, Robu et al. — *Fairness of Energy Distribution Mechanisms in Collective Self-Consumption Schemes* | arXiv:2508.16819 (2025) | Confronto di meccanismi con fairness egalitaria, min-max e meritocratica (G1) |
| Awerkin, Falbo, Vargiolu — *Optimal Investment and Fair Sharing Rules of the Incentives for Renewable Energy Communities* | arXiv:2311.12055 (rev. mar. 2025); inserzione Annals of OR ago. 2026 (relazione non confermata) | Regola di ripartizione dell'incentivo orario con investimento (G4, G8) |
| Limmer — *Empirical Study of Stability and Fairness of Schemes for Benefit Distribution in Local Energy Communities* | Energies 16(4):1756 (2023), doi:10.3390/en16041756 | Shapley, nucleolo, Shapley-core su dati reali |
| Bigi, Fioriti, Frangioni, Passacantando, Poli — *Least cores in energy community games* | arXiv:2511.05291 (2025) | Least core; veto player; 10–200 utenti sintetici |
| Fioriti et al. — *Fair Least Core* | IEEE Trans. Energy Markets, Policy and Regulation (2025) | Allocazione stabile e equa con row generation |
| Shooshtari, Pepiciello, Domínguez-García — *Grid-informed Sharing Coefficients in RECs*; *Sharing Coefficient-Based Price Signals for DR in RECs* | arXiv:2509.12847 (2025); arXiv:2607.09357 (lug. 2026) | Accoppiamento coefficienti di ripartizione–risposta della domanda |
| Conte, Silvestro, Vinci, Di Fazio — *Optimal Coordination and Discount Allocation in Residential RECs with Smart Home Appliances* | arXiv:2301.06452 (2023) | REC italiana, flessibilità, ripartizione dello sconto |
| Wangen, Clastres — *Cost Allocation in Energy Communities* | IAEE Energy Forum, Q1 2024 | Rassegna dei metodi e dei principi di equità |
| *Designing energy sharing in energy communities: Review of coordination mechanisms and internal tariff structures* | RSER (2026). https://www.sciencedirect.com/science/article/abs/pii/S1364032126004387 | Rassegna che valuta incentive compatibility e fairness |
| *Renewable energy communities and energy poverty: A novel benefit-sharing model based on differentiated pricing and incentive allocation* | 2026. https://www.sciencedirect.com/science/article/pii/S2772427126001452 | G5 (povertà energetica) |
| *Benefits and allocation principles of sector-coupled energy communities* | Applied Energy (2026). https://www.sciencedirect.com/science/article/pii/S0306261926001492 | Schemi cooperativo vs competitivo |
| *Incentivising community self-consumption in energy markets: Stable coalition formation using cooperative game theory* | Applied Energy (2025). https://www.sciencedirect.com/science/article/pii/S0306261925012383 | Stabilità (G3) |
| Rollo et al. — *Load Shifting and Demand-Side Management in RECs* | Energies 18(4):872 (2025). https://doi.org/10.3390/en18040872 | Load shifting in REC |
| Bianchini, Casini, Gholami | Energies 18, 4904 (2025) | Ripartizione dei premi di risposta della domanda |
| Stai et al. | IEEE Access (2024) | Gioco non cooperativo su allocazione proporzionale vs uguale |
| *A value sharing method for heterogeneous energy communities archetypes* | PMC10777070 | Confronto EQ/Shapley/MC con load shifting |
| Magni, Bricca, Familiari | JSDEWES (2025). http://www.sdewes.org/jsdewes/pid13.0589 | Scenari D.M. 414/2024 |
| PRIN 2022 «Compensation Rules Among Members of Heterogeneous Energy Communities» (Brescia/Torino) | https://energycommunities-lab.unibs.it/ | Progetto sullo stesso tema (G4); risultati non letti |
| arXiv:2606.30359 (decision-support PV self-consumption); arXiv:2606.30083 (new member integration, prospect theory); Energies 18(18):4815; arXiv:2311.18792; HAL-02520203; arXiv:2010.05544; arXiv:2309.05363; arXiv:2303.07879 | come indicato | Ibrido equità/contributo marginale, nuovi membri, core non vuoto, incentivi alla flessibilità |
