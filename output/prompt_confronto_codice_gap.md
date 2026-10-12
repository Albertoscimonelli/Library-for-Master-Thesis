# Prompt — Confronto fra il mio codice e il gap di letteratura (RQ-1)

> Da incollare in una sessione che ha accesso al mio codice. Il prompt è autosufficiente: non richiede i file del repository della tesi. Dove cito «piano» o «outline» mi riferisco a `output/fase4_piano_modello_matlab.md` e `output/fase4_outline_imrad.md`, che puoi leggere se li hai.

---

## 1. Ruolo e regole di lavoro

Sei un revisore tecnico con competenze di energy systems, teoria dei giochi cooperativi e Matlab. Confronta il **codice che ti indico** con il **gap di letteratura e il modello atteso** descritti sotto.

Regole, da applicare sempre:
- Usa solo ciò che vedi nel codice e ciò che è scritto in questo prompt. **Non inventare** risultati, numeri o citazioni. Se un'informazione manca o è ambigua, scrivilo esplicitamente e chiedimelo.
- Distingui sempre **ciò che il codice fa** (con `file:riga`) da **ciò che deduci** (etichetta `[INFERENZA]`).
- Non «salvare» scelte indifendibili: se una scelta del codice è sbagliata o non risponde alla RQ, dillo in modo diretto.
- Non modificare il codice finché non te lo chiedo. Prima produci il report (sezione 6).
- Output in italiano; termini tecnici in inglese.

## 2. Il gap scelto

**Tema.** Ripartizione dei benefici economici di una Comunità Energetica Rinnovabile (CER): effetto dei meccanismi di allocazione su esiti economici, sociali e sull'engagement.

**Gap.** I lavori sulla ripartizione dei benefici confrontano poche regole e per lo più su una sola nozione di fairness. Mancano indicatori quantitativi comuni, calcolati sulle **stesse regole e sugli stessi dati**, che mostrino se **l'ordinamento (ranking) delle regole dipende dalla nozione di fairness adottata** e dalla **composizione della comunità**.

**Basi nella letteratura (future work degli autori; citazioni verificate parola per parola sui PDF):**
- `volpato2024b` (Sez. 4, p. 22): «identify parameters that can quantitatively compare the different benefit distributions based on the "individual", "collective" and "proportional" fairness».
- `dynge2025` (Sez. 8, p. 12): «additional investigation is needed to refine fairness indicators»; «More concrete evaluation criteria could also be derived to perform a more generalisable and comprehensive evaluation of multiple fairness indicators».
- `gasca2025` (Sez. 3.5, p. 12): esplorare «additional types of comparisons […] within the same framework», in particolare per metriche non economiche.
- `cremers2023` (Sez. 6, p. 13): «there are many other fairness concepts that could be explored in energy applications, and it would be relevant to compare their outcome to Shapley values».

Il contesto italiano (GSE, TIP, quota vincolata) è un **caso di studio**, non il gap.

**Domanda di ricerca (RQ-1).**
> In una CER che ripartisce un incentivo calcolato sull'energia condivisa oraria, il ranking delle regole di ripartizione appartenenti alle sei famiglie della tassonomia cambia al variare della nozione di fairness (uguaglianza, proporzionalità al contributo fisico, stabilità, inclusione) e della composizione della comunità? Quale insieme minimo di indicatori basta a discriminarle?

Sotto-domande: **RQ1.a** migliori e peggiori regole per nozione, con margine in valore; **RQ1.b** concordanza fra i ranghi di nozioni diverse; **RQ1.c** riduzione degli indicatori a poche dimensioni; **RQ1.d** regole robuste a tutte le nozioni; **RQ1.e** effetto di composizione e parametri.

**Elementi che distinguono il lavoro:** (1) banco di prova comune per le sei famiglie; (2) test esplicito della dipendenza del ranking dalla nozione; (3) composizione come fattore sperimentale; (4) insieme minimo di indicatori come output operativo.

**Che cosa RQ-1 NON include** (se il codice lo fa, segnalalo come fuori perimetro, non come errore): Price of Fairness (non calcolabile con profili fissi: tutte le regole distribuiscono lo stesso valore); effetti comportamentali, ambientali e di engagement (appartengono a una possibile RQ-2); mercati locali P2P/LEM; Nash bargaining (con `v({i}) = 0` coincide con la divisione in parti uguali `[INFERENZA]`).

