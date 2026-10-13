# awerkin2026 — Optimal investment and fair sharing rules of incentives in virtual renewable energy communities

- **File sorgente:** `Paper/Optimal_investment_and_fair_sharing_rules_of_incentives_in_virtual_renewable_energy_communities.pdf` (47 pagine; testo estraibile; Fig. 1–11 non ispezionate, descritte dal testo)
- **Tipo:** articolo su rivista (Annals of Operations Research); modello analitico a due livelli (Stackelberg + Nash) in tempo continuo con processi di Lévy, calibrato su prezzi italiani storici; caso stilizzato a due agenti.
- **Lettura:** integrale del corpo (pp. 1–37, incluse Prop. 4.3, 4.6, 4.9 con le condizioni degli equilibri e tutta la sezione 5); appendice: lette la dimostrazione del Lemma 4.1 e la parte iniziale e centrale di quella della Prop. 4.9; **dimostrazioni non verificate riga per riga**; Appendice B (stima delle stagionalità) e bibliografia non lette.
- **Convenzioni:** pagine = indici di pagina del PDF (pagina PDF = pagina della rivista − 2750). `[INFERENZA]` = mia valutazione. `[NON SPECIFICATO]` = informazione assente. Le virgolette « » riportano il testo degli autori.

## 1. Riferimento bibliografico
Awerkin, A.; Falbo, P.; Vargiolu, T. (2026). *Optimal investment and fair sharing rules of incentives in virtual renewable energy communities.* **Annals of Operations Research**, 364, 2751–2797. https://doi.org/10.1007/s10479-026-07336-1. Ricevuto 2/1/2026; accettato 23/6/2026; online 4/8/2026. Università di Padova (Matematica) e Università di Brescia (Economia). Open access. Dati: serie pubbliche GME (PUN, gas PSV) e ARERA (consumi), Eurostat per il prezzo di acquisto (pp. 22–23).

## 2. Obiettivo e research question
- **Obiettivo (abstract p. 1):** esaminare insieme l'investimento in tecnologie rinnovabili e la ripartizione equa degli incentivi in una REC «under the so-called virtual framework», composta da una famiglia e un produttore di biogas.
- **Quattro RQ (Sez. 2.1, p. 7):** (1) interazione fra regola di ripartizione e investimenti di membri eterogenei; (2) se la REC emerge come equilibrio di Nash del gioco decentralizzato degli investimenti; (3) come cambia l'equilibrio quando la regola è scelta da un coordinatore; (4) implicazioni di policy, in particolare quando serve «guidance on the internal allocation of the collective benefit».
- **Gap dichiarati:**
  - (p. 3) «a critical issue, which, to the best of our knowledge, has not yet been addressed in the literature, is the development of a fair and effective mechanism for distributing the incentive among the members of a virtual REC.»
  - (p. 6) «a gap remains in the analytical characterization of RECs under both virtual and physical frameworks, where agents decide competitively with respect to their investment. Most existing works assume a cooperative environment where a central planner or a cooperative game dictates the distribution of benefits.»
  - `[INFERENZA]` Il primo è una universale negativa non coerente con la stessa rassegna del paper (p. 5–6), che cita come studi sulla ripartizione degli incentivi `moncecchi2020` (Shapley), `norbu2021a`, `zatti2021` e altri. Per la nostra tesi conta il secondo: il paper colloca la propria novità nell'analisi *analitica* con investimenti strategici, non nella ripartizione ex post.

## 3. Contesto
- **Paese / quadro normativo:** Italia come esempio di «virtual framework» (Sez. 1, pp. 2–3): tutta la produzione è venduta al mercato tramite un'autorità (GSE), i membri continuano ad acquistare dai propri fornitori e l'autoconsumo della REC è definito per ora come «the minimum of collective consumption and generation» (p. 3). Incentivo proporzionale all'autoconsumo cumulato.
- **Tipo di REC:** due agenti rappresentativi: un produttore di biogas (BP, con turbina gas-to-power) e una famiglia (aggregato di utenti omogenei) che può installare FV; BP senza domanda propria. Con questa struttura «the BP's veto power is not contractual, but arises de facto» (p. 7): senza BP non c'è REC; la famiglia può partecipare anche con zero FV, come consumatore puro.
- **Coordinatore (p. 13):** un ente (comune o ESCo) che sceglie la regola di ripartizione.

