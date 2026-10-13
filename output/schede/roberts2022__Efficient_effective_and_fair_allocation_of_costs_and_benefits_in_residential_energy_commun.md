# roberts2022 — Efficient, effective and fair allocation of costs and benefits in residential energy communities deploying shared photovoltaics

- **File sorgente:** `Paper/Efficient, effective and fair allocation of costs and benefits in residential energy communities deploying shared photovoltaics.pdf` (15 pagine, testo estraibile)
- **Tipo:** articolo su rivista (Applied Energy, Elsevier)
- **Lettura:** integrale (corpo pp. 1–14); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Valute in AU$.

## 1. Riferimento bibliografico
Roberts, M. B.; Sharma, A.; MacGill, I. (2022). *Efficient, effective and fair allocation of costs and benefits in residential energy communities deploying shared photovoltaics.* **Applied Energy**, 305, 117935. DOI 10.1016/j.apenergy.2021.117935. Ricevuto 10/3/2021; rivisto 21/9/2021; accettato 22/9/2021; online 8/10/2021. UNSW Sydney. Finanziato da Energy Consumers Australia (AP841).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1):** esplorare, con un caso reale di 72 appartamenti, come distribuire costi e benefici di un PV condiviso fra proprietari e residenti in una **embedded network (EN)** confrontando strutture tariffarie (volumetriche piatte o a fasce, con o senza demand charge) per recupero dell'investimento, incentivo a comportamenti efficienti e accettazione da parte dei clienti.
- **Contributo concettuale (p. 4):** il "**quadrilemma**" di quattro requisiti in conflitto — *cost-recovery*, *efficiency*, *consumer acceptance* e *universal benefit* (nessun cliente peggio del BAU).
- **Gap dichiarato (p. 5):** "To the authors' knowledge, none of these three contributions can be found in the existing literature" (negativa universale; i tre contributi sono: distribuzione fra attori con incentivi in conflitto e profili diversi; vincolo di *universal benefit*; effetto dell'opt-out sull'adozione di tariffe cost-reflective).
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Australia (NSW; strata title; clienti di una EN con diritto di uscire e passare al mercato retail); tariffe BAU Flat/ToU con sconto 15% (Tab. 1, p. 6). Non è un contesto CER europeo.
- **Tipo di CER:** rete incorporata di un edificio con PV condiviso (75, 110, 145 kW), investimento a carico della strata/proprietari in parti uguali (p. 6).
- **Membri:** 72 appartamenti (proprietari-occupanti, locatori, inquilini); misure semi-orarie per 28 appartamenti da giugno 2016 a maggio 2017; gli altri 44 stimati (p. 7).

## 4. Metodo
- **Modello:** strumento open source *morePVs* (esteso a più tariffe, con demand charge e risultati per appartamento) (p. 6). Confronto di configurazioni: PV individuali dietro il contatore (BTM_I), EN senza PV, EN con PV condiviso (EN_PV).
- **Schemi di distribuzione (Tab. 3):** Flat, ToU e Solar ToU con sconti `_15` (benefici tutti ai proprietari), `_H` (metà ai residenti) e `_Z` (tutto ai residenti, profitto EN nullo); *Pass-through* della tariffa del contatore madre con demand charge sul picco del consumatore (PT_D, PT_N, PT_Z) o sul contributo al picco dell'edificio (PTBP_D, PTBP_Z).
- **Software:** MorePVs; PVWatts/NREL SAM per il PV (p. 8).

## 5. Meccanismi di ripartizione analizzati
Tariffe interne (Tab. 3 sopra); la distribuzione fra proprietari è in parti uguali. Il lavoro cita la teoria dei giochi (Abada et al.) solo come letteratura: "simple pro-rata rules (per capita, pro-rata to volume or peak demand) can be efficient for similar households but, for households with diverse load profiles, there is a trade-off between equity and efficiency" (p. 3).

## 6. Metriche
- **Economiche:** NPV a 20 anni dei risparmi aggregati per appartamento; risparmio medio di bolletta nel primo anno; beneficio per i proprietari; autoconsumo PV.
- **Equità:** correlazioni di Pearson fra risparmio e caratteristiche di carico (energia media giornaliera, picco, metrica di autoconsumo; Tab. 8); distribuzione dei risparmi fra appartamenti (Fig. 4–7); Tab. 10 (valutazione qualitativa a simboli). L'articolo evita il termine "fairness" e usa "savings equity", "customer acceptance", "universal benefit" (p. 4).
- **Sociali / ambientali / engagement:** nessuna misura esplicita; accettabilità e trasparenza trattate qualitativamente.

