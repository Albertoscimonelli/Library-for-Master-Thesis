# gianaroli2024 — Development of dynamic sharing keys: Algorithms supporting management of renewable energy community and collective self consumption

- **File sorgente:** `Paper/Development of dynamic sharing keys_ Algorithms supporting management of renewable energy community and collective self consumption.pdf` (17 pagine, testo estraibile; alcune pagine sono solo figure)
- **Tipo:** articolo su rivista (Energy & Buildings, Elsevier, open access)
- **Lettura:** integrale (corpo e Appendice A, pp. 1–16); bibliografia non letta riga per riga. I risultati per utente sono in parte solo in figura; le percentuali di Tab. 3 sono nel testo.
- **Convenzioni:** pagine = indici di pagina del PDF (coincidono con la numerazione stampata). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua.

## 1. Riferimento bibliografico
Gianaroli, F.; Ricci, M.; Sdringola, P.; Ancona, M. A.; Branchini, L.; Melino, F. (2024). *Development of dynamic sharing keys: Algorithms supporting management of renewable energy community and collective self consumption.* **Energy & Buildings**, 311, 114158. DOI 10.1016/j.enbuild.2024.114158. Ricevuto 12/12/2023; rivisto 5/3/2024; accettato 4/4/2024; online 8/4/2024. ENEA (Roma) e Università di Bologna.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1; p. 3):** definire nuovi criteri di allocazione dell'energia condivisa fra i membri che "reward virtuous behaviour" ma senza incentivare un aumento dei consumi dopo la creazione della comunità; quattro algoritmi di chiavi dinamiche (consumo-proporzionale, correlazione di Pearson, trend/sharing rate, combinazione) confrontati con un metodo di letteratura.
- **Gap dichiarato (p. 3):** "scientific literature often focuses on price optimization or complex optimization schemes in energy sharing or exchange mechanisms, rather than on practical and implementable sharing concepts."
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Italia, fase sperimentale (art. 42-bis DL 162/2019, L. 8/2020; decreto attuativo del 15/9/2020): energia condivisa = minimo orario fra immissione e prelievi; incentivo per 20 anni di 100 €/MWh per CSC e 110 €/MWh per REC; i membri regolano i rapporti con contratto di diritto privato e un soggetto delegato ripartisce l'energia condivisa, quindi "full freedom to manage the benefits deriving from shared energy is granted" (p. 2).
- **Tipo di CER:** virtuale; impianto PV che immette tutta l'energia in rete; i metodi servono nelle ore in cui l'immissione è minore del prelievo totale (p. 3).
- **Membri (caso 1, nord Italia, Tab. 1, p. 8):** 8 utenze: u1 PMI manifatturiera (prosumer, 419.894 kWh/anno); u2–u5 residenziali (31.491; 70.950; 61.743; 44.917 kWh/anno); u6–u8 profili ARERA medi per classe di potenza (190.897; 86.077; 65.760 kWh/anno). I profili residenziali sono stati moltiplicati ×20 "to achieve a global energy sharing exceeding 90%". **Caso 2 (Appendice A, p. 13):** 8 attività alberghiere nel nord Italia (52.659–195.349 kWh/anno).

## 4. Metodo
- **Modello:** allocazione oraria dell'energia condivisa `SH_i,j = r_i,j · E_inj,j` con chiave dinamica `r_i,j` (Eq. 2); quando l'immissione eccede il consumo totale ciascuno riceve il proprio consumo (Eq. 1). Simulazione annuale oraria 1/4/2022–31/3/2023 (caso 1) e 1/1–31/12/2022 (caso 2).
- **Dati:** profili reali del distributore locale (u2–u5), dati anonimi della PMI (u1), profili medi ARERA (u6–u8); "The authors do not have permission to share data" (p. 12).
- **Software:** script Python ad hoc, `scipy.stats` per Pearson (p. 4).
- **Parametri arbitrari dichiarati:** costante di decadimento ξ = 1,386 (ottenuta assumendo SR = 0,5 quando consumo/immissione = 1,5); pesi α = β = 0,5 in M5 ("arbitrarily", pp. 5).

## 5. Meccanismi di ripartizione analizzati (dell'energia condivisa, Sez. 2.1)
- **M1:** proporzionale al consumo orario (`r = C_i/ΣC`).
- **M2:** da Minuto & Lanzini (rif. [22], presente nel corpus): ciascuno riceve almeno il consumo orario del membro più piccolo e il resto tende a essere distribuito equamente (progressivo, stile water-filling).
- **M3:** chiave basata sulla correlazione di Pearson giornaliera fra consumo individuale e immissione dell'impianto (rimappata in [0,1]); virtuoso = consumare quando l'immissione è alta.
- **M4:** chiave basata sullo "sharing rate" SR: lineare crescente se consumo/immissione < 1, esponenziale decrescente se ≥ 1 (penalizza il sovraconsumo).
- **M5:** combinazione pesata di M3 e M4 (`α·p + β·SR`).

