# V3 — «Gap individuato e posizionamento della tesi» (bozza in italiano)

**Stato.** Bozza di lavoro in italiano. La versione inglese in LaTeX (con le stesse chiavi `\cite` del V1/V2) la preparo **dopo la tua approvazione di questo testo**. Le citazioni tra «» sono riportate parola per parola dai PDF del corpus e sono state ricontrollate (§ finale). I segnaposto `[DA VERIFICARE: …]` indicano ciò che non ho potuto controllare. Le sezioni del testo sono quelle del V2 (`sec:2.2`, `sec:2.3`, `sec:2.5`, `ch:italian_context`), che non ho visto.

**Che cosa cambia rispetto al V2** (dettaglio nel §10):
- il bisogno di ricerca non nasce più dal regime regolato né da González-Asenjo e Izquierdo 2026, ma da una **richiesta esplicita di analisi multi-periodo** (González-Asenjo et al. 2025) e da **richieste indipendenti di indicatori comuni** (Volpato, Dynge e Cali, Cremers, Gasca), con una rassegna 2026 (Chatel) come diagnosi di campo;
- il regime regolato diventa **il contesto che rende calcolabile la domanda**, in un solo paragrafo;
- è stato letto e inserito **Couraud et al. 2025**, il confronto più vicino alla domanda (§ 1.4); Limmer 2023 e Rodrigues 2026 sono esclusi per tua scelta e non sono citati;
- la RQ è quella (riformulata) che hai trovato interessante, con in più la grandezza dei trade-off; la dimensione «sostenibilità economica» esce dalla RQ (§8, decisione D1).

---

## 1. Gap individuato e posizionamento della tesi

I capitoli precedenti descrivono un panorama maturo. La teoria dei giochi cooperativi offre il riferimento canonico per la ripartizione dei benefici [shapley1953, moncecchi2020]; un insieme di approssimazioni e scomposizioni ne ha reso fattibile il calcolo anche per comunità grandi [castro2009, cremers2023, alonsopedrero2024, ferrucci2025]; gli approcci semplificati restano attraenti per la loro trasparenza verso utenti non esperti [kulmala2021, fioriti2023]; e un gruppo di indicatori di equità, importati da altre discipline, permette di valutare le ripartizioni risultanti (Sez. `sec:2.3`). Il problema aperto non è più *come calcolare* una ripartizione equa, ma *come scegliere* fra ripartizioni che possono tutte essere calcolate.

### 1.1 Il bisogno di ricerca da cui parte il lavoro

**Che cosa è stato stabilito.** L'analisi assiomatica più recente valuta otto metodi di ripartizione rispetto a sette proprietà desiderabili e conclude che «no computationally efficient CAM satisfies all desirable properties simultaneously, highlighting structural tensions between fairness axioms, incentive compatibility, and ease of implementation» [gonzalezasenjo2025, p. 2]. Per una famiglia di metodi la tensione è un teorema: «this trade-off is inherent to the entire price-based family», perché nessun metodo basato su prezzi può soddisfare insieme la proprietà P4 e la P7, né la P5 e la P7 [gonzalezasenjo2025, p. 12] (P4: monotonia del costo rispetto al consumo individuale; P5: continuità; P7: convenienza della partecipazione di gruppo, cioè appartenenza al core; definizioni dalla mia scheda del paper `[DA VERIFICARE su Sez. 2]`).

**Dove il risultato si ferma, secondo gli autori.** Il loro modello è «intentionally minimal» e assume «known and deterministic consumption and generation within each time slot» [gonzalezasenjo2025, p. 5]: un singolo intervallo di tempo, senza sincronismo fra membri. Fra gli sviluppi indicano, come terzo punto, l'estensione del quadro assiomatico a contesti più complessi: «Future work could consider settings with dynamic pricing, storage, network constraints, household flexibility, or multi-period coupling. Extending the framework to such contexts would help evaluate the robustness of CAM properties under more realistic conditions» [gonzalezasenjo2025, p. 13]; e come quarto punto l'applicazione a pattern di consumo e generazione reali di comunità operative [gonzalezasenjo2025, p. 13]. *Dichiarazione:* dei quattro punti usiamo solo il terzo (e del quarto la parte sui dati realistici); il primo e il secondo, sul nucleolo (caratterizzazione formale e algoritmi efficienti), non sono perseguiti. La parte del quarto punto sulle «user perceptions» non è calcolabile da un modello e non è assunta.

