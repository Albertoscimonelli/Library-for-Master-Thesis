# Integrazione consigliata e gap più forte in assoluto (13/10/2026)

**Basi:** 63 schede (56 + 7 nuove), il tuo `GAP_FINALE_V1`, il README del codice, `PROPOSTE_ANCORA_GAP.md`, `SPUNTI_NUOVI_PAPER.md`, il prompt RQ-1 che hai riallegato. Non ho letto `Paper/Directive` né i `.m`. Tre lavori vicini sono noti **solo da riassunti web**, non letti: Couraud et al. 2025, Limmer 2023, Rodrigues et al. 2026. Le citazioni tra virgolette sono verificate sui PDF; le inferenze sono marcate `[INFERENZA]`.

## 0. Verdetto

1. **Integrazione consigliata (Parte A).** Tieni RQ-1 come domanda principale, ma ancorala a una **richiesta esplicita di analisi multi-periodo/multi-proprietà** (González-Asenjo 2025, FW #3) e a **tre richieste indipendenti di confronto quantitativo fra nozioni di fairness** (Volpato 2024b, Dynge 2025, Cremers 2023), con Chatel 2026 come diagnosi di campo. Il tuo codice (τ-b, inversioni, forza incentivante, eccesso di coalizione, Pareto, griglia taglia × penetrazione) fa già quasi tutto: il cambiamento è nel testo, non nel codice.
2. **Correzione onesta a RQ-1.** «Il ranking dipende dalla nozione di fairness» è **in parte già mostrato** da Couraud 2025 (egalitaria contro meritocratica, 250 comunità casuali, dal riassunto web). La novità difendibile non è quella frase, ma: (a) la nozione di **stabilità di coalizione** e la **forza incentivante** accanto all'equità, (b) le regole **game-theoretic e italiane insieme**, (c) la **composizione** come fattore, (d) l'**insieme minimo** di indicatori. RQ-1 va riscritta di conseguenza (§A.3).
3. **Gap più forte in assoluto (Parte B).** Le due premesse mai verificate su cui si regge tutta la letteratura: (i) che la regola di ripartizione cambi il comportamento dei membri; (ii) che gli indicatori di fairness misurino ciò che i membri percepiscono come equo. Nessuna è testata empiricamente nel corpus. È il gap con più richieste esplicite, ma richiede dati o esperimenti che una tesi magistrale non ha.

---

## Parte A. Integrazione consigliata con il tuo lavoro

### A.1 Le richieste del corpus, in ordine di forza

Criterio B.1: forte = future work o conclusione **generale** di un paper che è già un confronto multi-metodo; debole = estensione del proprio metodo.

| # | Richiesta (verbatim) | Dove | Forza B.1 | Che cosa chiede rispetto al tuo lavoro |
|---|---|---|---|---|
| 1 | «Extending the axiomatic framework to more complex EC settings. Future work could consider settings with dynamic pricing, storage, network constraints, household flexibility, or multi-period coupling. Extending the framework to such contexts would help evaluate the robustness of CAM properties under more realistic conditions.» | `gonzalezasenjo2025`, p. 13, punto 3 | **Forte** (8 metodi × 7 proprietà, Energies, nov. 2025) | Valutare le proprietà (fairness, stabilità, incentivo) con tempo esplicito: il tuo codice è multi-periodo (8.760 h) |
| 2 | «identify parameters that can quantitatively compare the different benefit distributions based on the "individual", "collective" and "proportional" fairness» | `volpato2024b`, p. 22 | **Forte** (confronto multi-regola, tre nozioni) | Indicatori quantitativi comuni sulle stesse regole: è RQ-1 |
| 3 | «additional investigation is needed to refine fairness indicators»; «a more generalisable and comprehensive evaluation of multiple fairness indicators» | `dynge2025`, p. 12 | **Forte** (4 indicatori × 9 casi) | Valutazione generalizzabile di più indicatori |
| 4 | «there are many other fairness concepts that could be explored in energy applications, and it would be relevant to compare their outcome to Shapley values» | `cremers2023`, p. 13 | **Forte** (confronto di concetti) | Altre nozioni confrontate con Shapley |
| 5 | «fairness metrics derived from other fields are being applied indiscriminately to ECs' context» | `gasca2025`, p. 13 (conclusione) | Diagnosi critica di un confronto 10 × 4 | Validità degli indicatori |
| 6 | Mancanza di «conceptual alignment between performance metrics» e di una «systematic articulation of how these criteria interact or conflict»; «efficiency, fairness, scalability, and regulatory embedding are not orthogonal dimensions» | `chatel2026`, pp. 19–20 | Diagnosi di una rassegna RSER 2026 (qualitativa) | Come interagiscono e confliggono i criteri: i trade-off |
| 7 | «while leaving a systematic theoretical and numerical comparison of alternative allocation principles to future research» | `awerkin2026`, p. 15 | **Mista**: tema generale, ma paper a regola unica e due agenti | Confronto sistematico di principi di allocazione |

**Quale scelgo come pilastro.** Il **#1**, per due ragioni:
- è una *richiesta di analisi* di ciò che il tuo codice già fa (proprietà valutate con tempo esplicito), in un paper che è già un confronto e che ha un risultato interessante (impossibilità per la famiglia price-based: «no price-based CAM can satisfy both P4 and P7», p. 12);
- non dipende dal regime regolatorio.

Il **#2–#4** sono il secondo pilastro (la parte «indicatori comuni»); il **#6** dà autorevolezza di campo; il **#7** è un sostegno, non un'ancora.

**Cosa NON uso come pilastro:** il regime regolato; `gonzalezasenjo2026` p. 35 (limiti generici); i future work di `biancardi2026`, `avanzini2026`, `thomopulos2026`, `dadamo2026` (autoreferenziali, test B.1).

### A.2 Che cosa porta il nuovo materiale (verificato)

| Paper | Contributo alla base | Limite |
|---|---|---|
| `chatel2026` | La diagnosi di campo (#6): criteri non allineati e non ortogonali | Qualitativa, non misura |
| `awerkin2026` | **Perché la regola conta anche con torta fissa**: la quota `β` determina quali investimenti avvengono e se la REC nasce (p. 36); ripartizione interna «a regulatory issue in its own right» (p. 37). Sostituisce il «regime regolato» come motivazione | Due agenti, niente profili orari, una sola regola |
| `calcagnotto2026` | I KPI aggregati nascondono grandi differenze individuali (Tab. 4, mia lettura); chiede di garantire benefici individuali, specie ai vulnerabili (p. 12, frase di chiusura) | Due casi, nessun indicatore di equità |
| `avanzini2026` | La ripartizione interna «is not modelled in this study» (p. 13): limitazione, non richiesta | Nessuna regola |
| `biancardi2026`, `dadamo2026` | Dati e parametri per la nozione di inclusione (quote per categoria, vincolo del 10% del reddito) | Autoreferenziali; `dadamo2026` non confronta regole |

`[INFERENZA]` Il ruolo giusto della motivazione è: Awerkin dice *perché la regola conta*; Chatel, Volpato, Dynge e Cremers dicono *che manca la misura comune*; González-Asenjo 2025 dice *dove la analisi va estesa* (multi-periodo).

### A.3 Formulazione consigliata

**Gap (bozza di testo in italiano, da tradurre in inglese accademico).**
La letteratura ha mostrato in modo assiomatico che, per le regole basate su prezzi, equità, stabilità e incentivo sono incompatibili (González-Asenjo 2025), ha richiesto di estendere l'analisi a contesti multi-periodo e con flessibilità, e chiede da più parti indicatori quantitativi comuni per confrontare le regole sulle diverse nozioni di fairness (Volpato 2024b; Dynge e Cali 2025; Cremers 2023). Una rassegna recente osserva che i criteri non sono allineati né ortogonali e che manca una trattazione sistematica del loro conflitto (Chatel 2026). Non è documentato, a nostra conoscenza dai lavori letti, come le regole di famiglie diverse (game-theoretic, semplici, prezzi, performance-based, multi-criterio) si ordinano e a quale costo si scambiano equità, stabilità e forza incentivante quando il tempo è esplicito, e come ciò dipende dalla composizione della comunità.

**RQ principale (versione di RQ-1 che consiglio).**
> Quando i profili orari di un anno vengono ripartiti con regole di famiglie diverse, (i) il ranking delle regole cambia con la nozione di fairness (uguaglianza, proporzionalità al contributo fisico, stabilità, inclusione) e con la composizione della comunità; (ii) quanto costa, lungo la frontiera di Pareto, guadagnare su una nozione perdendo su un'altra, inclusa la forza incentivante; (iii) quale insieme minimo di indicatori basta a discriminare le regole?

**Sotto-domande:** RQ1.a–e come nel tuo prompt, più **RQ1.f** (grandezza dei trade-off). Se la portata è eccessiva per una tesi, RQ1.f diventa estensione e (i)+(iii) restano il nucleo.

**Regime regolato:** una frase sola, «setting in cui il valore è un trasferimento unitario comune e non c'è prezzo interno», come condizione che rende calcolabile la domanda, non come contributo.

### A.4 Che cosa fa già il tuo codice e che cosa manca (dal README, non dai `.m`)

| Elemento della RQ | Nel codice (README) | Da aggiungere |
|---|---|---|
| Ranking per indicatore, τ-b, inversioni | Presente | — |
| Composizione come fattore | Parziale (taglia × penetrazione) | Categoria, quota di persone fisiche, ripetizioni con semi (README §12) |
| Stabilità (eccesso di coalizione) | Presente (fino a 18 membri) | — |
| Forza incentivante | Presente, ancorata a Bilardo = 1 | Test di monotonia opzionale (script nuovo) per parlare la lingua degli assiomi |
| Pareto/trade-off | Presente | — |
| Insieme minimo di indicatori | Non presente | Cluster e rappresentanti (script nuovo) |

### A.5 Rischi, senza giri di parole

1. **Couraud et al. 2025 (arXiv 2508.16819) — ora letto (scheda `couraud2025`).** Confronta 4 meccanismi di mercato locale a prezzo uniforme su 4 nozioni (uguaglianza, min-max, meritocratica, utilitaria) in 250 comunità da 20 membri e conclude che nessun meccanismo risponde a tutti i tipi di fairness (p. 5). Il test «il verdetto dipende dalla nozione» c'è quindi già, ma in forma grafica, senza regole cooperative, stabilità, forza incentivante, inclusione, concordanza numerica né variazione di taglia. La novità difendibile resta nei punti (b)–(d) di §A.3; la RQ (i) va presentata come estensione quantitativa, non come primo test.
2. **Rodrigues 2026 e Limmer 2023:** esclusi per tua scelta; non letti, non citati nel V3.
3. **Impossibilità proved solo per la famiglia price-based e a singolo slot.** Le tue misure sono analoghe, non identiche, alle proprietà P4 e P7 (K5 del memo precedente). Non scrivere «verifichiamo il teorema»: scrivi «quantifichiamo grandezze analoghe».
4. **Circolarità.** Quasi ogni indicatore ha una regola campione per costruzione (README §7.0): riporta le perdite delle altre regole, non solo i vincitori.
5. **Rischio «ovvio».** Che indicatori diversi discordino è atteso: il contributo è la struttura (dimensioni indipendenti, regole robuste, soglie di composizione), non il fatto.
6. **Evidenza numerica, non teoremi.** Verbo «quantify», non «prove».

---

## Parte B. Il gap più forte in assoluto (a prescindere dal tuo progetto)

### B.1 Candidati valutati

| Candidato | Richieste nel corpus | Copertura trovata | Fattibilità | Giudizio |
|---|---|---|---|---|
| **(a) Le due premesse non verificate**: la regola cambia il comportamento; gli indicatori misurano l'equità percepita | Molte (sotto) | Nessuna evidenza nel corpus; ricerca web: trial su load-shifting senza regola di ripartizione; esperimenti di scelta sull'accettazione di impianti eolici, non sulla regola interna di una REC | Bassa per una tesi (servono dati/esperimenti) | **Più forte** |
| (b) Investimento accoppiato alla regola con n membri | `gasca2025` p. 12, `gonzalezasenjo2026` p. 35, `berg2024` | Occupato: `awerkin2026` (2 agenti); Energies 18(8):1920 `[WEB]`, `fioriti2021` | Media | Importante ma già lavorato |
| (c) Regolazione endogena al gioco (valore di coalizione non monotono) | `chatel2026` p. 17 | Non trovato nei riassunti, derivazione tua dal README (§7.5) | Media (verifica numerica di nucleo e monotonia) | Il più interessante in teoria, ma legato al regime italiano |
| (d) Stabilità dinamica e uscita dei membri nel tempo | `volpato2023` p. 10 | Poche tracce | Media | Meno fondato |

### B.2 Perché (a) è il più forte

**Il problema.** Ogni confronto fra regole, incluso il tuo, presuppone due cose che nessun paper del corpus testa:
1. **La regola cambia il comportamento** (consumo spostato, investimento, permanenza). L'unico test di comportamento nei 56 paper originali riguarda una sola regola, in simulazione (`zatti2021`, Tab. 9–10). `awerkin2026` fornisce il canale teorico ma non evidenza.
2. **Gli indicatori misurano l'equità percepita.** `gasca2025` (p. 13) avverte che la misura è «not straightforward from an engineering and mathematical perspective due to its highly subjective nature»; nessun paper collega un indicatore a una percezione misurata.

**Richieste esplicite (verificate sui PDF):**
- `gonzalezasenjo2025`, p. 13: l'applicazione a pattern reali «would help assess how theoretical properties translate into practical outcomes and user perceptions».
- `gonzalezasenjo2026`, p. 35: l'analisi astrae da «subjective behavioural factors», «a natural direction for future research».
- `basilico2025`, pp. 15–16: ricerca empirica su partecipazione e motivazioni (generale ma non operazionalizzata).
- `dadamo2026`, p. 11: gli aspetti sociali «must be validated through real-world social analyses».
- `giudice2026`, p. 18, e `bilardo2025`, p. 13: valutare gli effetti di lungo periodo dell'incentivo sul comportamento (autoreferenziali).
- `alonsopedrero2024`, p. 13 (limitazione): comprensibilità e fiducia nella regola.

**Perché è il più forte `[INFERENZA]`.** (1) È a monte di tutto: se la premessa 1 è falsa, la «forza incentivante» e l'engagement non hanno senso; se la 2 è falsa, i ranking sugli indicatori non guidano la scelta. (2) Ha il maggior numero di richieste indipendenti. (3) Il risultato sarebbe generalizzabile oltre l'Italia.

**Disegno possibile (schizzo, non un piano).**
- Esperimento di scelta o fattoriale su membri o potenziali membri di REC, con le regole di ripartizione come attributi (uguale, proporzionale al consumo, premiante il sincronismo, quota per categoria con riserva ai vulnerabili) e valutazioni di equità percepita e intenzione di partecipare.
- Confronto fra equità percepita e gli indicatori calcolati sulle stesse regole (valida o invalida le nozioni).
- Dove i dati lo permettono: dati misurati di REC con regole di ripartizione note, per stimare la risposta del consumo.

**Che cosa il tuo progetto offre a questo gap:** le regole, gli indicatori e la misura di forza incentivante come **ipotesi pronte da testare**. È il passo naturale dopo RQ-1 (o la RQ-2 che avevamo scartato per dati), e va dichiarato come sviluppo futuro, non come contributo.

### B.3 Cautele sulla Parte B
- «Più forte» è un mio giudizio, basato sulle richieste nel corpus e su ricerche web a livello di riassunto (nessun testo completo letto). Non scrivere «mai testato»: scrivi «non trovato nei lavori letti».
- Lavori da leggere prima di qualsiasi claim: Basilico et al. 2026 (*Energy Policy* 210, 115078, rif. [17] di `dadamo2026`), Hanke et al. 2026 (*Energy Policy* 208), Strazzera et al. 2026 (esperimento di scelta in Sardegna sull'eolico, `[WEB]`), Rodrigues et al. 2026.
- Il candidato (c) è quello che farei in parallelo come contributo teorico breve, perché usa solo il tuo gioco e il quadro di Chatel.

---

## Decisioni che servono da te
1. Confermi la **Parte A** (pilastro `gonzalezasenjo2025` #3 + richieste #2–#4) come base del V3? Se sì scrivo il V3 con verifica verbatim.
2. Carichi i PDF di Couraud 2025 (arXiv 2508.16819) e, se li trovi, Rodrigues 2026 e Limmer 2023, così fisso la frase sulla novità?
3. Per la Parte B: la vuoi come sezione «Future work» della tesi, oppure come progetto separato?
