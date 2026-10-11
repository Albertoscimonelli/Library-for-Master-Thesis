# casalicchio2022b — Optimal Allocation Method for a Fair Distribution of the Benefits in an Energy Community

- **File sorgente:** `Paper/Optimal Allocation Method for a Fair Distribution of the Benefits in an Energy Community.pdf` (11 pagine; testo estraibile; Tab. 1–7 e Fig. 3–6 lette su immagine perché le tabelle non sono estratte in modo utilizzabile)
- **Tipo:** articolo di tipo *Perspective* su rivista (Solar RRL, Wiley, open access CC BY), 9 pagine di testo + bibliografia e biografie
- **Lettura:** integrale (pp. 1–9); bibliografia (p. 10, 26 voci) letta.
- **Convenzioni:** pagine = indici di pagina del PDF (pp. 1–11 = 2100473 (1 of 11) … (11 of 11)). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Chiave `casalicchio2022b` = versione Solar RRL (breve, con regola di contributo e business model A–E); `casalicchio2022a` = versione Applied Energy (modello più ampio con DSM, scheda separata).

## 1. Riferimento bibliografico
Casalicchio, V.; Manzolini, G.; Prina, M. G.; Moser, D. (2022). *Optimal Allocation Method for a Fair Distribution of the Benefits in an Energy Community.* Solar RRL, 6(5), 2100473. DOI 10.1002/solr.202100473. Ricevuto 30/06/2021, rivisto 09/09/2021, pubblicato online 28/10/2021. EURAC Research (Bolzano); Politecnico di Milano. Finanziamento: nessuno dichiarato, salvo copertura dei costi di open access della Provincia Autonoma di Bolzano (p. 9). Conflitti di interesse: dichiarati assenti. Dati e codice: `[NON SPECIFICATO]`. Il modello di EC è citato come in revisione ([14] = `casalicchio2022a`).

## 2. Obiettivo e research question
- **Obiettivo (abstract p. 1; pp. 2–3):** proporre un metodo per la distribuzione ottima del beneficio fra i partecipanti "based on their own contribution to the system", da confrontare con altri metodi (business model, BM) tramite un indice di equità; il modello di EC è un LP a singolo obiettivo (oemof); il contributo di ciascun utente si quantifica con ottimizzazioni sequenziali; si studia l'effetto dell'eterogeneità della comunità.
- **Gap dichiarato (pp. 1–3):** "An important aspect in this context, not assessed and considered in detail, concerns the distribution of the economic benefit among participants and the impact of the composition of the EC. In fact, at the regulatory level, no indication is given about how to distribute and allocate the economic benefit arising from the establishment of the EC, but this choice is left to the EC itself." (p. 1); "there are very few researches that assess it in detail as refs. [2,3,6,7]" (p. 3). Lo Shapley "has the disadvantage of a high computational burden" e il Nucleolo "grows exponentially with the size of the EC and does not satisfy fairness, by favoring members who do not install generation units" (p. 1 e p. 2, citando [3] = `moncecchi2020` per lo Shapley e [7] = Fioriti, Frangioni, Poli, Applied Energy 2021 per il Nucleolo; [7] è nel corpus come "Optimal sizing of energy communities with fair revenue sharing and exit clauses").
  `[INFERENZA — test B.3]` "very few researches" non è un'universale negativa vera e propria, ma non è verificabile; l'affermazione sul Nucleolo non è confermata da questo paper (nessun confronto numerico).
- **RQ formulata come domanda?** No. Contributi (p. 2): euristica basata sul contributo marginale; indice di equità (FI) del business model; analisi dell'impatto dell'eterogeneità.