**Avvertenza.** Due lavori vicini (Couraud et al. 2025; Limmer 2023) li conosco solo da riassunti di ricerca web, non letti: potrebbero coprire in parte i punti (1)–(2). La novità certa è nei punti (3)–(4).

## 3. Il modello atteso

**Gioco.** `G_t = Σ_i g_it`, `W_t = Σ_i w_it`, `e_t = min(G_t, W_t)`, valore da ripartire `B = Σ_t c_t e_t` (`c_t` costante di default; TIP orario come variante). Valore di coalizione `v(S) = Σ_t c_t · min(Σ_{i∈S} g_it, Σ_{i∈S} w_it)`, `v(∅) = 0`. Ogni regola produce `R_i` con `Σ_i R_i = B`. Risoluzione oraria, 8.760 ore, `0/0 := 0`.

**Parametri di default.** `π` = 0,4 (quota ai produttori per le regole semplici; prove 0,2/0,4/0,6); `γ` = (0,2; 0,5; 0,3) per le categorie in CT; `(n_q, q_cap)` = (0,02; 0,5) per SW; `M` = 500 permutazioni per SVa; soglia di taglio dei cluster `cut` = 0,25.

**13 regole in 6 famiglie** (`pot_P = π B`, `pot_C = (1 − π) B`):

| ID | Famiglia | Definizione |
|---|---|---|
| SV | game-theoretic | Shapley esatto |
| NUC | game-theoretic | Nucleolo (LP iterativi, moltiplicatori duali) |
| MC | approssimazioni | Contributo marginale normalizzato: `R_i = B m_i/Σ m_j`, `m_i = v(N) − v(N∖{i})` |
| SVa | approssimazioni | Shapley campionato con `M` permutazioni |
| EQ | semplici | `pot_P/#P` ai produttori, `pot_C/#C` ai consumatori |
| PA | semplici | Proporzionale alle quantità annue (`g_i`, `w_i`) |
| PS | semplici | Come PA, ma sulle sole ore condivise |
| PH | semplici | Pro-rata orario: `Σ_t c_t e_t [π g_it/G_t + (1 − π) w_it/W_t]` |
| PG | semplici | Progressiva (water-filling orario) sul lato consumo; produttori come PH |
| CT | semplici/multi-criterio | Albero per categorie: produttori come PS; consumatori della categoria `k` ricevono `pot_C γ_k`, ripartito con `w_i^S`; cluster vuoto → `γ` ridistribuita |
| EP | prezzi/tariffe | Il lato scarso prende l'ora: `π_t = 1` se `G_t < W_t`, 0,5 se uguali, 0 altrimenti |
| PF | performance-based | Chiave giornaliera `corr(w_it, G_t)` rimappata in [0,1] (da `gianaroli2024`, M3; da ricontrollare sul PDF) |
| SW | multi-criterio/equità | Quota riservata ai vulnerabili `s_V = min(q_cap, n_q·#V)` |

**Indicatori** (orientati: più alto = meglio; rango 1 = migliore):

| Nozione | Indicatori |
|---|---|
| Uguaglianza | E1 `1 − Gini(R_C)`; E2 Jain; E3 MinMax `min/max`; E4 `1 − Gini(R_i/w_i)` |
| Garanzia minima | S3 `min_i R_i / B` |
| Proporzionalità fisica | P1c e P1p: `1 − ½ Σ abs(R_i/R_lato − q_i)`, con `q_i` quota fisica sull'energia condivisa |
| Stabilità di gruppo | S1 `−ε_max/B` con `ε_max = max_{S≠∅,N}[v(S) − R(S)]`; S2 `1 −` quota di coalizioni bloccanti |
| Inclusione | Q1, Q2 (persone fisiche, vulnerabili): quota di premio / quota di teste; Q1′, Q2′ rispetto al contributo fisico |
| Basati su riferimento | D_MC, D_SV (distanza da MC e da SV): **circolari**, riportati in blocco separato |

Descrittore: `π_eff = Σ_{i∈P} R_i / B`. Quasi ogni indicatore ha una regola che lo vince per costruzione: il risultato interessante è come si piazzano le altre regole e se una regola non perde troppo su nessuno.

