Eksperimentell og numerisk analyse av rullende kule på
krum bane – TFY4104/07
09/10/26
Gruppe 3 - Adrian Andersen, Thomas Neegård, Håkon Asheim, Filip Gløckner, Hilmar Holmen-Løkke
og Anna Hødnebø
1. Rapporststruktur og innholdsdisposisjon
Tittelside / Topptekst
• Prosjekttittel: Eksperimentell og numerisk analyse av rullende kule på krum bane (eller
tilsvarende emnetittel for TFY4106/TFY4125).
• Emnekode, gruppenummer, dato og forfatternavn.
1. Sammendrag (Abstract)
I dette forsøket ble bevegelsen til en kompakt kule som ruller langs en krummet bane undersøkt ved
hjelp av en numerisk modell og eksperimentelle data fra videoanalyse. Banens form ble modellert
med basert på åtte målte festepunkter. Modellen tok utgangspunkt i ren rulling og energibevaring.
Den numeriske modellen ga en teoretisk rulletid på 1,828 s og en teoretisk slutthastighet på 1,242
m/s. Eksperimentelt ble den gjennomsnittlige rulletiden målt til 2,277 ± 0,061 s, mens gjennomsnittlig
slutthastighet var 0,994 ± 0,029 m/s, der usikkerheten er oppgitt som standardavvik for åtte forsøk.
Det gjennomsnittlige mekaniske energitapet ble beregnet til 11,98 ± 1,26 mJ, tilsvarende omtrent
35,8 % av den tilgjengelige mekaniske energien.
Resultatene viser at den eksperimentelle kula beveget seg langsommere enn modellen forutsier.
Dette tyder på at den ideelle modellen ikke fullt ut tar hensyn til energitap i det virkelige forsøket,
blant annet på grunn av rullemotstand, friksjon og andre ikke-ideelle effekter. Modellen beskriver
likevel hovedtrekkene i kulas bevegelse og gir et grunnlag for sammenligning mellom teori og
eksperiment.
2. Teori og beregningsgrunnlag
Presenter fysikken og formlene som koden er bygget på:
• Baneprofil: Kubisk spline gjennom 8 festeskruer med naturlige randbetingelser,
helningsvinkel 𝛽 = arctan(𝑦′) og banens krumning:
𝜅 =
𝑦′′
(1 + (𝑦′)
2)
3/2
• Ren rulling og energibevarelse: Treghetsmoment for kompakt kule 𝐼 = 𝑐𝑚𝑟
2
(𝑐 = 2/5).
𝐾 = 𝐾trans + 𝐾rot =
1
2
𝑚𝑣
2 +
1
2
𝐼𝜔
2 =
1
2
(1 + 𝑐)𝑚𝑣
2 =
7
10 𝑚𝑣
2
• Teoretisk fart og tid:
𝑣(𝑦) = √
2𝑔(𝑦0 − 𝑦)
1 + 𝑐
, 𝑑𝑡 =
𝑑𝑥
𝑣𝑥
=
𝑑𝑥
𝑣 cos 𝛽
• Krefter og vilkår for ren rulling:
o Normalkraft: 𝑁 = 𝑚(𝑔 cos𝛽 + 𝑣
2𝜅)
o Friksjonskraft: 𝑓 = −
𝑐
1+𝑐
𝑚𝑔 sin𝛽
o Skli-krav: |𝑓/𝑁| ≤ 𝜇𝑠
for at kula ikke skal slure.
• Usikkerhetsanalyse: Definisjon av gjennomsnitt 𝑥, utvalgsstandardavvik 𝛿𝑥 (med 𝑁 − 1 i
nevner) og standardfeil 𝛿𝑥 = 𝛿𝑥/√𝑁.
2. Teori og beregningsgrunnlag
I dette forsøket undersøkes bevegelsen til en kompakt kule som ruller langs en krummet bane. Den
numeriske modellen bygger på Newtons bevegelseslover, rotasjonsmekanikk og prinsippet om
bevaring av mekanisk energi. Det antas at kula starter fra ro og ruller uten å gli, og at energitap som
følge av rullemotstand og luftmotstand kan neglisjeres. Modellen beskriver dermed en idealisert
bevegelse som senere sammenlignes med eksperimentelle målinger.
2.1 Baneprofil og geometri
Banens form beskrives ved en funksjon (y(x)), der (x) angir horisontal posisjon og (y) angir høyden.
Med utgangspunkt i de åtte festepunktene benyttes kubisk splineinterpolasjon for å konstruere en
kontinuerlig baneprofil. En kubisk spline består av tredjegradspolynomer mellom hvert festepunkt,
der funksjonen og dens første- og andrederiverte er kontinuerlige. Det benyttes naturlige
randbetingelser, slik at den andrederiverte er null ved banens endepunkter.
For å beskrive bevegelsen langs banen defineres helningsvinkelen (\beta) ved
[
\beta(x)=\arctan(y'(x)).
]
Banens krumning (\kappa) er gitt ved
[
\kappa(x)=\frac{y''(x)}{(1+y'(x)^2)^{3/2}}.
]
Helningsvinkelen benyttes til å dekomponere tyngdekraften i komponenter parallelt med og normalt
på banen, mens krumningen benyttes til å bestemme kulas normalakselerasjon.
2.2 Ren rulling og energibevaring
For en kule som ruller uten å gli, er translasjonshastigheten (v) og vinkelhastigheten (\omega) knyttet
sammen ved betingelsen
[
v=r\omega,
]
der (r) er kulas radius.
Den totale kinetiske energien er summen av translasjonsenergien og rotasjonsenergien:
[
K=\frac12 mv^2+\frac12 I\omega^2.
]
For en homogen, kompakt kule er treghetsmomentet om massesenteret
[
I=\frac25 mr^2.
]
Ved å sette inn betingelsen for ren rulling får vi
[
K=\frac12 mv^2+\frac15 mv^2
=\frac{7}{10}mv^2.
]
Mer generelt kan dette skrives som
[
K=\frac12(1+c)mv^2,
\qquad c=\frac25.
]
Under antakelsen om at ingen mekanisk energi går tapt, er den totale mekaniske energien bevart:
[
E=U+K=mgy+\frac12(1+c)mv^2,
]
der (U=mgy) er den potensielle energien.
Siden kula slippes fra ro ved starthøyden (y_0), gir energibevaring
[
mgy_0=mgy(x)+\frac12(1+c)mv(x)^2.
]
Ved å løse for hastigheten får vi
[
\boxed{v(x)=\sqrt{\frac{2g(y_0-y(x))}{1+c}}}.
]
Dette uttrykket benyttes i den numeriske modellen til å beregne kulas hastighet langs hele banen.
Hastigheten avhenger dermed av høydeforskjellen fra startpunktet og av hvordan kulas kinetiske
energi fordeles mellom translasjons- og rotasjonsbevegelse.
2.3 Beregning av rulletid
For å bestemme tiden kula bruker på å bevege seg gjennom banen, benyttes sammenhengen mellom
hastighet og posisjon. Siden (v) er hastigheten langs banen, er den horisontale
hastighetskomponenten gitt ved
[
v_x(x)=v(x)\cos\beta(x).
]
Fra definisjonen av hastighet følger
[
dt=\frac{dx}{v_x(x)},
]
og den totale rulletiden kan dermed uttrykkes som
[
T=\int_{x_0}^{x_f}\frac{dx}{v(x)\cos\beta(x)}.
]
I koden beregnes integralet numerisk ved å dele banen inn i små intervaller med lengde (\Delta
x=0,001\ \mathrm{m}). For hvert intervall tilnærmes tidsforbruket ved å benytte gjennomsnittet av
de horisontale hastighetene i intervallets endepunkter:
[
\Delta t_i\approx
\frac{2\Delta x}{v_{x,i-1}+v_{x,i}}.
]
Siden kula starter fra ro, behandles det første intervallet separat ved å anta tilnærmet konstant
akselerasjon. Den totale rulletiden finnes deretter ved å summere tidsbidragene fra alle intervallene.
2.4 Krefter og betingelsen for ren rulling
I tillegg til å bestemme hastigheten beregner modellen normalkraften og den statiske friksjonskraften
som virker på kula. Disse kreftene er nødvendige for å beskrive bevegelsen langs den krumme banen
og undersøke om betingelsen for ren rulling kan oppfylles.
Newtons andre lov anvendt normalt på banen gir
[
N-mg\cos\beta=ma_n,
]
der (a_n) er den fortegnsbestemte normalakselerasjonen. Denne er gitt ved
[
a_n=v^2\kappa.
]
Dermed blir normalkraften
[
\boxed{N(x)=m\left(g\cos\beta(x)+v(x)^2\kappa(x)\right)}.
]
Normalkraften avhenger altså både av tyngdekraftens normalkomponent og av banens krumning. I
partier med positiv krumning vil normalakselerasjonen gi et positivt bidrag til normalkraften, mens
negativ krumning gir et negativt bidrag.
For bevegelsen langs banen må vi også ta hensyn til rotasjonsbevegelsen. Ved å kombinere Newtons
andre lov for translasjon med dreiemomentlikningen og betingelsen om ren rulling, fås
tangentialakselerasjonen
[
a_t=-\frac{g\sin\beta}{1+c}.
]
Den nødvendige statiske friksjonskraftens størrelse blir dermed
[
\boxed{|f(x)|=\frac{c}{1+c}mg|\sin\beta(x)|}.
]
Den statiske friksjonen sørger for at forholdet mellom translasjons- og rotasjonsbevegelsen
opprettholdes. Ved ideell rulling på en stillestående bane utfører denne friksjonskraften ikke arbeid,
siden kontaktpunktet mellom kula og underlaget er momentant i ro.
For at kula skal rulle uten å gli, må den nødvendige friksjonskraften ikke overstige den maksimale
statiske friksjonen:
[
|f|\leq\mu_s N,
]
der (\mu_s) er den statiske friksjonskoeffisienten.
Dette gir betingelsen
[
\boxed{\mu_s\geq\max_x\left(\frac{|f(x)|}{N(x)}\right)}.
]
I den numeriske modellen beregnes derfor forholdet (|f/N|) langs hele banen. Den maksimale
verdien angir den minste statiske friksjonskoeffisienten som kreves for at antakelsen om ren rulling
skal være fysisk mulig i modellen.
2.5 Eksperimentell energi og mekanisk energitap
For å sammenligne den teoretiske modellen med eksperimentelle observasjoner benyttes posisjonsog tidsmålinger fra videoanalyse. Hastighetskomponentene beregnes numerisk fra endringene i
posisjon over tid, og den totale hastigheten bestemmes ved
[
v=\sqrt{v_x^2+v_y^2}.
]
Ved hjelp av den målte hastigheten kan kulas kinetiske energi beregnes fra uttrykket utledet i del 2.2.
I motsetning til den ideelle modellen vil den mekaniske energien i det virkelige forsøket ikke
nødvendigvis være bevart. Energitapet bestemmes derfor som differansen mellom den mekaniske
energien ved start og slutt:
[
\Delta E=E_{\mathrm{start}}-E_{\mathrm{slutt}}.
]
Siden kula antas å starte fra ro, får vi for hvert forsøk
[
\boxed{
\Delta E_i=
mg(y_0-y_f)-\frac12(1+c)mv_{f,i}^2
}.
]
Her er (y_f) banens slutthøyde og (v_{f,i}) den målte sluttfarten i forsøk (i). En positiv verdi av (\Delta
E_i) tilsvarer et tap av mekanisk energi under rullebevegelsen.
2.6 Statistisk behandling og usikkerhet
For å undersøke hvor pålitelige de eksperimentelle resultatene er, gjennomføres åtte separate
rulleforsøk. De målte sluttfartene benyttes til å beregne energitapet i hvert enkelt forsøk.
For (n) målinger av en størrelse (q) defineres middelverdien som
[
\bar q=\frac1n\sum_{i=1}^{n}q_i.
]
Spredningen i målingene beskrives ved utvalgsstandardavviket
[
s_q=
\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(q_i-\bar q)^2}.
]
Standardavviket beskriver variasjonen mellom enkeltmålingene, mens usikkerheten i den beregnede
middelverdien uttrykkes ved standardfeilen
[
s_{\bar q}=\frac{s_q}{\sqrt n}.
]
For det gjennomsnittlige mekaniske energitapet rapporteres dermed resultatet som
[
\boxed{\overline{\Delta E}\pm s_{\overline{\Delta E}}}.
]
Denne statistiske behandlingen gir et estimat på den tilfeldige usikkerheten i middelverdien av
energitapet. Eventuelle systematiske feil, eksempelvis feil ved kalibrering av videoanalysen eller avvik
mellom den idealiserte modellen og den faktiske bevegelsen, må vurderes separat.
Usikkerhetsbegrepene og uttrykkene følger Lilledahl og Risinggårds notat Målinger og usikkerhet.
3. Eksperimentell metode
• Oppsett: Beskriv banen, måling av de 8 skruehøydene (og måleusikkerhet på
linjal/skyvelære), kulas masse (𝑚 = 31 g) og radius (𝑟 = 11 mm).
I forsøket brukte vi en berg-og-dal-bane som ble formet ved hjelp av åtte justerbare skruer. Høydene
på skruene ble bestemt ut fra beregningene vi hadde gjort i Python på forhånd. Vi justerte deretter
skruene slik at banen fikk omtrent samme form som den vi hadde simulert.
Høydene på de åtte skruene var:
Høydene ble målt med linjal, så det kan ha oppstått små målefeil både ved avlesning og justering av
skruene. Dette kan føre til at den faktiske banen ikke blir helt lik den beregnede banen.
Kula vi brukte hadde en masse på 31 g og en radius på 11 mm. Vi gjorde om disse verdiene til SIenheter:
m = 31 g = 0,031 kg
r = 11 mm = 0,011 m
• Datainnsamling: Kameraoppsett på stativ, innstilling for å unngå perspektivfeil, 30 fps, filming
av 8 separate slipp fra ro.
For å måle bevegelsen til kula brukte vi et mobilkamera som var festet på et stativ. Kameraet ble
plassert slik at vi fikk med hele banen i bildet. Vi prøvde også å plassere kameraet mest mulig rett
foran banen for å unngå perspektivfeil.
Vi filmet med 60 bilder per sekund (60 fps). Det betyr at tiden mellom hvert bilde var:
Δt = 1 / 60 = 0,0167 s
Vi gjennomførte åtte separate forsøk der kula ble sluppet fra ro ved starten av banen. Vi prøvde å
slippe kula på samme måte hver gang, slik at forsøkene skulle bli mest mulig like.
Hvert opptak startet da kula ble sluppet ved den første skruen, og sluttet rett etter at kula hadde
passert den siste skruen. Videoene ble deretter overført til PC for videre analyse.
• Analyse i Tracker: Valg av koordinatsystem og målestokk, autotracking/manuell sporing av
kulas massesenter, og metode for beregning av sluttfart (differanse over de to siste bildene
ved siste skrue).
For å finne sluttfarten brukte vi kulas posisjon i det siste bildet før og det første bildet etter at den
passerte den siste skruen.
Vi regnet først ut hastigheten i x- og y-retning:
vₓ = (x₂ − x₁) / (t₂ − t₁)
vᵧ = (y₂ − y₁) / (t₂ − t₁)
Siden vi filmet med 60 fps, var tidsforskjellen mellom to bilder:
Δt = 1 / 60 = 0,0167 s
Dermed fikk vi:
vₓ = (x₂ − x₁) / 0,0167
vᵧ = (y₂ − y₁) / 0,0167
Til slutt regnet vi ut den totale sluttfarten ved hjelp av Pytagoras:
v_slutt = √(vₓ² + vᵧ²)
Dette gjorde vi for alle de åtte forsøkene.
4. Resultater
Strukturer resultatdelen i tre underkapitler:
4.1 Numeriske resultater
• Tabell eller utskrift over teoretiske nøkkeltall:
o Teoretisk rulletid: 𝑡teor = 1,71 s
o Teoretisk sluttfart: 𝑣teor = 1,24 m/s
o Total teoretisk mekanisk energi: 𝐸mek = 0,091 J (eller tilsvarende ut fra
referansenivå)
• Figur: Normalkraft og friksjonskraft langs banen (𝑁(𝑥) og 𝑓(𝑥) i samme figur med to ulike
linjefarger/stiler).
• Figur: Forholdet |𝑓/𝑁| som funksjon av 𝑥 (angi banens maksimale verdi).
4.2 Sammenligning: Numerisk modell vs. Eksperiment (Video 1)
Posisjon x [m]
Figur 3: Horisontal posisjon x(t) som funksjon av tid
1.4 Numerisk x(t)
--- Eksperimentell x(t) (Video 1) 1.2-
1.0-
0.8
0.6
0.4
0.2-
0.0
0.0 0.5 1.0 1.5 2.0
Tid t [s]
Fart v Im/s]
Figur 2a: Hastighet v(x) langs banen
1.4 1.4
1.2 1.2
1.0 1.0
0.8
0.6
Fart v [m/s]
0.8
0.6
Figur 2b: Hastighet v(t) over tid
0.4 0.4
0.2 0.2
- Numerisk v(x)
0.0 -- Eksperimentell v(x) (Video 1) 0.0
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 0.0 0.5 1.0 1.5
Posisjon x [m] Tid t [s]
- Numerisk v(t)
--- Eksperimentell v(t) (Video 1)
2.0
Høyde
y [m]
Figur 1: Baneform y(x) - Numerisk vs. Eksperimentell
0.300
0.275
0.250
0.225
0.200
0.175
0.150
0.125
0.0 0.2 0.4 0.6 0.8 1.0
Posisjon x [m]
Numerisk baneform y(x)
Målte festepunkter (skruer)
Eksperimentell bane (Tracker, Video 1)
1.2 1.4
Presenter de fem påkrevde sammenligningsplottene (heltrukken linje for numerisk, stiplet/punkter
for eksperimentelt):
1. Baneform 𝑦(𝑥): Numerisk kurve, målte skruepunkter og Tracker-sporet.
2. Hastighet som funksjon av posisjon 𝑣(𝑥).
3. Hastighet som funksjon av tid 𝑣(𝑡).
4. Posisjon som funksjon av tid 𝑥(𝑡).
5. Energier langs banen: 𝐸pot(𝑥), 𝐸kin(𝑥) og 𝐸mek(𝑥) sammenlignet for modell og måling.
4.3 Statistikk over alle 8 forsøk
• Resultattabell for de 8 forsøkene:
Forsøk Rulletid t
[s]
Sluttfart vslutt
[m/s]
Kinetisk energi K
[mJ]
Tapt energi ΔE
[mJ]
1 2,3657 0,9615 14,33 9,58
2 2,2357 0,9770 14,88 9,11
3 2,2990 0,9965 15,39 8,52
4 2,2534 0,9483 13,94 9,97
5 2,2324 1,0322 16,51 7,40
Forsøk Rulletid t
[s]
Sluttfart vslutt
[m/s]
Kinetisk energi K
[mJ]
Tapt energi ΔE
[mJ]
6 2,3657 1,0181 16,07 7,84
7 2,2157 1,0105 15,83 8,08
8 2,2157 1,0105 15,83 8,08
• Samlet statistikk:
o Gjennomsnittlig energitap: Δ𝐸 ± 𝛿Δ𝐸 = (12,0 ± 0,5) mJ
o Standardavvik: 𝛿(Δ𝐸) = 1,3 mJ
o Prosentvis tap av mekanisk energi: 35,8 %
o Gjennomsnittlig rulletid: (2,28 ± 0,02) s
o Gjennomsnittlig slutthastighet: (0,99 ± 0,01) m/s
5. Diskusjon
5.1 Sammenligning av numerisk modell og eksperimentelle observasjoner
Den teoretiske modellen forutsa en total rulletid på 𝑡teor = 1,83 s og en slutthastighet på
𝑣teor = 1,24 m/s ved banens ende (𝑥 = 1,40 m). De eksperimentelle målingene over 𝑁 = 8
forsøk ga en gjennomsnittlig rulletid på 𝑡 = (2,28 ± 0,02) s og en gjennomsnittlig sluttfart på
𝑣slutt = (0,99 ± 0,01) m/s.
Målt rulletid er dermed omtrent 0,45 s lengre (en økning på ca. 25 %), og målt sluttfart er ca.
0,25 m/s lavere (en reduksjon på ca. 20 %) enn den ideelle modellen forutsier.
Studerer man utviklingen av hastigheten over tid og posisjon, 𝑣(𝑥) og 𝑣(𝑡), ser man at det
eksperimentelle forløpet følger den teoretiske kurveformen kvalitativt godt: Kula akselererer
i de bratte nedoverbakkene, retarderer oppover bakketoppene, og når sitt lokale maksimum i
bunnen av den dypeste dalen. Avviket oppstår imidlertid gradvis: I starten av banen ligger
målingene tett opptil teorien, men etter hvert som kula ruller, faller den målte farten stadig
mer bak den teoretiske kurven på grunn av friksjonstap.
Årsaken til at rulletiden påvirkes så kraftig av et moderat fartstap ligger i tidsintegrasjonen:
𝑡 = ∫
𝑑𝑥
𝑣𝑥
(𝑥)
Siden farten 𝑣𝑥
(𝑥) inngår i nevneren, fører selv små hastighetsreduksjoner over lengre
strekninger (spesielt i slake partier eller mot toppen av bakketopper der farten allerede er
lav) til en markant økning i det kumulative tidsforbruket.
5.2 Analyse av mekanisk energitap og bevegelsens dynamikk
Den teoretiske modellen er formulert under forutsetning om et konservativt system der
mekanisk energi er bevart (𝐸mek = 𝐸pot + 𝐸kin = konstant). Eksperimentelt ser vi derimot et
betydelig energitap. Total tilgjengelig potensiell energi fra start til slutt var:
𝐸pot, start = 𝑚𝑔(𝑦0 − 𝑦slutt) = 0,031 kg ⋅ 9,81 m/s2
⋅ (0,300 m − 0,190 m)
= 0,0335 J (33,5 mJ)
Gjennomsnittlig målt kinetisk energi ved banens slutt var 𝐾 = (21,5 ± 0,4) mJ. Dette gir et
gjennomsnittlig energitap på:
Δ𝐸 = (12,0 ± 0,5) mJ
med et standardavvik på 𝛿(Δ𝐸) = 1,3 mJ. Kula taper dermed i snitt hele 35,8 % av sin
tilgjengelige mekaniske energi underveis.
Dette energitapet skyldes i hovedsak tre fysiske mekanismer:
1. Rullemotstand (rullefriksjon): Dette er den dominerende tapsfaktoren. Banen består
av to parallelle plastskinner eller et plastspor som kula hviler på. Kulas tyngde og
sentripetalkrefter fører til en mikroskopisk deformasjon av både kula og underlaget.
På grunn av elastisk hysterese (at materialet ikke spretter like raskt tilbake som det
trykkes inn) oppstår det et motvirkende kraftmoment mot kulas rotasjon. I tillegg
ruller kula ikke på et enkelt punkt, men har to kontaktlinjer mot skinnens sidekanter,
noe som introduserer differensialfriksjon.
2. Krav til ren rulling og mikroskopisk sluring: Modellen forutsetter ren rulling (𝑣 = 𝑟𝜔)
uten energitap til friksjon (𝑊𝑓 = 0). For at ren rulling skal opprettholdes, må den
nødvendige statiske friksjonskraften ikke overskride den maksimale statiske
friksjonen:
|𝑓| ≤ 𝜇𝑠𝑁 ⟹ |
𝑓
𝑁
| ≤ 𝜇𝑠
Den numeriske beregningen viser at |𝑓/𝑁| holder seg under typiske verdier for statisk
friksjonskoeffisient (𝜇𝑠 ≈ 0,15--0,25 for metall mot hard plast) langs mesteparten av banen.
Likevel kan det ved det bråeste startfallet eller i overgangspartier med stor krumning 𝜅
oppstå kortvarig mikroskopisk sluring. Dersom kula glir/slurer fremfor å rulle rent, gjør den
kinetiske friksjonskraften et negativt arbeid på kulas massesenter og dissiperer mekanisk
energi direkte til termisk energi (varme).
3. Luftmotstand: Med hastigheter opp mot 1 m/s og en relativt liten kule (𝑟 = 11 mm)
er luftmotstandskreftene (𝐹𝑑 ∝ 𝑣
2
) beskjedne sammenlignet med tyngdens
komponenter, men bidrar svakt til det totale tapet over hele banens lengde.
5.3 Usikkerhetsanalyse: Tilfeldige og systematiske feilkilder
For å vurdere påliteligheten til resultatene skilles det mellom tilfeldige (stokastiske) og
systematiske feil.
Tilfeldige feil (Presisjon)
De tilfeldige feilene gjenspeiles i spredningen mellom de 8 uavhengige måleseriene og
kvantifiseres gjennom standardavviket 𝛿𝑥 og standardfeilen 𝛿𝑥 = 𝛿𝑥/√𝑁:
• Rulletiden har et standardavvik på 𝛿𝑡 = 0,06 s og en standardfeil på kun 𝛿𝑡 = 0,02 s.
• Sluttfarten har et standardavvik på 𝛿𝑣 = 0,03 m/s og en standardfeil på 𝛿𝑣 =
0,01 m/s.
Den lave relative standardfeilen (under 1 % for rulletid og under 2 % for sluttfart) viser at
forsøksoppsettet har høy presisjon og svært god reproduserbarhet.
Kildene til de tilfeldige feilene er:
• Håndslipp: Små variasjoner i hvordan kula ble sluppet fra ro ved 𝑥 = 0 (f.eks. om
kulas startfart var eksakt null eller om fingeren ga en svak impuls eller rotasjon ved
frislipp).
• Bildesporing i Tracker (Pikselusikkerhet): Ved autotracking eller manuell markering av
kulas massesenter oppstår det en tilfeldig feil på ±1--2 piksler per bilde. Siden
hastigheten beregnes fra posisjonsdifferanser over korte tidssteg (Δ𝑡 = 1/30 s),
forsterkes pikselstøyen når man deriverer posisjon med hensyn på tid. Dette forklarer
hvorfor den eksperimentelle kurven for 𝑣(𝑥) viser små, lokale fluktuasjoner rundt
den glatte trendlinjen.
• Vibrasjoner i banen: Når kula ruller gjennom dalene med maksimal sentripetalkraft,
kan skinnene ha vibrert svakt, noe som gir små variasjoner fra forsøk til forsøk.
Systematiske feil (Nøyaktighet)
Systematiske feil forskyver målingene konsekvent i én retning og påvirker målingens
nøyaktighet. Disse feilene reduseres ikke ved å øke antall målinger 𝑁.
Viktige systematiske feilkilder i forsøket:
• Modellfeil (neglisjert friksjon): Den mest fremtredende systematiske feilen ligger ikke
i måleinstrumentet, men i den teoretiske modellen, som antar null energitap. Dette
gjør at målt fart konsekvent havner under beregnet fart.
• Perspektivfeil og optisk distorsjon: Mobilkameraet sto plassert i endelig avstand fra
banen. En vidvinkellinse på et mobilkamera har tønneforvrengning som buer linjer ut
mot bildekantene. Videre projiseres en 3D-bevegelse ned på et 2D-plan; dersom
kamerastativet ikke sto 100 % vinkelrett på banens vertikalplan, vil
lengdemålestokken i Tracker variere noe mellom start (𝑥 = 0) og slutt (𝑥 = 1,4 m).
• Kalibreringsusikkerhet: Kalibreringsstaven i Tracker ble satt manuelt ut fra kjente
referansepunkter på banen. Dersom denne referanselengden var feilkalibrert med
f.eks. 1 %, vil samtlige beregnede posisjoner, hastigheter og kinetiske energier
forskyves proporsjonalt gjennom hele måleserien.
• Måling av skruehøyder: Hver av de 8 festeskruene ble stilt inn med målebånd eller
linjal. En måleusikkerhet på ±1--2 mm på skruehøydene gir en endret reell baneform
sammenlignet med den glatte, matematiske spline-kurven koden beregner.
5.4 Vurdering av modellens gyldighet
Den numeriske simuleringen gir en god kvalitativ beskrivelse av kulas dynamikk og
baneprofil, og fungerer utmerket som en øvre teoretisk grense (grensetilfelle uten
dissipasjon). Den kan imidlertid ikke benyttes til presise tids- og hastighetsprediksjoner for en
fysisk rullende kule uten å inkludere en tapsmodell. For å oppnå kvantitativ
overensstemmelse mellom teori og eksperiment burde modellen utvides med:
• Et ledd for rullefriksjon proporsjonalt med normalkraften (𝐹rull = 𝜇𝑟𝑁).
• En hastighetsavhengig luftmotstandskraft (𝐹𝑑 =
1
2
𝜌𝐶𝑑𝐴𝑣
2
).
Alt i alt demonstrerer forsøket tydelig forskjellen mellom et idealisert teoretisk system og et
reelt eksperiment, og understreker hvor essensielt det er å kombinere numeriske
beregninger med grundig usikkerhets- og feilanalyse i ingeniør- og fysikkfag.
6. Avsluttende oppgaver
• Svar systematisk på spørsmålene fra labheftets sluttdel.
• Bruk nummererte delavsnitt, referer til fysikkformler og trekk inn figurene fra resultatdelen
som understøttelse.
1. Grafen for friksjonskraften virker rimelig ut fra baneformen. I figur 5a ser vi at friksjonskraften
varierer etter hvor bratt banen er. Den er størst der banen heller mest, og omtrent null i topp- og
bunnpunktene hvor banen er horisontal.
Når kula ruller nedover, er friksjonskraften positiv i beregningene våre, mens den er negativ når kula
ruller oppover. Dette stemmer med formelen:
f = −(2/7) · mg · sin(β)
Den største beregnede friksjonskraften i absoluttverdi var 0,0378 N. Grafen virker derfor rimelig ut fra
baneformen og helningen underveis.
2. Grafen for normalkraften virker også rimelig. I figur 5a ser vi at normalkraften varierer langs banen.
Den blir størst i områder der banen krummer oppover og kula har høy fart, spesielt rundt det første
bunnpunktet.
Den største normalkraften var 0,4840 N, mens den minste var 0,2468 N. Dette stemmer med at
normalkraften vanligvis blir større i bunnpunktene og mindre i toppunktene.
Dette kan forklares med formelen:
N = m · (g · cos(β) + v² · κ)
Her er κ banens krumning. Resultatene virker derfor rimelige ut fra formen på banen.
3. For at kula skal rulle uten å gli, må den statiske friksjonskraften være stor nok. Dette kan vi finne
ved å bruke forholdet mellom friksjonskraften og normalkraften:
μₛ ≥ maks(|f/N|)
I figur 5b ser vi at den største verdien av |f/N| er 0,144.
Dermed får vi:
μₛ ≥ 0,144
Det betyr at den statiske friksjonskoeffisienten minst må være 0,144 for at kula skal kunne rulle uten å
gli langs hele banen, ifølge den numeriske modellen.
4. Grafen for krumningen er sammenhengende, men har knekkpunkter for hver 20. cm. Dette er som
forventet siden banen er laget ved hjelp av åtte festepunkter med 20 cm mellomrom.
I Python brukte vi kubisk splineinterpolasjon for å lage en jevn bane mellom punktene. Selv om selve
banen er jevn, kan krumningen endre seg ulikt på hver side av festepunktene.
Dette gjør at vi får knekkpunkter i krumningsgrafen ved x = 0,2 m, 0,4 m, 0,6 m og videre langs banen.
5. I beregningene antar vi at kulas radius er mye mindre enn banens krumningsradius.
Kulas radius var:
r = 11 mm = 0,011 m
Den minste krumningsradiusen til banen var omtrent:
R_min = 0,322 m
Vi sammenligner disse ved å regne ut forholdet:
R_min / r = 0,322 / 0,011 ≈ 29,3
Det betyr at banens minste krumningsradius er omtrent 29 ganger større enn kulas radius.
Antagelsen er derfor rimelig, og vi kan bruke tilnærmingen om at kulas massesenter følger omtrent
samme baneform som underlaget.
6. Fra de åtte forsøkene fikk vi et gjennomsnittlig tap i mekanisk energi på:
ΔE = (11,98 ± 0,45) mJ
Her er 0,45 mJ standardfeilen, mens standardavviket var 1,26 mJ.
Energitapet ble beregnet ved hjelp av formelen:
ΔE = mg(y₀ − yₛ) − 0,7mv²
Resultatene viser at omtrent 35,8 % av energien som ble frigjort ved høydeforskjellen, gikk tapt. Dette
stemmer ikke helt med den ideelle modellen, hvor vi antar at den mekaniske energien er bevart.
Energitapet kan skyldes rullemotstand, luftmotstand og små deformasjoner i kula og banen. Det kan
også ha oppstått litt glidning underveis. Resultatene viser derfor at den ideelle modellen ikke
beskriver forsøket helt nøyaktig, men energitapet betyr ikke nødvendigvis at kula har glidd.
7. De eksperimentelle og teoretiske resultatene stemmer delvis overens, men vi ser også noen
forskjeller.
I figur 1 sammenlignes den eksperimentelle og numeriske baneformen. Begge viser omtrent samme
form, med et bunnpunkt rundt x = 0,5 m og et toppunkt rundt x = 0,9 m. Det er likevel noen avvik
mellom kurvene, som kan skyldes unøyaktigheter i målingene og oppsettet av banen.
I figur 2a ser vi at hastigheten øker når kula ruller ned mot det første bunnpunktet rundt x = 0,5 m, og
avtar når den ruller oppover igjen. Dette stemmer med teorien. Den eksperimentelle hastigheten
varierer likevel mer enn den numeriske, noe som blant annet kan skyldes måleusikkerhet i Tracker.
Vi fikk følgende resultater:
Teoretisk rulletid = 1,828 s
Målt rulletid = 2,277 s
Teoretisk sluttfart = 1,242 m/s
Målt sluttfart = 0,994 m/s
Dette viser at kula brukte lengre tid og hadde lavere sluttfart enn forventet. Dette ser vi også i figur 3,
der den eksperimentelle bevegelsen tar lengre tid enn den numeriske.
I figur 4a ser vi at den totale mekaniske energien holder seg konstant i den numeriske modellen. I
figur 4b varierer den eksperimentelle energien mer. Vi beregnet et gjennomsnittlig energitap på 11,98
mJ.
Forskjellene kan skyldes rullemotstand, luftmotstand, små feil i skruehøydene og unøyaktigheter i
videoanalysen. Den teoretiske modellen tar ikke hensyn til slike energitap, og derfor blir den
beregnede sluttfarten høyere enn den målte.
Vi kan derfor si at resultatene stemmer ganske godt med teorien når det gjelder hvordan kula
beveger seg langs banen, men at det er tydelige forskjeller i hastighet, rulletid og energi.
7. Konklusjon
• Kort oppsummering av om forsøket bekreftet hypotesen, hvor presis og nøyaktig måleserien
var, og hva hovedårsaken til avvikene mellom modell og virkelighet er.
8. Referanser og Vedlegg
• Referanser: Labhefte (TFY4106/TFY4125 Vår 2024), notat om målinger og usikkerhet
(Lilledahl & Risinggård).
• Vedlegg: Fullstendig, kommentert Python-kode (lab_2.py).
2. Figur- og formatkontroll
Gå over alle figurer i rapporten mot kravene:
1. Aksetitler og enheter: Alle akser må ha symbol og enhet i klammeparentes, f.eks. Posisjon 𝑥
[m], Hastighet 𝑣 [m/s], Energi [J].
2. Figurtitler og bildetekster: Hver figur skal ha et figurnummer og en forklarende tekst under
figuren (f.eks. Figur 2: Sammenligning av numerisk og målt hastighet som funksjon av
posisjon).
3. Linjeskille: Hvis to kurver er i samme plott, skal de skilles med både farge og linjestil (f.eks.
hel blå linje for modell, rød stiplet linje for måledata).
4. Signifikante siffer: Tall med usikkerhet skal avrundes etter usikkerheten, f.eks.
(2,28 ± 0,02) s, ikke 2,278374 s.
3. Fremdriftsplan (Steg-for-steg)
[Steg 1: Generer grafer] ──> [Steg 2: Fyll inn tabell] ──> [Steg 3: Skriv Metodedel]
 │ │ │
 ▼ ▼ ▼
[Steg 4: Teori & Formler] ──> [Steg 5: Svar oppgaver] ──> [Steg 6: Diskusjon]
 │
 ▼
 [Steg 7: Sammendrag & Konklusjon]
1. Generer og lagre alle figurer: Kjør Python-skriptet med Video 1 og lagre de ferdige figurene
som høyoppløselige PNG- eller PDF-filer.
2. Sett opp tabellene: Lim inn tallene for de 8 forsøkene i Word/LaTeX.
3. Skriv metode og teori: Sett inn formlene for spline, ren rulling, energier og standardfeil.
4. Besvar de avsluttende oppgavene: Formuler svarene grundig med referanse til plottene.
5. Skriv diskusjonen: Sammenlign teori mot måling, og drøft energitapet og feilkildene.
6. Skriv sammendrag og konklusjon: Gjør dette til slutt når alle tall og drøftinger er ferdigstilt.
Skal fikses
Avvik i tapt energi i resultater. , uvisst hva som er årsak
I koden står det: f = -(c / (1.0 + c)) * m * g * np.sin(beta)
Dette bør stå 