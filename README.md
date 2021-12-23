# Final_project_engeto
Třetí projekt na Python Akademii od Engeta

## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz najdete [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103).
## Instalace knihoven
Knihovny, které jsou použity jsou uloženy v requirements.txt. Pro instalaci využijte nové virtuální prostředí a je potřeba mít nainstalovaného manažera následně spustíte: 
<p>Zkontroluji verzi manažera: <code>$ pip --version</code></p>
<p>Nainstalujeme knihovny: <code>$ pip install -r requirements.txt</code></p>

## Spuštění projektu
<p>Spuštění souboru <code>election_scraper.py</code>lze spustit pomocí příkazového řádku a požaduje dva povinné argumenty.</p>

```$ python3 election_scraper.py <odkaz-uzemniho-celku> <vysledny-soubor>```

Následně se výsledky stáhnou a uloží jako soubor s příponou <code>.csv</code>.

## Ukázka projekt 
Výsledky hlasování pro okres Kladno:

1. argument: **ht<span>tp://</span>volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103**
2. argument: **vysledky_kladno.csv**

<p>Spuštění programu:<p>
<code>python3 election_scraper.py "ht<span>tp://</span>volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103" "vysledky_kladno.csv"</code>
  
<p>Průběh stahování:</p>
<pre><code>DOWNLOADING DATA FROM SELECTED URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103
SAVING TO FILE: vysledky_kladno.csv
QUITTING: election scraper
</code></pre>

<p>Částečný výstup:</p>
<pre><code>CODE,LOCATION,REGISTERED,ENVELOPES,VALID,...
535010,Běleč,262,181,181,23,0,0,19,0,13,11,1,2,0,0,0,22,0,0,11,61,0,0,6,0,1,1,1,8,1
532070,Běloky,135,101,102,12,0,0,10,0,6,12,1,0,3,0,0,16,0,0,8,21,0,0,3,0,0,0,0,9,0
532088,Beřovice,272,152,152,21,0,0,12,0,13,6,3,3,2,1,0,18,0,0,5,50,0,1,0,0,0,0,0,17,0
...
</code></pre>