**Conferma indipendente.** Il confronto data-driven degli stessi autori su quasi quattordicimila configurazioni simulate conclude che «no single cost allocation method dominates across all dimensions and configurations» [gonzalezasenjo2026, p. 34], che «formal property compliance alone is insufficient to assess real-world performance and must be complemented by scenario-specific analysis» [gonzalezasenjo2026, p. 35], e dichiara di procedere «abstracting from investment decisions, network constraints, and subjective behavioural factors» [gonzalezasenjo2026, p. 35].

**Che cosa non è noto.** Due domande restano senza risposta da queste affermazioni.
1. Le incompatibilità sono dimostrate per la famiglia basata su prezzi e per un singolo intervallo. Se tensioni comparabili compaiano nelle altre famiglie (game-theoretic, semplici, performance-based, multi-criterio) quando il tempo è esplicito e i membri differiscono per il sincronismo delle loro immissioni e dei loro prelievi, per quanto abbiamo letto non è stato quantificato.
2. Gli assiomi sono soddisfatti o violati; la scelta di una regola richiede però di sapere *di quanto* essa rinuncia a una proprietà per ottenerne un'altra.

### 1.2 Il secondo bisogno: una misura comune delle nozioni di equità

La seconda domanda richiede un metro condiviso, e la letteratura indica più volte che manca.
- Dynge e Cali osservano che gli indicatori in uso sono stati «adapted for use in the context of local electricity markets» da altre discipline e che, prima del loro studio, «no research has been found addressing or comparing the performance of these indicators»; ne valutano quattro e concludono che «additional investigation is needed to refine fairness indicators, ensuring their effectiveness across diverse market models», auspicando «a more generalisable and comprehensive evaluation of multiple fairness indicators» [dynge2025, p. 12 e Introduzione].
- Gasca et al. avvertono che «fairness metrics derived from other fields are being applied indiscriminately to ECs' context» e che misurare l'equità non è immediato «from an engineering and mathematical perspective due to its highly subjective nature» [gasca2025, p. 13].
- Volpato et al. indicano fra gli sviluppi di «identify parameters that can quantitatively compare the different benefit distributions based on the "individual", "collective" and "proportional" fairness» [volpato2024b, p. 22].
- Per Cremers et al. «there are many other fairness concepts that could be explored in energy applications, and it would be relevant to compare their outcome to Shapley values» [cremers2023, p. 13].
- Couraud et al. aprono con la stessa constatazione sul piano pratico: le comunità «often lack guidance on which approach best aligns with their values» [couraud2025, p. 1].
- Una rassegna recente del settore osserva che manca «conceptual alignment between performance metrics», con criteri tecnici e di benessere usati insieme «without a systematic articulation of how these criteria interact or conflict» [chatel2026, p. 19], e conclude che efficienza, equità, scalabilità e inserimento regolatorio «are not orthogonal dimensions. Improving one dimension often weakens another» [chatel2026, p. 20].

Il vocabolario stesso non è condiviso: Gasca et al. chiamano *equity* «the equal allocation of costs/benefits for all users, regardless of their contribution» [gasca2025, p. 5], mentre Dynge e Cali scrivono che «Equity commonly refers to rewarding individuals proportionally to individual contribution» [dynge2025, p. 2, nota]. La stessa parola ha significati opposti.

### 1.3 Perché la regola conta anche quando il valore da ripartire è fissato

Quando il valore da ripartire è determinato ex post dalle misure orarie, la regola non lo modifica: ripartisce soltanto. Sarebbe quindi legittimo chiedersi se la scelta fra regole sia rilevante. Il lavoro più vicino sulla questione la risolve in modo esplicito, benché in un modello stilizzato a due agenti (un produttore di biogas e una famiglia): la regola di ripartizione «is not a mere redistribution device but a determinant of the equilibrium investment pattern» [awerkin2026, p. 36], e rendere la ripartizione dell'incentivo una scelta regolatoria a sé: «This makes the allocation of the collective benefit a regulatory issue in its own right, rather than a purely internal matter of the community» [awerkin2026, p. 37]. Gli autori lasciano esplicitamente a lavori futuri «a systematic theoretical and numerical comparison of alternative allocation principles» [awerkin2026, p. 15]. Il loro modello non ha profili orari, ha due agenti e una sola regola (Nash bargaining): è un argomento sulla rilevanza della scelta, non una misura. Il presente lavoro non studia come i membri reagiscono alla regola (§ 6, limiti), ma misura *che cosa ciascuna regola premia*.

