# ceglia2022 — Addressing Energy Poverty in the Energy Community: Assessment of Energy, Environmental, Economic, and Social Benefits for an Italian Residential Case Study

- **File sorgente:** `Paper/Addressing_Energy_Poverty_in_the_Energy_Community.pdf` (22 pagine)
- **Tipo:** articolo su rivista (Sustainability, MDPI, open access)
- **Lettura:** integrale. **Nota di leggibilità:** nel PDF le pp. 5–14 hanno due strati di testo sovrapposti (numerazione "x of 22" e "x of 23"); l'estrazione standard è parzialmente illeggibile. Ho riletto Metodi e Risultati con estrazione `-raw` (pulita) e verificato la Fig. 12 sull'immagine della pagina 16. Bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF (la numerazione stampata "x of 22" coincide solo per alcune pagine). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Ceglia, F.; Marrasso, E.; Samanta, S.; Sasso, M. (2022). *Addressing Energy Poverty in the Energy Community: Assessment of Energy, Environmental, Economic, and Social Benefits for an Italian Residential Case Study.* **Sustainability**, 14(22), 15077. https://doi.org/10.3390/su142215077. Ricevuto 4/10/2022; accettato 8/11/2022; pubblicato 14/11/2022. Università del Sannio; Durham University; KIIT.

## 2. Obiettivo e research question
- **Obiettivo (autori, p. 4):** (i) valutare i benefici energetici, ambientali, economici e sociali di una REC fotovoltaica nel sud Italia rispetto al caso senza REC, per valutare la mitigazione della povertà energetica (EP); (ii) definire un nuovo indicatore sociale per misurare il potenziale della REC nel mitigare l'EP.
- **Gap dichiarato (p. 4):** "the capability of RECs to mitigate EP has scarcely been investigated in the scientific literature, especially in comprehensive studies which aimed to assess the contemporary energy, environmental, economic, and social aspects of these new entities."
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Italia (San Felice a Cancello, Caserta; zona climatica C). Condivisione **virtuale** sotto la stessa cabina primaria (direttive ARERA; p. 8). Incentivo per l'energia condivisa 0,169 €/kWh "including all contributions"; prezzo di vendita 0,047 €/kWh (Ritiro Dedicato); prezzo di acquisto 0,32 €/kWh IVA inclusa (p. 12).
- **Tipo di CER:** REC residenziale con impianto PV comune da 18 kWp sul tetto dell'edificio di R#1 e R#2 (circa 202 m²). Il gas naturale per riscaldamento/ACS e le pompe di calore reversibili non sono parte della condivisione (solo elettricità; p. 9).
- **Membri:** 3 utenze residenziali in 2 edifici: R#1 e R#2 (stessa palazzina, 100 e 140 m²), R#3 (villetta del 1970 riqualificata nel 2020, a circa 300 m). Carichi reali 2021 da dati DSO a livello di POD: 5197, 3746 e 4398 kWh/anno (p. 6).

## 4. Metodo
- **Modello:** simulazione dinamica oraria di un anno con HOMER Pro (REC) e post-processing in MATLAB (e Excel); confronto fra "simple users" (SU, senza PV) e REC (p. 10–11).
- **Equazioni (pp. 11–13):** energia condivisa = min(prelievo dalla rete tramite la cabina, produzione PV immessa) (Eq. 1); indici di autosufficienza `s` e autoconsumo `d` (Eq. 2–3); risparmio di energia primaria con rendimento orario del sistema elettrico italiano (Eq. 4); emissioni di CO₂ con fattori orari (Eq. 5–7); costi operativi SU e REC (Eq. 8–10); payback semplice `SPB = f·IC_PV / OC_REC` (Eq. 11); indicatori di povertà energetica "10%" (costo energetico totale / reddito) e **10%_ISEE** (costo / ISEE, con ISEE = redditi + 20% del patrimonio) (Eq. 12–13).
- **Parametri economici (Tab. 5, p. 17):** investimento PV 18.000 €; manutenzione 1.800 €/anno; incentivo 20 anni; quota di investimento coperta da supporto economico f = 50%.

## 5. Meccanismi di ripartizione analizzati
**Nessun meccanismo di ripartizione tra i membri è definito o confrontato.** Il paper confronta REC vs non-REC e riporta indicatori per utente (Fig. 12). `[NON SPECIFICATO]` la regola con cui costi e incentivi della REC sono attribuiti ai tre utenti; il testo fornisce solo i pesi sul costo totale dell'elettricità acquistata (38%, 29%, 33%; p. 12).

