# sassone2024 — A Profit Optimization Model for Renewable Energy Communities based on the Distribution of Participants

- **File sorgente:** `Paper/A Profit Optimization Model for Renewable Energy Communities Based on the Distribution of Participants.pdf` (6 pagine, testo estraibile)
- **Tipo:** conference paper (IEEE, EEEIC / I&CPS Europe 2024)
- **Lettura:** integrale del corpo (pp. 1–6); bibliografia non letta riga per riga. Alcune formule e la Tab. II sono estratte in modo disordinato dal PDF: gli elementi incerti sono segnalati.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Sassone, A.; Ahmed, S.; D'Angola, A. (2024). *A Profit Optimization Model for Renewable Energy Communities based on the Distribution of Participants.* 2024 IEEE International Conference on Environment and Electrical Engineering and 2024 IEEE Industrial and Commercial Power Systems Europe (EEEIC / I&CPS Europe). DOI 10.1109/EEEIC/ICPSEUROPE61470.2024.10751093. School of Engineering, University of Basilicata, Potenza.

## 2. Obiettivo e research question
- **Obiettivo (autori, p. 2):** valutare "the best number distribution of prosumers and consumers inside the REC, in order to obtain the maximum profitability", rispettando i vincoli normativi. I consumatori possono diventare prosumer (da t0 a t1, Fig. 2).
- **RQ formulata come domanda?** No; esiste un obiettivo di ottimizzazione.

## 3. Contesto
- **Paese / quadro normativo:** Italia. Potenza massima della REC 1 MW (rif. [26] del paper); CER riferita a una cabina primaria (p. 2). Valorizzazione dell'energia condivisa e delle perdite evitate secondo GSE / "Decreto CER" (rif. [26], [30]; p. 4).
- **Tipo di CER:** REC solo-fotovoltaico; prosumer con impianto individuale o comune (Fig. 1); membri produttori e consumatori.
- **Membri:** REC "chiusa" con Nc + Np = 100 partecipanti; consumatori e prosumer hanno lo stesso profilo di carico (casa unifamiliare a due piani, dati RSE basati su un'indagine ISTAT su 20.000 famiglie; p. 4). Località: Potenza (p. 4).

## 4. Metodo
- **Modello:** enumerazione di tutte le combinazioni (Nc, Np) con Nc + Np fisso (flowchart Fig. 3, p. 3). Per ciascuna combinazione bilanci orari: energia condivisa = min(eccedenza PV non autoconsumata, carico orario dei consumatori) (Eq. 2, p. 3); vincolo di potenza REC < 1 MW (Eq. 9).
- **Ipotesi chiave:** tutti i prosumer hanno la stessa domanda Dp; il PV di ciascuno è dimensionato per coprire una frazione fissa della domanda annua (60%, 80%, 95%; Eq. 8, p. 3).
- **Indicatore economico:** NPV con CAPEX, OPEX, altri costi, ricavi da autoconsumo, vendita e energia condivisa (Eq. 10–12, p. 3); "profitability" = profitto con REC − profitto senza REC (Eq. 13–14, p. 4).
- **Parametri (Tab. II, p. 4; mappatura delle righe incerta per l'estrazione):** PV 1100 €/kWp; vita utile 20 anni; tasso di sconto 3%; degrado PV 1%/anno; valorizzazione energia condivisa 0,12 €/kWh; valorizzazione perdite di distribuzione evitate 0,00848 €/kWh; costo di gestione/consulenza 500 €/anno.
- **Dati:** PVGIS (produzione PV), RSE (carichi). Risoluzione oraria. Simulazioni per stagione.
- **Software:** `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati
**Nessuno.** Il paper calcola il guadagno aggregato della REC rispetto al caso senza REC, non come viene distribuito fra i membri. Una frase generica (p. 2) dice che i consumatori "receive a part of the benefit of the incentive", senza definire alcuna regola.

## 6. Metriche
- **Economiche:** profitto/NPV della REC e differenza REC vs non-REC.
- **Tecniche:** energia condivisa, venduta, autoconsumata.
- **Sociali / equità / engagement:** nessuna misura (benefici sociali e ambientali citati solo come motivazione).
- **Ambientali:** nessuna misura propria (cita un valore di CO₂ evitata da un altro studio, rif. [15], p. 1).

## 7. Risultati principali
- Esiste una composizione ottima (p. 4): **40 prosumer e 60 consumatori** se la copertura della domanda dei prosumer è 80% o 95% (potenza PV totale 50 kWp o 59,3 kWp); con 60% l'ottimo è Np = 50 con 46,8 kWp.
- Configurazioni estreme (90 prosumer + 10 consumatori; 10 prosumer + 90 consumatori) producono meno energia condivisa e meno profitto (p. 5, Fig. 9–10).
- I valori numerici del profitto sono solo nelle figure (Fig. 4): `[NON SPECIFICATO nel testo]`.

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata; nessuna limitazione dichiarata esplicitamente nel testo.

## 9. Future work dichiarati dagli autori
- p. 6 (Sez. IV): "This work could be a helpful tool for the design and management of a REC and can be extended in future in order to consider different classes of renewable production and load in which participant could be inserted. Class distribution could give a more detailed analysis of information to be adopted in the design optimization of a REC. Moreover, in the study the role of storage can be included in order to investigate the possible technical and economical benefit on the profit."

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Il titolo parla di "profit … based on the distribution of participants" ma non c'è alcuna regola di ripartizione dei benefici: il paper è utile solo per il tema *composizione della CER*.
- `[INFERENZA]` Membri omogenei per costruzione (stesso profilo di carico, stessa domanda): impossibile misurare equità o dispersione dei benefici.
- `[INFERENZA]` Future work *self-referential* (estensione del proprio modello a classi di carico/produzione e storage): non regge da solo un gap generale.
- `[INFERENZA]` I valori di profitto non sono in tabella: non si possono citare numeri senza rielaborare le figure.