### 1.4 I confronti esistenti sotto incentivo regolato sono circoscritti

Confronti fra meccanismi di ripartizione con un incentivo regolato per l'energia condivisa esistono, ma poggiano su un singolo caso studio: tre membri in [volpato2023], cinque in [trevisan2024], dieci in [fioriti2023], un solo comune in [campagna2024]. Lo studio che varia taglia, quota di prosumer e diversità degli utenti su 64 casi applica un solo meccanismo [ferrucci2025]. Gasca et al. incrociano dieci approcci e quattro indici, concludono che «existing fairness indexes do not adequately represent fairness» e che «the findings are sensitive to user assets and profile changes», ma subito dopo affermano che «the same conclusions apply to other types of ECs with diverse user types» [gasca2025, p. 11]: una generalità rispetto alla composizione che il loro disegno, una sola comunità di sette famiglie osservata per un mese, non verifica.
Il confronto più vicino alla domanda di questa tesi è quello di Couraud et al. Quattro meccanismi di distribuzione dell'energia in un mercato locale a prezzo uniforme (pro-rata, glass-filling, glass-filling con priorità, doppia asta) sono valutati su 250 comunità residenziali generate a caso, con quattro nozioni di equità (uguaglianza, min-max, meritocratica, utilitaria), e gli autori concludono che «there is not one distribution approach that addresses all types of fairness» [couraud2025, p. 5]: il glass-filling con priorità prevale su uguaglianza e min-max, il pro-rata e la doppia asta sulla meritocrazia, il glass-filling semplice è un compromesso [couraud2025, p. 1]. Il risultato è letto da grafici, per meccanismi di mercato a prezzo uniforme, con taglia fissa di venti membri e la sola penetrazione del fotovoltaico come fattore. Non figurano regole cooperative né regole semplici a quote o performance-based; non figurano indicatori di stabilità di coalizione o di forza incentivante; la fairness basata sul bisogno non è valutata, per mancanza di dati («this work that will not address it for the same reason» [couraud2025, p. 4]); la concordanza fra nozioni non è quantificata. Il valore ripartito è il risparmio in bolletta con prezzi locali, non un incentivo regolato sull'energia condivisa. `[INFERENZA, dalla mia lettura del paper (scheda couraud2025)]`

### 1.5 Il gap

Mettendo insieme i punti precedenti, in questa lettura il gap è il seguente. L'incompatibilità fra equità, stabilità e incentivo è stata dimostrata per una famiglia di metodi in un modello a singolo intervallo; la letteratura chiede sia di estendere l'analisi al tempo esplicito [gonzalezasenjo2025, p. 13] sia di disporre di indicatori quantitativi comuni per confrontare le nozioni di equità [volpato2024b; dynge2025; cremers2023]; una rassegna recente conferma che i criteri non sono né allineati né ortogonali [chatel2026]. Il test se il verdetto sui meccanismi dipenda dalla nozione di equità è stato condotto per quattro meccanismi di mercato locale e quattro nozioni [couraud2025]. Non risulta, nei lavori letti, che regole di famiglie diverse (game-theoretic, semplici, performance-based, multi-criterio) siano state ordinate sugli stessi dati e con un insieme comune di indicatori che includa, oltre all'uguaglianza e alla proporzionalità, la **stabilità di coalizione** e la **forza incentivante**; che l'accordo fra nozioni e il costo con cui se ne scambia una con l'altra lungo la frontiera di Pareto siano stati **quantificati** (non solo letti da grafici); e che l'ordinamento sia stato ripetuto su configurazioni che variano sistematicamente taglia, penetrazione e composizione della comunità, quando il valore da ripartire è un trasferimento regolato sull'energia condivisa oraria.

### 1.6 Contributo della tesi e sue estensioni

La tesi affronta questo bisogno con un modello tecnico-economico di simulazione a risoluzione oraria, in cui le regole sono valutate nelle stesse condizioni operative e con gli stessi indicatori. Il nucleo è la domanda del § 3; da questo nucleo il lavoro si estende in tre direzioni, ciascuna motivata dalla letteratura.

