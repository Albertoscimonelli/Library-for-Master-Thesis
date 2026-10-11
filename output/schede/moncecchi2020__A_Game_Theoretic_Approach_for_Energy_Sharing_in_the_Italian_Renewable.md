# moncecchi2020 — A Game Theoretic Approach for Energy Sharing in the Italian Renewable Energy Communities

- **File sorgente:** `Paper/A Game Theoretic Approach for Energy Sharing in the Italian Renewable.pdf` (25 pagine, testo estraibile)
- **Tipo:** articolo su rivista (open access, MDPI)
- **Lettura:** integrale del corpo (pp. 1–23); l'elenco bibliografico non è stato letto riga per riga.
- **Convenzioni:** le pagine citate sono indici di pagina del PDF. `[INFERENZA]` = mia valutazione, non dichiarata dagli autori. `[NON SPECIFICATO]` = informazione assente o ambigua nel paper.

## 1. Riferimento bibliografico
Moncecchi, M.; Meneghello, S.; Merlo, M. (2020). *A Game Theoretic Approach for Energy Sharing in the Italian Renewable Energy Communities.* **Applied Sciences**, 10(22), 8166. doi:10.3390/app10228166. Ricevuto 19/10/2020, accettato 16/11/2020, pubblicato 18/11/2020. Dipartimento di Energia, Politecnico di Milano.

## 2. Obiettivo e research question
- **Obiettivo (autori):** creare una nuova REC in due passi: (1) modello dei flussi energetici secondo lo schema italiano per trovare il portafoglio ottimo di impianti/accumulo; (2) usare lo Shapley value per distribuire i benefici tra i membri (abstract, p. 1).
- **Obiettivo del gioco (p. 13):** "to find a stable and fair allocation rule that gives an adequate payoff to the players, so that each one is encouraged to take part to the EC."
- **RQ formulata come domanda?** No. Il paper dichiara obiettivi, non una research question.

