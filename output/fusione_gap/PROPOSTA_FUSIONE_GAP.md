# Fusione dei due gap: proposta

**Che cosa trovi.** `GAP_FINALE_V2.tex` (testo in inglese LaTeX, stessa struttura e stessi comandi del tuo V1); `GAP_V1_V2_diff.txt` (differenze parola per parola: `[-tolto-]{+aggiunto+}`); questo memo. `GAP_FINALE_V1.tex` è il tuo file, copiato solo per il confronto.

**Come ho lavorato.** Ho letto per intero il tuo `GAP_FINALE_V1` e tutto il README (1.521 righe). **Non ho aperto i file `.m`**: ciò che dico sul codice viene dal README. Ho verificato parola per parola sui PDF del corpus tutte le citazioni del V1 (17) e del V2 (22): ognuna contro il paper citato subito dopo. Ho riletto sui PDF i fatti che uso sugli altri lavori. Distinguo sempre ciò che dicono gli autori (con pagina) da ciò che è una mia inferenza (`[INFERENZA]`).

---

## 0. In breve

1. **I due gap sono compatibili.** Condividono la parte centrale (confronto multi-regola e multi-indicatore, accordo fra indicatori, dipendenza dalla composizione) e differiscono nell'incipit: tu parti da González-Asenjo e Izquierdo 2026 e dal regime di trasferimento regolato; noi dalla dipendenza del ranking dalla nozione di fairness. La fusione è facile **nel testo**.
2. **Il tuo codice già implementa quasi tutta la nostra RQ-1** (τ-b, inversioni di graduatoria, Pareto, griglia taglia × penetrazione, 16 metodi, 11 indicatori). Non serve nessuna modifica obbligatoria al codice.
3. **Il V1 ha dieci punti attaccabili** (§2, l'ultimo è solo di bibliografia). I tre più seri: un'affermazione di novità quasi universale che ha controesempi nel corpus; una frase che il tuo stesso codice contraddice (l'identità dei membri cambia il valore da ripartire quando F > 0); una frase falsa sull'unico criterio endogeno. Nel V2 sono tutti corretti.
4. **Il testo promette più di quanto il codice oggi mostri** (§3): composizione per categoria non variata, soglia di ammissibilità che sui tuoi dati non morde, sostenibilità economica calcolabile solo su alcune schede. Si risolve con **nuove schede (dati) o ammorbidendo il testo**, non cambiando il codice.
5. **Decisioni che servono da te:** §5.

---

## 1. Che cosa ho preso da ciascuno

| Elemento | Tuo V1 | Nostro RQ-1 | Nel V2 |
|---|---|---|---|
| Ancora principale | Limiti di González-Asenjo e Izquierdo 2026 (p. 35) | Future work di `volpato2024b`, `dynge2025`, `gasca2025`, `cremers2023` | Tengo la tua ancora; le nostre quattro diventano ancore delle tre estensioni (citazioni verificate) |
| Regime regolato e ammissibilità | Pilastro del gap | Il contesto italiano è un caso studio, mai il gap (B.4) | Tenuto, formulato come regime generale e non italiano; ridimensionato dove i dati non lo sostengono (§3, T2) |
| Dipendenza del ranking dalla nozione | «Quanto concordano gli indicatori» | RQ-1 centrale | Invariata nella sostanza |
| Insieme minimo di indicatori | Assente | Output operativo di RQ-1 | Aggiunto alla RQ come clausola **opzionale** (richiede lo script K2 del §4) |
| Composizione | Taglia, penetrazione, categoria | PV/carico, eterogeneità, sincronismo, produttori, quota di persone fisiche | Tengo i tuoi tre assi; i nostri fattori solo come nuove schede (§4, K1) |
| Evidenza sotto incentivo regolato | Assente | Tabella di posizionamento | **Nuovo paragrafo** con cinque lavori verificati (appendice) |
| Liste complete di future work (B.2) | Non dichiarate | Sempre dichiarate | Dichiarazione aggiunta su González-Asenjo 2026 |
| Termini della RQ calcolabili (B.5) | Rimandati al capitolo metodologico | Tabella dei termini calcolabili | **Paragrafo breve** dopo la RQ |
| Indicatori che vincono per costruzione o circolari | Nel codice (README §7.0, §7.6), non nel testo | Centrale | Due frasi nel V2 |
| Price of Fairness e QoE | Esclusi nel codice (README §7.1) | PoF tolto da RQ-1 | Nessuna azione: coincidono |
| «Nash bargaining = parti uguali» | — | Vale per il Nash classico con disaccordo nullo | **Non lo applico al tuo codice**: il tuo metodo 3 è Yan et al. 2023, proporzionale al contributo marginale. Non va toccato |
| 13 regole del mio pilot Python, istanza golden | — | Fase 4 | Non servono: hai 16 metodi |
| Ipotesi H1–H5 con soglie | — | Fase 4 | Solo se separi run esplorativi e confermativi (§4, K1) |

---

## 2. Punti attaccabili del V1 e correzione nel V2

| ID | Gravità | Dove (V1) | Problema | Evidenza | Correzione nel V2 |
|---|---|---|---|---|---|
| P1 | Alta | Ultimo paragrafo del gap: «It is not known how benefit allocation methods rank … regulated transfer» | Affermazione di novità quasi universale (B.3). Esistono confronti sotto incentivo regolato, anche se piccoli | `fioriti2023` (p. 1 e p. 5: premio per unità di energia condivisa, Italia, 10 utenti commerciali; Shapley, nucleolo, Variance Least Core e due schemi semplici); `volpato2023` (incentivo 0,12 €/kWh, 3 membri, Shapley contro prezzo uniforme); `trevisan2024` (TIP, 5 membri, Shapley contro proporzionale); `campagna2024` (p. 2: incentivo definito dal Ministero, comune di Teglio); `ferrucci2025` (64 casi, un solo meccanismo) | Nuovo paragrafo che cita i cinque lavori; enunciato riformulato in «what the evidence above does not establish … in the literature reviewed». **Non uso `volpato2024b`** come esempio di regime regolato: i suoi benefici derivano da scambio P2P a prezzi interni (mia scheda, §3) |
| P2 | Alta | «the identity of the members who contribute does not change the amount to be distributed» | Il tuo codice la contraddice: con F > 0 e categorie esenti `v(S)` dipende da chi consuma, e non è monotona (esempio del README §7.5: 1,00 € contro 0,75 €) | README §7.5 | La frase vale solo con remunerazione unitaria comune; aggiunto che il riduttore e le esenzioni rendono il valore dipendente dalla categoria |
| P3 | Alta | «the only endogenous criterion for ranking alternative allocation rules also disappears» | Falsa nel tuo modello: la stabilità di coalizione (nucleolo, eccesso di coalizione) è endogena e la usi come indicatore | README §7.0, §7.3 | «the price-dispersion channel … disappears» |
| P4 | Media | «most European energy communities are based on virtual metering» | Presentata come fatto; è l'affermazione di Minuto e Lanzini (2022, p. 6). Gjorgievski 2023 (p. 2) descrive tre regimi diversi, non «la maggior parte» | PDF `minuto2022` p. 6; `gjorgievski2023` p. 2 | Attribuzione a Minuto e Lanzini; aggiunta la tripartizione di Gjorgievski (esenzione oneri, premio, net-metering virtuale) |
| P5 | Media | «The gap … is therefore the one that those authors declare they have not addressed» | Salto inferenziale: «regulatory constraints and tariff structures» non è «il valore è un trasferimento regolato», è la tua lettura. Inoltre «these aspects» (p. 35) copre anche investimenti, rete e fattori comportamentali (B.2) | PDF `gonzalezasenjo2026` p. 35 | «in our reading, a specific instance of the direction left open»; dichiarato che gli altri aspetti restano fuori |
| P6 | Media | «The most extensive attempt» | Superlativo non verificabile | 6.120 + 7.650 = 13.770 configurazioni (somma mia dalle Sez. 3.1.1 e 3.2.1) | «The largest simulation-based comparison among the works reviewed» |
| P7 | Bassa | Citazioni | `generalize` nel PDF è `generalise` (p. 34); «Price heterogeneity» ha la maiuscola nel PDF | PDF | Corrette. Le altre 15 citazioni erano già esatte |
| P8 | Bassa | Parafrasi e verbi | Fina 2024: «beyond which a mechanism is no longer sensibly applicable» non è fedele (il testo parla del «critical set-up» per cui i meccanismi sono applicabili con sostenibilità per tutti i membri); `ferrucci2025` (VLC) non è un'approssimazione dello Shapley; «widely used» non è sostenuto da `kulmala2021` e `fioriti2023` | PDF | «approximations and decompositions»; «attractive in practice»; Fina riformulata |
| P9 | Media | «one representative mechanism for each of the families … axiomatic criterion of Section 2.5» | Il README descrive 16 metodi su 5 famiglie e nessuno della 2.2.4; non parla del criterio assiomatico | README §6 | Riscritta: sedici meccanismi, cinque famiglie. Reinserisci il criterio assiomatico solo se è vero |
| P10 | Bassa | Bibliografia | `gasca2024`: il paper è RSER 208 (2025) 115054, online il 6/11/2024: scegli un anno e usalo ovunque. `volpato2024` è ambiguo (nel corpus ci sono `volpato2024a` e `volpato2024b`; qui serve Energies 17, 4788). «valorization» e «valorisation» sono mescolati | — | Nel V2 uso «valorisation» e le chiavi del V1 |

---

## 3. Dove il testo promette più del codice (da README)

| ID | Il testo dice | Il README mostra | Come chiudere senza toccare il codice |
|---|---|---|---|
| T1 | Il confronto varia «the composition by member category» (anche nella RQ) | §12: «Resta non variata la composizione per categoria» | **Nuove schede** con mix di categorie diversi (README §9: aggiungere una scheda non richiede modifiche al codice; `cer_config_writer.py` ne redige la bozza), oppure togli la clausola |
| T2 | La regolazione «defines which allocations are admissible» e questo è un pilastro del gap | §7.4: sulle 7 schede originali il rapporto energia condivisa su immessa va dal 2,2% al 25,7%, contro la soglia del 55%: il vincolo **non morde** («strutturalmente irrilevante»); «non è stato rimisurato sulle schede più grandi» | (a) Controlla `RESULTS(i).soglia.isBinding` sulle 28 schede. (b) Se non morde mai, dillo come risultato e declassa l'ammissibilità da pilastro a verifica. (c) Se vuoi che morda, servono schede con poco FV rispetto al carico. Nel mio pilot Python con profili **inventati** la quota di energia immessa che viene condivisa andava da 0,33 a 0,70 variando PV/carico da 1,5 a 0,5 `[PILOT, non un risultato]`: la leva è il rapporto PV/carico, non il numero di prosumer |
| T3 | «economic sustainability of participation» come dimensione del ranking | §7.6 (limite 3): il VAN esiste solo dove `quota_inv_EUR` è compilata, cioè nelle schede a penetrazione 100%. §12: l'incentivo vale il 2–3% del flusso annuo dei prosumer di `CER_2_5_0`, contro il 60–90% della vendita dell'eccedenza | Compilare `quota_inv_EUR` in tutte le schede (dato). **Rischio**: se l'incentivo pesa così poco, la regola di ripartizione potrebbe non discriminare sulla sostenibilità. Controllalo prima di promettere questa dimensione |
| T4 | «incentive strength of the rule» | §7.0-bis: è un proxy ex post (covarianza quota–virtuosità), non un'elasticità; il segno si ribalta con un solo prosumer a seconda dell'asse (netto o lordo; coseno 0,224) | Il V2 lo dichiara. Nei risultati riporta sempre entrambi gli assi |
| T5 | Quanto il ranking dipende dalla composizione (inversioni nel 20–46% delle coppie, README §7.6) | §12: i seed sono deterministici e ogni scheda sembra una sola realizzazione `[INFERENZA dal README]` | Senza repliche non puoi separare l'effetto della composizione dal rumore del generatore di profili. Genera 3–5 seed per due o tre celle e misura le inversioni **fra repliche della stessa cella**: è il livello di rumore con cui confrontare il 20–46% |
| T6 | Stabilità fra i criteri di valutazione | §14.1: sopra i 18 membri Shapley, Nucleolo, Nash e eccesso di coalizione sono saltati, quindi si confrontano tredici metodi e la stabilità non è disponibile | Dichiaralo nei limiti: la stabilità è valutata solo fino a 18 membri |
| T7 | «sixteen mechanisms» | §6: il metodo 16 (Tri-level EP) è provvisorio, su dati segnaposto, e «non va usato per produrre risultati»; compare sul fronte di Pareto nel 75% dei casi (§7.6) | Escludilo dalle conclusioni o rieseguilo con dati veri; poi aggiorna il numero nel testo |

---

## 4. Modifiche al codice

**Nessuna modifica obbligatoria.** Non toccherei i 16 metodi, gli indicatori né `MAIN.m` e `MAIN2.m`.

| ID | Intervento | Tipo | Quando serve |
|---|---|---|---|
| K1 | Nuove schede: mix di categorie (T1), poco FV rispetto al carico per far mordere la soglia (T2), `quota_inv_EUR` ovunque (T3), 3–5 seed per alcune celle (T5). Meglio separare il run esplorativo (quello che hai già visto) da uno **confermativo** su schede nuove, con soglie di rilevanza fissate prima | Dati | Se tieni le promesse del testo |
| K2 | Script nuovo `indicator_clusters.m` (non modifica nulla): legge `Tfair` e `accordo_indicatori.csv`, raggruppa gli indicatori su distanza `(1 − τ̄)/2`, sceglie un rappresentante per cluster e calcola quanto il Borda dei soli rappresentanti ricostruisce quello completo | Aggiunta | Solo se tieni la clausola «which subset of indicators suffices» |
| K3 | Funzione nuova `extreme_price_cer.m` (circa 20 righe): il lato scarso prende l'ora. Con `F = 0` e remunerazione comune sta nel core: per ogni ora il pagamento di una coalizione è almeno `c · min(G_S, W_S)` `[INFERENZA, dimostrazione mia di tre righe; verificata numericamente nel mio pilot]`. Darebbe una regola stabile e scalabile anche oltre i 18 membri e un rappresentante della famiglia 2.2.4 che non usa un prezzo interno | Aggiunta | Solo se vuoi coprire la 2.2.4 (decisione D4) |
| K4 | Prima di scrivere: eseguire `RESULTS(i).soglia.isBinding` sulle 28 schede | Controllo, nessun cambio | Subito |

---

## 5. Decisioni che servono da te

| ID | Decisione | La mia raccomandazione |
|---|---|---|
| D1 | Tenere le tre dimensioni (equità, forza incentivante, sostenibilità) nella RQ? | Sì, ma solo dopo aver verificato T3: se la sostenibilità non discrimina fra regole, togli la terza dimensione o definiscila come quota di incentivo sul flusso di cassa |
| D2 | Clausola «which subset of indicators suffices» nella RQ? | Sì se fai K2 (poco lavoro e dà un output pratico); altrimenti cancellala dal V2 |
| D3 | Variare la composizione per categoria con nuove schede, o togliere la clausola dal testo? | Variarla: è il punto dove il tuo codice è già pronto e il testo la promette |
| D4 | La tua famiglia 2.2.4 presuppone un prezzo interno? | Se sì, la frase del V2 resta; se no, aggiungi K3 e cancella la frase |
| D5 | Frasi sul decreto (soglia, riduttore F, esenzione delle persone fisiche) | Le ho riscritte dal README. **Non ho letto `Paper/Directive/`**, come da tua regola: verificale tu sul testo del decreto e aggiungi le citazioni (Regole Operative GSE 2025 e DM 127/2025, vedi il TODO nel V2) |
| D6 | Couraud et al. 2025, Limmer 2023, Rodrigues et al. 2026 | Li conosco solo da riassunti di ricerca web, non letti. Se uno di loro confronta regole di ripartizione sotto incentivo regolato, la frase «has not been verified in the literature reviewed» va rivista. Se carichi i PDF in `Paper/` li leggo |

---

## 6. Che cosa non ho verificato

- **Il codice:** tutto da README (letto per intero), nessun `.m` aperto.
- **Il decreto e le Regole Operative:** non letti (cartella `Directive` esclusa dalla tua regola).
- **Il tuo Capitolo 2 e 3:** non visti. Le frasi che rimandano a sezioni (`sec:2.2`, `sec:2.3`, `sec:2.5`, `ch:italian_context`) sono quelle del V1.
- **Fonti fuori dal corpus:** `shapley1953`, `castro2009`, `schmeidler1969` e il decreto MASE.
- **Numeri:** i dati sugli altri lavori (3, 5, 10 membri; 64 casi; sette famiglie in un mese) sono ricontrollati sui PDF; la somma 13.770 è mia.
- **Git:** il push resta bloccato (errore 403 di autorizzazione). I file sono nel container e li invio in chat.

---

## Appendice. Tabella di posizionamento (opzionale, da mettere in tesi dopo le tue verifiche)

| Lavoro | Valore ripartito | Meccanismi confrontati | Comunità | Composizione variata | Verifica |
|---|---|---|---|---|---|
| `gonzalezasenjo2026` | Surplus di scambio interno (spread acquisto–vendita) | 5 (BS, PB, PTE, nucleolo, Shapley) | Da 10 a 1.000 membri | Sì (mix di profili, penetrazione, campionamento) | Mia scheda e PDF pp. 13–20, 34–35 |
| `gasca2025` | Costo della bolletta | 10 approcci, 4 indici | 7 famiglie, 1 mese | No | PDF p. 8, p. 11 |
| `volpato2024b` | Risparmi con scambio P2P a prezzi interni | 4 (SW, Nash, Shapley, nucleolo) | 4 utenti | No | PDF p. 21; scheda §3 |
| `volpato2023` | Incentivo regolato 0,12 €/kWh | 2 (Shapley, prezzo uniforme) | 3 membri | No | PDF pp. 3–4; scheda |
| `trevisan2024` | Incentivo regolato (TIP) | 2 (Shapley, proporzionale) | 5 membri | No | PDF p. 3; scheda |
| `fioriti2023` | Premio per energia condivisa | Shapley, nucleolo, Variance Least Core e due schemi semplici (sharing, financing) | 10 utenti commerciali | No | PDF pp. 1, 5–6; scheda |
| `campagna2024` | Incentivo del Ministero più proxy ARERA | Più regole (Shapley, proprietà, proporzionale, Packets e miste) | Comune di Teglio | No | PDF p. 2, p. 12; scheda |
| `ferrucci2025` | Premio per kWh condiviso | 1 (Variance Least Core) | Da 10 a 50 membri (repliche di 10), quota di prosumer 10–100% | Sì (64 casi) | PDF p. 1; scheda |