**Prima direzione, i meccanismi.** Gli autori del confronto data-driven osservano che «the modular nature of this framework allows for the evaluation of methods not considered in this paper» [gonzalezasenjo2026], e il loro disegno copre tre delle sei famiglie della Sez. `sec:2.2`; il confronto di Couraud et al. riguarda soltanto meccanismi di mercato locale a prezzo uniforme. Gasca et al. indicano fra gli sviluppi «additional types of comparisons» nello stesso quadro, «particularly for evaluating metrics beyond economic metrics» [gasca2025, p. 12]. L'estensione alle famiglie restanti non risponde solo a un criterio di completezza: se le tensioni sono dimostrate per i metodi basati su prezzi, la domanda aperta riguarda proprio i metodi che non li usano, fra cui quelli performance-based, progettati per premiare il sincronismo [gianaroli2024, giudice2026]. La famiglia basata su prezzi interni e tariffe dinamiche (Sez. `sec:2.2.4`) fa eccezione: presuppone il prezzo che il contesto qui adottato non ha, e non è rappresentata.
`[DA VERIFICARE contro la definizione della famiglia in Sez. 2.2.4: se alcuni suoi meccanismi non richiedono un prezzo interno, aggiungerli e cancellare la frase.]`

**Seconda direzione, la valutazione.** Gli assiomi non bastano: «formal property compliance alone is insufficient to assess real-world performance and must be complemented by scenario-specific analysis» [gonzalezasenjo2026, p. 35]. Per questo il lavoro usa un insieme di indicatori e non uno solo, tratta il loro accordo come un risultato da osservare, e riporta a parte gli indicatori definiti come distanza da un'allocazione di riferimento, il cui valore è per costruzione ottimo per il meccanismo che fornisce il riferimento. Le grandezze del modello sono analoghe, non identiche, alle proprietà assiomatiche: la forza incentivante (covarianza fra quota e sincronismo) non coincide con P4 e l'eccesso di coalizione non coincide con P7. Il lavoro quantifica grandezze analoghe e non verifica il teorema.

**Terza direzione, le configurazioni.** La richiesta di variare la composizione compare in forme diverse: comunità con «a higher number of members (e.g., tens or more)» [volpato2024b], «the different EC compositions (number of members in the UT groups)» [minuto2022], «the critical set-up» oltre il quale i meccanismi di ridistribuzione restano applicabili [fina2024], «the number and composition of community members» [giudice2026]. Il confronto è quindi ripetuto su configurazioni che variano sistematicamente numero di membri, penetrazione dei prosumer e composizione per categoria.
`[DA VERIFICARE (T1): la composizione per categoria non è ancora variata nelle comunità simulate (README §12). O si aggiungono le configurazioni, o si cancella l'ultima clausola.]`

## 2. Contesto empirico: perché il caso italiano e il valore regolato

Il caso italiano è il contesto empirico del lavoro, non la sua motivazione. Esso è un'istanza operativa e documentata di un regime in cui il valore da ripartire non è un arbitraggio sui prezzi ma un trasferimento regolato: la quantità condivisa è il minimo orario fra immissioni e prelievi aggregati e la remunerazione unitaria è comune a tutti i membri. In questo regime il canale della dispersione dei prezzi, che il confronto data-driven indica come motore dei risultati («Price heterogeneity emerges as a central driver of CAMs' behaviour»; «conclusions drawn under uniform pricing may not generalise to heterogeneous market contexts» [gonzalezasenjo2026]), scompare per costruzione: i membri differiscono solo per l'allineamento temporale fra prelievi e immissioni e, dove la norma lo prevede, per categoria. È il caso più semplice in cui porre la domanda del § 3, e per questo è quello adottato. Le categorie definite per legge entrano nel modello come vincoli del quadro simulato, e l'ammissibilità di ogni ripartizione è verificata a posteriori sulla soglia del quadro normativo, e riportata.
`[DA VERIFICARE (T2, D5): il vincolo di ammissibilità sulle schede esistenti non morde (README §7.4: rapporto fra energia condivisa e immessa dal 2,2% al 25,7% contro il 55%): va controllato su tutte le 28 schede prima di presentarlo come elemento del disegno, altrimenti va ridotto a una nota. Le frasi sul decreto (soglia, fattore di riduzione, esenzione delle persone fisiche) sono riscritte dal README: non ho letto Paper/Directive; servono le citazioni (Regole Operative GSE 2025, DM 127/2025).]`

## 3. Domanda di ricerca

> Quando i profili orari di un anno vengono ripartiti con meccanismi di famiglie diverse, (i) l'ordinamento dei meccanismi cambia con la nozione di equità adottata (uguaglianza, proporzionalità al contributo fisico, stabilità di coalizione, inclusione) e con la taglia, la penetrazione dei prosumer e la composizione per categoria della comunità; (ii) quanto costa, lungo la frontiera di Pareto, guadagnare su una nozione perdendo su un'altra, inclusa la forza incentivante della regola; (iii) quale insieme minimo di indicatori basta a discriminare i meccanismi?

