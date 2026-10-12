# Fase 4 (parte 2) — Piano del modello Matlab per RQ-1 (con modulo opzionale RQ-2)

**Stato:** piano di lavoro, non codice Matlab. **Data:** 12/10/2026. **Lingua:** italiano.
**File collegati:** `output/fase4_outline_imrad.md` (RQ-1 definitiva, outline dell'articolo), `output/gap_e_research_question.md` (Fase 3), `output/supporto_fase4/` (implementazione di riferimento in Python, test, istanza di verifica, pilot).

> **Avvertenza sulla verifica.** Nell'ambiente non c'è Matlab né Octave. Tutto ciò che è stato eseguito e verificato è l'**implementazione di riferimento in Python** (`output/supporto_fase4/pilot_engine.py`), con test automatici e un'istanza «golden» per confrontare il futuro codice Matlab. Il pseudo-codice di questo documento **non è stato eseguito**. Il pilot (§13) gira su profili sintetici inventati e con le mie definizioni: serve a verificare la fattibilità e a correggere il progetto, **non produce risultati della tesi**.

---

## 0. Scopo, perimetro e assunzioni

**Scopo.** Un modello che, per una comunità con `n` membri e profili orari di immissione e prelievo, (1) calcola l'incentivo orario sull'energia condivisa, (2) lo ripartisce con 13 regole di sei famiglie, (3) misura ogni ripartizione con indicatori di quattro nozioni di fairness, (4) analizza se e come il ranking delle regole cambia con la nozione e con la composizione (RQ-1, vedi `fase4_outline_imrad.md` §1).

**Che cosa non fa nel caso base.** Non modifica il comportamento dei membri (profili fissi), non ottimizza investimenti, non rappresenta mercati locali P2P, non usa dati di CER italiane operative.

| ID | Assunzione del caso base | Dove si allenta | Fonte / stato |
|---|---|---|---|
| A1 | Il valore da ripartire è `B = Σ_t c_t · e_t` con `c_t` costante (normalizzato a 1) | `c_t` orario (TIP, Eq. 32 di `cecini_tesi`) come variante | `[PAPER]` Eq. 32, p. 57 di `cecini_tesi` |
| A2 | Dispacciamento fisso: i profili sono esogeni, quindi `B` è uguale per tutte le regole | RQ-2 (strato di risposta) | `[INFERENZA]` coerente con C2/K8 della sintesi |
| A3 | `v(S)` è l'energia condivisa che la sola coalizione `S` produrrebbe | — | `[PAPER]` stessa definizione in `gonzalezasenjo2025`, p. 7 (a singolo slot) |
| A4 | Nessuna opzione esterna: `v({i}) = 0` per ogni `i` | Variante con vendita dell'eccedenza nel valore di coalizione | `[INFERENZA]` |
| A5 | Tutti i membri sono sotto la stessa cabina primaria: ogni sottoinsieme può costituire una CER | Costo fisso o dimensione minima delle coalizioni nei test di stabilità | Da verificare nel tuo Cap. 3 |
| A6 | Membri puri (produttori o consumatori) | Prosumer con immissione e prelievo nello stesso POD (§3.4) | Come in `cecini_tesi` Sim 1 |
| A7 | Vulnerabilità sintetica (flag assegnati) | Dati reali se disponibili | `marrasso2025` e `cecini_tesi` segnalano dati ISEE difficili da ottenere |
| A8 | Un anno, 8.760 ore (8.784 se bisestile, come in `cecini_tesi`) | Risoluzione a 15 minuti come variante | — |

---

## 1. Architettura

```
 dati ──► [profili] ──► [energia condivisa e gioco v(S)] ──► [regole] ──► premi R_i
 (sintetici o                 e_t, B, v(maschera)              13 regole      │
  misurati)                                                                   ▼
                                                  [indicatori] ◄──────────────┘
                                                       │
                                                       ▼
                       [esperimenti: scenari × repliche] ──► tabella lunga ──► [analisi del ranking] ──► figure, tabelle
```

**Struttura proposta del codice** (pacchetto `+cer`; i nomi sono indicativi):

| File / cartella | Funzione | Note |
|---|---|---|
| `config_default.m` | Struttura `cfg` con tutti i parametri (§2) e i livelli degli scenari (§7) | Salvata con ogni risultato, insieme all'hash del commit |
| `gen_profiles.m` | Generatore sintetico di archetipi (§8) con seme | Equivalente di `make_community` del riferimento Python |
| `load_profiles.m` | Lettura di profili misurati (CSV/MAT) in `inj`, `wd`, `meta` | |
| `net_pod.m` | Netting dei prosumer e aggregazione oraria | §3.4 |
| `shared_energy.m` | `e_t`, `B`, `SCR`, `SSR` | |
| `coalition_values.m` | Vettore `v` per tutte le coalizioni (maschera di bit), a blocchi | N ≲ 16–18 |
| `coalition_values_perm.m` | Valori dei prefissi di permutazioni con somme cumulate | Campionamento, N fino a 200 |
| `rules/rule_*.m` | Una funzione per regola: `R = rule_XX(com, aux, cfg)` | EQ, PA, PS, PH, PG, CT, EP, PF, SW, MC, SV, SVa, NUC |
| `rules/waterfill.m` | Water-filling esatto con ordinamento | |
| `indicators/ind_*.m` | Indicatori per gruppo; `gini.m`, `jain.m` | §5 |
| `analysis/` | `rank_matrix`, `tau_matrix`, `cluster_indicators`, `pareto_rules`, `minimax_regret`, `meta_regression`, `bootstrap_ci` | §6 |
| `experiments/run_experiment.m` | Cicli su scenari e repliche; risultati in tabella lunga | `parfor` sulle repliche |
| `validation/` | Test (`matlab.unittest`) e confronto con l'istanza golden | §9 |
| `plots/fig_*.m` | Una funzione per figura dell'articolo | Esportazione vettoriale |

**Toolbox necessari (da confermare sulla tua licenza):** Optimization Toolbox (`linprog`, con `lambda.ineqlin` per i moltiplicatori duali usati dal nucleolo); Statistics and Machine Learning Toolbox (τ di Kendall con `corr(…,'Type','Kendall')`, `linkage`, `cluster`, `tiedrank`); Parallel Computing Toolbox solo per `parfor`. Nella documentazione va controllato che `corr` con `'Kendall'` gestisca le parità come τ_b; in caso contrario si implementa τ_b a mano (poche righe).

**Riproducibilità.** Un seme per replica (`rng(seed,'twister')` o flussi indipendenti con `RandStream('Threefry')` dentro `parfor`); `cfg` e versione del codice salvati con ogni file di risultati; formato dei risultati identico a quello del riferimento Python, per il confronto.

**Formato dei risultati (tabella lunga, una riga per osservazione).** Colonne: `scenario_id`, `replica`, `regola`, `indicatore`, `valore`, `rango`; tabelle separate per i premi `R_i` (colonne `scenario_id`, `replica`, `regola`, `membro`, `premio`) e per i descrittori di composizione.

---

## 2. Notazione, variabili e parametri

**Insiemi e indici.** `i ∈ N = {1..n}` membri; `P` produttori, `C` consumatori (un prosumer sta in entrambi, §3.4); `t ∈ T` ore (`|T| = 8760`); `d` giorni; `S ⊆ N` coalizioni; `k` categorie (`NP` persone fisiche, `SME`, `OE` altri enti); `V ⊆ C` vulnerabili.

**Dati in ingresso (per replica)**

| Simbolo | Significato | Unità | Dimensione |
|---|---|---|---|
| `g_it ≥ 0` | Immissione del membro `i` nell'ora `t` (al punto di connessione) | kWh | `T × n` |
| `w_it ≥ 0` | Prelievo del membro `i` nell'ora `t` | kWh | `T × n` |
| `c_t` | Valore unitario dell'energia condivisa (€/kWh); costante = 1 nel caso base | €/kWh | `T × 1` |
| `role_i`, `type_i`, `vuln_i` | Ruolo (P/C), categoria (PR, NP, SME, OE), flag di vulnerabilità | — | `n` |

**Variabili derivate**

| Simbolo | Definizione |
|---|---|
| `G_t = Σ_i g_it`, `W_t = Σ_i w_it` | Immissione e prelievo totali |
| `e_t = min(G_t, W_t)` | Energia condivisa oraria |
| `B = Σ_t c_t e_t` | Valore totale da ripartire |
| `v(S) = Σ_t c_t · min(Σ_{i∈S} g_it, Σ_{i∈S} w_it)` | Valore della coalizione `S` (gioco) |
| `R_i` | Premio assegnato al membro `i` da una regola (`Σ_i R_i = B`) |
| `SCR = Σ_t e_t / Σ_t G_t`, `SSR = Σ_t e_t / Σ_t W_t` | Autoconsumo condiviso e autosufficienza condivisa |

**Parametri**

| Simbolo | Significato | Default | Intervallo di prova | Fonte |
|---|---|---|---|---|
| `π` | Quota di `B` ai produttori per le regole semplici | 0,4 | 0,2 · 0,4 · 0,6 | `[PAPER]` `cecini_tesi` (50% o 20% della quota non vincolata), `candela2022` (25%): scelti dagli autori (K7) |
| `γ = (γ_NP, γ_SME, γ_OE)` | Percentuali dei cluster di consumatori nella regola CT | (0,2; 0,5; 0,3) | ±0,1 | `[PAPER]` `cecini_tesi` Sez. 5.2, pp. 95–97 |
| `(n_q, q_cap)` | Quota riservata ai vulnerabili: `n_q` per vulnerabile, tetto `q_cap` | (0,02; 0,5) | 0,01–0,05; 0,3–0,5 | `[PAPER]` `campagna2024` (n% = 2% «arbitrarily set», tetto 50%) |
| `M` | Permutazioni per lo Shapley campionato | 500 | 50 · 100 · 500 · 2.000 | `cremers2023` (campionamento) |
| `tol` | Tolleranza per le coalizioni bloccanti | `1e-9·max(1, abs(v(N)))` | — | Scelta mia |
| `cut` | Soglia di distanza per i cluster di indicatori | 0,25 (τ̄ ≥ 0,5) | 0,2–0,35 | Scelta mia |
| `R` | Repliche per cella di scenario | 30 | 10–100 | Scelta mia |
| `B_boot` | Ricampionamenti bootstrap | 2.000 | — | Scelta mia |

---

## 3. Il gioco dell'energia condivisa

### 3.1 Definizione e proprietà

```
G_t = Σ_i g_it ;  W_t = Σ_i w_it ;  e_t = min(G_t, W_t) ;  B = Σ_t c_t e_t
v(S) = Σ_t c_t · min( Σ_{i∈S} g_it ,  Σ_{i∈S} w_it ) ,   v(∅) = 0 ,   v({i}) = 0 per i membro puro
```

Proprietà `[INFERENZA]`. Le prime due sono verificate numericamente nel riferimento Python; la terza è verificata a mano e sul gioco giocattolo della Fase 3:
- **Monotonia.** `v` non decresce aggiungendo membri (minimo di somme non negative), quindi i contributi marginali sono ≥ 0 e lo Shapley è ≥ 0.
- **Bilanciatezza.** `v` è la somma di giochi orari del tipo «minimo di due misure additive» (giochi di mercato a due lati): per Bondareva–Shapley il core è non vuoto. Nel pilot l'ε* del least core è ≤ 0 in tutte le istanze provate. `v` è anche un gioco di produzione lineare (Owen) con risorse `(g_it, w_it)`: il core contiene l'allocazione ottenuta con i prezzi duali orari, cioè con il lato scarso che prende l'ora, che è la regola **EP**; ne segue che EP sta nel core per costruzione; nel riferimento Python l'eccesso massimo di EP è ≤ 0 in tutte le istanze provate (test T9). Il riferimento teorico (Owen 1975) è esterno al corpus e va verificato. Letteratura sul core non vuoto nei giochi di condivisione dell'energia: arXiv:2311.18792 e HAL-02520203 `[WEB, non letti]`.
- **Lato scarso.** Con un solo produttore e offerta nettamente scarsa il core tende a ridursi al punto in cui il produttore prende tutto (gioco guanto 1+2: nucleolo `(1, 0, 0)`); con offerta abbondante il core ammette ripartizioni in cui i consumatori ricevono di più (Fase 3, Appendice B). Per `gonzalezasenjo2025` (p. 8) lo Shapley può non stare nel core: il controesempio è un gioco «guanto». È lo stesso gioco di cui `gonzalezasenjo2025` usa la versione a singolo slot: `v(S) = (p_b − p_s)·min(Σ e^NC, Σ e^NP)` (p. 7).

### 3.2 Calcolo di `v(S)` per tutte le coalizioni (N ≲ 16–18)
- Maschere di bit `m = 0..2^n−1`; matrice `bits` di dimensione `2^n × n`.
- Per blocchi di `chunk` coalizioni: `Gs = bits(blk,:) · g'` e `Ws = bits(blk,:) · w'` (`chunk × T`); `v(blk) = sum(min(Gs, Ws) .* c', 2)`.
- Accelerazioni: (i) tenere solo le ore con `G_t > 0` (fuori dalle ore di produzione `min = 0` per ogni coalizione): dimezza `T`; (ii) aggiornamento incrementale con ordine di Gray (un membro alla volta: `O(T)` per coalizione invece di `O(nT)`).
- Memoria: ≈ `2 · chunk · T · 8` byte per blocco (con `chunk = 1.024`, `T = 8.760`: 144 MB).

### 3.3 Calcolo senza enumerazione (N grande)
Per ogni permutazione dei membri si fanno somme cumulate lungo l'ordine di `g` e di `w` (`T × n`), si prende il minimo ora per ora e si somma su `T`: si ottengono i valori di tutti i prefissi in `O(Tn)`. Ripetuto per `M` permutazioni dà lo Shapley campionato (§4). Gli indicatori di stabilità a N grande si stimano su un insieme campionato di coalizioni (limite inferiore dell'eccesso massimo).