## 7. Risultati principali (numeri dal paper)
- **Livello edificio (Tab. 5, p. 9):** NPV 20 anni dei risparmi per appartamento: EN_PV 75 kW AU$2.430; 110 kW AU$2.436; 145 kW AU$2.073; BTM_I 75/110/145 kW: 1.321/1.624/1.481; EN senza PV 2.231. Autoconsumo EN_PV 93%/80%/68%.
- **Tariffe che replicano il BAU:** beneficio ai proprietari AU$279 (Flat) e 209 (ToU) per appartamento/anno; nessun beneficio agli inquilini, che possono uscire dalla EN ("mini-death-spiral", p. 10).
- **Tariffe volumetriche scontate:** i residenti risparmiano, ma i benefici sono distribuiti in modo disuguale; correlazione del risparmio con l'energia media giornaliera 1,000 (Flat), 0,999 (ToU), 0,977 (SToU); con il picco 0,845/0,858/0,806 (Tab. 8, p. 11).
- **Pass-through (Tab. 9, p. 12):** PT_D aumenta la bolletta media di AU$193 con profitto EN di AU$403 per appartamento; singoli esiti da −AU$20 a +AU$416. PT_Z (profitto nullo): risparmio medio AU$209, ma "very uneven, and is uncorrelated with energy use, peak demand, contribution to building peak or self-consumption metric". PTBP_Z richiede un demand charge di 70,10 c/kW/giorno, e gli esiti individuali vanno da −AU$595 a +AU$1.288.
- **Conclusione (p. 13):** "the requirement for universal benefit therefore acts as a hard constraint on tariff design", che "effectively prohibits tariff arrangements (particularly application of peak demand charges) that incentivise socially beneficial behaviours".

## 8. Limitazioni dichiarate dagli autori
- p. 14 (Sez. 5): "a limitation of the study is that data was collected from only 28 of 72 apartments. In particular, some uncertainty is introduced by the assumption that the distribution of demand peaks of the metered apartments is representative of all the apartments. Additionally, in this analysis, household contribution to the building peak has been used as a proxy for cost-reflectivity."

## 9. Future work dichiarati dagli autori (p. 14, Sez. 5)
- "Further analysis would benefit from the development of an improved cost-reflectivity metric that includes a consumer's contributions (fixed, volumetric and peak demand) to the bill paid at the parent meter, the lower cost of photovoltaic energy and an additional element for repayment of infrastructure costs."
- "The list of potential tariff arrangements tested in this study is by no means exhaustive and future research might fruitfully explore a wider range of options."
- "It would also be of interest to include the impact of household demand response in the modelling, particularly where automation of significant loads such as electric hot water, air conditioning or electric vehicles could significantly increase solar self-consumption, reduce peak demand and improve outcomes for all consumers."
- "Further exploration of the implications under different existing and potential regulatory frameworks would be valuable."
`[INFERENZA — test B.1]` In prevalenza **self-referential** (più tariffe, demand response); l'ultimo punto (altri quadri regolatori) è più generale ma resta un'estensione del proprio caso.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Il vincolo di *universal benefit* ("no one worse off") è l'analogo della proprietà di razionalità individuale (P3 di `gonzalezasenjo2025`) in un contesto di opt-out: utile come concetto per i criteri di partecipazione/engagement.
- `[INFERENZA]` Il paper riguarda la *ripartizione dei costi di approvvigionamento tramite tariffe*, non di un incentivo sull'energia condivisa: non è comparabile con il regime CACER senza riformulare la funzione di valore.
- `[INFERENZA]` Mostra empiricamente che criteri di allocazione "cost-reflective" sul picco producono esiti individuali molto dispersi (da −595 a +1.288 AU$): un esempio di *dispersione dei benefici* come misura di rischio per l'adesione.
- `[INFERENZA]` Dati su soli 28 appartamenti su 72 con stima dei restanti 44: i risultati individuali dipendono da ipotesi dichiarate.