**Rapporto con Couraud et al.** La parte (i) della domanda estende all'insieme di famiglie, alle nozioni di stabilità e inclusione e alle configurazioni variate il test che [couraud2025] conduce su quattro meccanismi di mercato e quattro nozioni; la differenza non sta nel porre la domanda, ma nel quantificarla (concordanza di rango, frontiera di Pareto, soglie di inversione) sulle stesse regole e sugli stessi dati.

**Sotto-domande.** (a) migliori e peggiori meccanismi per nozione, con il margine in valore; (b) concordanza fra i ranghi di nozioni diverse; (c) riduzione degli indicatori a poche dimensioni; (d) meccanismi robusti a tutte le nozioni; (e) effetto di composizione e parametri; (f) grandezza dei trade-off fra nozioni, inclusa la forza incentivante.

**Ogni termine corrisponde a una grandezza calcolata dal modello.**
- *Equità distributiva*: indicatori di uguaglianza, di proporzionalità al contributo fisico, di inclusione e di stabilità di coalizione, tutti valutati sulle stesse allocazioni.
- *Stabilità di coalizione*: eccesso massimo delle coalizioni bloccanti rispetto al valore da ripartire; calcolabile fino a 18 membri, oltre i quali non è disponibile (README §14.1) `[T6]`.
- *Forza incentivante*: covarianza trasversale fra la quota ricevuta da ciascun membro e l'allineamento temporale del suo profilo con la comunità, normalizzata su un meccanismo di riferimento. Indica quanto una regola premia il sincronismo, non come i membri reagirebbero: la risposta comportamentale è fuori perimetro. È un proxy ex post, il suo segno dipende dall'asse (netto o lordo) e va sempre riportata con entrambi (README §7.0-bis) `[T4]`.
- *Accordo fra indicatori*: correlazione di rango τ_b di Kendall fra i ranghi che inducono.
- *Dipendenza dalla configurazione*: frequenza con cui l'ordine di una coppia di meccanismi si inverte lungo gli assi di taglia e penetrazione.
- *Insieme minimo*: indicatori rappresentanti dei gruppi in cui gli indicatori si raggruppano per distanza `(1 − τ̄)/2`, e quanto il loro ordinamento ricostruisce quello completo `[richiede lo script nuovo K2; se non lo implementi, cancella (iii)]`.

## 4. Il modello

Il modello è organizzato in due strati. Lo strato di valorizzazione non ha gradi di libertà: a partire dai profili orari dei membri determina il valore da ripartire e i vincoli che agiscono su di esso. Lo strato di allocazione è l'oggetto dello studio e implementa sedici meccanismi di cinque delle sei famiglie della Sez. `sec:2.2`, tutti ripartiscono lo stesso valore e sono valutati con gli stessi indicatori. La definizione operativa degli indicatori e la caratterizzazione del gioco sono sviluppate nel capitolo metodologico.
`[DA VERIFICARE (T7): il sedicesimo meccanismo (Tri-level EP) è provvisorio, su dati segnaposto, e non va usato per produrre risultati. Escluderlo o rieseguirlo con dati veri, poi aggiornare il numero.]`

## 5. Risultato atteso

Il risultato atteso non è l'identificazione di un meccanismo ottimo, ma la struttura dell'interazione fra equità, stabilità e forza incentivante: le configurazioni in cui l'ordinamento si inverte e quelle in cui gli indicatori concordano o divergono. Poiché diversi indicatori sono massimizzati per costruzione da un meccanismo specifico, la grandezza di interesse è la perdita che gli altri meccanismi subiscono sugli indicatori restanti, non l'identità del vincitore su ciascuno.

## 6. Limiti e perimetro