## 4. Metodo
- **Autoconsumo della REC (Eq. 16, p. 13):** `q(t) = min(D(t), α·y_h + y_b)`, con produzione FV **costante** `α y_h` (α = 1500/8760) e domanda `D` stocastica (processo di Lévy geometrico). «While constant PV generation is an evident simplification…» (p. 11). Quindi **nessun profilo orario**.
- **Incentivo:** tariffa piatta `Z` per unità di energia autoconsumata su un periodo di durata aleatoria `τ` esponenziale di parametro `λ`; quota `β` alla famiglia e `1 − β` al BP (p. 13). Decisioni statiche, prese a `t = 0`, orizzonte infinito.
- **Struttura (Fig. 3, p. 15):** gioco di Nash fra i due membri per ogni `β` (best response in forma chiusa, Prop. 4.3 e 4.6; Prop. 4.9: nove tipi di equilibri), poi il coordinatore massimizza il prodotto di Nash dei guadagni rispetto ai punti di disaccordo `d_h, d_b` (profitti da stand-alone, Eq. 18–19, 44–45).
- **Calibrazione (Sez. 5.1, pp. 22–24):** PUN orario 2014–2024, prezzo gas PSV, domanda residenziale mensile; destagionalizzazione per regressione armonica; salti stimati con soglia a 3σ; ipotesi di martingala per domanda, prezzo e gas (p. 24).
- **Parametri (Tab. 3, p. 25):** `c_h` = 1.600.000 €/MW; `c_b` = 1.500.000 €/MW; `θ_h` = 0,3125 MW (budget 500.000 €); `θ_b` = 0,20 MW; `Z` = 110 €/MWh («the example of the Italian incentive tariff»); `r` = 3,4247·10⁻⁶ 1/h (3% annuo); `λ` = 0,00001.

