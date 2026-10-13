# Tre ancore alternative per il gap (senza il cambio di regime come cuore)

**Premessa (Parte A, senza giri di parole).** Hai ragione sul cuore del V1. Il «cambio di regime regolato» è debole per tre motivi: (1) il tuo stesso README mostra che il vincolo di ammissibilità sulle schede esistenti non morde (§7.4: dal 2,2% al 25,7% contro il 55%); (2) invita la domanda «e quindi?»: cambiare regime cambia il contesto, non produce di per sé una conoscenza nuova; (3) il passo di González-Asenjo e Izquierdo 2026 su «regulatory constraints» è una frase generica di limiti. Il regime può restare, ma come **condizione che rende possibile la domanda**, non come contributo.

Ho cercato nel corpus affermazioni che siano (a) di portata concettuale, (b) verificabili alla lettera, (c) generali nel senso di B.1 (future work o conclusioni di un paper che è già un confronto multi-metodo). Le tre proposte usano ancore diverse e **cuori diversi**. Tutte le citazioni sotto sono verificate parola per parola sul PDF del paper citato subito dopo, con la pagina.

---

## Proposta 1 (consigliata). «Il costo misurato di un'impossibilità»

**Cuore.** L'analisi assiomatica ha dimostrato che per una famiglia di regole equità, incentivo e stabilità sono incompatibili. Nessuno ha misurato **di quanto** lo siano, né se la tensione compaia nelle altre famiglie quando il tempo è esplicito. È una domanda da impossibility theorem: da un risultato binario a una frontiera quantitativa.

**Ancora principale** (`gonzalezasenjo2025`, Energies 18(23), 6236, Nov. 2025):

| Dove | Citazione | Tipo |
|---|---|---|
| p. 2 | “The analysis reveals that no computationally efficient CAM satisfies all desirable properties simultaneously, highlighting structural tensions between fairness axioms, incentive compatibility, and ease of implementation.” | Risultato (non future work) |
| p. 12 | “Importantly, this trade-off is inherent to the entire price-based family, as shown by the following two propositions: Proposition 2. No price-based CAM can satisfy both P4 and P7. Proposition 3. No price-based CAM can satisfy both P5 and P7.” (P4 = «environmental friendliness», monotonia del costo rispetto al consumo individuale; P5 = continuità; P7 = partecipazione di gruppo vantaggiosa, cioè core) | Teorema |
| p. 5 | “The EC model used here is intentionally minimal […] It assumes known and deterministic consumption and generation within each time slot” | Limite dichiarato |
| p. 13, punto 3 | “Extending the axiomatic framework to more complex EC settings. Future work could consider settings with dynamic pricing, storage, network constraints, household flexibility, or multi-period coupling. Extending the framework to such contexts would help evaluate the robustness of CAM properties under more realistic conditions.” | Future work **generale** (otto metodi × sette proprietà) |
| p. 13, punto 4 | “Applying the framework to real consumption-generation patterns from operational energy communities would help assess how theoretical properties translate into practical outcomes and user perceptions.” (uso solo la parte sui profili reali: le «user perceptions» non sono calcolabili, B.5) | Future work generale |

**Sostegno.** `gonzalezasenjo2026`, p. 35: “formal property compliance alone is insufficient to assess real-world performance and must be complemented by scenario-specific analysis”; p. 34: “no single cost allocation method dominates across all dimensions and configurations”.

**Dichiarazione B.2.** Dei quattro punti di future work di `gonzalezasenjo2025` uso solo #3 e #4. #1 e #2 (caratterizzazione formale del nucleolo e suoi algoritmi) non sono perseguiti: la bozza lo dice.

**Perché è interessante.**
- Ha la struttura di un risultato di impossibilità e ne chiede la **versione quantitativa**: quanto costa, in equità o in stabilità, guadagnare in incentivo. Dà conclusioni generalizzabili, non una classifica.
- Genera **congetture verificabili** sulle famiglie non price-based, dove la dimostrazione non c'è.
- Il gioco della tua tesi è la versione multi-periodo dello stesso gioco: `v(S) = Σ_t c_t · min(Σ g, Σ w)` contro il `v(S) = (p_b − p_s)·min(…)` a singolo slot di `gonzalezasenjo2025` (p. 7) `[INFERENZA dalla mia lettura del paper]`. Il cambio di regime torna utile in un punto preciso: senza prezzi interni la famiglia price-based non si applica, quindi la domanda sulle altre famiglie è quella che resta aperta.

