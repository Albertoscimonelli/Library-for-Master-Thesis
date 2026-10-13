# Fase 4 (parte 1) — RQ-1 definitiva e outline IMRaD dell'articolo

**Stato:** bozza di lavoro. L'articolo **non** è scritto: qui c'è la struttura. Il piano del modello Matlab è in `output/fase4_piano_modello_matlab.md`.
**Data:** 12/10/2026. **Lingua:** italiano per le bozze; il testo destinato alla tesi/articolo sarà in inglese accademico LaTeX (B.6).
**File collegati:** `output/gap_e_research_question.md` (Fase 3), `output/sintesi.md` (Fase 2), `output/schede/` (Fase 1), `output/supporto_fase4/` (pilot di fattibilità in Python, test e istanza di verifica).

---

## 0. Decisione registrata e conseguenze

**Decisione dell'utente (12/10/2026):** «punterei con RQ1 ed eventualmente una volta conclusa una possibile aggiunta con RQ2». Quindi:
- **RQ-1** (dipendenza del ranking delle regole dalla nozione di fairness) è la domanda principale.
- **RQ-2** (forza incentivante e trade-off con l'equità) è un'estensione facoltativa, da valutare **dopo** i risultati di RQ-1 (§4).

Le altre domande del checkpoint di Fase 3 (§7) non hanno avuto risposta. Assunzioni di lavoro, da correggere se sbagliate:
- `gonzalezasenjo2025` #3/#4 (con la dichiarazione B.2 sui punti #1–#2 sul nucleolo) servono **solo** all'estensione RQ-2: non sono ancore di RQ-1.
- I lavori trovati online (Appendice C della Fase 3) restano **non letti** (host accademici bloccati dall'ambiente). Per RQ-1 questo pesa di più che per RQ-2, perché i concorrenti più vicini sono lì (§1.4).
- Lingua della Fase 4: italiano.

**Conseguenze che vanno dette senza giri di parole (Parte A)**
1. **Con RQ-1 da sola non rispondi a tutto il tuo macro-tema.** RQ-1 copre l'esito *economico* (importi per membro e per categoria) e quello *sociale-distributivo* (fairness, categorie, vulnerabili). Le dimensioni **ambientale** e **engagement** non sono oggetto di RQ-1: con dispacciamento fisso gli indicatori ambientali sono identici per tutte le regole (Fase 3, §6 punto 3) e l'engagement richiede la forza incentivante di RQ-2. Due strade coerenti: (a) restringere titolo e obiettivi della tesi a «economic and social (distributive) outcomes» e dichiarare RQ-2 come lavoro futuro; oppure (b) impegnarsi su RQ-2 con un punto di decisione dopo RQ-1 (§4). Non va scritto nel titolo qualcosa che il modello non calcola (B.5).
2. **RQ-1 è la scelta a rischio di sovrapposizione più alto.** Nella Fase 3 l'avevo valutata a «novità bassa-media, rischio alto di me-too» (Couraud et al. 2025, Limmer 2023, `gonzalezasenjo2025/2026`, rassegne 2024–2026). Resta vero. Il lavoro è difendibile solo con i quattro elementi distintivi del §1.4, e **prima di scrivere Introduzione e novità bisogna leggere per intero almeno Couraud 2025 e Limmer 2023**.
3. **Tre correzioni emerse mentre progettavo il modello**, che cambiano la formulazione di Fase 3:
   - Il **Price of Fairness non è calcolabile** nell'ambiente di RQ-1: con ripartizione ex post e profili fissi tutte le regole distribuiscono lo stesso valore `B`, quindi la perdita di efficienza è nulla per costruzione. Si definisce solo se la regola modifica il comportamento (RQ-2). L'ho tolto da RQ-1 (errata nella Fase 3).
   - Il **Nash bargaining** con punti di disaccordo nulli (`v({i}) = 0` per tutti, vero nel gioco del solo incentivo) coincide con la divisione in parti uguali fra tutti i giocatori `[INFERENZA]`: non lo includo come regola distinta.
   - Gli indicatori «distanza dallo Shapley» e «distanza dal contributo marginale» sono **circolari** per le regole che li usano come riferimento (K1/K5 della sintesi). Li riporto sempre in un blocco a parte e ripeto le analisi senza di essi.

---

## 1. RQ-1 definitiva

### 1.1 Formulazione

> **RQ-1.** *In una comunità energetica rinnovabile che ripartisce un incentivo calcolato sull'energia condivisa oraria, il ranking delle regole di ripartizione appartenenti alle sei famiglie della tassonomia cambia al variare della nozione di fairness (uguaglianza, proporzionalità al contributo fisico, stabilità, inclusione) e della composizione della comunità? Quale insieme minimo di indicatori basta a discriminarle?*

Sotto-domande (tutte calcolabili dal modello):

| ID | Domanda | Risposta calcolata come |
|---|---|---|
| RQ1.a | Per ogni nozione, quali regole sono migliori e peggiori, e con quale margine? | Valori e ranghi degli indicatori per regola; margini in valore, non solo ranghi |
| RQ1.b | I ranghi indotti da nozioni diverse sono concordi? | Tau di Kendall (τ_b) fra coppie di indicatori; W di Kendall; quota di coppie con τ < 0 |
| RQ1.c | Gli indicatori si riducono a poche dimensioni indipendenti? | Cluster gerarchici su distanza (1 − τ̄)/2; rappresentanti e τ di ricostruzione |
| RQ1.d | Esistono regole robuste a tutte le nozioni? | Insieme di Pareto sui ranghi per cluster; rimpianto minimax; probabilità di essere fra le prime tre |
| RQ1.e | Come cambiano concordanza e ranking con la composizione e con i parametri? | Stabilità del ranking fra celle; meta-regressione della concordanza su descrittori di composizione; sensibilità a `π` |

Controllo di robustezza R1 (non è una RQ): le approssimazioni dello Shapley per campionamento (`SVa`) preservano il ranking? Con quanti campioni?

### 1.2 Termini della RQ e loro calcolabilità (B.5)

| Termine | Operazionalizzazione | Dove si calcola |
|---|---|---|
| Incentivo sull'energia condivisa oraria | `B = Σ_t c_t · min(G_t, W_t)` con `G_t` immissione totale, `W_t` prelievo totale, `c_t` valore unitario (costante di default; TIP orario come variante) | Piano modello §3 |
| Regola di ripartizione | Una delle 13 regole del catalogo (6 famiglie) con parametri esplicitati | Piano modello §4 |
| Nozione di fairness | Gruppo di indicatori: uguaglianza, proporzionalità al contributo fisico, stabilità, inclusione (e, separatamente, indicatori basati su un riferimento game-theoretic) | Piano modello §5 |
| Ranking | Ordinamento delle regole per un indicatore (rango 1 = migliore, ranghi medi in caso di parità) | Piano modello §6 |
| Cambia al variare di… | τ_b fra ranking; W; stabilità del ranking fra celle di composizione | Piano modello §6 |
| Composizione | Descrittori: rapporto PV/carico, eterogeneità dei consumi, sincronismo carico–PV, numero e concentrazione dei produttori, quota di persone fisiche | Piano modello §7 |
| Insieme minimo di indicatori | Un rappresentante per cluster con τ di ricostruzione ≥ soglia | Piano modello §6 |

**Che cosa RQ-1 non dice**
- Non dice quale regola sia «la più equa» in assoluto: dice come cambiano gli ordinamenti a seconda della nozione.
- Non stima effetti comportamentali, ambientali o di engagement (sono di RQ-2).
- Non valida nulla su CER italiane operative: i profili sono sintetici o pubblici, e questo si dichiara (B.4: il caso italiano è un caso studio, un'applicazione dei vincoli del Cap. 3.5 nel Cap. 4).
- Non descrive le regole di fatto adottate dagli statuti delle CER: per quelle servono dati che non ho.
- Non copre i meccanismi di mercato locale (MMR, SDR, P2P): la famiglia dei prezzi e delle tariffe (Cap. 2.2.4) è rappresentata solo da regole di suddivisione tariffaria (scarsità oraria EP e prezzo medio AP = PH a `π` = 0,5). «Sei famiglie» va quindi dichiarato con questa riserva (piano modello §4.2).

### 1.3 Ipotesi operative (da fissare prima di guardare i risultati definitivi; **non** sono risultati)

| ID | Ipotesi | Come si falsifica |
|---|---|---|
| H1 | Nel caso base e in almeno l'80% degli scenari il τ medio fra indicatori di nozioni diverse è inferiore a 0,3 | τ medio ≥ 0,3 nella maggioranza degli scenari |
| H2 | Gli indicatori si raggruppano in al più cinque cluster, e il cluster «uguaglianza/garanzia minima/inclusione» è associato negativamente (τ̄ < −0,3) con quello «proporzionalità fisica/stabilità» | Cluster più numerosi o associazione non negativa |
| H3 | La stabilità del ranking di un indicatore fra composizioni (τ̄ ≥ 0,6) è maggiore della concordanza fra indicatori nella stessa composizione, tranne per gli indicatori di stabilità quando varia il rapporto PV/carico | Il contrario |
| H4 | Esiste almeno una regola non dominata in ≥ 90% degli scenari con rimpianto minimax sotto la mediana | Nessuna regola con queste proprietà |
| H5 | La quota ai produttori `π` modifica il ranking delle regole semplici sugli indicatori di stabilità e di garanzia minima, non su quelli di uguaglianza interna al lato o di proporzionalità fisica | `π` modifica anche i secondi |

Le soglie (0,3; 0,6; 90%) sono indicative e vanno fissate nel protocollo prima delle simulazioni definitive. Il pilot in Python (piano modello §13) è coerente con H1–H4 su dati inventati e con le mie definizioni: **non** è un risultato della tesi.

### 1.4 Che cosa aggiunge RQ-1 rispetto ai lavori più vicini (formulazione positiva, B.3)

1. **Banco di prova comune.** Le sei famiglie di regole, comprese le regole semplici di tipo italiano (percentuali per categoria, progressiva «Layered», pro-rata orario) e quelle game-theoretic (Shapley, nucleolo) e le loro approssimazioni, sullo stesso valore da ripartire (un incentivo orario), sugli stessi membri, con gli stessi indicatori.
2. **Test esplicito della dipendenza del ranking dalla nozione** (τ_b, cluster, rimpianto minimax), non solo il confronto indicatore per indicatore.
3. **Dipendenza dalla composizione** come fattore sperimentale (PV/carico, eterogeneità, sincronismo, produttori, quota di persone fisiche) con meta-regressione.
4. **Insieme minimo di indicatori** come output operativo per statuti e decisori.

**Tabella di posizionamento (da usare nel Cap. 2.6 e nella Sez. 2.3 dell'articolo).** Le colonne «Ranking vs nozioni» sono una mia lettura delle schede `[INFERENZA]`; le righe `[WEB]` si basano sul solo riassunto del motore di ricerca.

| Lavoro | Regole confrontate | Indicatori | Dati / N | Composizione variata? | Concordanza fra nozioni |
|---|---|---|---|---|---|
| `volpato2024b` | SW, Nash bargaining, Shapley, nucleolo | Costo, Price of Fairness, eccedenze; tre nozioni qualitative | Padova, 8 giorni tipici; N = 4 | No | Dichiarata come lavoro futuro (p. 22) |
| `dynge2025` | Nessuna regola (prezzo SDR); valuta gli indicatori | MinMax, QoS (Jain), QoE, Equality Index e varianti | Oslo, 10 famiglie, 9 casi | Casi con 0/1/5/10 PV e batterie | Mostra che gli indicatori discriminano in modo diverso; non confronta ranghi di regole |
| `gasca2025` | Shapley, OPT, EANSV, PR; Pool e P2P | Jain, MinMax, QoE, distanza dallo Shapley | Francia, 7 famiglie, 1 mese | No | «I quattro indici danno giudizi diversi» (sintesi); nessun test di concordanza |
| `cremers2023` | MC, SEV, campionamento adattivo (approssimazioni dello Shapley) | Distanza dallo Shapley esatto | UK, 10–5.251 famiglie | Classi di consumo | No |
| `gonzalezasenjo2025` | Otto metodi in tre famiglie | Sette proprietà assiomatiche | Analitico, un solo slot | n.a. | Proprietà, non ranking |
| `gonzalezasenjo2026` | BS, price-based, PTE, nucleolo, Shapley | Risparmi, partecipazione, quote per ruolo, tempi | Prezzi del mercato spagnolo; n = 10–1.000 | Sì (mix di profili, penetrazione) | No |
| `campagna2024` | Shapley, Owners, Proportional, Packets e miste con EP | Ricavo per membro, LIHC | Teglio, N = 16 | No | No |
| `fioriti2023` | Shapley, nucleolo, VarLeastCore contro schemi semplici | ΔNPV per utente | N = 10 | No | No |
| `cecini_tesi` | Albero con Proportional contro Layered | Gini, quote per categoria | 4 CER sintetiche, N = 12–16 | 4 composizioni | No |
| `kulmala2021` | Otto metodi (qualitativo) | Equità, stabilità, comprensibilità, incentivi, calcolo | Nessun dato | n.a. | Confronto qualitativo |
| Couraud et al. 2025 `[WEB]` | Pro rata, glass-filling, double auction (energia) | Egalitaria, min-max, meritocratica | 250 comunità casuali, 20 famiglie | Casuale | Non noto (testo non letto) |
| Limmer 2023 `[WEB]` | Shapley, nucleolo, Shapley-core | Stabilità ed equità nel tempo | Dati reali australiani | Dimensione | Non noto (testo non letto) |

**Rischio residuo.** Le due righe `[WEB]` potrebbero coprire in parte i punti 1–2. Se la lettura integrale lo conferma, la novità si riduce ai punti 3–4 e alla presenza delle regole di tipo italiano: va allora dichiarato così (§5, rischio R1).

---

## 2. Outline IMRaD dell'articolo

**Rivista bersaglio (mia valutazione `[INFERENZA]`, da verificare sullo scope ufficiale):** *Applied Energy* (contributo metodologico e computazionale) come prima scelta; *Energy Policy* come alternativa se si dà più peso alle implicazioni per statuti e regolazione. *RSER* è orientata alle rassegne: meno adatta.

**Titoli di lavoro (inglese)**
1. *Which fairness? Rank consistency of benefit-allocation rules in renewable energy communities with an hourly shared-energy incentive.*
2. *Fairness notions and allocation rules in energy communities: a rank-concordance analysis across six rule families.*
3. *How to share the incentive: a cross-family comparison of allocation rules under multiple fairness notions.*

**Lunghezza indicativa:** 8.000–10.000 parole di testo, 8–10 figure, 4–5 tabelle, appendici.

| Sezione | Contenuto | Fonti dal corpus / dal modello | Parole |
|---|---|---|---|
| **Abstract** (strutturato) | Contesto, obiettivo, metodo (13 regole, 6 famiglie, indicatori per 4 nozioni, analisi di concordanza), risultati (da scrivere a fine lavoro), conclusioni | — | 200–250 |
| **Highlights** | 3–5 punti (nessun risultato scritto prima di averlo) | — | 5 × 85 caratteri |
| **1. Introduction** | (i) Il problema: l'incentivo sull'energia condivisa è ripartito da regole private (C1); (ii) perché la regola conta: effetti su grandi/piccoli consumatori e persone fisiche (`gianaroli2024`, `cecini_tesi`, `santos2025`); (iii) il problema di misura: nozioni di fairness e indicatori non comparabili (K5, `gasca2025` p. 5); (iv) base del gap: quattro future work generali (`volpato2024b`, `dynge2025`, `gasca2025`, `cremers2023`), citazioni verificate; (v) RQ-1, contributi, struttura | `gap_e_research_question.md` §3.1 | 1.200 |
| **2. Background and related work** | 2.1 Tassonomia a sei famiglie e regole rappresentative; 2.2 Nozioni di fairness e indicatori (Gini, Jain, MinMax/QoE, proporzionalità fisica, stabilità/core, inclusione); 2.3 Confronti più vicini e che cosa resta aperto (tabella §1.4) | Cap. 2 della tesi; `sintesi.md` §3–§5 | 1.500 |
| **3. Methodology** | 3.1 Il gioco dell'energia condivisa (notazione, `v(S)`, proprietà); 3.2 Regole (Tabella 1: 13 regole, famiglie, parametri); 3.3 Indicatori (Tabella 2); 3.4 Analisi di concordanza (τ_b, W, cluster, Pareto, rimpianto minimax, meta-regressione); 3.5 Scenari e dati (Tabella 3); 3.6 Implementazione, verifica e riproducibilità (test, istanza di verifica, codice) | Piano modello §3–§9 | 2.500 |
| **4. Results** | 4.1 Caso base: premi per regola e categoria (Fig. 3); 4.2 Indicatori e ranghi (Fig. 4, heatmap); 4.3 Concordanza fra nozioni e cluster (Fig. 5); 4.4 Regole robuste: Pareto e rimpianto minimax (Fig. 6–7); 4.5 Effetto della composizione (Fig. 8) e di `π` (Fig. 9); 4.6 Approssimazioni e scala (Fig. 10); 4.7 (facoltativo) strato regolatorio italiano | Esperimenti del §7 del piano | 2.200 |
| **5. Discussion** | 5.1 Risposte a RQ1.a–e; 5.2 Implicazioni per gli statuti: quale regola per quale obiettivo, e quali indicatori riportare; 5.3 Rapporto con la letteratura (conferme e smentite rispetto a Couraud 2025, Limmer 2023, `gonzalezasenjo2025/2026`, `volpato2024b`, `gasca2025`); 5.4 Limiti e minacce alla validità; 5.5 Lavoro futuro (RQ-2: forza incentivante; validazione su dati reali) | — | 1.500 |
| **6. Conclusions** | Risposta in tre-quattro frasi, raccomandazioni operative, limite principale | — | 250 |
| **Back matter** | Disponibilità di dati e codice (codice Matlab, generatore sintetico, istanza di verifica); dichiarazione sull'uso di strumenti di scrittura; finanziamenti | — | — |
| **Appendici** | A: equazioni delle regole e casi limite; B: definizioni degli indicatori; C: parametri degli scenari; D: test di verifica; E: sensibilità aggiuntive | Piano modello §4, §5, §7, §9 | — |

**Elenco figure e tabelle**

| ID | Contenuto | Scopo |
|---|---|---|
| Fig. 1 | Schema del modello: dati → gioco → regole → indicatori → analisi | Orientare il lettore |
| Fig. 2 | Profili tipici per archetipo e produzione PV (settimana estiva e invernale) | Mostrare i dati sintetici |
| Fig. 3 | Premio per membro e per regola nel caso base (barre per categoria) | RQ1.a |
| Fig. 4 | Heatmap dei ranghi (regole × indicatori) nel caso base | RQ1.a–b |
| Fig. 5 | Matrice τ di Kendall fra indicatori e dendrogramma | RQ1.b–c |
| Fig. 6 | Piano uguaglianza–stabilità con le regole (frontiera di Pareto) | RQ1.d |
| Fig. 7 | Rimpianto minimax e probabilità di essere non dominata, per regola | RQ1.d |
| Fig. 8 | τ medio e stabilità del ranking al variare di PV/carico, mix e eterogeneità | RQ1.e |
| Fig. 9 | Effetto di `π` sugli indicatori di stabilità e di garanzia minima | RQ1.e, H5 |
| Fig. 10 | Errore e tempo del campionamento dello Shapley per `M` e `N` | R1 |
| Tab. 1 | Tassonomia: 13 regole, famiglie, parametri, fonte | Metodo |
| Tab. 2 | Indicatori: definizione, orientamento, gruppo, circolarità | Metodo |
| Tab. 3 | Scenari e fattori | Metodo |
| Tab. 4 | Posizionamento rispetto ai lavori più vicini (§1.4) | Introduzione/Sez. 2 |
| Tab. 5 | Risposte sintetiche a RQ1.a–e con soglie di H1–H5 | Discussione |

**Ordine di scrittura consigliato.** Prima la Sez. 3 (stabile e già fissata dal piano), poi le Sez. 4–5 a esperimenti conclusi, poi Introduzione e Background (dopo la lettura integrale dei lavori online), per ultimo Abstract e Highlights.

---

## 3. Mappa articolo ↔ capitoli della tesi

| Capitolo della tesi | Stato (da `ISTRUZIONI_E_CONTESTO.md`) | Parte dell'articolo che lo alimenta o che ne deriva |
|---|---|---|
| Cap. 1 Introduzione | Non trattato | Sez. 1 (versione estesa) |
| Cap. 2 Literature Review (§2.1–§2.6) | Scritto; §2.6 in revisione | Sez. 2 e Tab. 4; §2.3 ↔ indicatori; §2.5 ↔ composizione; **§2.6 ↔ bozza dell'Appendice A di questo file** |
| Cap. 3 Quadro normativo (§3.5 vincoli di modello) | Scritto | Sez. 3.1 (specifiche) e strato regolatorio opzionale (Sez. 4.7) |
| Cap. 4 Metodologia | Da sviluppare | Sez. 3 (versione estesa con tutte le equazioni, il piano di verifica e i parametri) |
| Cap. 5 Simulazione | Da sviluppare | Sez. 4 (versione estesa con tutti gli scenari) |
| Conclusioni | — | Sez. 5–6; più, se si fa RQ-2, un capitolo dedicato |

**Specifiche italiane da trasferire nel Cap. 4** (B.4: mai nel gap): energia condivisa oraria come minimo fra immissione e prelievo; tariffa premio `TIP_h = {min[CAP; TP_base + max(0; 180 − P_z)] + FC_zonal}·(1 − F)` (Eq. 32 di `cecini_tesi`, p. 57); quota vincolata/non vincolata con soglia 55% (45% per gli impianti con contributo in conto capitale); categorie esenti da `F`; ripartizione a posteriori centralizzata dal GSE e decisione interna alla CER. I valori numerici (CAP, TP_base, `F = 1,25·g`) vanno presi dal tuo Cap. 3.5 e non li reintroduco io.

---

## 4. Estensione RQ-2 (dopo RQ-1)

**Che cosa si aggiunge al modello** (dettagli nel piano §11): funzioni di perturbazione dei profili, misure di forza incentivante (a) dispersione a parità di energia, (b) quota del guadagno marginale trattenuta, (c) sensibilità al consumo aggiuntivo nelle ore vincolate, strato di risposta con quota flessibile `φ`, fattori di emissione orari, Price of Fairness (ora definito).

**Che cosa si aggiunge all'articolo.** Opzione 1: seconda sezione dei risultati e una sezione di metodo (articolo più lungo). Opzione 2 (consigliata): secondo articolo o capitolo separato, citando RQ-1 come base.

**Condizioni di partenza (gate), da verificare a fine RQ-1:**
1. I risultati di RQ-1 sono stabili (cluster e rimpianto minimax non cambiano con nuovi semi).
2. Ho letto per intero Rodrigues et al. 2026 e si vede la differenza con la misura cross-famiglia di RQ-2 (Fase 3, §3.2).
3. C'è tempo per un modulo aggiuntivo con ipotesi esplicite di flessibilità (`φ`).
4. Le ancore di RQ-2 sono citate con la dichiarazione B.2: `gonzalezasenjo2025` #3 (household flexibility, multi-period coupling) e `gonzalezasenjo2026` (limite «ex post / fattori comportamentali»), **non** quelle sul nucleolo (#1–#2).

**Estensioni non decise.** Interazione con RQ-3 (quota ai produttori): nel modello `π` è già un parametro e un asse di scenario; se H5 risulta forte conviene una sezione dedicata.

---

## 5. Rischi, assunzioni e decisioni aperte

| ID | Rischio o decisione | Effetto | Che cosa serve |
|---|---|---|---|
| R1 | Sovrapposizione con Couraud 2025 e Limmer 2023 (non letti) | Novità ridotta ai punti 3–4 di §1.4 | Lettura integrale: sblocco dei domini di rete o PDF in `Paper/` |
| R2 | Dati sintetici: i risultati sui ranghi possono dipendere dal generatore | Validità esterna | Ripetere su profili misurati pubblici (Thames Valley Vision, ecc.) e dichiararlo |
| R3 | Il gioco del solo incentivo ignora l'opzione esterna del produttore (vendita, autoconsumo) | Gli indicatori di stabilità sono relativi a questo gioco | Dichiararlo; variante con valore di coalizione che include la vendita come analisi di robustezza |
| R4 | Indicatori circolari (distanza da Shapley/MC) | Favoriscono per costruzione le regole di riferimento | Blocco separato e analisi senza di essi |
| R5 | Perimetro: 13 regole × 13 indicatori × composizioni | Tempo di calcolo e di analisi | Piano a livelli di N (piano §7) |
| R6 | Il tuo titolo/obiettivi promettono ambientale ed engagement | Incoerenza con RQ-1 | §0, conseguenza 1 (restringere o impegnarsi su RQ-2) |
| R7 | Licenza Matlab: servono Optimization Toolbox (`linprog`) e Statistics and Machine Learning Toolbox (τ di Kendall, cluster) | Realizzabilità | Conferma dei toolbox disponibili al Politecnico |
| R8 | Parte del risultato è prevedibile: ogni nozione ha una regola «campione per costruzione» (EQ per l'uguaglianza, PH per la proporzionalità fisica, NUC per la stabilità), che vince sul proprio indicatore | Un revisore può dire che il risultato è ovvio | Spostare l'attenzione su ciò che non è ovvio: l'entità delle perdite delle regole non campioni sugli altri indicatori, le regole robuste (rimpianto minimax), le soglie di composizione e l'insieme minimo di indicatori; riportare dimensioni dell'effetto e non solo ranghi |
| D1 | Rivista bersaglio | Struttura e lunghezza | Scelta tua |
| D2 | Strato regolatorio italiano nei risultati principali o come caso studio separato | Complessità | Mia proposta: caso studio separato (Sez. 4.7) |
| D3 | Risoluzione temporale (oraria come da GSE, 15 minuti come variante) | Dimensione dei dati | Mia proposta: oraria come caso base |
| D4 | Se esiste accesso a RECON (ENEA) per generare configurazioni di CER coerenti con le regole GSE (usato da `cecini_tesi`) | Dati del caso studio | Verifica da parte tua |

---

## Appendice A — Bozza della motivazione del gap per §2.6 (italiano; da tradurre in inglese LaTeX)

*Bozza che segue la struttura della Parte A: paper recente → future work chiaro → base del gap → il lavoro risponde → estensione senza sostituire il gap. Citazioni verificate parola per parola sul PDF nella Fase 3. Formulazioni positive (B.3); il contesto italiano non compare (B.4).*

> Tra i confronti multi-metodo analizzati, `volpato2024b` confronta quattro regole (SW, Nash bargaining, Shapley, nucleolo) e le associa alle nozioni di fairness individuale, collettiva e proporzionale; come sviluppo futuro indica di “identify parameters that can quantitatively compare the different benefit distributions based on the "individual", "collective" and "proportional" fairness” (Sez. 4, p. 22). `dynge2025`, che valuta quattro indicatori in nove casi, osserva che “additional investigation is needed to refine fairness indicators” e aggiunge che “More concrete evaluation criteria could also be derived to perform a more generalisable and comprehensive evaluation of multiple fairness indicators” (Sez. 8, p. 12). `gasca2025` propone di esplorare “additional types of comparisons […] within the same framework, […] particularly for evaluating metrics beyond economic metrics” (Sez. 3.5, p. 12), e `cremers2023` osserva che “there are many other fairness concepts that could be explored in energy applications, and it would be relevant to compare their outcome to Shapley values” (Sez. 6, p. 13).
>
> Queste indicazioni convergono su un'esigenza non soddisfatta nei lavori analizzati: un insieme di indicatori quantitativi comuni, calcolati sulle stesse regole e sugli stessi dati, che renda confrontabili le nozioni di fairness e mostri se l'ordinamento delle regole dipende dalla nozione adottata. Questo lavoro risponde costruendo un banco di prova in cui regole di sei famiglie ripartiscono lo stesso incentivo orario, misurandole con indicatori di uguaglianza, proporzionalità al contributo fisico, stabilità e inclusione, e analizzando la concordanza dei ranghi al variare della composizione della comunità. L'estensione al comportamento dei membri (forza incentivante delle regole) è sviluppata separatamente e non sostituisce questo gap.

**Dichiarazioni B.2 da riportare nel testo:** `volpato2024b` ha due punti di future work (il primo, comunità più grandi con più unità energetiche, non è usato); `dynge2025` ha anche indicazioni sul dialogo interdisciplinare e sulla privacy, non usate; `gasca2025` ha sette punti e si usano solo quelli sulle comparazioni e sulle metriche non economiche; `cremers2023` ha quattro punti e si usa solo l'ultimo. Il contesto di `dynge2025` è il mercato locale P2P, non la CER.

**Da non scrivere:** «nessuno studio ha mai confrontato…» (B.3). Dopo la lettura integrale di Couraud 2025 e Limmer 2023 va rivista la frase «non soddisfatta nei lavori analizzati».

---

## Appendice B — Errata della Fase 3

1. §4 RQ-1, «Termini calcolabili»: il **Price of Fairness** va tolto (non calcolabile a torta fissa). Corretto nel file `gap_e_research_question.md`.
2. §4 RQ-2, «Termini calcolabili»: il Price of Fairness è definibile come perdita di `B` rispetto alla regola che massimizza `B`, solo con lo strato di risposta. Corretto.
3. §3.1 e §4 RQ-3: il nucleolo esatto è risultato calcolabile fino a N = 16 nel pilot Python (66–75 s), oltre il «N ≲ 14» indicato; il campionamento con somme cumulate arriva a N = 200 (piano §10).
