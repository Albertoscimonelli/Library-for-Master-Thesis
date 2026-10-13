# calcagnotto2026 — Comparison of methods for generating ex-ante distribution coefficients for collective self-consumption

- **File sorgente:** `Paper/Comparison_of_methods_for_generating_exante_distribution_coefficients_for_collective_selfconsumption.pdf` (13 pagine; testo estraibile; la Tab. 5 dell'appendice (case study 2) è ruotata e il testo estratto è degradato: **non letta in dettaglio**; Fig. 1–15 non ispezionate; Tab. 1–4 lette dal testo)
- **Tipo:** articolo su rivista (Energy & Buildings); simulazione deterministica su due casi studio spagnoli (uno con dati misurati + simulati, uno con dati misurati + profili medi).
- **Lettura:** integrale (corpo pp. 1–12); appendice parziale (Tab. 4 letta, Tab. 5 no); bibliografia non verificata riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente. Le virgolette riportano il testo degli autori.

## 1. Riferimento bibliografico
Calcagnotto, M.; Ortiz, J.; Maskova, I.; Madrid, F.; Pascual, J.; Salom, J. (2026). *Comparison of methods for generating ex-ante distribution coefficients for collective self-consumption.* **Energy & Buildings**, 364, 117605. https://doi.org/10.1016/j.enbuild.2026.117605. Ricevuto 22/10/2025; rivisto 27/4/2026; accettato 6/5/2026; online 9/5/2026. IREC (Barcellona). Fondi: Horizon 2020 (syn.ikia, ARV). Dati: «The authors do not have permission to share data.» (p. 13). Ottimizzazione: Python, SciPy, Basin-Hopping (p. 4).

## 2. Obiettivo e research question
- **Obiettivo (abstract p. 1; §1.3 p. 2):** valutare 16 modalità di generazione di coefficienti di ripartizione **ex-ante** (statici o variabili orari) per l'autoconsumo collettivo (CSC) spagnolo, combinando risoluzione temporale e metodo di calcolo (proporzionale al consumo, PTC, oppure ottimizzazione numerica, OPT, che massimizza il tasso di autoconsumo della REC).
- **Gap dichiarato (p. 2):** «From the identified studies, none has explored different calculation modes for ex-ante distribution coefficients, combining temporal resolution with method of calculation: proportional to consumption (PTC) and numerical optimisation (OPT).» `[INFERENZA]` È un'universale negativa del tipo che la regola B.3 sconsiglia; qui interessa solo come dato sulla posizione degli autori.
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Spagna, Real Decreto 244/2019 e modifiche; la norma «only covers ex-ante static coefficients» (p. 2): fino a 8760 coefficienti orari per partecipante, modificabili ogni quattro mesi, somma pari a 1 in ogni ora; entro 2000 m dall'impianto (p. 2). Compensazione semplificata delle eccedenze (net billing) per impianti fino a 100 kWp.
- **Casi studio (pp. 5–8):**
  - CS1 (Santa Coloma de Gramenet): edificio residenziale a energia positiva (aree comuni, 39,1 kWp) e struttura sanitaria (30 kWp, con proprio FV che resta dedicato); solo due consumatori; condivisione dell'impianto residenziale. Profili residenziali simulati (TRNSYS), sanitari misurati.
  - CS2 (Palma): una scuola (66,8 MWh/anno, FV da 114,95 kWp, 181,6 MWh/anno) e 159 abitazioni (profilo medio Datadis, circa 2.795 kWh/anno ciascuna, trattate in modo aggregato); ripartizione iniziale di progetto 30% alla scuola e 70% alle abitazioni.
  - Tariffe 3.0TD (6 periodi), 2.0TD (3 periodi) e PVPC (prezzo orario); eccedenze a 0,065, 0,06 e (media 2024 PVPC) 0,062 €/kWh.

## 4. Metodo
- **Coefficienti:** `E_g,i,t = β_i,t · E_g,t` con somma dei `β` pari a 1 in ogni ora (Eq. 1, p. 4). Sedici modi = {IDEAL, OPT, PTC} × {insieme giornaliero: costante (CON) o 24 coefficienti orari} × {tipo di giorno: unico (S), feriale/festivo (WDWE), mensile (M), WDWE + M} (Tab. 2, p. 5). IDEAL assume tutta l'energia disponibile alla comunità: «equivalent to the case of ex-post dynamic allocation» (p. 5). Nel CS2 si valutano solo 8 modi (niente 24 h).
- **OPT:** massimizza `SCR_REC`; vincoli: coefficienti non negativi e somma pari a 1; equità ed efficienza computazionale «are not directly included in the optimisation but are analysed» (p. 4).
- **PTC:** `β_i,t = p_i,t / Σ_j p_j,t` (Eq. 4, p. 4).
- **KPI:** SCR (Eq. 2), SSR (Eq. 3), risparmi annui sulla componente energia della bolletta (potenza invariata; imposta 5,113% e IVA 21%).
- **Compensazione dei membri (p. 11):** tariffa interna fissa o quota annua affinché il membro che perde rispetto allo scenario individuale recuperi la perdita.

## 5. Meccanismi di ripartizione analizzati
Ripartizione **fisica/contabile dell'energia** (non del beneficio economico): PTC (proporzionale al consumo, a più risoluzioni) e OPT (massimizza l'autoconsumo aggregato). Il beneficio economico individuale ne è conseguenza. La compensazione proposta a p. 11 è l'unica regola esplicita di ripartizione economica: ripristino del livello individuale del prosumer (tariffa 0,112 €/kWh nel CS1; quota annua 50,2–57,7 € per abitazione nel CS2), applicata come esempio per il solo modo migliore.