## 3. Contesto
- **Paese / quadro normativo:** Italia (regole ARERA, MiSE, GSE del 2020, p. 4). Tab. 1 (p. 5): componenti della bolletta (materia energia 48–89 €/MWh; trasporto e gestione del contatore 8,61 €/MWh; oneri di sistema 33–74 €/MWh; imposte 36–40 €/MWh), rimborso ARERA 7,61 + 0,61 €/MWh, rimborso MiSE 110 €/MWh per la REC.
- **Tipo di CER:** 6 edifici monofamiliari, ciascuno un membro (B1–B6); PV e batterie ottimizzati; stesso profilo PV normalizzato per tutti (caso 1) o profili diversi (caso EC #5).
- **Membri:** profili di carico da LoadProfileGenerator, scalati al consumo italiano medio; composizioni: 1 residente, coppia senza figli, coppia con figli, 4 residenti single con figli, 5 residenti, 6 residenti (Fig. 2). Casi ad hoc: "These case studies have been generated ad hoc to show the potential of the introduced model." (p. 4)

## 4. Metodo
- **Modello di EC (Sez. 2.1, p. 2):** oemof, minimizza `OF_EC = Σ E·vc + inv·epc` (Eq. 1) con ottimizzazione di operazione ed espansione di capacità (da [14]). Parametri (Tab. 2, p. 5): PV 1198 €/kW (OPEX 1,5%, vita 30 anni), batteria 587 €/kWh (OPEX 5%, 15 anni), sconto 5%, detrazione 50% del CAPEX.
- **Contributo e distribuzione (Sez. 2.2, p. 3):** `MC_i = opt(EC) − opt(EC∖{i})` (Eq. 2); `D_cd,i = MC_i/Σ_i MC_i` (Eq. 3–4), "inspired by the Vickrey–Clarke–Groves (VCG) mechanism". Si ottiene con `m_tot + 1` simulazioni contro `2^m_tot` dello Shapley: "the number of combinations simulated is reduced by 90%" (p. 5–6, con 6 membri: 7 contro 64).
- **Business model (Sez. 2.3 e Appendice, pp. 3, 9):** BM A omogeneo includendo gli investimenti (`1/m_tot`, Eq. 9); BM B omogeneo escludendo gli investimenti (Eq. 10); BM C in proporzione ai carichi (Eq. 11); BM D in proporzione al numero di persone (Eq. 12); BM E in proporzione all'autoconsumo (Eq. 13). Nel testo di p. 3 il quinto BM è chiamato "BM F": `[INFERENZA]` refuso (l'Appendice lo definisce BM E).
- **Indici (Sez. 2.4, pp. 4–5):** indice di Gini normalizzato come misura di eterogeneità della composizione (Eq. 6; `GI` = 0 se tutte le famiglie sono uguali, 1 se le frequenze sono uniformi); Fairness Index `FI(m)` (Eq. 8) come in `casalicchio2022a`: `Σ|D_BM,i − D_cd,i|/Σ|D_w,i − D_cd,i|` se tutti hanno quota positiva, altrimenti il numero di "unhappy members"; la distribuzione peggiore `D_w` "is the one that distributes all the benefit obtained to only one member, the one who is contributing the least" (p. 4).
- **Software:** `[NON SPECIFICATO]` (oemof è un framework in Python; il paper non indica il solver).

## 5. Meccanismi di ripartizione analizzati
Distribuzione "ottima" per contributo marginale normalizzato (riferimento) contro BM A–E (sopra). Il paper considera la quota di beneficio come "income that remains after accounting for all expenses, and costs" (p. 3).

## 6. Metriche
- **Economiche:** risparmio in bolletta (%) e capacità installate (Fig. 3, 5); quota di contributo di ciascun utente (Fig. 4, 6).
- **Energetiche:** autoconsumo e energia condivisa in % (Tab. 4, 7).
- **Equità:** FI e deviazione standard `σ` della differenza fra distribuzione BM e distribuzione di riferimento (Tab. 5); indice di Gini della composizione come descrittore (Eq. 6).
- **Sociali, ambientali, engagement:** nessuna; il FI conta anche i membri "unhappy" (quota non positiva) e il testo parla di "free and voluntary participation" (p. 9).

