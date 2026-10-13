# Spunti dai sette nuovi paper (13/10/2026)

**Perimetro.** I sette paper (tutti 2026) sono: Chatel et al., Avanzini et al., Biancardi et al., Thomopulos et al., Calcagnotto et al. (arrivati per primi) e D'Adamo et al. e Awerkin et al. (arrivati dopo). Tutti letti per intero dai PDF, tranne le dimostrazioni in appendice di Awerkin (non verificate riga per riga). Le idee d'uso sono **mie inferenze** e lo dico caso per caso. Non ho letto `Paper/Directive` né i file `.m` del tuo codice (solo il README).

## 1. Valutazione onesta in una tabella

| Paper | Utilità per il tuo paper | Perché |
|-------|--------------------------|--------|
| `chatel2026` (RSER) | **Alta come citazione**, nulla come evidenza | Rassegna recente e autorevole con dichiarazioni di gap utilizzabili come ancora; non misura nulla |
| `calcagnotto2026` | **Media** | Dà un'ancora sul tema equità individuale e un contrasto utile ex-ante contro ex-post; ma 2 casi, nessun indicatore di equità |
| `biancardi2026` | **Media** (per il codice) | Pesi di categoria empirici italiani per il Cascading Tree; disegno a due fattori; ma ha incongruenze numeriche e conflazione autoconsumo/energia condivisa |
| `avanzini2026` | **Media-bassa** | Evidenza indipendente che la contabilizzazione pesa più dell'energia; dichiara la ripartizione interna come non modellata |
| `awerkin2026` (Annals of OR) | **Alta come argomento concettuale, bassa come evidenza** | Mostra che la regola di ripartizione cambia gli investimenti e la nascita della REC; dice che la norma italiana tace sulla ripartizione interna; unico future work del corpus che nomina un confronto sistematico fra principi di allocazione. Ma ha 2 agenti, niente profili orari, una sola regola (Nash bargaining) |
| `dadamo2026` | **Bassa-media** | Regola ad hoc su 7 membri con vincolo del 10% sul reddito dei vulnerabili; nessun confronto fra regole, nessun indice di equità; afferma più di quanto mostra |
| `thomopulos2026` | **Bassa** | Non ripartisce nulla; interessa solo per il secondo flusso di valore e per un controllo sul prezzo (PUN o zonale) |

## 2. Spunti, dal più utile

### 2.1 Chatel come ancora per le tre proposte (e forse per una quarta)
Chatel (RSER, maggio 2026) contiene quattro frasi che coprono i tre assi delle `PROPOSTE_ANCORA_GAP.md`:

| Asse | Frase di Chatel (verificata sul PDF) | Pagina | Proposta |
|------|--------------------------------------|--------|----------|
| Compromessi | «Third, efficiency, fairness, scalability, and regulatory embedding are not orthogonal dimensions. Improving one dimension often weakens another.» | 20 | 1 (impossibilità assiomatica → trade-off misurato) |
| Misura | «A first limitation concerns the lack of conceptual alignment between performance metrics. […] without a systematic articulation of how these criteria interact or conflict.» | 19 | 2 (validità delle misure di equità) |
| Equità integrata | «fairness is rarely embedded simultaneously across dispatch decisions, pricing rules, and regulatory conditions» | 19 | 1, 3 |
| Regolazione | «Many optimization-based models treat regulation as an exogenous constraint rather than an endogenous design parameter» | 17 | **4 (nuova)** |

**Onestà sui limiti.** Sono dichiarazioni qualitative (la Tab. 2 usa giudizi verbali, p. 17) e la rassegna non cita il caso italiano. Funzionano da «stato dell'arte autorevole», non da evidenza. Il suo future work (p. 20, quattro punti) è generale, quindi regge meglio dei future work autoreferenziali degli altri (test B.1), ma è una rassegna: la sua forza è l'autorevolezza della sede, non la precisione.

### 2.2 Proposta 4 (nuova): la regolazione come parte del gioco
Hai detto che «il cambio di regime regolatorio» come cuore ti sembra banale. Chatel offre un modo diverso di dirlo: il problema non è *che* il regime cambia, ma che la letteratura tratta la regolazione come vincolo esogeno. Nel tuo modello la regolazione **entra nel gioco**: con il fattore di riduzione F e le categorie esenti, il valore di coalizione dipende dalla composizione per categoria e non è monotono (README §7.5, esempio 1,00 € contro 0,75 €). Quindi:

- **Formulazione possibile `[INFERENZA]`:** «Quando la regolazione entra nel valore di coalizione, le proprietà su cui si basano le regole di teoria dei giochi (monotonia, bilanciamento) cessano di valere; quali regole mantengono nucleo non vuoto, e con quale perdita di fairness?»
- **Perché è meno banale:** la domanda è sulle proprietà del gioco, non sul fatto che ci sia una legge nuova.
- **Rischi (da dichiarare):** (a) l'esempio 1,00 € contro 0,75 € è tuo (README), non della letteratura; devo vedere nel codice come F è implementato prima di scrivere il claim; (b) non so se il nucleo sia vuoto nei tuoi casi: è una verifica numerica, non un dato; (c) è un'ancora **concettuale** (Chatel) più una **dimostrazione tua**: va bene per un paper, ma bisogna che la parte dimostrativa regga.
- **Compatibile con "codice poco modificato":** la verifica del nucleo e della monotonia con F è un controllo su `v(S)` che hai già; non servono nuovi metodi.

### 2.3 Calcagnotto: l'equità individuale come ancora debole ma utile
La sua frase finale (p. 12): «Future work could also address more in detail the fairness aspect of allocation, i.e., assuring individual benefits for the REC's members, especially in the case of members in vulnerability.» È **generica** (non legata al suo metodo), quindi passa il test B.1 meglio degli altri future work, ma è una frase di chiusura senza argomentazione: non farne l'ancora principale.

Due cose più solide:
1. **Evidenza che i KPI aggregati nascondono i rischi individuali** (mia lettura della Tab. 4, CS1): `SavingsREC` varia tra 32,03% e 32,55% fra i 16 modi, mentre `SavingsComAreas` va da 18,03% a 28,32%. Con due soli membri è un'illustrazione, non una prova.
2. **Contrasto ex-ante contro ex-post.** Nel loro regime la regola determina la torta; in quello italiano no. Utile nella discussione per dire perché i loro risultati sulla «efficienza della regola» non si trasferiscono e perché nel tuo regime la domanda è solo distributiva `[INFERENZA]`.

### 2.4 Biancardi: pesi per categoria da usare nel codice
- Pesi dichiarati dai 403 rispondenti: produttori 35%, consumatori 31%, famiglie in difficoltà economica 13%, riqualificazione territoriale 18,5% (testo e Tab. 14), Stato 2,5%. Il caso illustrativo usa 18,0% e 3,0% (incongruenza interna, la segnalo).
- **Uso `[INFERENZA]`:** tarare le percentuali dei metodi ad albero (Cascading Tree) con una fonte empirica italiana invece di una scelta arbitraria, e provare il disegno a due fattori che suggeriscono (pesi di categoria × regola interna, p. 12). Non richiede nuovo codice, solo nuovi parametri.
- **Cautele:** i pesi sono preferenze scelte su sei profili predefiniti, non un ottimo; lo «Stato» e la «riqualificazione territoriale» come destinatari non sono discussi giuridicamente (non ho letto la norma); il modello applica l'incentivo a una quota di autoconsumo e non al minimo orario, quindi **non** replicare i loro IRR.

### 2.5 Avanzini: sostegno al tuo schema a due strati
«the economic outputs are largely decoupled from energy performance and are mainly determined by accounting rules» (p. 15) e «The implications for individual actors ultimately depend on how the revenues from shared energy are redistributed within the REC, which is not modelled in this study» (p. 13). La seconda frase è una **limitazione dichiarata, non un future work**: puoi citarla come «gli autori stessi indicano che la ripartizione interna non è modellata», non come «gli autori chiedono». Supporta la separazione valorizzazione/allocazione del tuo modello.

### 2.6 Thomopulos: solo spunti laterali
Il valore ripartibile può avere più flussi (incentivo + mercato del bilanciamento) e spostare carichi può ridurre l'energia condivisa (la dipendenza dal rapporto produzione/domanda, p. 14). Fuori dal perimetro attuale: lo annoto per una eventuale RQ-2.

### 2.7 Awerkin, Falbo, Vargiolu (Annals of OR, agosto 2026): l'ancora che cercavi?
Hai detto che il solo cambio di regime regolatorio è banale. Questo paper offre una ragione diversa per cui la regola conta, e una frase di policy forte:

| Cosa dice (verificato sul PDF) | Pagina | Come usarla `[INFERENZA]` |
|---|---|---|
| «the sharing rule is not a mere redistribution device but a determinant of the equilibrium investment pattern» | 36 | Motivo per cui la regola ex post conta anche con torta fissa: cambia investimenti e comportamenti futuri. Il tuo `IS` è il proxy di quel canale |
| «This makes the allocation of the collective benefit a regulatory issue in its own right, rather than a purely internal matter of the community.» | 37 | Ancora per la ripartizione interna come questione regolatoria. Conclusione degli autori sul loro modello, non una verifica giuridica |
| «the current Italian framework [...] by remaining silent on the principles governing the distribution of the incentives inside a REC, it potentially leaves unresolved a coordination problem» | 37 | Idem; attenzione al «may not yet appear complete», è formulata con cautela |
| «while leaving a systematic theoretical and numerical comparison of alternative allocation principles to future research» | 15 | Future work di tipo M (B.1): tema generale, ma estensione del proprio modello a regola unica. Dichiara anche che richiederebbe di cambiare il quadro matematico |

**Cautele:** (1) è un modello stilizzato a due agenti (biogas e famiglia), con produzione FV costante e senza profili orari; non è un competitor sul confronto di regole, ma neppure un'evidenza empirica; (2) la sua frase «has not yet been addressed in the literature» (p. 3) è contraddetta dalla loro stessa rassegna: non usarla; (3) la Nash bargaining con due giocatori è un caso particolare, non toccare il tuo metodo 3 (Yan et al.).

**Come cambia la Proposta 1:** l'impossibilità assiomatica di `gonzalezasenjo2025` e il «not orthogonal» di Chatel si possono affiancare a un argomento di *perché la regola conta anche ex post*. Per la Proposta 4: Awerkin suggerisce che i parametri regolatori non vanno trattati come esogeni, in coerenza con Chatel p. 17.

### 2.8 D'Adamo et al. (Energy Nexus 2026): da leggere con cautela
Stesso gruppo di `basilico2025` e `biancardi2026`. Utile per due cose: (1) un vincolo esplicito di accettabilità dei prosumer (prezzo interno mai sotto il prezzo di vendita al GSE), che è una condizione di razionalità individuale da considerare nel tuo codice come vincolo o indicatore; (2) la definizione di vulnerabile come spesa oltre il 10% del reddito, con parametri 0,133 e 0,12 €/kWh. **Problemi:** l'abstract dice che la ripartizione mirata è «more effective than uniform allocation approaches», ma nel paper non c'è alcuno scenario con ripartizione uniforme (Tab. 7 confronta con e senza consumatori e incentivi); il trasferimento di incentivo è 60 €/anno su 14.255 € (0,42%); l'energia condivisa è annuale e la TIP è fissata al massimo; la Tab. 2 etichetta 0,124 €/kWh come comprensivo della componente ARERA, ma il testo lo deriva senza.

## 3. Controlli da fare sul tuo codice (non ho potuto farli io)
1. **Contributo ARERA (valori discordanti nel corpus).** `avanzini2026` e `biancardi2026` riportano 10,57 €/MWh (0,01057 €/kWh nel secondo); `dadamo2026` scrive «around 8 €/MWh in 2025» (p. 4) e poi usa 0,124 €/kWh senza la componente ARERA. Verifica se `P_CER_h` lo contiene e se la scelta è coerente con la norma.
2. **PUN o prezzo zonale nella TIP.** `thomopulos2026` (Eq. 16) usa il PUN più una costante zonale `k_z`; il tuo README (`load_zonal_price.m`) e gli altri documenti usano il prezzo zonale orario. Va deciso sulla norma, che non ho letto.
3. **Implementazione di F e categorie esenti** (per la Proposta 4): mi serve vedere il file `.m` che calcola `v(S)`.

## 4. Cose che NON conviene fare
- Citare Chatel come prova che «i compromessi esistono»: è giudizio qualitativo di rassegna.
- Usare i future work di Avanzini, Biancardi, Thomopulos o D'Adamo come ancora: sono autoreferenziali. Quello di Awerkin è misto: usabile con la cautela di §2.7.
- Usare l'affermazione di D'Adamo sulla ripartizione mirata più efficace di quella uniforme: nel paper non è confrontata.
- Riprendere IRR e tempi di ritorno di Biancardi, o i tempi di calcolo di Calcagnotto (Tab. 3 ha righe che sembrano scambiate).
- Dire che «nessuno ha fatto X» in base ai gap dichiarati dagli autori (B.3): sono universali negative.

## 5. Decisione che serve da te
Quale ancora: Proposta 1, 2, 3, l'assemblaggio, oppure la **Proposta 4**; Awerkin (§2.7) può affiancare la 1 o la 4 (regolazione nel gioco, ancorata a Chatel)? Scelta quella, scrivo la V3 con verifica verbatim. Se la Proposta 4 ti interessa, prima faccio il controllo numerico di monotonia e nucleo con F sui dati che hai, per vedere se regge.
