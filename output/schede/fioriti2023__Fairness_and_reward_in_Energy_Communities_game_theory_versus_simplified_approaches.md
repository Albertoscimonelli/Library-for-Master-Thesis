# fioriti2023 — Fairness and reward in Energy Communities: game-theory versus simplified approaches

- **File sorgente:** `Paper/Fairness and reward in Energy Communities_ game-theory versus simplified approaches.pdf` (6 pagine; testo estraibile; Fig. 1–5 lette su immagine, i risultati sono solo grafici, senza tabelle numeriche)
- **Tipo:** conference paper (2023 IEEE EEEIC / I&CPS Europe), 6 pagine
- **Lettura:** integrale (pp. 1–6); bibliografia (p. 6) non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Valori da figura = letture approssimative.

## 1. Riferimento bibliografico
Fioriti, D.; Ferrucci, T.; Poli, D. (2023). *Fairness and reward in Energy Communities: game-theory versus simplified approaches.* In: 2023 IEEE International Conference on Environment and Electrical Engineering and 2023 IEEE Industrial and Commercial Power Systems Europe (EEEIC / I&CPS Europe). DOI 10.1109/EEEIC/ICPSEurope57605.2023.10194696. DESTEC, University of Pisa. Finanziamento/ringraziamenti: `[NON SPECIFICATO]`. Disponibilità del codice (pacchetto Julia citato a p. 2): `[NON SPECIFICATO]`.

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1; p. 2):** confrontare schemi per ripartire ricavi e premi fra i membri di una comunità: l'ottimizzazione cooperativa (con aggregatore) rispetto alla non cooperativa; schemi semplici (proporzionali all'energia condivisa e ai costi di investimento) rispetto agli approcci di teoria dei giochi (**Shapley, Nucleolo, VarLeastCore**). "A numerical case study suggests that the procedure can be implemented in practice and suggests approximate techniques to address reward distribution schemes for Energy Communities."
- **Posizionamento (pp. 1–2):** lo Shapley è "sometimes used as a key indicator for fairness" ma può non essere stabile; il Core non è unico; il Nucleolo "is computationally heavy to compute and hardly justifiable for the EC context"; LeastCore è non unico; VarLeastCore e ShapleyLeastCore da [6] riducono l'arbitrarietà. Gli schemi semplici hanno "theoretical soundness […] generally lacking [14]".
- **Gap dichiarato:** nessuna sezione di gap con claim negativi; l'obiettivo è "to highlight potential synergies and differences" (p. 2).
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Italia (caso di studio); si cita l'approccio italiano/UK in cui l'ente EC è premiato per ogni unità di energia condivisa e decide come distribuire il premio ("neither the national nor the local legislation prescribes the specific reward distribution", p. 1). Energia condivisa = prodotta da un membro e consumata da un altro nello stesso intervallo di 15 minuti (p. 2).
- **Tipo di CER:** EC no-profit con un **aggregatore/ESCO** a pagamento (remunerato in proporzione al beneficio rispetto al caso base, cfr. [6]); asset di proprietà e a carico delle singole utenze, non della EC (p. 2); obiettivo: massimizzare l'NPV globale.
- **Membri:** 10 utenti commerciali; dati di carico da una sottostazione portoghese (UCI, [18]); PV e vento da Renewables.ninja; tutti tranne tre possono installare PV, due anche eolico e cinque batterie; spazio per PV 50–100 kWp (pp. 5–6).