**Aderenza al tuo codice (README).** Alta, senza modifiche: frontiera di Pareto e piano uniformità × stabilità (`plot_fairness_tradeoff.m`, §11.1), forza incentivante (§7.0-bis), eccesso di coalizione (§7.3), sintesi di Pareto (`sintesi_risultati.m`, §7.6).

**Rischi.**
1. **Le misure sono analoghe, non identiche, alle proprietà.** P4 è una monotonia sul costo; la tua forza incentivante è una covarianza quota–virtuosità. Per parlare la lingua degli assiomi servirebbe un test di monotonia (perturbare il consumo di un membro in un'ora condivisa e rileggere la sua quota): è uno script nuovo, non una modifica (K5 qui sotto).
2. **I tuoi risultati saranno evidenza numerica, non teoremi.** La bozza lo dice (verbo «quantified», non «proved»).
3. **Concorrente non letto:** Rodrigues et al. 2026 (`[WEB]`, Utilities Policy) tratta il trade-off fra forza incentivante meritocratica ed equità sociale. Va letto prima di scrivere «non è stato quantificato».
4. La forza incentivante ha ancore per costruzione (la regola di Bilardo vale 1): va sempre riportata con entrambi gli assi (README §7.0-bis).

**Bozza** (inglese LaTeX, stesse chiavi del V1):

```latex
Axiomatic analysis has recently clarified what a cost allocation method for an energy community can and cannot achieve. González-Asenjo et al. evaluate eight methods against seven desirable properties and conclude that \textit{``no computationally efficient CAM satisfies all desirable properties simultaneously, highlighting structural tensions between fairness axioms, incentive compatibility, and ease of implementation''} \cite{gonzalezAsenjo2025}. For one family of methods the tension is a theorem: \textit{``this trade-off is inherent to the entire price-based family''}, because no price-based method can satisfy at the same time the monotonicity of the allocated cost with respect to individual consumption, which they call environmental friendliness, and the stability of the grand coalition \cite{gonzalezAsenjo2025}.

The same authors state where the result stops. Their model is, in their words, \textit{``intentionally minimal''}, with \textit{``known and deterministic consumption and generation within each time slot''} \cite{gonzalezAsenjo2025}. Among future developments they list the extension of the axiomatic framework to settings with \textit{``household flexibility, or multi-period coupling''}, in order to \textit{``evaluate the robustness of CAM properties under more realistic conditions''}, and its application to real patterns, which \textit{``would help assess how theoretical properties translate into practical outcomes''} \cite{gonzalezAsenjo2025}. The same list includes the formal characterisation of the nucleolus and the design of efficient algorithms for it, which this work does not pursue. The data-driven follow-up by the same group confirms that the evidence is context-specific: \textit{``no single cost allocation method dominates across all dimensions and configurations''}, and \textit{``formal property compliance alone is insufficient to assess real-world performance and must be complemented by scenario-specific analysis''} \cite{gonzalezAsenjo2026}.

Two questions follow that these statements do not settle. The incompatibilities are proved for price-based methods; whether comparable tensions arise for the simplified, performance-based and game-theoretic mechanisms, when time is explicit and members differ in the timing of their injections and withdrawals, has not to our knowledge been quantified. And axioms are satisfied or violated, whereas the choice of a rule requires knowing by how much it gives up one property to obtain another. In our reading, these two questions define the gap addressed by this thesis. A regime in which the value of shared energy is a regulated transfer is the natural setting for them: without internal prices the price-based family does not apply, and the shared-energy game keeps the structure analysed by those authors, namely the minimum between aggregate injections and aggregate withdrawals, here summed over the hours of a year.
% TODO: confirm the correspondence with the characteristic function of Chapter 4.

\begin{quote}
\emph{When a year of hourly profiles is allocated by mechanisms from the different families, how large are the trade-offs among distributive equity, coalitional stability and incentive strength; do the tensions proved for price-based methods reappear in the other families; and how do they change with the size, the prosumer penetration and the composition of the community?}
\end{quote}
```

---

## Proposta 2. «La fairness non è una scala»

**Cuore.** Gli indicatori di fairness sono importati da altre discipline e non è mai stato verificato se concordino sull'ordine delle regole. È un problema di **validità di misura**: prima di dire quale regola è più equa bisogna sapere se «più equa» ha un significato unico.

**Ancora principale.**

| Paper | Dove | Citazione | Tipo |
|---|---|---|---|
| `gasca2025` | p. 13 (conclusioni) | “fairness metrics derived from other fields are being applied indiscriminately to ECs’ context. However, it is essential to highlight that measuring fairness in ECs is not straightforward from an engineering and mathematical perspective due to its highly subjective nature.” | Conclusione critica di un confronto 10 approcci × 4 indici |
| `dynge2025` | p. 12 | “additional investigation is needed to refine fairness indicators, ensuring their effectiveness across diverse market models” e “a more generalisable and comprehensive evaluation of multiple fairness indicators” | Future work generale (4 indicatori × 9 casi) |
| `dynge2025` | introduzione | indicatori «adapted for use in the context of local electricity markets»; «no research has been found addressing or comparing the performance of these indicators» | Affermazione di primato (B.3: attribuita agli autori) |
| `volpato2024b` | p. 22 | “identify parameters that can quantitatively compare the different benefit distributions based on the "individual", "collective" and "proportional" fairness” | Future work generale |
| `cremers2023` | p. 13 | “there are many other fairness concepts that could be explored in energy applications, and it would be relevant to compare their outcome to Shapley values” | Future work generale |

**Un dettaglio che rende il problema concreto.** Il vocabolario non è condiviso: `gasca2025` (p. 5) chiama «equity» “the equal allocation of costs/benefits for all users, regardless of their contribution”, mentre `dynge2025` (p. 2, nota) scrive “Equity commonly refers to rewarding individuals proportionally to individual contribution”. Stessa parola, significati opposti.

**Perché è interessante.** Sposta la domanda da «quale regola» a «che cosa stiamo misurando»: il risultato è una struttura (quante dimensioni indipendenti, quali regole sono robuste a tutte) e un **insieme minimo di indicatori** riutilizzabile da altri. Il tuo README ha già un indizio: l'accordo fra uniformità e stabilità è negativo in 6 comunità su 7 e cambia segno con la penetrazione (§7.6).

**Aderenza al codice.** Alta: τ-b, `accordo_indicatori.csv`, `orientamenti.csv`, inversioni, fronti di Pareto. L'unica aggiunta per l'insieme minimo è lo script K2 (cluster e rappresentanti), senza toccare il resto.

**Rischi.** (1) «Gli indicatori misurano cose diverse, quindi discordano» può sembrare ovvio: serve mostrare la **struttura** (dimensionalità, regole robuste, soglie di composizione), non il fatto. (2) Rischio di sovrapposizione con Couraud et al. 2025 (`[WEB]`, non letto): confronta meccanismi su misure egalitarie, min-max e meritocratiche. (3) Parte dell'esito è per costruzione (ogni indicatore ha una regola campione: README §7.0): riportare le perdite delle altre regole, non solo il vincitore.

**Bozza.**

```latex
The fairness indicators applied to energy communities are, for the most part, imported from other disciplines. Dynge and Cali note that they were \textit{``adapted for use in the context of local electricity markets''} and that, before their study, \textit{``no research has been found addressing or comparing the performance of these indicators''} \cite{dynge2025}. Gasca et al. conclude that \textit{``fairness metrics derived from other fields are being applied indiscriminately to ECs' context''}, and warn that \textit{``measuring fairness in ECs is not straightforward from an engineering and mathematical perspective due to its highly subjective nature''} \cite{gasca2024}.

The vocabulary itself is not shared. Gasca et al. use equity for \textit{``the equal allocation of costs/benefits for all users, regardless of their contribution''} \cite{gasca2024}, whereas Dynge and Cali write that \textit{``Equity commonly refers to rewarding individuals proportionally to individual contribution''} \cite{dynge2025}. Studies that compare several mechanisms ask for a remedy in similar terms: to \textit{``identify parameters that can quantitatively compare the different benefit distributions''} \cite{volpato2024}, to derive criteria for \textit{``a more generalisable and comprehensive evaluation of multiple fairness indicators''} \cite{dynge2025}, and to compare \textit{``many other fairness concepts''} with the Shapley value \cite{cremers2023}.

None of these studies examines whether the verdict depends on the yardstick: whether the ordering of a set of allocation mechanisms is the same under different notions of fairness, how many independent notions the indicators actually express, and in which configurations the ordering changes. In our reading this is the gap addressed by this thesis. A regime in which the value of shared energy is a regulated transfer, and no internal price enters the allocation, is the simplest setting in which to ask it, because members differ only in the timing of their injections and withdrawals.

\begin{quote}
\emph{To what extent does the ranking of allocation mechanisms depend on the notion of fairness used to evaluate it; how many independent dimensions do the indicators express, and which minimal subset suffices to discriminate among the mechanisms; and how does the answer change with the size, the prosumer penetration and the composition of the community?}
\end{quote}
```

---

## Proposta 3. «Dal "dipende dal contesto" alla mappa del contesto»

**Cuore.** Tutta la letteratura comparativa conclude che il metodo migliore dipende dalla comunità; nessuno ha mappato **dove** l'ordine delle regole cambia. Il contributo è una mappa delle configurazioni critiche (soglie di inversione).

**Ancore** (nessuna è la principale: qui l'ancora è la **convergenza**, ed è il limite della proposta):

| Paper | Dove | Citazione | Tipo |
|---|---|---|---|
| `gonzalezasenjo2026` | p. 34 | “the choice of allocation mechanism should be guided by the specific characteristics and priorities of the Energy Community, including its size, degree of heterogeneity, renewable penetration level, and tolerance for computational complexity” | Conclusione |
| `kulmala2021` | p. 5 | “a table that can support the selection process for a value sharing method for a particular EC” | Scopo dichiarato (analisi qualitativa) |
| `gasca2025` | p. 11 | “the findings are sensitive to user assets and profile changes” seguito da “the same conclusions apply to other types of ECs with diverse user types” | Generalizzazione non testata (un caso, 7 famiglie, 1 mese) |
| `volpato2024b` | p. 22 | “a higher number of members (e.g., tens or more)” | Future work (autoreferenziale in parte) |
| `fina2024` | future work | “the critical set-up” della comunità per cui i meccanismi sono applicabili | Future work generale (tre meccanismi) |
| `minuto2022` | p. 15 | “the different EC compositions (number of members in the UT groups)” | Future work autoreferenziale |

**Perché è interessante.** Una mappa delle inversioni ha valore pratico (statuti, decisori) e ricalca la nozione di «critical set-up» di Fina. **Perché è la più debole come ancora:** B.1 dice che ancore autoreferenziali o vaghe, anche convergenti, non reggono un gap da sole.

**Aderenza al codice.** Massima: `reversals_by_axis`, `ranking_grid`, `QuotaModale`, soglia di rilevanza (README §7.6).

**Rischi.** (1) `ferrucci2025` varia già taglia, prosumer e diversità su 64 casi, ma con una sola regola: va citato e distinto. (2) Senza repliche di seed non separi la composizione dal rumore (README §12): vedi T5 nel memo precedente. (3) La composizione per categoria non è ancora variata nel codice.

**Bozza.**

```latex
The comparative literature agrees on one conclusion: the best mechanism depends on the community. The data-driven comparison of González-Asenjo and Izquierdo finds that \textit{``no single cost allocation method dominates across all dimensions and configurations''} and that the choice \textit{``should be guided by the specific characteristics and priorities of the Energy Community, including its size, degree of heterogeneity, renewable penetration level, and tolerance for computational complexity''} \cite{gonzalezAsenjo2026}. Kulmala et al. had proposed a table \textit{``that can support the selection process for a value sharing method for a particular EC''} \cite{kulmala2021}.

Context dependence is thus asserted, but the dependence itself has not been mapped. Gasca et al. acknowledge that \textit{``the findings are sensitive to user assets and profile changes''} and then state that \textit{``the same conclusions apply to other types of ECs with diverse user types''} \cite{gasca2024}, on the basis of one community of seven households observed over one month. Studies that compare mechanisms list the variation of the configuration among their future developments: communities with \textit{``a higher number of members (e.g., tens or more)''} \cite{volpato2024}, \textit{``the critical set-up''} of a community at which the mechanisms remain sensibly applicable \cite{fina2024}, and \textit{``the different EC compositions (number of members in the UT groups)''} \cite{minutoLanzini2022}. The study that varies size, prosumer share and user diversity most widely applies a single mechanism \cite{ferrucci2025}.

In our reading, what is missing is a map: for which combinations of community size, prosumer penetration and composition the ordering of the mechanisms is stable, where it reverses, and how far the reversal points move with the notion of fairness.

\begin{quote}
\emph{For which configurations of an energy community, in terms of size, prosumer penetration and composition by category, does the ranking of allocation mechanisms reverse; and are the reversal points the same under different notions of fairness?}
\end{quote}
```

---

## Confronto e assemblaggio consigliato

| | Proposta 1 | Proposta 2 | Proposta 3 |
|---|---|---|---|
| Forza dell'ancora (B.1) | Alta: teorema e future work generale | Alta: conclusione critica più future work generali | Media-bassa: convergenza di ancore deboli |
| Interesse accademico | Alto (impossibilità → quantificazione) | Alto (validità di misura) | Medio (utile, descrittivo) |
| Aderenza al codice | Alta | Alta | Massima |
| Rischio di sovrapposizione | Rodrigues 2026 `[WEB]` | Couraud 2025 `[WEB]`, Dynge 2025 | `ferrucci2025`, GA2026 |
| Lavoro extra | Test di monotonia (opzionale) | Script K2 (opzionale) | Schede nuove (dati) |

**Consiglio: usare la Proposta 1 come cuore e le altre due come estensioni.** Si innesta sulla tua struttura a tre direzioni senza riscrivere tutto:
- **Cuore** (Proposta 1): dalla impossibilità assiomatica alla sua misura.
- **Direzione 1, meccanismi:** coprire anche le famiglie non price-based, per le quali l'impossibilità non è dimostrata.
- **Direzione 2, valutazione:** la Proposta 2, cioè indicatori come versioni graduate degli assiomi, accordo fra indicatori e insieme minimo.
- **Direzione 3, configurazioni:** la Proposta 3, cioè la mappa delle inversioni.
- **Il regime regolato** compare una volta sola, come perché il problema si pone così: niente prezzi interni e valore unitario comune.

**RQ combinata (bozza):** *When a year of hourly profiles is allocated by mechanisms from the different families, how large are the trade-offs among distributive equity, coalitional stability and incentive strength; to what extent does the verdict depend on the notion of fairness used to evaluate it; and for which configurations of the community does the ranking of mechanisms reverse?*

## Cosa non ho verificato e cosa serve da te
- **Rodrigues et al. 2026, Couraud et al. 2025, Limmer 2023:** noti solo da riassunti web, non letti. Se carichi i PDF in `Paper/` li leggo prima che tu fissi la frase «non è stato quantificato».
- **Mappatura assiomi → indicatori** (P4 → forza incentivante, P7 → eccesso di coalizione): è una mia lettura, da discutere. Se vuoi parlare di P4 alla lettera, serve il test di monotonia (script nuovo K5, ~30 righe, non modifica nulla).
- **Il tuo Cap. 2.5** (quadro assiomatico) non l'ho visto: la Proposta 1 funziona bene se lì presenti le sette proprietà di `gonzalezasenjo2025`.
- **Quale proposta vuoi?** Scegli una (o l'assemblaggio) e scrivo il V3 completo, con la stessa verifica parola per parola.