**Analisi dei ranghi.** Ranghi con parità a rango medio; τ_b di Kendall fra coppie di indicatori; W di Kendall; cluster gerarchici su `(1 − τ̄)/2`; un rappresentante per cluster; insieme di Pareto sui ranghi per cluster; rimpianto minimax; stabilità del ranking fra celle di composizione; meta-regressione della concordanza sui descrittori di composizione; analisi ripetuta senza D_MC e D_SV; bootstrap sulle repliche.

**Scenari.** Caso base `n = 12` (3 produttori, 9 consumatori: persone fisiche, PMI, altro ente, 2 vulnerabili). Fattori: rapporto PV/carico (0,5/1,0/1,5), eterogeneità dei consumi, sincronismo carico–PV, numero e concentrazione dei produttori, quota di persone fisiche, `N` (8, 12, 16 esatti; 50, 100 solo campionamento), `π`, `c_t`, risoluzione, prosumer. Repliche `R` = 30 per cella. Un seme per replica.

**Proprietà note del gioco** (mie inferenze, da verificare): `v` è monotono; il core è non vuoto; la regola EP sta nel core; Shapley e PH a `π` = 0,5 in generale no.

## 4. Checklist di confronto

Per ogni riga indica: **Presente / Parziale / Assente / Diverso**, con `file:riga` e una frase.

| ID | Requisito |
|---|---|
| C1 | `B` e `v(S)` come sopra (min orario di somme di immissione e prelievo); `0/0 := 0`; `Σ_i R_i = B` verificato per ogni regola |
| C2 | Le stesse serie `g_it`, `w_it` e lo stesso `B` per tutte le regole nella stessa replica |
| C3 | Quali delle 13 regole sono implementate, e con quali differenze di definizione (elenca ogni scostamento) |
| C4 | Famiglie coperte: game-theoretic, approssimazioni, semplici, prezzi/tariffe, performance-based, multi-criterio |
| C5 | Calcolo di `v(S)` per tutte le coalizioni (N ≲ 16) e campionamento per N grande |
| C6 | Nucleolo: metodo, tolleranze, controllo che stia nel core |
| C7 | Indicatori per ciascuna nozione (uguaglianza, proporzionalità fisica, stabilità, inclusione), e come sono orientati |
| C8 | Indicatori di stabilità basati su `v(S)` (S1, S2) |
| C9 | Ranking per indicatore con gestione delle parità; τ_b (non τ_a) fra indicatori |
| C10 | Cluster di indicatori, rappresentanti, rimpianto minimax, Pareto |
| C11 | Composizione come fattore sperimentale (PV/carico, eterogeneità, sincronismo, produttori, quota persone fisiche) |
| C12 | Repliche con semi, intervalli di confidenza, salvataggio di configurazione e versione |
| C13 | Dati: profili sintetici o reali? Quali? Risoluzione? |
| C14 | Il codice calcola qualcosa che RQ-1 non richiede o che richiede un'altra RQ? (comportamento, CO2, Price of Fairness, mercato) |
| C15 | Test (casi a mano, simmetria, efficienza, ordine dei membri, casi limite: ore con `G_t = 0` o `W_t = 0`, categoria vuota, nessun vulnerabile) |

## 5. Domande a cui il report deve rispondere in modo diretto

1. Con questo codice, posso rispondere a RQ1.a–e? Quali sotto-domande no, e che cosa manca?
2. Il confronto fra regole è davvero «sugli stessi dati e sugli stessi indicatori», o ci sono scorciatoie che favoriscono qualche regola?
3. Ci sono indicatori circolari o regole che vincono per costruzione senza che il codice lo separi?
4. Ci sono errori matematici (normalizzazioni, orientamento degli indicatori, parità, divisioni per zero) che cambierebbero i ranghi?
5. Che cosa nel codice **non serve** a RQ-1 e andrebbe rimandato?

## 6. Formato del report

1. **Inventario del codice** (file, funzioni, flusso dei dati) in 10 righe.
2. **Tabella della checklist** C1–C15.
3. **Scostamenti dalle definizioni** (regola o indicatore, definizione nel codice, definizione attesa, effetto probabile sui ranghi).
4. **Errori o rischi** in ordine di gravità, con `file:riga`.
5. **Risposte alle domande della sezione 5.**
6. **Ordine di lavoro proposto** (max 8 passi), senza modificare il codice.
7. **Domande aperte** per me, se qualcosa è ambiguo.

Non riscrivere il codice e non scrivere l'articolo in questa fase.