## 6. Metriche
- **Energetiche (allocazione):** energia condivisa assegnata a ciascun utente (kWh/anno e % rispetto al totale immesso), confronto con il consumo (Fig. 13) e con il **Shared_limit** `SH_lim = min(E_inj, C_i)`, definito come "the maximum energy each member could share with the community in the absence of the other members" (p. 9); variazione % rispetto a M1.
- **Altre:** distribuzione dei coefficienti di Pearson normalizzati (Fig. 11–12).
- **Economiche / sociali / ambientali / engagement:** nessuna misura monetaria o di equità aggregata; l'incentivo (110 €/MWh) è citato ma non applicato ai risultati; "virtuous behaviour" non è simulato (profili fissi).

## 7. Risultati principali
- Energia condivisa a livello di comunità: quasi il 90% dell'energia immessa (79.855 kWh/anno) (p. 7).
- **Tab. 3 (p. 12), quota dell'energia condivisa per utente (% rispetto all'immissione) per M1/M2/M3/M4/M5:** u1 22,6/7,6/10,8/8,1/9,1; u2 3,6/6,8/6,7/5,7/6,4; u3 10,2/12,5/12,2/12,4/12,4; u4 7,2/10,3/10,4/9,8/10,4; u5 5,9/8,5/9,3/7,8/8,9; u6 20,7/18,5/14,7/20,4/16,5; u7 10,2/12,9/12,7/13,1/13,1; u8 8,5/11,7/12,1/11,4/12,1.
- M1, il metodo più usato, assegna le quote maggiori ai maggiori consumatori (u1, u6) "can lead to overestimation of the assigned energy, since it doesn't consider the distribution of consumption's hours" (p. 12). Rispetto a M1, u1 perde il 66,5% con M2 e il 64,1% con M4; M3 lo penalizza meno (p. 11). M3 penalizza u6 (bassa correlazione). M2–M5 tendono a distribuire in modo più uniforme.
- Il caso 2 conferma il comportamento (p. 11–12). Abstract: "some of the algorithms assign to users with the highest consumption an amount of shared energy higher than their real sharing potential, while users with greater sharing potential are penalised."

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata. Elementi: parametri scelti arbitrariamente (ξ, α, β); dati non condivisibili; profili residenziali replicati ×20; per u1 le differenze nei coefficienti di Pearson dipendono dal weekend di chiusura (pp. 8–9).

## 9. Future work dichiarati dagli autori
- p. 12 (Sez. 4): "Other aspects that deserve further studies in the future concern the application of dynamic distribution keys to a larger cluster of users, identifying which algorithms are best suited to the type of user without penalizing them; other studies could consider vulnerable users in energy poverty through the development of social indicators. Furthermore, as members of a REC or CSC can voluntarily enter or exit the established legal entity, future studies will need to evaluate indicators of potential expansion or decline of community members with the same production plants."
- p. 12 (Sez. 4), conclusione di merito: "an energy community require the implementation of allocation mechanisms that consider the different types of users who contribute to energy sharing."
`[INFERENZA — test B.1]` **Prevalentemente self-referential** (estensione delle proprie chiavi a cluster più grandi), con due elementi di portata più generale: indicatori sociali per utenti vulnerabili e indicatori di ingresso/uscita dei membri.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` Studio **fortemente aderente al regime italiano** (energia condivisa oraria, incentivo, soggetto delegato) ma **non converte in € né misura equità**: la comparazione è in kWh assegnati.
- `[INFERENZA]` Nel modello l'energia condivisa è allocata solo in base ai prelievi `C_i`: non c'è remunerazione separata per il produttore (la PMI u1 è produttore e maggior consumatore), quindi il trade-off produttore/consumatore non è modellato.
- `[INFERENZA]` Non c'è risposta comportamentale: "virtuous behaviour" è un'ipotesi di progetto, non un risultato; i metodi M3–M5 sono valutati su profili statici.
- `[INFERENZA]` La composizione è molto sbilanciata (una PMI con 420 MWh/anno e residenziali replicati ×20): i risultati dipendono da questa scelta di dimensionamento (>90% di condivisione).
- `[INFERENZA]` Il concetto `Shared_limit` è un benchmark utile ("potenziale di condivisione individuale"): è un riferimento riusabile come misura di *contributo* senza ricorrere allo Shapley.