### 3.4 Prosumer
Un prosumer ha immissione e prelievo nello stesso punto: nel gioco entra con le sue due serie `g_i`, `w_i` aggregate ora per ora (come nel calcolo GSE, da confermare nel Cap. 3). Nelle regole per lato compare in entrambi i lati (peso di produttore da `g_i`, peso di consumatore da `w_i`); nelle regole `EQ` conta in entrambi gli insiemi. Negli indicatori il suo premio totale `R_i = R_i^P + R_i^C` è attribuito alla categoria del membro. Nel caso base non ci sono prosumer (come nella Sim 1 di `cecini_tesi`); la quota di prosumer è un fattore dello scenario (§7).

### 3.5 Strato regolatorio italiano (opzionale)
`TIP_t` orario (Eq. 32 di `cecini_tesi`), fattore `F` sulle immissioni di impianti con contributo in conto capitale e categorie esenti, quota vincolata oltre la soglia 55% (45% con contributo) riservata a consumatori non business e finalità sociali, spese della CER. I valori numerici vengono dal tuo Cap. 3.5. Nelle regole che non sono un albero (tutte tranne CT) il vincolo si applica con una maschera di eleggibilità sulla quota vincolata; per i giochi cooperativi la quota vincolata va trattata con un gioco a parte. È un'estensione: nel caso base `F = 0` e nessuna quota vincolata (§7, stadio D).