## 6. Metriche
SCR e SSR individuali e di comunità; risparmi individuali e della comunità (%, € nel CS1: 17.953 € in media, 32,2%); tempo di calcolo (Tab. 3). **Nessun indicatore di equità** (confermato dagli autori, p. 4 e p. 12).

## 7. Risultati principali (numeri dal paper)
- **CS1 (Tab. 4 p. 12):** `SCR_REC` individuale 67,01%; IDEAL 88,35%; OPT da 85,40% a 87,48%; PTC da 84,72% a 86,01%. Media OPT 86,36% e media PTC 85,43% (mie medie sulla Tab. 4); l'abstract riporta 86,4% e 85,3% (p. 1, p. 12): lo scarto sul PTC (85,3 contro 85,43) è mio calcolo e non spiegato dagli autori.
- **CS2:** `SCR_REC` individuale 24,6%, medio dei modi 89,0%; OPT supera PTC di 0,43 punti percentuali (p.p.) su `SCR_REC` e 0,15 p.p. su `SSR_REC`; risparmi della comunità +96,8% (PVPC) e +157,1% (3P) rispetto all'individuale (p. 10); la scuola perde in media il 68,5% dei risparmi individuali (p. 10).
- **Asimmetrie individuali (p. 9–10):** nel CS1 la struttura sanitaria incassa l'82% dei risparmi totali, le aree comuni il 18%; rispetto all'individuale, la prima guadagna +93,8% e le seconde perdono il 60% in media: «comAreas does not benefit economically from sharing» (p. 10).
- **Effetto del modo di calcolo:** piccolo sui KPI di comunità («variation observed across modes is not pronounced», p. 10; deviazione massima dei risparmi 1,63% nel CS1; 3,94% PVPC e 1,16% 3P nel CS2), più grande sui KPI individuali (aree comuni: risparmi 18,03%–28,32% a seconda del modo; Tab. 4).
- **Granularità e tempi:** coefficienti orari (24 h) migliorano di poco `SCR_REC` (0,07 p.p. in media nell'OPT) e per il PTC peggiorano (0,21 p.p.), con tempi fino a 8,32 min (Tab. 3).

## 8. Limitazioni dichiarate dagli autori
(a) Solo due tipi di profili di consumo in entrambi i casi (p. 12); (b) i coefficienti sono ex-ante e basati su dati storici o simulati: «intrinsic uncertainty»; (c) il PTC è programmato «to treat each producer as the only power source, overlooking the fact that a consumer may be supplied by multiple sources», con sovra-allocazione (p. 8); (d) il beneficio economico dipende dal prezzo di compensazione delle eccedenze, oggi basso (p. 11); (e) l'investimento è fuori ambito (p. 8); (f) raccogliere dati orari di tutti i partecipanti complica l'attuazione.

## 9. Future work dichiarati dagli autori
Elenco (pp. 10–12; verifica B.2): (i) più consumatori e maggiore diversità di profili (p. 10–11); (ii) vendita delle eccedenze tramite aggregatore o con accumulo (p. 11); (iii) ottimizzazione più complessa con altri KPI come obiettivi secondari (p. 12); (iv) «Further studies are needed to assess energy and economic balances combined…» (p. 12); (v) «Future work could also address more in detail the fairness aspect of allocation, i.e., assuring individual benefits for the REC's members, especially in the case of members in vulnerability.» (p. 12); (vi) KPI dei coefficienti ex-ante applicati a consumi orari misurati a posteriori (p. 12).
`[INFERENZA — test B.1]`
- (i), (ii), (iii), (iv), (vi): **autoreferenziali** (estensioni dello stesso metodo).
- (v): **generico** (equità dell'allocazione e benefici individuali dei vulnerabili), non legato al metodo; è l'unico ad avere peso come ancoraggio per un gap sull'equità, ma è una frase di chiusura senza argomentazione.

## 10. Note del lettore (inferenze mie)
- **Rilevanza diretta per la tesi: media.** Non ripartisce il beneficio con regole di teoria dei giochi, ma tre cose sono utili: (1) il confronto tra KPI di comunità e KPI individuali; (2) la differenza strutturale tra regime *ex-ante* spagnolo, dove la regola (i coefficienti) determina la torta, e regime italiano *ex-post*, dove l'energia condivisa è fissata dalle misure orarie e la regola ripartisce soltanto; (3) il richiamo esplicito all'equità individuale.
- **Evidenza (mia lettura della Tab. 4):** nel CS1 `SavingsREC` varia di pochi decimi di punto tra i 16 modi (32,03%–32,55%) mentre `SavingsComAreas` va da 18,03% a 28,32%: i KPI aggregati nascondono variazioni individuali ampie. Con due soli membri non si può generalizzare `[INFERENZA]`.
- **Incoerenze interne (mie verifiche):**
  - §3.3 (p. 10) dice che il modo migliore «coincided for both case studies» (OPT-CON-WDWE + M), ma per il CS1 §3.1.1 e la Tab. 4 indicano OPT-24 h − WDWE + M come migliore su `SCR_REC` (87,48% contro 87,25%).
  - Tab. 3 (p. 10): i totali di coefficienti non coincidono con quelli della Tab. 2 moltiplicati per il numero di consumatori in modo ordinato (CON-WDWE 24 e CON-M 4; 24 h-WDWE 384 e 24 h-M 64): sembrano scambiate le righe WDWE e M; non è possibile stabilirlo dal testo `[NON SPECIFICATO]`.
  - «Increase of 14%» nel CS1 (abstract) e «13,7%» (p. 9): con i valori della Tab. 4 (32,2/28,37) ottengo +13,5%, differenza trascurabile.
- **Fairness inteso come minimo individuale:** gli autori trattano l'equità come garanzia del beneficio individuale (individual rationality), non come distanza da una regola di riferimento: concetto vicino a quello del tuo codice (coalition excess) `[INFERENZA]`.
- **Non confrontabile direttamente con il caso italiano:** l'incentivo spagnolo è un risparmio in bolletta, non una tariffa premio sull'energia condivisa; i risultati non si trasferiscono senza adattamento.
