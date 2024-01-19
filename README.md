# Lietojumprogrammatura-Projekts
## Apraksts
Šis projekts atrod un izvada vispopulārākās kārtis spēlē Magic: the Gathering. Magic: the Gathering ir galda spēle kura tiek spēlēta ar kavām uztaisītām no vairāk par 50 000 unikālām kārtīm, lai labāk saprastu kā veidot savu kavu es izvēlējos taisīt šo projektu.

Mans Projekts sastāv no divām programām MoxfieldScraper.py un DeckAnalyzer.py. Programma MoxfieldScraper.py izmanto mājaslapu moxfield.com lai nokopētu no tās Magic: the Gathering kavas un tos ieraksta failos. Programma DeckAnalyzer.py ievada mapi ar kavu failiem un izvada vispopulārākās kārtis.

Fails DecSourceMini.txt ir domāts testēšanas nolūkiem.

## MoxfieldScraper.py
<b>selenium bibliotēka:</b> Tiek izmantota, lai automatizētu pārlūkprogrammas darbību un veiktu darbības lapās, piemēram, noklikšķinot uz pogas vai ievadot informāciju.

<b>time bibliotēka:</b> Tiek izmantota, lai programmu apstādinātu uz īsu laiku, ļaujot pārlūkprogrammai ielādēt lapu vai veikt citas darbības.

<b>pyperclip bibliotēka:</b> Tiek izmantota, lai izgūtu tekstu no "clipboard" pēc tam, kad pārlūkprogramma ir noklikšķinājusi uz "Download" pogas un ir noklikšķinājusi uz apstiprinošā dialoga.

<b>os bibliotēka:</b> Tiek izmantota, lai izveidotu direktoriju un saglabātu kavu failus šajā direktorijā.

Programma lasa kavu saites no faila 'deckSource.txt', apstrādā tās vienu pēc otras, lejupielādē kavu failus un saglabā tos teksta failos, kuru nosaukumi ir numerēti un tiek saglabāti direktorijā 'Decks'

## DeckAnalyzer.py
<b>os bibliotēka:</b> Tiek izmantota lai izveidotu direktoriju.

Programma izveido vārdnīcu, kurā glabājas kāršu vārdi un to atkārtojumu skaits. Pēc tam, izmantojot šo vārdnīcu, programma izdrukā 30 visbiežāk sastopamo kavu vārdus un to atkārtojumu skaitu.