## 4. Metodo
- **Modelli (Sez. IV, pp. 4–5):** problema non cooperativo `NPV^NC_j = max −NPC_j` (Eq. 14–21) e cooperativo `NPV^CO = max R^SH + Σ_j(−NPC_j)` (Eq. 22–23), con ricavo `R^SH` = tariffa feed-in sull'energia condivisa; `E^SH_t ≤ min(Σ P^M−/Δ, Σ P^M+/Δ)` (Eq. 30); funzione di valore `v(J) = NPV^CO(J) − NPV^NC(J)` (Eq. 31). Il testo introduttivo parla di "Linear Programming" (p. 2), l'abstract di MILP: `[NON SPECIFICATO]` quale sia il tipo effettivo.
- **Parametri (Sez. V-B, p. 5):** PV 1.400–1.700 €/kWp; eolico 3.000 €/kWp; batterie 400 €/kWh e 200 €/kW (efficienza round-trip 92%); vite utili 25/20/15/10 anni (PV/eolico/batterie/convertitori); manutenzione 1–2% dell'investimento; prezzi "pre-crisis" 18 c€/kWh (acquisto) e 5 c€/kWh (vendita); quota potenza 36 €/kW/anno. Valore della tariffa sull'energia condivisa `π^SH`: `[NON SPECIFICATO]`.
- **Procedura (p. 5):** (1) ottimizzazioni CO e NC; (2) schemi di teoria dei giochi per ripartire; (3) "simulate the use of simplified reward allocation schemes to capture the reward allocation described by a game-theoretic approach for every user independently", cioè prezzi equivalenti **per utente**.
- **Software:** pacchetto Julia sviluppato dagli autori (p. 2).

## 5. Meccanismi di ripartizione analizzati
**Teoria dei giochi (Sez. III-A):** Shapley (Eq. 2); Nucleolo (Eq. 3–4); Least Core (Eq. 5–6); **VarLeastCore** (Eq. 7–8): fra le allocazioni nel Least Core sceglie quella che minimizza la varianza dei benefici.
**Schemi semplici (Sez. III-B):** (i) *sharing* `R_j = π^SH(E^SH+ + E^SH−) − NPC_j`: premio proporzionale all'energia condivisa prodotta o consumata, con `π^SH+ = π^SH−`; (ii) *financing* `R_j = γ_0 + Σ γ_i x_{i,j}` e, per semplicità, `R_j = γ^F·CAPEX_j`: premio proporzionale all'investimento (Eq. 11–13). Gli autori: lo schema sharing "is simple and promotes the coordination of consumption and production" ma il ricavo non è noto a priori (rischio per gli investitori); lo schema finanziario è "risk-reducing for investors" ma sposta il rischio sull'aggregatore (p. 3–4).

## 6. Metriche
- **Economiche:** `ΔNPV_j = NPV^CO_j − NPV^NC_j` per utente e per aggregatore (Fig. 3); CAPEX e OPEX attualizzati (Fig. 1); premio allocato (Fig. 4); prezzi equivalenti `π^SH` (€/kWh) e `γ^F` (€/€) (Fig. 5); quota del beneficio all'aggregatore (16–24%).
- **Energetiche:** energia condivisa consumata/prodotta e autoconsumo per utente (Fig. 2).
- **Equità / sociali / ambientali / engagement:** nessun indice; l'equità è identificata con il concetto di soluzione (Shapley, Nucleolo, VarLeastCore). Nessuna metrica ambientale o di coinvolgimento.

## 7. Risultati principali (numeri dal paper)
- **Fig. 1–2 (p. 5):** nella configurazione cooperativa gli utenti 2, 3, 6, 8 e 9 aumentano gli investimenti in rinnovabili e batterie, "partially compensated by lower operational costs, the remainder is covered by appropriate rewarding schemes"; senza cooperazione non c'è energia condivisa e l'autoconsumo è minore.
- **Fig. 3 (p. 6, lettura approssimativa):** Shapley e Nucleolo "tend to behave similarly", mentre VarLeastCore "tends to reduce the benefit awarded to the aggregator, in favor of the users": l'aggregatore passa da circa 105–110 k€ (Shapley e Nucleolo) a circa 49 k€ (VarLeastCore); i consumatori puri 5, 7 e 10 ottengono circa 33–36, 23–25 e 27–30 k€ con Shapley/Nucleolo e circa 46–49 k€ con VarLeastCore; gli altri utenti circa 3–8 k€.
- **Fig. 4 (p. 6):** "the benefit and reward allocation maps do not match. In particular, prosumers 2, 3 and 8, do receive a large share of reward, but their total benefit is lower. Indeed, a large portion of the reward they receive is to compensate the larger investments needed to maximize the benefits for the community." Gli autori proseguono con VarLeastCore perché ha "better reward allocation to the users".
- **Fig. 5 e testo (p. 6):** "about 16-24% of DNPV is allocated to aggregators"; prezzi equivalenti per lo schema sharing tra "1.5 and 7.2 c€/kWh" (altrove "1-7"), per lo schema finanziario da 4 a 21 c€/€; gli utenti 5, 7 e 10 (consumatori puri) "require a fixed benefit to assure reward allocation, which introduces uncertainties into the business model of operators".
- **Conclusione (p. 6):** "game-theoretic approach are robust, yet a simplification may be required to implement them in practice".

