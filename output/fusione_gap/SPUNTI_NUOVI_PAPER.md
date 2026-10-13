# Spunti dai cinque nuovi paper (13/10/2026)

**Perimetro.** Hai scritto «7 paper», ma nella cartella caricata ci sono **5 PDF**: Chatel et al., Avanzini et al., Biancardi et al., Thomopulos et al., Calcagnotto et al. (tutti 2026). Se mancano due paper, caricali e li aggiungo. Tutto ciò che segue è letto per intero dai PDF; le idee d'uso sono **mie inferenze** e lo dico caso per caso. Non ho letto `Paper/Directive` né i file `.m` del tuo codice (solo il README).

## 1. Valutazione onesta in una tabella

| Paper | Utilità per il tuo paper | Perché |
|-------|--------------------------|--------|
| `chatel2026` (RSER) | **Alta come citazione**, nulla come evidenza | Rassegna recente e autorevole con dichiarazioni di gap utilizzabili come ancora; non misura nulla |
| `calcagnotto2026` | **Media** | Dà un'ancora sul tema equità individuale e un contrasto utile ex-ante contro ex-post; ma 2 casi, nessun indicatore di equità |
| `biancardi2026` | **Media** (per il codice) | Pesi di categoria empirici italiani per il Cascading Tree; disegno a due fattori; ma ha incongruenze numeriche e conflazione autoconsumo/energia condivisa |
| `avanzini2026` | **Media-bassa** | Evidenza indipendente che la contabilizzazione pesa più dell'energia; dichiara la ripartizione interna come non modellata |
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

## 3. Controlli da fare sul tuo codice (non ho potuto farli io)
1. **Contributo ARERA da 10,57 €/MWh.** `avanzini2026` e `biancardi2026` lo includono nella remunerazione della CER (0,01057 €/kWh nel secondo). Verifica se `P_CER_h` lo contiene e se la scelta è coerente con la norma.
2. **PUN o prezzo zonale nella TIP.** `thomopulos2026` (Eq. 16) usa il PUN più una costante zonale `k_z`; il tuo README (`load_zonal_price.m`) e gli altri documenti usano il prezzo zonale orario. Va deciso sulla norma, che non ho letto.
3. **Implementazione di F e categorie esenti** (per la Proposta 4): mi serve vedere il file `.m` che calcola `v(S)`.

## 4. Cose che NON conviene fare
- Citare Chatel come prova che «i compromessi esistono»: è giudizio qualitativo di rassegna.
- Usare i future work di Avanzini, Biancardi o Thomopulos come ancora: sono autoreferenziali.
- Riprendere IRR e tempi di ritorno di Biancardi, o i tempi di calcolo di Calcagnotto (Tab. 3 ha righe che sembrano scambiate).
- Dire che «nessuno ha fatto X» in base ai gap dichiarati dagli autori (B.3): sono universali negative.

## 5. Decisione che serve da te
Quale ancora: Proposta 1, 2, 3, l'assemblaggio, oppure la **Proposta 4** (regolazione nel gioco, ancorata a Chatel)? Scelta quella, scrivo la V3 con verifica verbatim. Se la Proposta 4 ti interessa, prima faccio il controllo numerico di monotonia e nucleo con F sui dati che hai, per vedere se regge.