---

## 4. Regole di ripartizione

**Convenzioni.** `0/0 := 0`. Con `P` e `C` gli insiemi dei produttori e dei consumatori, `pot_P = π B`, `pot_C = (1 − π) B`. «Ore condivise» = `{t : e_t > 0}`. Le somme annue sono `g_i = Σ_t g_it`, `w_i = Σ_t w_it`; `g_i^S`, `w_i^S` le stesse somme sulle sole ore condivise.

### 4.1 Catalogo

| ID | Famiglia (Cap. 2.2) | Definizione | Parametri | Origine nel corpus | Costo |
|---|---|---|---|---|---|
| **SV** | 2.2.1 game-theoretic | Shapley esatto: `φ_i = Σ_{S⊆N∖{i}} s!(n−s−1)!/n! · [v(S∪{i}) − v(S)]`, con `s` numero di membri di `S` | — | `moncecchi2020`, `zatti2021`, `volpato2023/2024a/b`, `campagna2024`, `fioriti2021/2023`, `gasca2025`, `gonzalezasenjo2025/2026` | `O(2^n n)` dopo `v` |
| **NUC** | 2.2.1 | Nucleolo (LP iterativi: minimizza l'eccesso massimo, fissa le coalizioni con moltiplicatore duale positivo, ripete) | `tol` duale `1e-7` | `fioriti2021/2023`, `ferrucci2025` (variante), `volpato2024b`, `gonzalezasenjo2025/2026` | LP con `2^n − 2` vincoli |
| **MC** | 2.2.2 approssimazioni | Contributo marginale normalizzato: `m_i = v(N) − v(N∖{i})`, `R_i = B m_i / Σ_j m_j` | — | `casalicchio2022a/b`, `norbu2021a/b`, `cremers2023`, `cavalcante2025` (DMC-IV) | `O(n)` valutazioni di `v` |
| **SVa** | 2.2.2 | Shapley campionato con `M` permutazioni: media dei contributi marginali lungo le permutazioni | `M` | `cremers2023`, `alonsopedrero2024` (Nested), `norbu2021b` | `O(M n T)` con somme cumulate |
| **EQ** | 2.2.3 semplificate | `R_i = pot_P / #P` per `i ∈ P`; `R_i = pot_C / #C` per `i ∈ C` (`#X` = numero di elementi di `X`) | `π` | `gonzalezasenjo2025` (All Equal), `minuto2022` (SM1), `trevisan2022`, `berg2024` | `O(n)` |
| **PA** | 2.2.3 | Proporzionale alle quantità annue: `R_i = pot_P g_i / Σ_{j∈P} g_j` (produttori), `R_i = pot_C w_i / Σ_{j∈C} w_j` (consumatori) | `π` | `kachhad2024`, `berg2024`, `santos2025`, `marrasso2025` (parte tecnica) | `O(n)` |
| **PS** | 2.2.3 | Come PA ma con le somme sulle ore condivise: `g_i^S`, `w_i^S` | `π` | `cecini_tesi` «Proportional» (Sez. 4.2, p. 64) | `O(nT)` |
| **PH** | 2.2.3 | Pro-rata orario: `R_i = Σ_t c_t e_t [π g_it/G_t + (1 − π) w_it/W_t]` | `π` | `candela2022`, `trevisan2022/2024`, Eq. 34–35 di `cecini_tesi` (lato produttori), `gonzalezasenjo2026` (PTE) | `O(nT)` |
| **PG** | 2.2.3 | Progressiva (water-filling orario) sul lato consumo: ogni ora `a_it = min(w_it, λ_t)` con `Σ_i a_it = e_t`; `R_i = Σ_t c_t [π e_t g_it/G_t + (1 − π) a_it]` | `π` | `minuto2022` (SM2), `gianaroli2024` (M2), `cecini_tesi` (Layered), `campagna2024` (Packets), `giudice2026` | `O(nT log n)` |
| **CT** | 2.2.3 / 2.2.6 | Albero di categorie: produttori come PS con quota `π`; consumatori della categoria `k` ricevono `pot_C γ_k` ripartito dentro la categoria con `w_i^S`; se una categoria è vuota, la sua `γ_k` si ridistribuisce fra le categorie presenti | `π`, `γ` | `cecini_tesi` (Sez. 4.2 e 5.2), `candela2022`, `trevisan2022` | `O(nT)` |
| **EP** | 2.2.4 prezzi/tariffe | Lato scarso prende l'ora: `π_t = 1` se `G_t < W_t`, `0,5` se `G_t = W_t`, `0` altrimenti; `R_i = Σ_t c_t e_t [π_t g_it/G_t + (1 − π_t) w_it/W_t]` | — | `gonzalezasenjo2025` (Extreme Price) | `O(nT)` |
| **PF** | 2.2.5 performance-based | Chiave giornaliera di consumo: `ρ_id = corr_{t∈d}(w_it, G_t)` (0 se non definita), `ρ̃ = (1 + ρ)/2`, `k_id = ρ̃_id / Σ_{j∈C} ρ̃_jd`; `R_i = (1 − π) Σ_d B_d k_id` + lato produttori come PH; `B_d = Σ_{t∈d} c_t e_t` | `π` | `gianaroli2024` (M3, correlazione di Pearson giornaliera rimappata in [0,1]); `bilardo2025`, `giudice2026` (varianti) | `O(nT)` |
| **SW** | 2.2.6 multi-criteria/equità | Quota riservata ai vulnerabili: `s_V = min(q_cap, n_q · #V)`; `R_i = (1 − π)(1 − s_V) Σ_t c_t e_t w_it/W_t + 1[i∈V] · pot_C s_V w_i/Σ_{j∈V} w_j` per `i ∈ C`; produttori come PH | `π`, `n_q`, `q_cap` | `campagna2024` (EP + Proportional), `marrasso2025`, `fina2024`, `basilico2025` (PDM4) | `O(nT)` |

**Nota su PF.** La chiave `k_id` non dipende dal volume di consumo: con questa definizione, tratta dalla scheda di `gianaroli2024`, PF produce ripartizioni quasi egalitarie `[PILOT]`. È una proprietà della definizione, non un errore. Per rappresentare una regola «similarity × utilizzazione» alla `bilardo2025`, in cui il volume conta, si può aggiungere la variante PF2 con pesi `w_i ρ̃_id`. La rimappatura esatta di `gianaroli2024` va ricontrollata sul PDF prima dell'implementazione definitiva.

**Nota su AP.** L'«average price» di `gonzalezasenjo2025` coincide con PH a `π = 0,5` `[INFERENZA]`: non è una regola separata.

### 4.2 Regole escluse dal confronto e perché

| Regola | Motivo |
|---|---|
| Nash bargaining | Nel gioco del solo incentivo `v({i}) = 0`: con punti di disaccordo nulli coincide con la divisione in parti uguali fra tutti `[INFERENZA]` |
| Chiavi per proprietà o investimento | Servono dati di capitale; l'effetto è rappresentato dal parametro `π` e dalle percentuali di CT |
| Compensazione / non peggioramento | Banale qui (`v({i}) = 0`, premi ≥ 0); diventa rilevante con opzione esterna (variante A4) |
| Mercati locali (MMR, SDR, P2P) | Richiedono un altro gioco (risparmio dagli scambi con prezzi di rete): la famiglia 2.2.4 è rappresentata solo da regole di suddivisione tariffaria (EP, AP = PH a `π` = 0,5) |
| Prezzi discriminanti rawlsiani (`li2024`) | Richiedono prezzi e budget individuali |
| Chiavi con baseline dinamica (`giudice2026` completo) | Richiedono modelli di baseline; naturale per RQ-2 |

**Conseguenza per la RQ.** «Sei famiglie» va letto con questa riserva: la 2.2.4 è presente solo in forma tariffaria. Va dichiarato nel testo.

### 4.3 Casi limite (da testare)
Ore con `G_t = 0` o `W_t = 0` (nessun contributo, `0/0 := 0`); consumatore con consumo nullo nelle ore condivise (premio nullo in PS, PH, PG, SW); cluster vuoto in CT; tutti vulnerabili o nessun vulnerabile in SW; parità `G_t = W_t` in EP; membri identici (simmetria); giocatore nullo (non nel caso base); ordine dei membri (le regole non devono dipenderne).

---

## 5. Indicatori e KPI

### 5.1 Indicatori di fairness (orientati: valore più alto = migliore; rango 1 = migliore)

| ID | Gruppo (nozione) | Definizione | Distanza da una regola? | Regola campione per costruzione |
|---|---|---|---|---|
| E1 | Uguaglianza | `1 − Gini(R_C)`; `Gini = 2 Σ_k k x_(k) /(m Σ x) − (m+1)/m` sui `m` consumatori ordinati | No | EQ |
| E2 | Uguaglianza | Jain: `(Σ x)² /(m Σ x²)` su `R_C` | No | EQ |
| E3 | Uguaglianza | MinMax: `min R_C / max R_C` | No | EQ |
| E4 | Uguaglianza del tasso | `1 − Gini(R_i / w_i)` sui consumatori (premio per kWh consumato) | No | PA |
| S3 | Garanzia minima | `min_i R_i / B` (margine di razionalità individuale con `v({i}) = 0`) | No | EQ |
| P1c | Proporzionalità fisica (consumatori) | `1 − ½ Σ_{i∈C} abs(R_i/R_C − q_i^C)`, con `q_i^C = Σ_t e_t w_it/W_t / Σ_t e_t` | No | PH (è la definizione di `q`) |
| P1p | Proporzionalità fisica (produttori) | Come P1c con `q_i^P = Σ_t e_t g_it/G_t / Σ_t e_t` | No | PH, PG, PF, SW (stessa formula sul lato produttori) |
| S1 | Stabilità di gruppo | `−ε_max / B`, `ε_max = max_{S≠∅,N} [v(S) − R(S)]` (≤ 0: nel core) | No | NUC (minimizza `ε_max` per definizione) |
| S2 | Stabilità di gruppo | `1 −` quota di coalizioni con `v(S) − R(S) > tol` | No | Qualunque allocazione nel core (NUC, EP) |
| Q1 | Inclusione | `(quota di R_C alle persone fisiche) / (quota di consumatori persone fisiche)` | No | Dipende dalla composizione (EQ se le persone fisiche sono i consumatori piccoli) |
| Q2 | Inclusione | Stessa cosa per i vulnerabili | No | SW per costruzione sui vulnerabili; EQ se sono piccoli |
| Q1′, Q2′ | Inclusione rispetto al contributo | Come Q1, Q2 ma con la quota di `q^C` fisica al posto della quota di teste | No | PH |
| D_MC | Distanza dal contributo marginale | `−½ Σ_i abs(R_i/B − m_i/Σ m)` | **Sì** (da MC) | MC |
| D_SV | Distanza dallo Shapley | `−½ Σ_i abs(R_i − φ_i) / B` | **Sì** (da SV) | SV |

**Campioni per costruzione.** Quasi ogni indicatore ha una regola che lo ottimizza per definizione (colonna a destra). Il risultato di RQ-1 non è che il campione vinca sul proprio indicatore, ma come si piazzano le altre regole sugli altri indicatori e se esiste una regola che non perde troppo su nessuno (rimpianto minimax). Gli indicatori che sono una **distanza da una regola** (D_MC, D_SV) sono tautologici per quella regola e vengono sempre riportati in un blocco a parte; le analisi vanno ripetute senza.

**Descrittore (non indicatore).** `π_eff = Σ_{i∈P} R_i / B`: quota effettiva ai produttori.

**Indicatori tolti rispetto alla Fase 3.** Price of Fairness (non calcolabile a torta fissa: tutte le regole distribuiscono `B`). Il pilot ha anche mostrato che P1p (proporzionalità fisica lato produttori) discrimina poco: va letto come descrittore di lato.

**Gruppi per l'analisi.** Uguaglianza (E1–E4), Garanzia minima (S3), Proporzionalità fisica (P1c, P1p), Stabilità di gruppo (S1, S2), Inclusione (Q1, Q2, Q1′, Q2′), Basati su riferimento game-theoretic (D_MC, D_SV: analisi sempre ripetuta senza di essi). Nel pilot S3 si comporta come un indicatore di uguaglianza (τ̄ = 0,76 con E3) e non come uno di stabilità: la classificazione a priori e i cluster empirici vanno confrontati (RQ1.c).

### 5.2 KPI per dimensione

| Dimensione | KPI | In RQ-1? | Note |
|---|---|---|---|
| **Economica** | `B` (€/anno); `R_i` (€/anno); premio per kWh `R_i/w_i`; premio per kWp dei produttori; quantili dei premi per categoria; `π_eff` | Sì | Le cifre assolute dipendono da `c_t`; gli indicatori sono scale-free |
| **Sociale** | Q1, Q2, Q1′, Q2′; quota alle persone fisiche; indici di uguaglianza | Sì | Vulnerabilità sintetica (A7) |
| **Ambientale** | `SCR`, `SSR`; CO2 evitata `Σ_t EF_t e_t` se esistono fattori orari | Sì, **come contesto** | Identici per tutte le regole con dispacciamento fisso: **non discriminano** (Fase 3, §6 punto 3); riportati una volta per scenario |
| **Engagement** | Nessuno in RQ-1 | No | Solo attributi di praticità: tempo di calcolo, numero di parametri liberi, dati richiesti (contatore individuale orario; valori di coalizione); la forza incentivante è di RQ-2 |

---

## 6. Analisi del ranking (nucleo di RQ-1)

Per ogni cella di scenario `s` e replica `r` si ha la matrice `X^{s,r}` (regole × indicatori, orientata).

1. **Ranghi.** `tiedrank` su `−X` per colonna: rango 1 = miglior valore; parità = rango medio.
2. **Concordanza fra indicatori.** `τ_b` fra ogni coppia di colonne (13 regole per colonna). Statistiche per cella: τ medio fra coppie; quota di coppie con τ < 0; quota con τ > 0,8; W di Kendall fra indicatori (complessivo e dentro i cluster). Intervalli di confidenza: bootstrap sulle repliche (`B_boot` = 2.000).
3. **Cluster di indicatori.** Distanza `(1 − τ̄)/2` fra indicatori (τ̄ medio sulle celle); `linkage(…,'average')` e taglio a `cut`. Si riporta il dendrogramma e la stabilità dei cluster fra celle (indice di Rand corretto).
4. **Insieme minimo.** Un rappresentante per cluster (massimo τ̄ medio con gli altri membri del cluster). Si calcola il τ fra il Borda a pesi di cluster uguali e il Borda dei soli rappresentanti; obiettivo ≥ 0,8; verifica leave-one-scenario-out.
5. **Regole robuste.** Ranghi per cluster (media dei ranghi degli indicatori del cluster); (a) insieme di Pareto sui ranghi per cluster; (b) rimpianto minimax `min_r max_k (rango_k(r) − 1)`; (c) probabilità di stare fra le prime tre in ogni cluster. Si riportano sempre anche i valori (non solo i ranghi) per vedere i margini.
6. **Effetto della composizione.** (a) Stabilità del ranking di ogni indicatore fra celle (τ fra i vettori di rango medio); (b) meta-regressione della concordanza di cella su descrittori `[SCR, σ_consumi, corr(W_t,G_t), HHI dei produttori, quota di persone fisiche, N]` (regressione lineare con interazioni e, come controllo, foresta casuale con dipendenza parziale); (c) ricerca di soglie (per esempio il PV/carico in cui cambia l'ordine di SV e NUC su S1).
7. **Sensibilità.** `π`, `c_t` costante o orario, risoluzione oraria o a 15 minuti, definizione dell'insieme dei consumatori con i prosumer, frazione di vulnerabili, `M` del campionamento, `cut` dei cluster.
8. **Robustezza agli indicatori circolari.** Ogni punto sopra ripetuto con e senza D_MC e D_SV.

**Che cosa misurano gli intervalli di confidenza.** Il bootstrap sulle repliche riflette la sola variabilità del generatore (semi dei profili sintetici), non l'incertezza sui dati reali né sulle definizioni delle regole: va detto nei limiti.

**Uscite:** tabelle (τ, cluster, rappresentanti, rimpianto) e le Fig. 4–9 dell'outline.

---

## 7. Scenari e piano sperimentale

**Caso base B0.** `n = 12`: 3 produttori (quote di kWp 45/35/20%) e 9 consumatori: 5 persone fisiche (4 famiglie con picco serale, 1 con consumo diurno; 2 vulnerabili), 3 PMI (ufficio, negozio, industria leggera), 1 altro ente (scuola); consumo totale ≈ 160 MWh/anno; PV/carico = 1,0; `π` = 0,4; eterogeneità log-normale σ = 0,3; 8.760 ore. Ordine di grandezza confrontabile con la Sim 1 di `cecini_tesi` (12 POD; 137.889 kWh/anno di prelievo, 114.085 kWh/anno di immissione, somme mie dalla Tab. 2).

| Fattore | Livelli | Note |
|---|---|---|
| F1 PV/carico (generazione annua / consumo annuo) | 0,5 · 1,0 · 1,5 | Scarsità e abbondanza; nel pilot SCR da 0,70 a 0,33 |
| F2 Eterogeneità dei consumi σ | 0,3 · 1,0 | Log-normale con totale fissato |
| F3 Sincronismo | serale · bilanciato · diurno | Pesi relativi dei profili; nel pilot corr(carico, PV) 0,14–0,35 |
| F4 Produttori | 1 · 3 equi · 3 concentrati (60/30/10) | Concentrazione |
| F5 Persone fisiche | 5% · 8% (base) · 30% del consumo | Q1, Q2 |
| F6 N | 8 · 12 · 16 (esatti); 50 · 100 (solo campionamento) | §10 |
| F7 `π` | 0,2 · 0,4 · 0,6 | Regole semplici |
| F8 `c_t` | costante · TIP orario | Strato regolatorio parziale |
| F9 Risoluzione | oraria · 15 minuti | |
| F10 Prosumer | 0% · 25% · 50% delle famiglie con PV | §3.4 |
| F11 Strato regolatorio | spento · `F` e quota vincolata | Stadio D |

**Stadi**

| Stadio | Contenuto | Numero di run | Tempo stimato (proxy Python) |
|---|---|---|---|
| A | Fattoriale completo F1 × F2 × F3 a `N = 12` (18 celle × `R = 30`) | 540 | circa 1 ora |
| B | Un fattore alla volta intorno a B0 (F4, F5, F7, F8, F9, F10; `N` = 8, 16), `R = 30` | circa 450 + 30 a `N = 16` | circa 1–1,5 ore (`N` = 16: ordine di 100 s per run, stima = nucleolo 66–75 s + valori 9–13 s + resto; il run completo a `N` = 16 non è stato misurato) |
| C | Grandi comunità `N = 50, 100`, solo regole campionabili (SV → SVa; senza NUC), indicatori di stabilità campionati, `R = 10` | 20 | pochi minuti |
| D | Strato regolatorio italiano su B0 e sulle celle di A più informative | circa 100 | da stimare |

I tempi sono del riferimento Python (§10): su Matlab saranno diversi, ma dello stesso ordine. Gli stadi sono parallelizzabili sulle repliche.

---

## 8. Dati

**Specifica del generatore sintetico (riferimento: `make_community` e `load_profile` in `pilot_engine.py`).**
- *PV unitario (per kWp):* irradianza da altezza solare a 45° di latitudine, fattore di nuvolosità giornaliero (Beta) con stagionalità, rumore orario; normalizzato a 1.250 kWh/kWp/anno. Per la tesi va sostituito con serie orarie PVGIS (JRC), già citato in 16 schede; scelta di località, anno e database da fare.
- *Archetipi di carico:* famiglia con picco serale, famiglia con consumo diurno, ufficio (lun–ven 8–18), negozio (9–20), scuola o ente pubblico (lun–ven 8–16, calo estivo), industria leggera; ciascuno con stagionalità, rumore orario e giornaliero log-normale, normalizzato al consumo annuo.
- *Composizione:* produttori con quote di kWp; consumatori con consumo annuo da lista, scalato da un fattore log-normale con σ e totale fissato.
- Tutti i profili sono **inventati**: servono a controllare il modello, non a rappresentare comunità reali.

**Dati reali o semi-reali da valutare (da confermare con te)**

| Uso | Fonte nel corpus | Limiti |
|---|---|---|
| Carichi di famiglie misurati | Thames Valley Vision (`norbu2021a/b`, `cremers2023`): 200 famiglie, 30 minuti, 1 anno | Non italiani; disponibilità e licenza da verificare |
| Carichi sintetici di famiglie | LoadProfileGenerator (`alonsopedrero2024`, `casalicchio2022a/b`) | Sintetici |
| Tariffe, profili e valori ARERA | 16 schede | Dipende dal tipo di dato |
| Produzione PV | PVGIS (16 schede) | Scelta di località e anno |
| PMI e altri enti italiani | Nessun dato misurato nel corpus | Resta il generatore sintetico: va dichiarato |
| Fattori di emissione orari | `ceglia2022` (p. 15); media nazionale ISPRA in `cutore2023` | Fonte della serie oraria da verificare; serve solo come contesto o per RQ-2 |
| Configurazioni di CER coerenti con le regole GSE | RECON (ENEA), usato da `cecini_tesi` | Accesso da verificare |
| Dati di CER operative (GSE) | Nessuno nel corpus | Non disponibili: nessuna validazione su CER reali |

**Gestione.** Unità kWh/ora e €/kWh; un file per scenario con `inj`, `wd`, metadati e seme; nessun dato con licenza restrittiva nel repository.

---

## 9. Verifica e validazione

| ID | Test | Criterio | Stato nel riferimento Python |
|---|---|---|---|
| V1 | Efficienza di tutte le regole | `abs(Σ R − B) ≤ 1e-9 B` | Superato (13 regole) |
| V2 | Simmetria: membri identici ricevono lo stesso premio nelle regole simmetriche | Differenza ≤ `1e-9 B` | Superato per SV e NUC |
| V3 | Forme chiuse: gioco guanto 1+2 a offerta scarsa: Shapley `(2/3, 1/6, 1/6)`, nucleolo `(1, 0, 0)`; offerta abbondante: Shapley `(1, 1/2, 1/2)` | Esatto entro `1e-6` | Superato |
| V4 | PH, lato produttori, coincide con i pesi di Eq. 34–35 di `cecini_tesi` | Uguaglianza dei pesi normalizzati | Superato |
| V5 | Il nucleolo sta nel core (eccesso massimo ≤ 0); `ε*` del least core ≤ 0 (gioco bilanciato) | Tolleranza `1e-6 v(N)` | Superato |
| V6 | Convergenza dello Shapley campionato verso l'esatto; efficienza esatta | Errore L1 relativo < 3% con 4.000 permutazioni | Superato (1,2%) |
| V7 | Confronto Matlab–Python sull'istanza golden (`output/supporto_fase4/golden/`) | Errore relativo ≤ 1e-9 (regole deterministiche, SV, MC); ≤ 1e-6 (NUC); SVa con le permutazioni fornite | Da fare in Matlab |
| V8 | Replica della Tab. 1 di `gonzalezasenjo2025` (otto metodi × sette proprietà) su istanze a singolo slot, con le definizioni delle Sez. 2.3–2.4 e dell'Appendice A | Stesso schema Sì/No; per il nucleolo i tre «?» restano aperti | Da fare per le altre colonne: servono le definizioni esatte dal PDF. Controllo parziale già superato (T11): Shapley e Average Price (PH a `π` = 0,5) fuori dal core, Extreme Price (EP) nel core, come nella colonna P7 della Tab. 1; il modello di `gonzalezasenjo2025` ha `v(S)` uguale al nostro con la posizione netta di ciascun membro (Sez. 2.2) |
| V9 | Coerenza fra risoluzioni: aggregando a 15 minuti `v` e premi non cambiano oltre la tolleranza di aggregazione | Da definire | Da fare |
| V10 | Test unitari degli indicatori su casi calcolabili a mano e su regole campione (Gini; E1–E3 per EQ; P1c e P1p per PH; E4 per PA; `π_eff`) | Esatto entro `1e-9` | Superato (T10); mancano S1 e S2 su casi a mano |
| V11 | Indipendenza dall'ordine dei membri | Premi permutati allo stesso modo | Da fare |

**Istanza golden.** `output/supporto_fase4/golden/`: `N = 6` (2 produttori + 4 consumatori), 168 ore, profili sintetici con seme 2026, `π` = 0,4, `γ` = (0,2; 0,5; 0,3), 24 permutazioni fisse per SVa. File: `golden_inj.csv`, `golden_wd.csv`, `golden_meta.json`, `golden_perms_0based.csv` (indici da 0), `golden_values_v_by_mask.csv` (`v` per maschera: bit `i` = membro `i+1`), `golden_rewards.csv` (13 regole × 6 membri), `golden_indicators.csv` (13 regole × 14 colonne). Ricostruibile con `make_golden.py`.

---

## 10. Prestazioni e fattibilità

**Tempi del riferimento Python (numpy/scipy, 8.760 ore; indicativi per Matlab).** Dalle esecuzioni di `output/supporto_fase4/pilot_timing.py` (l'ultima è salvata in `pilot_timing_output.txt`):

| `N` | Valori `v(S)` di tutte le coalizioni | Shapley da `v` | Least core (LP) | Nucleolo (LP iterativi) |
|---|---|---|---|---|
| 8 | 0,1–0,2 s | < 0,01 s | < 0,1 s | ≤ 0,1 s |
| 10 | 0,9–1,3 s | < 0,01 s | < 0,1 s | 0,1 s |
| 12 | 0,4–1,6 s | < 0,01 s | < 0,1 s | 1,0–1,3 s |
| 14 | 2,3–3,2 s | ≤ 0,01 s | 0,2 s | 1,1–1,7 s |
| 16 | 8,9–13,0 s | 0,02–0,03 s | 0,8–1,3 s | 66,3–74,8 s |
| 18 | 37,5–47,8 s | 0,14–0,15 s | 7,9–9,4 s | non provato |

Shapley campionato con somme cumulate (500 permutazioni): `N` = 50: 5,4–6,3 s; `N` = 100: 10,3–12,3 s; `N` = 200: 25,8–29,3 s.

Gli intervalli sono il minimo e il massimo delle misure fatte sulla stessa macchina: tre esecuzioni di `pilot_timing.py` (la prima senza `N` = 18 e senza nucleolo a `N` = 16) e, per `N` = 16 e 18, una misura separata con lo stesso motore. Dunque ogni cella poggia su tre misure (quattro per i valori `v(S)` a `N` = 16), salvo il campionato (tre). Fra un'esecuzione e l'altra i tempi variano fino a un fattore 4 nelle celle sotto i 2 s (`N` = 12: 0,4–1,6 s) e di un fattore 1,3–1,5 in quelle grandi. In tutte le istanze provate `ε*` del least core è negativo (core non vuoto).

**Letture per il progetto**
- Il caso base `N = 12` è molto leggero (valori di coalizione ~1 s, nucleolo ~1 s): le repliche e gli scenari degli stadi A–B sono praticabili sul tuo portatile.
- Il nucleolo esatto è praticabile fino a `N = 16` (un minuto circa); sopra, serve generazione di vincoli (come `ferrucci2025`) o si usa il solo least core.
- Lo Shapley campionato con somme cumulate scala a centinaia di membri; è quello da usare allo stadio C.
- In Matlab: vettorizzare per blocchi, ridurre `T` alle ore con `G_t > 0`, usare Gray code se il costo dei valori di coalizione domina, controllare l'algoritmo di `linprog` disponibile nella tua versione.

---

## 11. Modulo opzionale RQ-2 (dopo RQ-1)

**Nuove funzioni:** `perturb_profiles.m` (sposta energia di un membro fra insiemi di ore preservando l'energia annua); `incentive_strength.m` (misure (a), (b), (c) della Fase 3, §3.2); `response_layer.m` (quota flessibile `φ` che si sposta in risposta a `ι_i`, punto fisso fra membri); `emission_factors.m`; `price_of_fairness.m` (perdita di `B` rispetto alla regola che massimizza `B`, definita solo con lo strato di risposta).

**KPI aggiunti.** Forza incentivante per regola; `ΔE_sh`, `ΔB`, ΔCO2 sotto ipotesi di flessibilità; Price of Fairness; robustezza delle proprietà (efficienza, razionalità individuale, stabilità) sotto risposta.

**Dati aggiuntivi.** Quota flessibile per archetipo (assunzioni esplicite); fattori di emissione orari.

**Condizioni (gate):** vedi `fase4_outline_imrad.md` §4. **Rischio principale:** Rodrigues et al. 2026 `[WEB, non letto]` (Fase 3, §3.2).

---

## 12. Piano di implementazione

| ID | Pietra miliare | Consegna e criterio di accettazione | Impegno (mia stima `[INFERENZA]`) |
|---|---|---|---|
| M0 | Decisioni e ambiente | `cfg`, scheletro delle cartelle, toolbox confermati, scelta dei dati | S |
| M1 | Nucleo del gioco | `gen_profiles`, `shared_energy`, `coalition_values`, SV, MC; V1, V3 | M |
| M2 | Regole semplici | EQ, PA, PS, PH, PG, CT, EP, PF, SW; V1, V2, V4 | M |
| M3 | Soluzioni cooperative | NUC (LP iterativi), SVa con somme cumulate; V5, V6 | M |
| M4 | Indicatori | Tutti gli indicatori; confronto con l'istanza golden (V7), V10 | M |
| M5 | Esperimenti | `run_experiment`, scenari, tabella lunga, parallelizzazione | M |
| M6 | Analisi | τ, cluster, rappresentanti, Pareto, rimpianto minimax, meta-regressione, bootstrap | M |
| M7 | Sensibilità e scala | Stadi B–C, V8, V9, V11 | M |
| M8 | Strato regolatorio e figure | Stadio D e figure dell'articolo | M–L |
| M9 | Modulo RQ-2 | Solo dopo il gate | L |

Legenda: S ≲ 2 giorni, M ≈ 1 settimana, L ≳ 2 settimane di lavoro. Sono stime mie, non misurate.

**Prossimi passi concreti (prime due settimane)**
1. Decidere il perimetro: titolo e obiettivi ristretti a «economic and social (distributive) outcomes», oppure RQ-2 come impegno con punto di decisione (`fase4_outline_imrad.md` §0).
2. Rendere leggibili i lavori online che pesano di più su RQ-1 (Couraud et al. 2025, Limmer 2023; poi Rodrigues et al. 2026): sblocco dei domini di rete o PDF in `Paper/`.
3. Confermare i toolbox Matlab disponibili e la versione.
4. Scegliere i dati: generatore sintetico come base, PVGIS per la produzione, un dataset pubblico di carichi per la verifica di robustezza.
5. Implementare M1 e M2 in Matlab e far passare V1–V4 e il confronto con l'istanza golden (V7) sulle regole semplici.

---

## 13. Pilot di fattibilità in Python `[PILOT]`

**Che cosa è.** `output/supporto_fase4/`: `pilot_engine.py` (profili sintetici, gioco, 13 regole, indicatori), `test_engine.py` (test T1–T11: V1–V6, V10, controllo di Eq. 34–35, categoria vuota di CT, EP nel core, coerenza con la colonna P7 di `gonzalezasenjo2025`), `pilot_run.py` (24 run: PV/carico {0,5; 1,0; 1,5} × σ {0,3; 1,0} × 4 semi), `pilot_run2.py` (composizione: PV/carico × mix × σ, 3 semi per cella; effetto di `π`), `pilot_timing.py`, `make_golden.py`, `run_all.sh`. Output salvati negli stessi file `*_output.txt`. Il test T7 conferma che il lato produttori di PH coincide con i pesi di Eq. 34–35 di `cecini_tesi`.

**Che cosa mostra (profili inventati e mie definizioni: nessuno di questi numeri è un risultato della tesi).**
- La pipeline completa funziona (13 regole × 13 indicatori × 24 run in 85 s nell'ultima esecuzione).
- τ medio fra indicatori ≈ 0,03; il 54% delle coppie ha τ medio < 0 e l'8% > 0,8: i ranghi sono in larga parte non concordi.
- Cluster di indicatori (soglia `cut` = 0,25): {E1, E2, E3, S3, Q1, Q2} (uguaglianza, garanzia minima, inclusione); {E4} (uguaglianza del tasso); {P1c, S1, S2, e D_MC} (proporzionalità fisica e stabilità); {P1p}; {D_SV}. Il primo cluster è associato negativamente al terzo (τ̄ da −0,4 a −0,7 fra le coppie di indicatori).
- Rimpianto minimax (rango medio per cluster − 1, massimo sui cluster): PG 6,1; EP 7,5; PH 8,1; … NUC 11,6; EQ 12,0. Rango medio sui cluster: PG 4,4. Un rappresentante per cluster ricostruisce il Borda a pesi di cluster uguali con τ = 0,85–0,90.
- Composizione: τ medio fra indicatori nella stessa cella 0,06; stabilità del ranking di uno stesso indicatore fra celle 0,63–0,95 (minimo 0,19). Nel pilot la nozione conta molto più della composizione.
- `π` non cambia i ranghi su E1 e P1c; cambia quelli su S1 e S3.
- Tempi: §10.

**Che cosa ha cambiato nel progetto**
1. Il Price of Fairness è stato tolto da RQ-1 (non calcolabile).
2. S3 (garanzia minima) è stato separato dalla stabilità di gruppo (si comporta come uguaglianza).
3. P1p (proporzionalità fisica lato produttori) discrimina poco, perché le regole con lo stesso lato produttori pareggiano: resta nell'elenco ma va letto come descrittore di lato.
4. E4 (uguaglianza del tasso) si è rivelato non ridondante con E1–E3 (τ̄ da −0,12 a −0,26).
5. Il Nash bargaining è escluso per via analitica (collasso nell'uguaglianza), non per effetto del pilot.
6. D_MC e D_SV sono confinati in un blocco a parte; ogni indicatore ha una regola campione per costruzione (§5.1).
7. PF è risultato quasi egalitario per definizione: da aggiungere la variante PF2 (§4.1).

**Limiti del pilot.** Profili e composizioni inventati; una sola struttura di comunità (3 produttori + 9 consumatori); poche celle e pochi semi; regole definite da me a partire dalle schede; nessuna incertezza stimata; nessun prosumer; nessun strato regolatorio. I risultati sui ranghi dipendono in parte dalle definizioni (per esempio PH vince P1c per costruzione, MC vince D_MC): per questo l'analisi senza indicatori circolari.

---

## 14. Rischi tecnici e mitigazioni

| Rischio | Effetto | Mitigazione |
|---|---|---|
| Nucleolo degenere o duali diversi fra solutori (HiGHS in Python, `linprog` in Matlab) | Cicli o soluzioni diverse | Confronto su golden e su istanze casuali; tolleranza duale regolabile; in caso di problemi, least core con scelta della soluzione |
| Costo di memoria `2^n × T` | Fuori memoria a N = 18 | Blocchi, Gray code, ore con `G_t > 0`, `single` se serve |
| Indicatori indefiniti (divisione per zero, `max R = 0`) | NaN nei ranghi | Convenzioni esplicite (§4.3); test dedicati |
| Ranghi con molte parità | τ_b instabile | `tiedrank`; riportare anche valori; soglia sulle differenze minime |
| Dipendenza dal generatore sintetico | Validità esterna | Ripetizione su profili misurati pubblici; confronto di due generatori |
| Troppe celle | Tempo di analisi | Stadi A–D; `R` ridotto in B–D |
| Differenze fra definizioni di PF, SW, CT nelle fonti e nel codice | Risultati non comparabili con i paper | Documentare ogni definizione e citare la fonte; ricontrollare i PDF prima della versione definitiva |
| Matlab non verificato qui | Errori di sintassi o di versione | Test e golden fin dal primo giorno |

---

## Appendice A — Pseudo-codice (non eseguito)

```
% valori di coalizione per blocchi (N <= 16-18)
bits = double(bitget(uint32((0:2^n-1)'), 1:n));          % 2^n x n
v = zeros(2^n,1);
for blk = blocks(2^n, chunk)
    Gs = bits(blk,:) * g';  Ws = bits(blk,:) * w';        % chunk x T
    v(blk) = sum( min(Gs, Ws) .* c', 2 );
end

% Shapley esatto da v
for i = 1:n
    no  = find(bitget(idx,i) == 0);                       % coalizioni senza i
    phi(i) = sum( wgt(popcount(no)+1) .* (v(no + 2^(i-1)) - v(no)) );
end                                                       % wgt(s+1) = s!(n-s-1)!/n!, s = cardinalità di S

% Shapley campionato con somme cumulate (N grande)
for m = 1:M
    perm = randperm(n);
    cg = cumsum(g(:,perm),2);  cw = cumsum(w(:,perm),2);
    vp = sum( min(cg,cw) .* c, 1 );                       % valori dei prefissi
    phi(perm) = phi(perm) + diff([0, vp]);
end
phi = phi / M;

% nucleolo: LP iterativi (Kopelowitz / Maschler-Peleg-Shapley)
fissi = {efficienza};
repeat
    [x,eps,lambda] = linprog(f, A_ub, b_ub, A_eq, b_eq);  % min eps  s.t.  x(S)+eps >= v(S)
    S_star = find(abs(lambda.ineqlin) > 1e-7);            % vincoli essenziali
    aggiungi uguaglianze  x(S) = v(S) - eps  per S in S_star; rimuovi S_star dai vincoli
until rank(uguaglianze) == n
```

---

## Appendice B — Configurazione di esempio (struttura `cfg`)

```
cfg.n          = 12;           cfg.T = 8760;       cfg.c_t = 'const';       % oppure 'tip'
cfg.pi         = 0.4;          cfg.gamma = [0.2 0.5 0.3];
cfg.vuln       = struct('n_q',0.02,'q_cap',0.5);
cfg.pv_to_load = 1.0;          cfg.sigma = 0.3;    cfg.mix = 'balanced';
cfg.M          = 500;          cfg.tol = 1e-9;     cfg.cut = 0.25;
cfg.R          = 30;           cfg.seed0 = 1000;   cfg.B_boot = 2000;
cfg.rules      = {'EQ','PA','PS','PH','PG','CT','EP','PF','SW','MC','SV','SVa','NUC'};
cfg.indicators = {'E1','E2','E3','E4','S3','P1c','P1p','S1','S2','Q1','Q2','D_MC','D_SV'};
```

---

## Appendice C — Corrispondenza con il riferimento Python

| Elemento | Nel riferimento Python | Nel modello Matlab |
|---|---|---|
| Valore unitario | `c_t = 1` | `c_t` costante o TIP orario |
| Prosumer | Assenti | Netting e doppio ruolo (§3.4) |
| CT con cluster vuoto | Ridistribuisce `γ_k` fra le categorie presenti (test T8) | Come in §4.1 |
| Water-filling | Bisezione (60 iterazioni) | Algoritmo esatto con ordinamento |
| Nucleolo | `scipy.optimize.linprog` con HiGHS | `linprog` |
| Campionamento | Permutazioni da un generatore o fornite (`golden_perms_0based.csv`) | Permutazioni fornite per il confronto; `randperm` per le prove |
| Indicatori | 13 + `pi_eff` | Gli stessi, più Q1′, Q2′ |
