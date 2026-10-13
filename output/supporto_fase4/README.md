# supporto_fase4 — implementazione di riferimento in Python e pilot di fattibilità

**Che cosa è.** Un'implementazione semplificata, in Python (numpy e scipy), del modello previsto in Matlab per RQ-1: gioco dell'energia condivisa, 13 regole di ripartizione, indicatori, analisi di concordanza dei ranghi. Serve a: (1) stimare i tempi di calcolo, (2) verificare che la pipeline di analisi funzioni, (3) avere un'implementazione indipendente con cui confrontare il codice Matlab (istanza `golden/`).

**Che cosa non è.** Non è il modello della tesi. I profili sono **inventati** (generatore sintetico), le regole sono definite da me a partire dalle schede, non ci sono prosumer né strato regolatorio, e i numeri prodotti dal pilot **non sono risultati della tesi**. Il piano del modello è in `../fase4_piano_modello_matlab.md`; l'outline dell'articolo in `../fase4_outline_imrad.md`.

**Requisiti.** Python 3 con numpy e scipy. Nessun'altra dipendenza.

## File

| File | Contenuto |
|---|---|
| `pilot_engine.py` | Profili sintetici, valori di coalizione, Shapley esatto e campionato, contributo marginale, nucleolo (LP iterativi), least core, 13 regole, indicatori |
| `test_engine.py` | Test T1–T11: forme chiuse del gioco guanto, efficienza e simmetria, nucleolo nel core, convergenza del campionamento, water-filling, efficienza di tutte le regole, PH contro un calcolo indipendente, equivalenza con le Eq. 34–35 di `cecini_tesi`, categoria vuota in CT, EP nel core, indicatori su casi a mano, coerenza con la colonna P7 (core) della Tab. 1 di `gonzalezasenjo2025` |
| `pilot_run.py` | 24 run (PV/carico × eterogeneità × semi): ranghi, τ di Kendall fra indicatori, cluster, rimpianto minimax, rappresentanti |
| `pilot_run2.py` | Effetto della composizione (PV/carico, mix serale/diurno, eterogeneità) e della quota ai produttori `π` |
| `pilot_timing.py` | Tempi di calcolo per N crescente |
| `make_golden.py` | Genera l'istanza di verifica `golden/` |
| `run_all.sh` | Rigenera tutti gli output (circa 8–10 minuti) |
| `*_output.txt`, `golden_stampa.txt` | Output salvati delle esecuzioni |
| `golden/` | Istanza N = 6, 168 ore, e risultati attesi (premi e indicatori per le 13 regole) |

## Come eseguire

```
python3 -B -I test_engine.py       # test di correttezza
sh run_all.sh                      # tutto (test, golden, pilot, tempi)
```

Gli script usano `-I` (modalità isolata): vanno lanciati con il loro percorso, dalla cartella o con il percorso completo.

## Istanza golden

`golden/` contiene un'istanza piccola (2 produttori e 4 consumatori, una settimana oraria, seme 2026), `π` = 0,4, percentuali dei cluster (0,2; 0,5; 0,3), 24 permutazioni fisse per lo Shapley campionato. Il codice Matlab, alimentato con `golden_inj.csv` e `golden_wd.csv`, deve riprodurre `golden_rewards.csv` e `golden_indicators.csv` con errore relativo ≤ 1e-9 per le regole deterministiche, lo Shapley e il contributo marginale, ≤ 1e-6 per il nucleolo (tolleranza dei solutori). I valori `v` per maschera di bit sono in `golden_values_v_by_mask.csv` (bit `i` = membro `i+1`; membri 1–2 produttori, 3–6 consumatori).

| File | Contenuto |
|---|---|
| `golden_inj.csv`, `golden_wd.csv` | Immissione e prelievo orari, 168 righe × 6 colonne |
| `golden_meta.json` | Ruoli, categorie, vulnerabilità, parametri |
| `golden_perms_0based.csv` | Permutazioni (indici da 0) per `SVa` |
| `golden_values_v_by_mask.csv` | `v(S)` per tutte le 64 maschere |
| `golden_rewards.csv` | Premi: 13 regole × 6 membri (ordine delle regole nell'intestazione) |
| `golden_indicators.csv` | Indicatori: 13 regole × 14 colonne (ordine nell'intestazione) |

## Avvertenze

- Un solo anno, un solo passo orario, valore unitario `c_t = 1`.
- Le definizioni di PF (Pearson giornaliero rimappato in [0,1], da `gianaroli2024` M3) e di SW (quota riservata ai vulnerabili, da `campagna2024`) vanno ricontrollate sui PDF prima della versione definitiva.
- I tempi dipendono dalla macchina e variano da un'esecuzione all'altra (fino a un fattore 4 nelle celle sotto i 2 s, di un fattore 1,3–1,5 in quelle grandi); gli intervalli riportati nel piano del modello (§10) sono minimo e massimo di più esecuzioni.