## 6. Metriche
- **Economiche:** costo operativo per utente (Tab. 4), SPB, flusso di cassa, reddito netto della comunità.
- **Energetiche / ambientali:** `s`, `d`, risparmio di energia primaria, ΔCO₂ con fattori di emissione orari.
- **Sociali:** indicatore "10%" e nuovo "10%_ISEE" (soglia 10%).
- **Equità / engagement:** nessun indice di equità fra membri; nessuna misura di engagement.

## 7. Risultati principali (numeri dal paper)
- Flussi annui (pp. 13–14): condivisa 30,48 MWh; prelevata dalla rete 8 MWh; venduta 2,02 MWh; produzione PV 32,5 MWh. `s` = 0,78; `d` = 0,94. Risparmio di energia primaria 61,6% (11,5 → 4,4 MWh/anno); ΔCO₂ 64% su base annua.
- **Effetto del fattore di emissione orario (p. 15):** usare la media annua (316,8 gCO₂/kWh) invece del valore orario sovrastima le emissioni del 5,3% alle 18:00 di agosto e del 50,3% alle 12:00 del 13 luglio.
- **Povertà energetica (Tab. 4, p. 16), indicatore 10% (SU):** R#1 5,71%; R#2 9,84%; R#3 6,60%. **10%_ISEE (SU):** 6,59%; 10,93%; 10,41% ⇒ con ISEE, R#2 e R#3 risultano in EP (soglia 10%). Nella REC nessun utente supera la soglia (p. 16).
- **Economia (p. 17):** SPB 10 anni (con detrazione fiscale), reddito netto della comunità 45.416 € su 20 anni; l'analisi di sensibilità su prezzi di acquisto/vendita mostra che con prezzo di acquisto più alto la REC risulta svantaggiosa per tutti i prezzi di vendita (autori, p. 17).

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata. Passaggi: lo storage elettrico migliorerebbe il mismatch estivo (p. 14); "These results show that the REC evaluation need be contextualized into electricity market scenarios" (p. 17); il caso è di soli 3 utenti residenziali e l'analisi economica è volutamente limitata al confronto REC vs singoli (p. 12).

## 9. Future work dichiarati dagli autori
- p. 18 (Sez. 4, Conclusions): "An additional evaluation could be obtained by including the possibility of improving envelope characteristics of the buildings to reduce the energy demands. Moreover, it could be useful to diversify the renewable energy sources used to satisfy the RECs energy needs by considering the greater flexibility ensured by "programmable" energy sources. In future studies, a more detailed analysis will be conducted on the economic and environmental advantages and disadvantages of renewable energy communities' configurations."
`[INFERENZA — test B.1]` **Self-referential / non pertinenti alla ripartizione.**

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` **Incoerenza testo/Fig. 12:** il testo (p. 16) riporta per R#2 e R#3 nella REC gli stessi valori (5,25% e 6,58%) per entrambi gli indicatori. Nella Fig. 12 i valori dell'indicatore 10% per R#2 e R#3 sono visibilmente inferiori (a lettura grafica circa 4,7% e 4,2%): i valori testuali sembrano ripetere quelli dell'indicatore ISEE. Il risultato qualitativo (nessuno sopra la soglia nella REC) regge.
- `[INFERENZA]` **Incoerenza di scala:** i consumi dichiarati sommano 13,34 MWh/anno (p. 6), ma i flussi della REC (30,48 condivisi + 8 prelevati) implicano un carico di circa 38,5 MWh/anno; l'energia condivisa non può superare il carico. Non riesco a riconciliare i due dati.
- `[INFERENZA]` Il ΔCO₂ annuo (64%) supera il massimo mensile riportato (44,2% in agosto; p. 14): una riduzione relativa annua non può eccedere il massimo dei valori mensili; probabile errore di stampa.
- `[INFERENZA]` Il valore "12–16%" di mitigazione della povertà energetica nell'abstract (p. 1) non compare nei risultati del corpo del testo.
- `[INFERENZA]` Eq. 11 usa il costo operativo della REC come flusso di cassa del payback anziché il costo evitato rispetto allo SU (Eq. 10); il fatto che prezzi di acquisto più alti rendano la REC "svantaggiosa" (p. 17) è controintuitivo e sembra legato a questa definizione.
- `[INFERENZA]` Utilità per la tesi: unico paper del corpus con un indicatore sociale esplicito basato sul reddito (10%, 10%_ISEE), ma applicato a tre utenti senza regola di ripartizione.