- **Fuori perimetro:** la risposta comportamentale dei membri alla regola (consumo spostato, investimento, permanenza), la percezione di equità, i mercati locali P2P e il Price of Fairness (non calcolabile quando tutte le regole ripartiscono lo stesso valore) `[Errata 12/10/2026]`.
- **Premesse non verificate.** Il lavoro presuppone che una regola che premia il sincronismo spinga i membri a sincronizzarsi (premessa 1) e che gli indicatori di equità misurino ciò che i membri considerano equo (premessa 2). Nessuna è testata nel corpus letto; gli stessi autori ne chiedono la verifica (ad esempio, per la premessa 2: «would help assess how theoretical properties translate into practical outcomes and user perceptions» [gonzalezasenjo2025, p. 13]). Questa è la naturale estensione del lavoro e va dichiarata come tale, non come suo contributo.
- **Lavori non inclusi.** Due lavori noti solo da riassunti (Limmer 2023; Rodrigues et al. 2026) non sono stati letti e, per tua scelta, sono esclusi dal testo.
- **Evidenza numerica, non dimostrazione.** I risultati sono evidenza su comunità simulate, non teoremi; il verbo è «quantificare», non «dimostrare».
- **Stabilità disponibile solo fino a 18 membri;** sopra, il confronto è su tredici metodi (README §14.1).
- **Ogni indicatore ha un campione per costruzione** (README §7.0): si riportano le perdite degli altri meccanismi.

## 7. Cose che il testo non afferma (regole B.1–B.4)

- Non si afferma che nessuno abbia mai confrontato regole su più nozioni: Couraud et al. lo fanno per quattro meccanismi e quattro nozioni; si dice che cosa non risulta nei lavori letti (§ 1.4–1.5).
- Il caso italiano non è presentato come gap (B.4).
- I future work degli autori usati sono generali (B.1): González-Asenjo 2025 (#3, #4), Volpato 2024b, Dynge e Cali 2025, Cremers 2023 (#4 della sua lista), Gasca 2025. Non sono usati future work autoreferenziali (Biancardi, Avanzini, Thomopulos, D'Adamo, Awerkin sono citati solo per ciò che affermano, non per ciò che chiedono, salvo la frase di Awerkin a p. 15, di tipo misto, usata come sostegno).

## 8. Decisioni aperte (da te)

| ID | Decisione | Mia raccomandazione |
|---|---|---|
| D1 | Togliere la «sostenibilità economica» (VAN) dalla RQ? Qui è tolta | Sì: il VAN esiste solo dove `quota_inv_EUR` è compilata (README §7.6) e l'incentivo vale il 2–3% del flusso annuo dei prosumer di `CER_2_5_0` (README §12). Tienila come analisi complementare |
| D2 | Tenere la clausola (iii) «insieme minimo» | Sì, se fai lo script K2 (lavoro piccolo, output pratico) |
| D3 | Variare la composizione per categoria con nuove schede | Sì: il codice è pronto e il testo la promette (T1) |
| D4 | La famiglia 2.2.4 presuppone un prezzo interno? | Se sì, la frase resta; se no, aggiungere `extreme_price_cer.m` e cancellarla |
| D5 | Frasi sul decreto (soglia, riduzione F, esenzione) | Verificale tu su `Paper/Directive` e inserisci le citazioni |
| D6 | Couraud 2025 (letto), Limmer 2023 e Rodrigues 2026 (esclusi) | Couraud è inserito (§ 1.4, 1.5). I due esclusi non sono citati: se un revisore li conosce, il § 1.5 va rivisto |
| D7 | Includere il § 1.3 (Awerkin) | Sì: dà la rilevanza al posto del regime. Rischio: modello stilizzato a due agenti; il testo lo dice |

## 9. Verifica delle citazioni

Le citazioni sono state ricontrollate parola per parola sui testi estratti dei PDF (verifica automatica per chiave, vedi sotto), e le pagine confrontate con le schede. Non verificate: `shapley1953`, `castro2009`, `schmeidler1969` e il decreto MASE (fuori corpus); le definizioni di P4, P5 e P7.

## 10. Differenze rispetto al V2

| Punto | V2 | V3 |
|---|---|---|
| Origine del bisogno di ricerca | Un passo di González-Asenjo e Izquierdo 2026 sui «regulatory constraints» | Una richiesta esplicita di analisi multi-periodo (González-Asenjo 2025, p. 13) e richieste indipendenti di indicatori comuni |
| Ruolo del regime regolato | Nucleo del gap | Contesto che rende calcolabile la domanda (§ 2) |
| Motivazione di rilevanza | Regime e ammissibilità | Awerkin 2026 (§ 1.3) |
| RQ | Tre dimensioni, con sostenibilità economica e ammissibilità | Quattro nozioni di equità, trade-off con la forza incentivante, insieme minimo |
| Diagnosi di campo | Assente | Chatel 2026 |
| Concorrente non letto | Nota generica | Segnaposto esplicito su Couraud 2025 (§ 1.4) |