## 8. Limitazioni dichiarate dagli autori
Nessuna sezione dedicata. Dichiarazioni: gli schemi semplici sono "not backed by strong mathematical background" e possono impedire l'ottimo globale (p. 3); Shapley e Nucleolo sono onerosi da calcolare (p. 2); il ricavo da schemi sharing non è noto a priori (p. 3).

## 9. Future work dichiarati dagli autori
Nessuno specifico. Unica frase finale (p. 6): "The methodology and the proposed results can lay the foundation for future work on sounded fair efficient reward allocation schemes in business models for ECs." `[INFERENZA — test B.2]` Non è un future work utilizzabile per fondare un gap (troppo generico).

## 10. Note del lettore (inferenze mie)
- `[INFERENZA]` I prezzi equivalenti degli schemi semplici sono **personalizzati per utente** (Fig. 5) per replicare il VarLeastCore: se una tariffa unica per tutti non riproduce l'allocazione di teoria dei giochi (da 1,5 a 7,2 c€/kWh), lo schema "semplice" richiede coefficienti individuali. Il paper non verifica quanto si perderebbe in equità o stabilità con una tariffa uniforme.
- `[INFERENZA — lettura figura]` In Fig. 3 lo Shapley assegna all'aggregatore circa 105 k€ su un totale di circa 230 k€ (≈ 46%) e il Nucleolo circa 110 k€; con VarLeastCore circa 49 k€ su circa 226 k€ (≈ 22%), cioè nella fascia 16–24% citata dagli autori. L'affermazione "about 16-24% of DNPV is allocated to aggregators" vale quindi per VarLeastCore ma non per Shapley e Nucleolo, perché l'aggregatore è un giocatore senza il quale `v(J)` è nullo (stesso meccanismo del condominio in `zatti2021`).
- `[INFERENZA — lettura figura]` In Fig. 5 il valore più alto dello schema finanziario (utente 2) sembra circa 0,245 €/€, oltre il limite di 21 c€/€ riportato nel testo; la lettura è approssimativa. Inoltre il testo riporta due diversi intervalli per `π^SH` (1–7 e 1,5–7,2 c€/kWh).
- `[INFERENZA]` Il paper confronta i meccanismi su **un solo caso** con 10 utenti commerciali, senza tabelle numeriche e senza indice di equità: l'evidenza è visiva (grafici). I dati di carico provengono da una sottostazione portoghese usata come proxy per l'Italia (p. 5).
- `[INFERENZA]` Il ricavo `R^SH` è una tariffa feed-in uniforme sull'energia condivisa, quindi il gioco ha una funzione di valore simile a quella del regime italiano (incentivo su min(immissione, prelievo) a 15 minuti), ma il valore numerico della tariffa non è indicato: non si può ricostruire il ΔNPV.
- `[INFERENZA]` Per la tesi: il paper confronta Shapley, Nucleolo, VarLeastCore e schemi proporzionali sulla *stessa* funzione di valore, in modo analogo a `fioriti2021` [6] (citato, non ancora letto in questa fase) e ad altri paper del corpus che confrontano più regole (es. `kulmala2021`, `gonzalezasenjo2025`); non va usato come evidenza di unicità. I suoi limiti di rappresentatività (un caso, 10 utenti) e di verificabilità (nessuna tabella) sono rilevanti per eventuali claim di gap sul confronto "teoria dei giochi vs regole semplici".
