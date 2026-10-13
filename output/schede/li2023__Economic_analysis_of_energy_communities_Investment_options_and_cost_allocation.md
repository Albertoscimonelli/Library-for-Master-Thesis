# li2023 — Economic analysis of energy communities: Investment options and cost allocation

- **File sorgente:** `Paper/Economic analysis of energy communities_ Investment options and cost allocation.pdf` (15 pagine, testo estraibile)
- **Tipo:** articolo su rivista (Applied Energy, Elsevier, open access)
- **Lettura:** integrale (corpo pp. 1–13); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Li, N.; Okur, Ö. (2023). *Economic analysis of energy communities: Investment options and cost allocation.* **Applied Energy**, 336, 120706. DOI 10.1016/j.apenergy.2023.120706. Ricevuto 25/8/2022; rivisto 8/12/2022; accettato 14/1/2023; online 27/1/2023. Faculty of Technology, Policy and Management, TU Delft.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1; Sez. 1.3 p. 3):** analisi di fattibilità economica di una comunità energetica con due opzioni di investimento (terza parte vs auto-investimento dei membri), considerando diversi metodi di allocazione dei costi.
- **Gap dichiarato (p. 3, Sez. 1.3):** "it lacks economic feasibility analysis of energy communities with different investment options: self-investment and third party investment. In addition, the rules for cost allocation among local community members for both investment options have not yet been studied so far. Furthermore, the impacts of investment options on cost allocation are not known yet."
- **Contributi (p. 3):** (i) fattibilità economica delle due opzioni; (ii) impatto dei metodi di allocazione sui costi energetici delle famiglie; (iii) possibilità di più metodi di allocazione nella stessa comunità; (iv) modello di ottimizzazione con tre casi su dati reali.
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Paesi Bassi (prezzo di acquisto medio famiglie 2019 per consumi di 2500–5000 kWh: 0,2061 €/kWh; prezzo di vendita ipotizzato 0,10 €/kWh); nessun incentivo sull'energia condivisa tipo CER italiana.
- **Tipo di CER:** comunità di 10 famiglie con PV e batteria condivisi; caso di **terza parte** (aggregatore che investe e vende ai membri) e caso di **auto-investimento** collettivo (Fig. 2, p. 5).
- **Membri:** 10 famiglie, 2500–5000 kWh/anno, dati orari UK Power Networks 2012; PV da Renewables.ninja (2019) (pp. 8–9).