## 7. Risultati principali (numeri dal paper)
- **Impatto dell'eterogeneità (Tab. 3–4, Fig. 3, pp. 5–6):** 4 composizioni con `GI` = 0, 0,33, 0,8, 1 (carico 21,6, 19,5, 17,6, 19,4 MWh): PV installato 12, 11, 10, 11 kW; batteria 3, 3, 2, 1 kWh; risparmio in bolletta 43%, 42%, 43%, 48%; autoconsumo 35,8, 34,4, 33,5, 36,2%; energia condivisa 0,0, 1,0, 3,4, 5,2%. Gli autori: la batteria "decreases by about 67% as heterogeneity increases" (3 → 1 kWh) e il beneficio sale del 12% da `GI` = 0 a 1 (abstract) o del 14% da 0,33 a 1 (p. 9).
- **Contributi:** con utenti uguali "no one contributes more to the welfare than the others" (p. 6); con maggiore eterogeneità un'allocazione omogenea "would be not fair for 5 users out of 6 already in the second graph where only a user is different" (p. 6).
- **FI dei BM (Tab. 5, p. 7; FI/σ):** EC #1 (GI = 0): tutti 0,000. EC #2 (GI = 0,33): A 0,116/0,053; B 0,0031/0,001; C **0,0006**/0,000; D 0,011/0,005; E 0,052/0,024. EC #3 (GI = 0,8): A 0,126/0,054; B 0,027/0,012; C **0,025**/0,011; D 0,085/0,041; E 0,096/0,036. EC #4 (GI = 1): A 0,200/0,085; B **0,026**/0,011; C 0,030/0,011; D 0,139/0,055; E 0,129/0,058. Raccomandazioni degli autori: BM C (in base ai carichi) per `GI` = 0,33 e 0,8, BM B per `GI` = 1; BM A "will not be recommended for a high heterogeneity EC" (FI = 0,200) (p. 9).
- **Profili PV diversi (Tab. 6–7, Fig. 5–6, pp. 7–8):** a `GI` = 0 con profili PV diversi (EC #5): autoconsumo 35,8 → 47,4% (+32%), energia condivisa 0 → 3,8%, PV 12 → 14 kW (+17%), batteria 3 → 7 kWh (+133%), risparmio in bolletta 43 → 62% (+44%); contributi per utente fra 14% e 20% invece del 16,7% uguale.
- **Abstract:** "their contribution is measured and ranges between 10% and 97%" (p. 1; ripetuto a p. 9: "from 10% to 97%").

## 8. Limitazioni dichiarate dagli autori
Citazioni testuali:
- "These case studies have been generated ad hoc to show the potential of the introduced model." (p. 4)
- "The distribution of benefits based on the marginal contribution of each member is feasible from a computational point of view, although the calculation time increases with the number of users of the EC." (p. 3)
- "For simplicity, we have shown only single-family housing buildings, but it is certainly possible to carry out the same analysis by using the described tool while also considering multifamily housing buildings." (p. 9)
- Se un membro non contribuisce, "in necessary cases the society could proceed according to other criteria and might still want to allocate something to this member (i.e., in energy poverty, where people are unable to access energy)" (p. 3).
- `[INFERENZA]` Non dichiarati: 6 membri, stesso profilo PV in quasi tutti i casi, composizioni scelte a mano; nessun confronto con lo Shapley né con altri criteri di ripartizione oltre ai 5 BM.

## 9. Future work dichiarati dagli autori
Elenco completo (B.2): non c'è una sezione di future work. L'unica indicazione è la frase conclusiva sui multifamiliari (p. 9, sopra). `[INFERENZA — test B.1]` Non utilizzabile per fondare un gap (autoreferenziale, minima).

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` **Rapporto con `casalicchio2022a`.** Stessa regola (Eq. 2–4 = Eq. 12–13 di `casalicchio2022a`), stesso FI, ma con 5 BM diversi (qui A–E con "omogeneo con/senza investimenti", carichi, persone, autoconsumo; là A–E con investimento, DSM, autoconsumo, edificio, carichi) e 6 membri anziché 21; non aggiunge risultati indipendenti sulle proprietà della regola. Lo stesso gruppo non confronta mai la regola con Shapley.
- `[INFERENZA]` **Il range "10%–97%" non è riconducibile ai risultati mostrati.** Le quote `D_cd,i` sono normalizzate (somma 1): in Fig. 4 la barra colore dei contributi per `GI` = 1 va da circa 5 a circa 30%, e per EC #5 da 14 a 20% (Fig. 6). Il paper non spiega a cosa si riferisca "10% to 97%" (probabilmente un'altra grandezza, es. contributo marginale rispetto al risparmio totale; `[NON SPECIFICATO]`).
- `[INFERENZA]` **Il FI è circolare e discontinuo** (come in `casalicchio2022a`): misura la vicinanza al riferimento proposto dagli stessi autori; vale in [0,1) se tutti hanno quota positiva e diventa un intero (membri "unhappy") altrimenti; `D_w` qui è definita (tutta la quota al membro che contribuisce meno), ma il FI in Tab. 5 non supera 0,2 e non attiva mai il regime "conteggio".
- `[INFERENZA]` **Eterogeneità come variabile del problema.** Con utenti uguali qualsiasi distribuzione uniforme coincide con il riferimento (FI = 0 per tutti i BM nel caso EC #1): il confronto fra BM ha contenuto solo quando i membri differiscono. La conclusione "a model will be more or less suitable depending on the composition" è basata su tre composizioni scelte ad hoc e su un indice (Gini–Simpson) che non misura la disuguaglianza dei consumi (cfr. `casalicchio2022a`, Sez. 10).
- `[INFERENZA]` **Incongruenze minori:** a p. 6 "see the lowest FI in Table 6" ma la tabella dei FI è la Tab. 5; "BM F" a p. 3 contro BM E in Appendice; il confronto di benefici "12%" (abstract) e "14%" (conclusioni) usa coppie di composizioni diverse (`GI` 0→1 e 0,33→1) senza dichiararlo nell'abstract.
- `[INFERENZA]` Rilevanza per la tesi: (i) formulazione compatta della regola di contributo marginale (N + 1 simulazioni) e di cinque BM semplici, riproducibile in un modello con il solo ciclo "ottimizza con e senza il membro `i`"; (ii) dà un esempio di come una scelta di BM dipende dall'eterogeneità dei membri, ma senza stabilità né confronto con regole di teoria dei giochi.
