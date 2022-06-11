alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
iloscWystapien = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

def cezar(napis,naj):
    najczestszaLitera
    indeksjezyka
    indekscezara
    indeks = 0
    maxilosc
    maxilosc = 0
    #sprawdz częstotliwość
    for letter in napis:
        for i in iloscWystapien:
            if letter == i:
                iloscWystapien[letter] += 1

    #sprawdz ktora litera wystepowala najczęściej
    for letter in iloscWystapien:
        if iloscWystapien[letter] > maxilosc:
            najczestszaLitera = letter
            maxilosc = iloscWystapien[letter]

    #spawdz index w którym jest podana najczestsza litera w danym języku
    for i in range(len(alfabet)):
        if alfabet[i] == naj:
            indeksjezyka = i
    #spawdz index w którym jest podana najczestsza litera w zaszyfrowanym tekście
    for j in range(len(alfabet)):
        if alfabet[j] == najczestszaLitera:
            indekscezara = j
            break
    
    #oblicz przeskok w szyfrze
    przeskok = indekscezara - indeksjezyka

    #rozszyfruj tekst w oparciu o podany przeskok
    rozszfrowanyTekst = ""
    for letterr in napis:
        #sprawdz indeks kazdej litery w zaszyfrowanym zdaniu
        if letterr==' ':
            rozszfrowanyTekst += ' '
        elif letterr=='.':
            rozszfrowanyTekst += '.'
        elif letterr==',':
            rozszfrowanyTekst += ','    
        elif letterr=='-':
            rozszfrowanyTekst += '-' 
        else:
            for k in range(len(alfabet)):
                if alfabet[k] == letterr:
                    indeks = k
                    #rozszyfruj literę
                    indeks -= przeskok
                    if indeks < 0:
                        indeks = 25 + indeks + 1 #przez tą jedną "1" myślałem nad tym o pół godziny dłużej ni powinienem
                    if indeks > 25:
                        indeks = indeks - 25
                    rozszfrowanyTekst += alfabet[indeks]
    print(rozszfrowanyTekst)
            



cezar("uhgfdht zpl zpukihk. tplzgrht zahsl d ihnkhkgpl. yvkgpjl tvp, btplyhqhj, gvzahdpsp tp d zwhkrb afzphj dvyvd gsvah, afzphj iljglr zyliyh, zav whshjvd, zav vnyvkvd p qlklu aygvuvdf ghi tlnv wyhkgphkrh, ravyf vqjplj tvq wygljovdfdhs d olihuvdlq zgrhabsjl, qhrv whtpharl p vzvispdvzj. wyhkgphklr tvq wyglg jhsl gfjpl jovyvdhs uh ivs glivd p jv wldplu jghz puuf ghi tbzphs dfyfdhj, ahr gl d rvujb qlklu tb afsrv ghi aygvuvdf wvgvzahs. btplyhqhj, rhghs zvipl dfydhj p alu vzahaup ghi aygvuvdf, ravyf wyglzglks d zwhkrb vk tlnv kgphkh kv tlnv vqjh, h vk vqjh -- kv tupl. ifs av gdfjghquf, glwzbaf p zjglyuphsf ghi. qlzalt wldplu, gl uh zdpljpl guhslgj tvguh ihykgv dplsl ahr zhtv glwzbafjo p zjglyuphsfjo glivd, sljg upl rhgkf g upjo ayhmph kv olihuvdlq zgrhabsrp, hif zahuvdpj whtpharl p vzvispdvzj. alu -- ayhmps. uplyhg, wygfnshkhqhj tb zpl g jplrhdvzjph p zghjburplt, dfviyhghslt zvipl, qhr alu ghi ivshs uplnkfz tlnv wyhkgphkh!","a")

