# avanzini2026 — Comparison of virtual energy sharing schemes for renewable energy communities under European regulations: A mixed-use case study in Italy

- **File sorgente:** `Paper/Comparison_of_virtual_energy_sharing_schemes_for_renewable_energy_communities_under_European_regulations__A_mixed_use_case_study_in_Italy.pdf` (16 pagine; testo estraibile; Tab. 6 e 7 ricostruite dal testo con `pdftotext -layout`; le figure 7–13 non sono state ispezionate)
- **Tipo:** articolo su rivista (Energy Reports, open access CC BY-NC); studio di simulazione (UBEM) su un caso reale parzialmente misurato.
- **Lettura:** integrale (corpo pp. 1–15); Appendice B (Tab. B.1–B.6, parametri degli edifici) non presente nel PDF; bibliografia (pp. 15–16) letta come elenco.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente. Le virgolette riportano il testo degli autori.

## 1. Riferimento bibliografico
Avanzini, M.; Guarino, F.; Cellura, M. (2026). *Comparison of virtual energy sharing schemes for renewable energy communities under European regulations: A mixed-use case study in Italy.* **Energy Reports**, 16, 109785. https://doi.org/10.1016/j.egyr.2026.109785. Ricevuto 24/4/2026; rivisto 11/9/2026; accettato 27/9/2026; online 6/10/2026. Università di Palermo (Center for Sustainability and Ecological Transition; Dipartimento di Ingegneria). Finanziamenti: `[NON SPECIFICATO]`. Dati: «Data will be made available on request.» (p. 15).

## 2. Obiettivo e research question
- **Obiettivo (abstract p. 1; p. 5):** analizzare la prestazione tecno-economica di una REC mista (campus universitario e quartiere residenziale) con sei scenari: due schemi di condivisione virtuale, Virtual Self-Consumption (VSC) e Virtual Net Metering (VNM), per tre configurazioni di proprietà del FV (produttore esterno centralizzato, prosumer centralizzato, prosumer decentralizzati).
- **Gap dichiarati (pp. 2, 5):** «the extent to which different enabling frameworks influence the actual techno-economic performance of RECs remains insufficiently quantified» (p. 2); «a relevant research gap persists in the analysis of interactions between residential and non-residential buildings within mixed-use RECs» (p. 5); «many devote limited attention to how the produced energy is allocated and shared among community members» (p. 5); «limited attention has been given to how different accounting mechanisms may alter the relationship between energy performance and economic outcomes, potentially leading to divergent incentives for REC participants» (p. 5).
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Italia (Palermo, zona prezzo Sicilia), ma i due schemi sono presentati come paradigmi europei (Tab. 1, p. 4: VNM, fra gli altri, in Austria, Croazia, Finlandia, Grecia, Lussemburgo, Portogallo, Slovenia e Spagna; VSC in Germania e in Italia). Definizioni operative (p. 3): VSC = «ex-post accounting of the simultaneity between electricity production and consumption»; VNM = allocazione ex ante di quote della produzione (statiche o dinamiche) «regardless of when members consume electricity». Per l'Italia (p. 4): un produttore terzo può mettere a disposizione la produzione di una REC senza esserne membro.
- **Tipo di REC:** mista, 38 edifici: 13 dell'università (campus Viale delle Scienze, consumi mensili misurati) e 25 blocchi di appartamenti del quartiere Cuba-Calatafimi (anni 1960–70; consumi simulati e tarati su TABULA) (pp. 6–7).
- **Proprietà (p. 7):** VSC1/VNM1: l'università è produttore esterno (2,75 MW, 3,96 GWh/anno); VSC2/VNM2: l'università è prosumer (stessa taglia); VSC3/VNM3: tutti gli edifici prosumer (3,7 MW, 5,33 GWh/anno). Consumo totale 9,18 GWh/anno (solo residenziale) o 18,11 GWh/anno (con università).