## 3. Contesto
- **Paese / quadro normativo:** Italia, fase sperimentale di recepimento degli artt. 21–22 della Direttiva 2018/2001, in vigore dal 1° marzo 2020 (p. 2). Membri sotto la stessa cabina MV/LV; nuovi impianti condivisi fino a 200 kW; configurazione "virtuale" (rete pubblica); alcune componenti tariffarie restituite sull'energia condivisa; tariffa incentivante sull'energia condivisa per 20 anni (p. 2).
- **Tipo di CER:** REC con impianti collettivi (produttori/finanziatori + consumatori passivi). Gli impianti PV preesistenti sono stati rimossi per ottenere un caso "greenfield" (p. 14).
- **Membri (caso studio Chiou, Porossan, Aosta – Valle d'Aosta):** 131 utenze: 99 domestici residenti (6 classi per numero di componenti), 15 domestici non residenti, 16 "altri usi", 1 illuminazione pubblica; consumo totale 217,2 MWh/anno (Tab. 1, p. 15). Candidati: 20 superfici PV (1400–2000 €/kW) + 1 idroelettrico (max 20 kW, 4000 €/kW) + storage fino a 200 kWh (Tab. 2–4, pp. 19–20).

## 4. Metodo
- **Modello:** ottimizzazione che massimizza l'NPV della CER (bilanci orari, vita utile 20 anni, tasso di attualizzazione 4%; blocchi di anni per ridurre il carico computazionale; Sez. 2, pp. 3–9). Poi gioco cooperativo TU con valore per coalizione `v(S)` = ricavi da vendita + energia condivisa × (SEsi + prezzo di acquisto + incentivo) (Eq. 40–41, p. 13).
- **Ipotesi chiave:** utenti passivi che non modificano il carico ("worst case", nota p. 13); partecipazione aperta e volontaria ⇒ stabilità della grande coalizione definita dagli autori "trivial" (p. 13).
- **Dati:** misure orarie del DSO (Cooperativa Elettrica di Gignod) sul trasformatore MV/LV; ISTAT per numero/tipo utenze (ipotesi: la cabina Chiou serve il 40% del villaggio); PVGIS per i profili PV; profilo idro standard dalla mediana di impianti monitorati in zona; 9 profili di carico sintetici (pp. 14–19). Consumo residenziale = 500 + 600·N_componenti kWh/anno (Eq. 42, p. 15).
- **Parametri economici (Tab. 3, p. 20):** incentivo sull'energia condivisa 110 €/MWh; SCsi 80 €/MWh; SEsi 8,22 €/MWh; costo amministrativo 5 €/utente/anno; crescita carico +2%/anno; prezzi −2%/anno.
- **Software:** Python/Pyomo + Gurobi per l'ottimizzazione; Shapley calcolato in Python (p. 14).

## 5. Meccanismi di ripartizione analizzati
- **Shapley value a due livelli (p. 14):** (1) Shapley tra produttori e *gruppi* di consumatori; (2) ripartizione **proporzionale** fra i singoli consumatori del gruppo. Gli autori ammettono che raggruppare i consumatori è un'approssimazione.
- Nessun confronto con altre regole di ripartizione (solo Shapley + proporzionale intra-gruppo).
- `[NON SPECIFICATO]` criterio di formazione dei gruppi di consumatori e numero esatto di giocatori.

## 6. Metriche
- **Economiche:** NPV, profitability index (PI), payback, ricavi per voce, risparmio annuo per consumatore (Sez. 5, pp. 20–22).
- **Sociali / equità:** nessun indice quantitativo di equità; l'equità è affidata agli assiomi dello Shapley (Pareto-efficienza, simmetria, additività, giocatore nullo; p. 11). Lotta alla povertà energetica citata solo qualitativamente (p. 21).
- **Ambientali:** nessuna (nessuna stima di CO₂ o autosufficienza).
- **Engagement:** nessuna misura.

## 7. Risultati principali (numeri dal paper)
- **Portafoglio ottimo (p. 20):** 14,4 kWp PV + 20 kW idro, nessuno storage (costo troppo alto). Produzione media 102,2 MWh/anno, 95,2% condivisa (97,4 MWh/anno), 4,8% venduta (4,9 MWh/anno). NPV 85.866 €, PI 1,84, payback < 9 anni. L'incentivo sulla energia condivisa vale il 66,9% dei ricavi complessivi, i risparmi il 31,5%, la vendita il 1,61%.
- **Dopo la ripartizione (p. 21):** NPV dei produttori 37.204 € (−56,7%), PI 1,36 (−0,48), payback +44,4%; il resto va ai consumatori, che in media risparmiano 32,1 €/anno senza esborso (salvo 5 €/anno di quota amministrativa).
- Conclusione degli autori (p. 23): metodologia "efficace" e facilmente applicabile; tutti i partecipanti ottengono un vantaggio economico e la sostenibilità per i finanziatori è verificata.

## 8. Limitazioni dichiarate dagli autori
Non c'è una sezione "Limitations". Passaggi che esprimono limiti, citati verbatim:
- p. 11–12 (Sez. 3.2.2): "One of the major drawbacks of the Shapley value is its computational burden as the number of players inside the coalition increases. It is not possible to evaluate the Shapley value for a set of hundreds of users like it could be the one of an energy community. Furthermore, it has to be noted that the Shapley value does not necessary lie in the core."
- p. 14 (Sez. 3.3.2): "The distribution based on group of consumers instead of each single consumer introduces an approximation, since the marginal contribution of the group of costumers can be different from the sum of marginal contributions of each single user. Nevertheless, in the planning phase, this can be accepted in exchange of a computational feasibility."
- p. 13 (nota a piè di pagina, Sez. 3.3.1): "In this planning phase we consider the worst case in which users are not changing their loads to increase the amount of energy shared. In real operation, the same game could become dynamic and users could also apply some demand response schema to maximise their payoff."
- p. 5 (nota, Sez. 2.4): "Allowing members' self-consumptions could increase the revenue of the community, but at the same time it requires a more complex way to redistribute the economical benefits, that may be unfairly concentrated on the users that self-consume the energy."

## 9. Future work dichiarati dagli autori
**Nessuno.** La Conclusione (p. 23) non indica sviluppi futuri. L'unico accenno implicito è la nota di p. 13 sul gioco che "could become dynamic" con demand response nell'operatività reale.

## 10. Note del lettore (inferenze mie, non degli autori)
- `[INFERENZA]` Non c'è un confronto fra regole di ripartizione: il paper mostra l'esito di *un* meccanismo (Shapley a gruppi), non l'effetto del meccanismo.
- `[INFERENZA]` L'errore introdotto dal raggruppamento dei consumatori non è quantificato (nessun Shapley esatto individuale come benchmark).
- `[INFERENZA]` La stabilità è dichiarata "trivial" per via della partecipazione volontaria, ma gli stessi autori dicono che lo Shapley può non stare nel core: i due punti non sono riconciliati.
- `[INFERENZA]` Incoerenza minore: a p. 18 si parla di "6 monitored hydroelectric power plants" ma si elencano 5 potenze (40, 6,4, 72, 45, 45 kW).
- `[INFERENZA]` Utile come riferimento "storico" per la formulazione `v(S)` in funzione dell'energia condivisa e dell'incentivo; nessuna metrica ambientale né di engagement.
