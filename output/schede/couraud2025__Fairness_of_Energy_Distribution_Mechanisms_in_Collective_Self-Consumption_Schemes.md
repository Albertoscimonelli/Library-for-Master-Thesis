# couraud2025 — Fairness of Energy Distribution Mechanisms in Collective Self-Consumption Schemes

- **File sorgente:** `Paper/Fairness_of_Energy_Distribution_Mechanisms_in_collective_self_consumption.pdf` (5 pagine; testo estraibile; Fig. 1–4 ispezionate come immagini: Fig. 3 e Fig. 4 solo qualitativamente, senza valori numerici leggibili; Tab. I e Eq. 1–3 lette sull'immagine di p. 4)
- **Tipo:** preprint arXiv (arXiv:2508.16819v1 [cs.CY], 22/8/2025), formato breve da conferenza `[INFERENZA dal formato]`; simulazione deterministica con profili reali su comunità generate a caso.
- **Lettura:** integrale (5 pagine, bibliografia inclusa).
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente. Le virgolette « » riportano il testo degli autori. Sede di pubblicazione: `[NON SPECIFICATO nel PDF]`.

## 1. Riferimento bibliografico
Couraud, B.; Robu, V.; Norbu, S.; Andoni, M.; Rozier, Y.; Chen, S.; Franquet, E.; Barre, P.-J.; Kanugrahan, S. P.; Berthou, B.; Flynn, D. (2025). *Fairness of Energy Distribution Mechanisms in Collective Self-Consumption Schemes.* arXiv:2508.16819v1. Università di Glasgow, CWI Amsterdam, Université Côte d'Azur (IMREDD), Enogrid. Finanziamento: progetti EPSRC HI-ACT e DISPATCH (p. 5). Dati: profili di consumo dal progetto Thames Valley Vision (200 consumatori), produzione solare da un impianto del sud-est della Francia (p. 4). Disponibilità di dati e codice: `[NON SPECIFICATO]`. Gli autori Couraud, Robu, Norbu, Andoni e Flynn compaiono anche in `cremers2023` (rif. [12] del paper).

## 2. Obiettivo e research question
- **Obiettivo (abstract, p. 1):** descrivere il processo di autoconsumo collettivo (CSC) in Francia, rassegnare i tipi di fairness rilevanti per i mercati energetici locali (LEM) con i relativi indicatori e confrontare l'equità di quattro meccanismi di distribuzione dell'energia locale con simulazioni su 250 comunità residenziali generate a caso.
- **Gap dichiarato (p. 1):**
  - «none of these studies actually compare the fairness of the main energy distribution mechanisms proposed to real-world energy communities»;
  - molti studi non trattano l'intero spettro dei tipi di fairness, «such as utilitarian [9], or meritocratic fairness [7]»;
  - «research works often lack integration with actual tariff structures from countries that have already implemented CSC regulatory frameworks».
  `[INFERENZA]` Sono universali negative di tipo B.3; qui interessano solo come posizione degli autori.
- **RQ formulata come domanda?** No. Contributi dichiarati (p. 1): armonizzare le prospettive di fairness, un nuovo indicatore meritocratico scalabile, il confronto sui quattro meccanismi.

## 3. Contesto
- **Paese / quadro normativo:** Francia (autoconsumo collettivo dal 2021; Personne Morale Organisatrice (PMO) che coordina; dati a 15 minuti dal gestore di rete; ripartizione ex post mensile da parte della PMO; prezzi locali che devono stare sotto il prezzo al dettaglio del fornitore e sopra la tariffa di immissione, pp. 2–3). Il testo cita l'Italia come altro esempio di CSC (p. 2) ma non la modella.
- **Valore ripartito:** non un incentivo regolato: il beneficio è il risparmio in bolletta di ciascun membro `u_i = B_i − B̂_i` (p. 3), con prezzi locali fissati dal meccanismo; le tariffe, i prelievi e le accise francesi sono modellati (Fig. 2, pp. 2–3).
- **Tipo di comunità:** residenziale, 20 membri, tariffa fissa o a fasce assegnata a caso; PV da 3 kW per i membri con PV, il 30% dei quali nuovo (tariffa di immissione ridotta a 4 c€/kWh) (p. 4).

## 4. Metodo
- **Simulazione (Sez. IV, pp. 4–5):** 50 comunità × 5 livelli di penetrazione del PV (da 0 a 80%) = 250 comunità; un anno; profili di consumo estratti a caso da un insieme di 200 consumatori. Passo temporale: `[NON SPECIFICATO]` nelle simulazioni (i dati del gestore sono a 15 minuti, p. 2).
- **Prezzo locale (p. 4):** uniforme per tutti, calcolato come media fra il più alto prezzo di immissione fra i produttori serviti e il più basso prezzo di acquisto fra i consumatori serviti, con IVA e accisa ma senza oneri di rete.
- **Indicatore meritocratico (Eq. 3, Tab. I, p. 4):** `C_i = Σ_t [ −sign(Ê_i^t) · min(|Ê_i^t|, |Ê_{−i}^t|) · Ê_{−i}^t ]`, con `Ê_i^t` l'immissione netta del membro `i` all'ora `t` (positiva se esporta) e `Ê_{−i}^t` quella di tutti gli altri; quota meritocratica ideale `û_i = C_i / Σ_j C_j · Σ_j u_j`; indice = `√(1/n Σ_i (u_i − û_i)²)`. Nota mia: come stampata la formula moltiplica due energie (il fattore finale è `Ê_{−i}^t` e non il suo segno), quindi `C_i` ha dimensione di un'energia al quadrato; non è chiaro se sia voluto `[INFERENZA, lettura mia della formula]`.

## 5. Meccanismi di ripartizione analizzati
Quattro, tutti di tipo «mercato locale» con prezzo uniforme (Sez. III-A, pp. 3–4):
1. **Pro-rata** (Eq. 1): l'energia locale è distribuita proporzionalmente alle importazioni o esportazioni di ciascun membro nell'ora. Il paper nota che alloca più energia ai consumatori che consumano di più, «which does not correspond to equal fairness» (p. 3).
2. **Glass-filling**: ogni consumatore riceve una quota uguale dell'energia locale, con il surplus dei consumatori a basso consumo redistribuito iterativamente a quelli a consumo maggiore (Eq. 2); stessa procedura per i produttori.
3. **Glass-filling con priorità**: a ogni ora la priorità va a chi ha ricevuto meno energia locale dall'inizio di un anno mobile.
4. **Doppia asta a prezzo uniforme**: distribuzione con priorità sul prezzo.
Nessuna regola di teoria dei giochi cooperativi (lo Shapley è citato solo come riferimento per la fairness meritocratica e non è implementato, p. 4); nessun nucleolo, nessuna regola semplice a quote fisse né performance-based.

## 6. Metriche
Tab. I (p. 4): equality (indice di Jain), min-max (rapporto min/max), meritocratic (indice nuovo), utilitarian (welfare sociale: somma dei guadagni), need-based (utilità pesata). Gini e QoS sono citati come alternativi per l'uguaglianza. Il tipo *need-based* **non è valutato**: «These weights are typically derived from exogenous data (e.g., income level, energy vulnerability), which is often unavailable—limiting the analysis of this fairness type in many studies, including this work that will not address it for the same reason» (p. 4). Nessuna misura di stabilità di coalizione, forza incentivante o inclusione.

## 7. Risultati principali (affermazioni degli autori)
- Risparmio medio in bolletta del 12% con il 40% di penetrazione PV, poi in calo (p. 5).
- «Among the four widely used LEM mechanisms assessed, glass-filling with prioritization yields the highest egalitarian and min-max fairness. Double auction and pro rata schemes promote meritocracy, while standard glass-filling offers a strong balance across fairness objectives.» (abstract, p. 1). A p. 5: «although there is not one distribution approach that addresses all types of fairness, the simple glass-filling method consistently offers a compromise between meritocratic and egalitarian fairness principles».
- Il welfare utilitario è «similarly achieved across all mechanisms» (p. 5), perché somma solo i guadagni.
- Le differenze fra i meccanismi si riducono sopra il 40% di penetrazione (p. 5).
- Risultati riportati solo in forma grafica (grafici radar normalizzati, Fig. 4; mappa di calore del risparmio, Fig. 3): nessun valore numerico degli indicatori nel testo. Nessun intervallo di confidenza o test di significatività `[NON SPECIFICATO]`.

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione di limitazioni. Dichiarazioni sparse: il tipo need-based non è valutato per mancanza di dati esogeni (p. 4); la valutazione meritocratica è limitata ai contributi finanziari «due to a lack of data on non-financial impacts» (p. 4); le simulazioni sono «without flexibility» (p. 5).
`[INFERENZA]` Non dichiarati: taglia fissa a 20 membri; penetrazione PV come unico fattore di configurazione; un solo contesto tariffario; profili di consumo del Regno Unito abbinati a produzione francese; i risultati sono grafici qualitativi; nessuna regola di teoria dei giochi cooperativi.

## 9. Future work dichiarati dagli autori
Nessuna sezione di future work. Unica indicazione, in chiusura (p. 5): i risultati «should be complemented by community engagement efforts to co-develop new algorithms that reflect local priorities and values, thereby enhancing social acceptability».
`[INFERENZA — test B.1]` Non è un future work sull'analisi quantitativa; è una raccomandazione di coinvolgimento: non utilizzabile come ancora (B.5: non calcolabile). Registrato come «—» nel registro dei future work.

## 10. Note del lettore (inferenze mie)
- **È il confronto più vicino alla domanda «il ranking dipende dalla nozione di fairness»** (RQ-1), e va citato come tale. Confronta quattro meccanismi su quattro nozioni (uguaglianza, min-max, meritocratica, utilitaria) su 250 comunità con profili reali e dichiara esplicitamente che nessun meccanismo risponde a tutti i tipi di fairness.
- **Ciò che non fa** (e che quindi resta aperto, nella mia lettura):
  - non include regole di famiglie diverse: sono tutti meccanismi di mercato locale a prezzo uniforme (nessuno Shapley, nucleolo, contributo marginale, regole semplici a quote o performance-based);
  - non ha un indicatore di **stabilità di coalizione** né di **forza incentivante**, e non misura **inclusione** (il need-based è escluso per mancanza di dati);
  - non quantifica la **concordanza** fra le nozioni (nessun τ di Kendall, nessun rango numerico): la conclusione è letta da grafici radar;
  - varia solo la penetrazione del PV; taglia fissa (20), niente composizione per categoria;
  - non valuta un incentivo regolato sull'energia condivisa oraria: il valore è il risparmio in bolletta con prezzo uniforme di mercato locale; il valore totale ripartito può dipendere dal meccanismo perché la doppia asta accoppia i prezzi (tariffe eterogenee, p. 4), cosa che nel regime con remunerazione unitaria comune non avviene `[INFERENZA]`;
  - nessun test della sensibilità dell'ordinamento alla scelta dell'indicatore meritocratico.
- **Gap e novità:** le tre affermazioni di gap di p. 1 sono universali negative; non vanno riprese. Il lavoro conferma però il bisogno (le comunità «often lack guidance on which approach best aligns with their values», p. 1) e ne dà una risposta parziale; il tuo lavoro lo estende lungo gli assi sopra.
- **Indicatore meritocratico come spunto per il tuo codice:** `C_i` misura il contributo fisico orario, simile alla tua proporzionalità al contributo fisico; è un candidato da confrontare con i tuoi indicatori di prossimità al contributo marginale e di quota fisica. Non è circolare rispetto allo Shapley, perché definito dai profili e non da una regola. Possibile refuso nella formula (sopra): se lo usi, riderivalo.
- **Collegamento con il corpus:** cita `dynge2025` ([7]), `gjorgievski2022` ([8], non nel corpus come scheda), `cremers2023` ([12]); confermano la rete di richieste di indicatori comuni descritta nel memo del gap.