## 4. Metodo
- **Modello:** City Energy Analyst (UBEM) a passo orario, anno meteorologico tipo; FV sul 50% della superficie di copertura disponibile (baseline); sensibilità 30–70%.
- **Allocazione VNM (Eq. 1a, p. 8):** quota oraria di produzione a ciascun edificio proporzionale alla superficie lorda (`PVQuota_b,h = Σ PVProduction · A_b / Σ A_b`), cioè **una sola chiave statica per area**. VSC: nessuna allocazione ex ante (Eq. 1b).
- **Energia condivisa nel VSC (Eq. 6, p. 9):** `REC_Self_h = min(Σ_b PVSurplus_b,h ; Σ_b EUncovered_b,h)` — il minimo orario fra eccedenza totale e carico residuo dopo l'autoconsumo diretto (struttura come nel tuo modello, `[INFERENZA]`).
- **Economia (pp. 9–10):** risparmio da autoconsumo (diretto e, in VNM, virtuale) valorizzato a 300 €/MWh (media offerte ARERA 2025); eccedenza venduta a prezzo zonale (media Sicilia 2025: 116 €/MWh, con minimo garantito 46,8 €/MWh); incentivo (Eq. 13–14): `REC_incentive_h = REC_Self_h · (TIP_h + TIP_reg + contributo ARERA)` con `TIP_h = min(120, 80 + max[0, 180 − p_zone,h]) €/MWh` (impianti < 200 kW), correzione regionale +10 €/MWh (Nord) e +4 €/MWh (Centro), contributo ARERA 10,57 €/MWh (GSE 2025). Nessun costo di investimento.
- **Sensibilità (p. 10):** quota di FV 30–70%; prezzi zonali 2019–2025 (Italia e Sicilia; Tab. 5).
- **Software:** CEA (Python); `[NON SPECIFICATO]` solutori e tempi.