## 5. Meccanismi di ripartizione analizzati
- **Regola implementata:** una sola, la percentuale `β` dell'incentivo alla famiglia scelta dal coordinatore con criterio di Nash bargaining (NB), con disaccordo = profitto individuale senza REC.
- **Regole discusse solo a parole (pp. 14–15):** parti uguali (`β = 1/n`), proporzionali (a capacità installata, investimento o contributo all'autoconsumo; richiederebbero un problema di punto fisso perché le capacità sono esse stesse esito di equilibrio), basate sul welfare (Abada et al. 2025), Shapley. Quest'ultima, in un gioco a due, «would either reduce to equal sharing or to an equal split of surplus above disagreement payoffs» (p. 14–15). A p. 6: «for a game with two participants, as in our case study, the Shapley value becomes trivial, allocating half of the value of the community to each player, missing the investment effort and demand contribution.»
- Le regole alternative sono lasciate al future work: «while leaving a systematic theoretical and numerical comparison of alternative allocation principles to future research» (p. 15).

## 6. Metriche
Profitti attesi scontati di famiglia e BP (`J_h`, `J_b`); capacità installate `y_h*`, `y_b*`; quota `β*`; autoconsumo atteso scontato `w` (Eq. 17, 21); surplus congiunto `F` (prodotto di Nash). Nessun indice di equità, nessun confronto fra regole.

## 7. Risultati principali (numeri dal paper)
- **Struttura analitica (Prop. 4.9, pp. 19–20):** nove equilibri di Nash. I casi 6.1 e 6.2 sono definiti «the socially desirable outcome» (p. 20): gli incentivi sono decisivi e l'investimento congiunto è vicino alla domanda attesa; i casi 1, 2, 3.x, 4.x, 7 indicano possibile «over-subsidization»; nei casi 7, 8 e 9 la REC non nasce.
- **Esempio calibrato (Tab. 4–5, pp. 25–26):** `g_h` = 2,4·10⁶ e `g_b` = −3,69·10⁶ (€/MW scontati); equilibrio 4.2 (famiglia investe al massimo senza bisogno di incentivo; il BP investe solo grazie all'incentivo). `β*` = 0,2543; `y_h*` = 0,3125 MW; `y_b*` = 0,1668 MW; capacità totale `α y_h* + y_b*` = 0,2203 MW contro `d` = 0,3 MW. Verifica mia: `g_h` e `g_b` ricalcolati dalla Tab. 2–3 (con `r_v = r_p = r` per l'ipotesi di martingala, p. 24) coincidono con la Tab. 4 (2,4·10⁶ e −3,69·10⁶); 0,1712·0,3125 + 0,1668 = 0,2203.
- **Sensibilità (pp. 26–36):** soglie di cambio equilibrio: `c_b` fino a 5,61 M€/MW (4.2), oltre solo FV (7); `r` = 2,305% e 7,6%; `σ_d` = 0,0095; domanda `d` = 0,06 MW; prezzo elettrico `x_v` a 32, 66 e 93 €/MWh; prezzo gas `p` a 30 e 40,7 €/MWh. A prezzi alti dell'elettricità (≥ 93 €/MWh) `β*` converge verso una ripartizione «approximately symmetric» e l'incentivo diventa «a pure transfer» (p. 35).
- **Conclusioni (pp. 36–37):**
  - la regola di ripartizione «is not a mere redistribution device but a determinant of the equilibrium investment pattern» (p. 36);
  - il coordinatore agisce da «equilibrium-selection device»;
  - «within our stylized setting a uniform incentive scheme cannot, in general, ensure economically efficient REC formation»;
  - «the current Italian framework, despite providing an advanced virtual REC scheme, may not yet appear complete: by remaining silent on the principles governing the distribution of the incentives inside a REC, it potentially leaves unresolved a coordination problem» (p. 37).

## 8. Limitazioni dichiarate dagli autori
- Struttura a due agenti e processi stilizzati «necessary to maintain analytical tractability» (p. 37).
- Produzione FV costante; ipotesi di martingala come benchmark «rather than as an empirical description» (p. 24).
- «The numerical values obtained in the calibrated case should be read as case-specific evidence, whereas the threshold structure and the equilibrium regimes are structural implications of the model.» (p. 22).
- La scelta di processi geometrici di Lévy (invece di mean-reverting) è motivata dalla trattabilità analitica (p. 10).
- Disaccordo = investimento stand-alone, decisioni statiche, nessun accumulo, nessun profilo orario; la dinamica dell'espansione delle capacità è fuori dalla classe trattabile (p. 6).
- `[INFERENZA]` Non dichiarato: la durata attesa dell'incentivo con `λ` = 10⁻⁵ 1/h è 1/λ = 100.000 h ≈ 11,4 anni (calcolo mio); per quanto ho letto il paper non lo discute rispetto alla durata normativa.

## 9. Future work dichiarati dagli autori
Elenco (pp. 15 e 37; verifica B.2): (i) separare giorno e notte nel profilo FV, con il G2P che sostiene l'autoconsumo quando il FV si ferma; (ii) accumulo a batteria; (iii) criteri alternativi per la regola di ripartizione: «The choice of alternative criteria for the sharing rule would also be extremely interesting. However, alternative criteria in many cases require significant changes in the economic assumptions and in the mathematical settings, so this line of research would benefit from a dedicated future study.» (p. 37); (iv) espansione dinamica delle capacità; (v) a p. 15: «a systematic theoretical and numerical comparison of alternative allocation principles».
`[INFERENZA — test B.1]`
- (i), (ii), (iv): autoreferenziali.
- (iii) e (v): **misti (M)**. Il tema è generale (confronto fra principi di allocazione), ma il paper è un lavoro con una sola regola (NB) e la richiesta è formulata come estensione del proprio modello; gli autori stessi dichiarano che richiederebbe cambiare il quadro matematico. È l'unico future work del corpus che nomina esplicitamente un confronto sistematico, teorico e numerico, di più principi di allocazione; ancora media, non forte.

## 10. Note del lettore (inferenze mie)
- **Rilevanza per la tesi: alta come argomento concettuale, bassa come evidenza.** Il paper non ripartisce un incentivo fra molti membri e non usa profili orari. Contribuisce con tre idee:
  1. **la regola cambia la torta quando gli investimenti sono endogeni**, mentre nel tuo modello ex post, con configurazione fisica fissa, la torta non dipende dalla regola (README). I due punti di vista sono complementari: il paper è il motivo per cui la regola ex post conta lo stesso (cambia gli investimenti e i comportamenti futuri), e il tuo indicatore di forza incentivante `IS` (covarianza fra quota e virtuosità) è un proxy di quel canale;
  2. **la ripartizione interna come questione regolatoria a sé**: «This makes the allocation of the collective benefit a regulatory issue in its own right, rather than a purely internal matter of the community.» (p. 37). È un'ancora autorevole (rivista di ricerca operativa, agosto 2026) per dire che la norma italiana tace sulla ripartizione interna; è una conclusione degli autori sul loro modello stilizzato, non una verifica giuridica `[non ho letto Paper/Directive]`;
  3. **il vincolo di razionalità individuale come punto di disaccordo**: la NB usa il profitto stand-alone come disaccordo, quindi è una versione a due giocatori del vincolo di partecipazione che nel tuo codice corrisponde alla coalition excess.
- **Nash bargaining con due giocatori (collegamento con la tua distinzione):** nel testo la NB è il criterio del coordinatore su `β`; con utilità trasferibili e torta fissata coincide con la divisione in parti uguali del surplus sopra il disaccordo (gli autori lo dicono a p. 14–15 per la regola alla Shapley). Qui la torta non è fissa perché dipende dagli investimenti, ed è la ragione per cui `β*` = 0,2543 non è 0,5. Il tuo metodo 3 (Yan et al. 2023, proporzionale al contributo marginale) è altra cosa e non è toccato.
- **Imprecisione da non copiare:** la frase «the Shapley value becomes trivial, allocating half of the value of the community to each player» (p. 6) è vera solo se i valori dei singoli sono uguali (qui lo sono se entrambi i valori da soli sono zero); in generale Shapley a due giocatori vale `v(N)/2 + (v(i) − v(j))/2` `[verifica mia]`. A p. 14–15 la formulazione è corretta («equal split of surplus above disagreement payoffs»).
- **Incongruenze minori (mie verifiche):**
  - il titolo della Sez. 5.3.1 dice «PV cost c_h» ma tratta il costo della turbina `c_b`; il titolo della Sez. 5.3.4 dice «power demand volatility d» e tratta `σ_d`;
  - gli autori scrivono che il risultato dell'esempio corrisponde a «NE 4.2 (g_h > 0, g_b < 0 and β > β_b)»: dalla Tab. 4 `β_b` = −0,2043, quindi la condizione è soddisfatta per ogni `β` positivo e non discrimina.
- **Limite per l'uso come competitor:** non è un competitor diretto. Non confronta regole, non ha profili orari, non ha più di due membri; la sua novità è analitica. Non ne dedurrei che «il gap sul confronto di regole» sia stato coperto (B.3), ma neppure che lo supporti da solo.