## 4. Metodo
- **Modello:** dimensionamento semplificato (PV = domanda annua × 1,1; batteria per un giorno medio senza PV; Eq. 1–2) e ottimizzazione MILP a due strati: livello famiglie (acquisto dalla comunità o dalla rete in base ai prezzi) e livello comunità (Eq. 11–28, pp. 6–8). Payback semplice, senza valore temporale del denaro (p. 5); prezzo fisso per tutta la vita (p. 9).
- **Parametri (Tab. 1, p. 9):** PV 240 €/kW (O&M 1,2, vita 25 anni); batteria 230 €/kWh (O&M 2,3, vita 12 anni, sostituzione a metà costo); EMS 10.000 €; connessione 20.000 €; cavi 1.000 €/casa; tasso di sconto 5%.
- **Software:** `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati (dei *costi*, Sez. 2.4)
- **M1 flat pricing** (stesso prezzo €/kWh a tutti).
- **M2 time-of-use** (prezzo di picco 16:00–23:00 e di fuori picco, legati da un fattore).
- **M3 segmented pricing** (prezzo sotto e sopra una soglia di consumo orario).
- Gli autori escludono i metodi della teoria dei giochi (Shapley, nucleolo) perché le famiglie "are not an independent entity, and thus there is no cooperation (coalition) between them" (p. 3).

## 6. Metriche
- **Economiche:** costo energetico delle famiglie su 25 anni (Tab. 2, 4, 5), profitto della terza parte, payback (anni), prezzo flat risultante (Fig. 7).
- **Equità / sociali / ambientali / engagement:** nessuna metrica quantitativa; solo osservazioni qualitative (la libertà di scelta del metodo "might get them more motivated to engage", p. 13).

## 7. Risultati principali
- **Riferimento (Tab. 2):** costo totale delle 10 famiglie in 25 anni acquistando dalla rete: 189.951 €.
- **Terza parte (pp. 9–10):** con payback di 15 anni il prezzo flat è 0,1989 €/kWh (appena sotto 0,2061 €/kWh); profitto massimo 64.767 € (54,62% dell'investimento, p. 12); le famiglie spendono 183.349 €, cioè 6.602 € in meno rispetto al riferimento.
- **Prezzi ToU e segmentati (Tab. 3):** fattore 0,86: picco 0,2031 e fuori picco 0,1960 €/kWh; fattore 0,72: sopra soglia 0,2029 e sotto soglia 0,1974 €/kWh. Con payback di 15 anni "there is no significant difference among the three cost allocation methods" (p. 10).
- **Più metodi nella stessa comunità (p. 10–11):** scegliendo per ogni famiglia il metodo più economico il costo totale scende di soli 305 € (183.044 vs 183.349 €); fattibile per payback 15–23 anni, non per 24–25.
- **Auto-investimento (Tab. 5, p. 12):** costi totali delle famiglie 118.582 € in 25 anni; per la terza parte 183.349 € (15 anni), 142.870 € (20), 118.582 € (25). I membri "benefit the most from a joint investment, despite the high initial investment costs".
- La varianza dei costi individuali fra i metodi è massima con payback di 25 anni (p. 12).

## 8. Limitazioni dichiarate dagli autori
Sez. 6.2 (p. 13) introdotta come "some limitations to the work, which lead to some recommendations for future work": (1) nel caso di auto-investimento i prezzi sono sotto il prezzo della rete; (2) prezzi costanti per tutta la vita; (3) solo due opzioni di investimento. Altre: dimensionamento "straightforward" perché l'ottimo è fuori obiettivo (p. 4).

## 9. Future work dichiarati dagli autori (Sez. 6.2, p. 13, verbatim)
"Firstly, for the self-investment-based energy community, the energy prices are set lower than the grid electricity price. It is possible to set energy prices higher than the grid electricity price, especially for ToU and segmented energy pricing methods. It is interesting to see how the pricing signals can affect the energy costs of households. Secondly, it is suggested to have energy prices for the energy community that vary every year, as long as the price is lower than the grid electricity price. [...] Therefore, it is recommended to have a risk-benefit analysis for the third party. Thirdly, besides the two investment options investigated in this paper, it is interesting to study the economic feasibility of hybrid investment options, e.g., households invest in PV panels, and a third party invests in community energy storage. Furthermore, with the hybrid investment, the allocation of operation costs to the two parties can be studied by using game theory."
`[INFERENZA — test B.1]` **Self-referential** (estensioni del proprio modello); utili solo per il tema investimento/allocazione.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` I tre metodi di allocazione producono differenze minime perché i prezzi sono vincolati entro ~0,7–0,8 c€/kWh dal prezzo di rete: l'esito "nessuna differenza significativa" dipende dalla regola di selezione dei prezzi, non da una proprietà dei metodi.
- `[INFERENZA]` Qui l'oggetto ripartito è il *costo di recupero dell'investimento* (non un incentivo): non è un caso di CER con incentivo sull'energia condivisa.
- `[INFERENZA]` Il paper cita come argomento per escludere la teoria dei giochi che le famiglie non sono indipendenti: posizione opposta a quella di molti altri paper del corpus (contraddizione metodologica da riportare in sintesi).
- `[INFERENZA]` Impostazione dei dati: carichi UK 2012, prezzi olandesi 2019, PV da Renewables.ninja: origine mista dei dati.