## 5. Meccanismi di ripartizione analizzati
Non si ripartiscono i benefici fra i membri. Si confrontano **due regole di contabilizzazione della condivisione** (VSC ex post sull'aggregato; VNM ex ante con chiave statica per area) con tre assetti proprietari. La ripartizione interna dei ricavi è esplicitamente fuori modello (p. 13).

## 6. Metriche
- **Energetiche (Eq. 7–10, p. 9):** DSC, VSC rate, DSS, VSS rate (tassi di autoconsumo e autosufficienza diretti e virtuali).
- **Economiche:** risparmi diretti, risparmi virtuali (VNM), incentivo (VSC), vendita dell'eccedenza, ricavo totale (Tab. 7).
- **Sociali / ambientali / equità / engagement:** nessuna.

## 7. Risultati principali (numeri dal paper)
- **Tab. 6, baseline (p. 13):** (DSC / VSC rate / DSS / VSS rate) VSC1 – / 80,5% / – / 35,2%; VSC2 68,8% / 99,0% / 15,1% / 21,8%; VSC3 76,0% / 95,9% / 22,5% / 28,4%; VNM1 – / 76,8% / – / 33,6%; VNM2 43,2% / 90,5% / 9,5% / 19,9%; VNM3 63,6% / 86,2% / 18,8% / 25,5%.
- **Tab. 7, baseline (p. 13), ricavo totale:** VSC1 865.936 € (incentivo 406.250 + vendita 459.686); VSC2 1.113.673 € (risparmi diretti 817.969; incentivo 152.266; vendita 143.438); VSC3 1.498.806 € (1.216.024; 134.581; 148.201); VNM1 1.020.121 € (risparmi virtuali 913.692; vendita 106.429); VNM2 1.119.643 € (diretti 513.823; virtuali 562.123; vendita 43.697); VNM3 1.464.349 € (1.016.391; 362.865; 85.093). Verifica mia: le somme tornano per tutte e sei le righe.
- **Energia:** «VSC schemes consistently achieve higher self-consumption and self-sufficiency rates than VNM schemes across all scenarios» (p. 14); la chiave statica per area riduce l'autoconsumo diretto degli edifici che producono sopra la propria quota.
- **Economia:** differenze «around 2%» fra VSC e VNM in VSC2/VNM2 e VSC3/VNM3, perché l'energia condivisa in VNM è contabilizzata come risparmio a prezzo di mercato (300 €/MWh), molto sopra l'incentivo (116 €/MWh in media); VNM1 batte VSC1 (1.020 k€ contro 866 k€) perché senza autoconsumo diretto il valore sta tutto nella condivisione (p. 11).
- **Abstract:** autoconsumo +35% (VSC) e +25% (VNM) rispetto alla baseline; ricavi fino a +20% in entrambi.
- **Conclusioni (p. 15):** «the economic outputs are largely decoupled from energy performance and are mainly determined by accounting rules, including incentive tariffs and market price structures, which can offset or even override the advantages observed in energy indicators.»

## 8. Limitazioni dichiarate dagli autori
- p. 13: «The implications for individual actors ultimately depend on how the revenues from shared energy are redistributed within the REC, which is not modelled in this study».
- p. 15: «the current framework does not account for more complex sharing mechanisms, such as dynamic pricing or P2P trading, nor for demand-side flexibility or storage».
- Nessun costo di investimento (p. 10); una sola chiave statica per VNM (p. 11: «Clearly, the application of dynamic sharing keys with more sophisticated allocation criteria […] could improve the performance of VNM schemes»); dati su richiesta.
- `[INFERENZA]` Non dichiarati: un solo caso (38 edifici), domanda residenziale simulata e non misurata, un solo anno tipo, aggregazione degli utenti residenziali per edificio (non per famiglia).

## 9. Future work dichiarati dagli autori
Elenco completo (Conclusioni, pp. 14–15; verifica B.2): (i) chiavi di condivisione dinamiche per migliorare il load matching del VNM («the adoption of dynamic sharing keys could improve the load-matching performance of VNM schemes»); (ii) incentivi più alti per rafforzare l'attrattività del VSC; (iii) applicare le strategie di ottimizzazione della letteratura a entrambi gli schemi («the relative advantages ultimately depend on their regulatory implementation»); (iv) meccanismi più complessi (dynamic pricing, P2P), flessibilità lato domanda e storage (limitazione indicata come direzione di ricerca).
`[INFERENZA — test B.1]` Il paper confronta due schemi di contabilizzazione e non regole di ripartizione; (i) e (iii) sono estensioni del proprio modello (autoreferenziali), (iv) è generale ma fuori tema (mercati e flessibilità). La frase di p. 13 sulla ripartizione interna è una **limitazione dichiarata**, non un future work formulato.

## 10. Note del lettore (inferenze mie)
- **Evidenza indipendente che il «livello di valorizzazione» pesa più della regola di energia.** Con un incentivo regolato (TIP) e un risparmio a prezzo di mercato (VNM) la stessa configurazione fisica dà esiti economici paragonabili: il valore ripartibile dipende da come si contabilizza, non solo da quanta energia si condivide. Sostiene la separazione in due strati del tuo modello (valorizzazione senza gradi di libertà; allocazione come oggetto di studio).
- **Composizione mista.** L'effetto dei prosumer non residenziali (grandi consumatori e produttori) su autoconsumo e redditività è il contributo dichiarato; è un'ancora debole per l'asse «composizione per categoria» (un caso, nessuna ripartizione interna) ma coerente con `povolato2023`, `minuto2022` e `giudice2026` sulle composizioni. Il ruolo dell'università come produttore esterno corrisponde al caso «produttore puro» che nel tuo progetto è la lettera `E` del nome della scheda `CER_C_P_E`.
- **Confronto con il tuo modello (README):** (a) energia condivisa `min(Σ eccedenze, Σ carichi residui)` — stessa struttura; (b) l'incentivo qui comprende, oltre alla TIP e alla correzione regionale, il contributo ARERA di 10,57 €/MWh; `Biancardi et al.` (`biancardi2026`) riporta lo stesso valore (0,01057 €/kWh), `marrasso2025` una componente cost-reflective «V» (0,7780 c€/kWh, 2022): va controllato se `P_CER_h` nel tuo codice la include `[da verificare nel codice e nella norma; non ho letto Paper/Directive]`.
- **Possibile incongruenza di lettura:** il paper usa «VNM» per un'allocazione ex ante a quote, mentre `minuto2022` lo definisce come flusso netto fra POD come se fossero un unico POD virtuale (p. 3 di questo paper lo riporta); sono usi compatibili ma non identici `[INFERENZA]`.
- **Limite per l'uso come ancora:** nessuna regola di ripartizione fra membri, nessun indicatore di equità; non è un confronto di regole.
