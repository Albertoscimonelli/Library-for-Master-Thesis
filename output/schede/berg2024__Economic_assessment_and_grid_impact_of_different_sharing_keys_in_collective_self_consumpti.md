# berg2024 — Economic assessment and grid impact of different sharing keys in collective self-consumption

- **File sorgente:** `Paper/Economic assessment and grid impact of different sharing keys in collective self-consumption.pdf` (5 pagine, testo estraibile)
- **Tipo:** conference paper (IEEE PES ISGT Europe 2024)
- **Lettura:** integrale (pp. 1–5); bibliografia non letta riga per riga.
- **Convenzioni:** pagine = indici di pagina del PDF. `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente o ambigua. Il simbolo "€" è estratto come "C".

## 1. Riferimento bibliografico
Berg, K.; Rana, R.; Taxt, H.; Dynge, M. F. (2024). *Economic assessment and grid impact of different sharing keys in collective self-consumption.* 2024 IEEE PES Innovative Smart Grid Technologies Europe (ISGT EUROPE). DOI 10.1109/ISGTEUROPE62998.2024.10863813. NTNU (Trondheim) e SINTEF Energy Research. Progetti FINE (308833) e FME CINELDI (257626).

## 2. Obiettivo e research question
- **Obiettivo (autori, abstract p. 1; p. 1):** studiare come il nuovo schema di autoconsumo collettivo (CSC) norvegese incide sulla riduzione dei costi dei membri e sullo scambio fisico con la rete, confrontando due chiavi di ripartizione statiche: **uguale** e **proporzionale al consumo annuo**.
- **Gap dichiarato (p. 1):** "there is no literature on CSC in Nordic countries, and none of the papers mentioned has quantified the impact on the grid" (negativa universale degli autori, cfr. B.3).
- **RQ formulata come domanda?** No.

## 3. Contesto
- **Paese / quadro normativo:** Norvegia; schema CSC in vigore da ottobre 2023, fino a 1 MW di generazione installata per proprietà; tariffe di rete con quota di capacità a scaglioni (Tab. II: 12,5; 20; 32,5; 45; 57,5 €/mese per i picchi mensili 0–2, 2–5, 5–10, 10–15, 15–20 kWh/h) e compensazione perdite 0,6 c€/kWh (apr–ott) e 0,85 c€/kWh (nov–mar) (p. 3).
- **Tipo di CER:** CSC con un impianto PV comune da 1 MWp (1/3 sud, 1/3 sud-est, 1/3 sud-ovest) e distribuzione *virtuale* oraria della produzione tramite chiave.
- **Membri:** 423 famiglie fittizie nell'area di Oslo con profili orari reali 2021 (58% appartamenti, 18% case a schiera, 15% unifamiliari, ecc.); carico annuo 5.064 MWh, PV 968 MWh (p. 3).

## 4. Metodo
- **Casi (Tab. I, p. 3):** Ref (nessun PV); No CSC-E (PV immesso in rete, ricavi divisi in parti uguali); E (CSC, chiave uguale `γ = 1/N`); YC (CSC, chiave proporzionale al consumo annuo `γ_h = E_h/ΣE`); YC-flex (come YC con possibilità di spostare il 20% del carico, costo di disagio 0,02 €/kWh).
- **Costo operativo di una famiglia:** `SC + GEC + T + GCC − ER` (spot, energia di rete, tasse, capacità di rete, ricavo di immissione; Eq. 1–3). Per YC-flex, MILP individuale per famiglia (Eq. 4–18).
- **Equità:** Equality Index (derivato dal Gini, rif. [10]) calcolato sulla differenza di costo rispetto al Ref: `EI_absolute` sul beneficio assoluto (equality) ed `EI_relative` sulla riduzione relativa (equity) (Eq. 19, p. 2).
- **Software:** `[NON SPECIFICATO]`.

## 5. Meccanismi di ripartizione analizzati
Chiavi statiche di distribuzione della produzione PV: **uguale** e **proporzionale al consumo annuo**; il caso senza CSC divide i ricavi di immissione in parti uguali.

## 6. Metriche
- **Economiche:** costi annuali (k€) per componente, riduzione di costo assoluta (€) e relativa (%) per famiglia (Fig. 4–5).
- **Tecniche:** import/export cumulati e di picco al punto di accoppiamento comune, tasso di autoconsumo (SCR).
- **Equità:** `EI_absolute` ed `EI_relative`.
- **Sociali / ambientali / engagement:** nessuna.

## 7. Risultati principali
- **Scambio con la rete (Tab. III, p. 4):** import 5.065 MWh (Ref) → 4.269 MWh (PV senza flessibilità) / 4.240 MWh (YC-flex); export 173 → 144 MWh; picco di import 1,35 MWh/h → 1,48 MWh/h con flessibilità (**+9,6%**); picco di export 0,51 → 0,47 MWh/h (−7,8%); SCR 82% → 85%.
- **Costi (Tab. IV, k€):** Ref 796; No CSC-E 731; E 698; YC 693; YC-flex 668. Gli autori: YC-flex "reduces total costs with 16% compared to the reference case, and by 9% compared to case E" (p. 4).
- **Distribuzione fra famiglie:** con YC le riduzioni assolute sono molto più disperse (fino a ≈ 1000 €, con flessibilità fino a ≈ 1200 €) ma le riduzioni relative restano entro il 25%; con No CSC-E ed E le riduzioni relative arrivano fino al 60% per alcune famiglie (Fig. 4–5).
- **Equità (Tab. V, p. 5):** `EI_absolute` / `EI_relative`: No CSC-E 1 / 0,66; E 0,936 / 0,71; YC 0,622 / 0,93; YC-flex 0,639 / 0,94. Gli autori: le due chiavi rappresentano "two different views of fairness: equality (case E) and equity (case YC)"; il confronto va fatto rispetto alla propria definizione, non fra le due.
- **Impatto sulla rete:** i costi di rete della comunità diminuiscono, ma il picco di import aumenta o resta invariato: "it is likely that the CSC scheme, with the present grid tariffs, will lead to grid costs being shifted over to other end-users" (p. 4–5).

## 8. Limitazioni dichiarate dagli autori
- p. 5 (Sez. III-C): "to get the full picture of the fairness, the investment costs and their distribution would need to be included."
- Altro: due sole chiavi statiche; comunità fittizia con profili reali; aumento del picco legato a flessibilità + prezzi spot + tariffe a scaglioni, "not a direct result of PV generation or the CSC scheme" (p. 4).

## 9. Future work dichiarati dagli autori
Nessuna sezione "future work". Passaggio di Sez. III-C (p. 5): "The fairness evaluation here is a good starting point for considering the distribution of investment costs and revenues when introducing shared assets within a CSC scheme. This is relevant also when introducing and comparing alternative sharing keys, as these could reflect the distribution of investment costs."
`[INFERENZA — test B.1]` Mix: l'ancora è un confronto di chiavi (2 chiavi) con richiesta di includere i costi di investimento e di confrontare chiavi alternative; il carattere è **generale** per il tema "più chiavi e distribuzione dell'investimento", ma la formulazione è un accenno, non un'indicazione esplicita.

## 10. Note del lettore (inferenze mie)
- `[INFERENZA — aritmetica sulla Tab. IV]` Rispetto al caso E (698 k€) YC-flex (668 k€) riduce il costo del 4,3%, non del 9%: il 9% (8,6%) corrisponde invece al confronto con "No CSC-E" (731 k€). Probabile errore di riferimento nel testo.
- `[INFERENZA]` È tra i pochi paper del corpus che usa **due indici di equità paralleli** (assoluto = equality, relativo = equity) sullo stesso esito: schema riusabile.
- `[INFERENZA]` Il contesto norvegese (prezzi spot, tariffe di capacità a scaglioni) è molto diverso dal regime italiano; i risultati sull'impatto di rete non sono trasferibili ma la metodologia di valutazione (picchi, SCR) sì.
- `[INFERENZA]` Le chiavi sono statiche e applicate alla *produzione PV*, non a un incentivo sull'energia condivisa; l'effetto di chiavi dinamiche è fuori campo.
