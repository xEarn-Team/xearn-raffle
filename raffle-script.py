import random

snapshot_example = """0xD4A22e (Thievv),2447,2447,494
0x9D4D95 (CryptoBabyH),616,616,248
0xa0aA4f (Elfman),391,391,197
0x3bc16D (Nestor),280,274,171
0x68A60a (Sticky9000__),260,260,161
0x8F8859 (Manna),210,116,201
0x4618F3 (Will),203,203,142
0xB1Ed26 (iceberrrrg),200,200,141
0x8a4385 (PVCQuest1),173,173,131
0x7Ec352 (DeadBolt),165,184,135
0xA78670 (Kalingag),163,0,163
0x6A474B,152,151,123
0x33dD11 (Dagon),150,143,126
0x292d1F (redskywalker88),138,236,153
0x4082e9 (Cajun),137,137,117
0x01A214 (BobsCrispyDuck),131,130,115
0x33c33e (Kingdom Guard),129,5,146
0xD90808 (LTCQuest),128,128,113
0xbDB28d (TINYOLO),120,116,111
0x102783 (LTCQuest2),110,110,104
0xd7b732 (Amras),103,103,101
0x6E5c05 (Sansi),96,96,97
0xc58148 (Dave),95,47,116
0xaf7F56 (Thonas1),92,12,114
0xB9BcE2 (PBM2),92,92,95
0xd62c9C (Apex Futz1),90,71,103
0xAaE01A (RMacPDX),89,86,95
0x842E31 (Drizz),87,87,93
0x0A7eB9 (BeauCastle),85,85,92
0xaf331D (skiinz),84,66,99
0x27848f (dotRambo),83,83,91
0x60ad07 (Sticky9000_),81,81,90
0xab0dc8 (Asher),81,76,92
0xfF0F0c (Retrinumun),80,80,89
0xB91f11 (chingpangwei),76,76,87
0x0b9ef7 (yyds),76,76,87
0xe09655 (Avalabs),74,74,86
0x285eFe (DJThroatRip),73,73,85
0xAdbE3D (cb561),73,73,85
0x3e2111 (BillyBoys),71,71,84
0xe802d5 (FluidDude2),66,71,84
0x00d3bE (Shwaver),65,65,80
0x91324c (Testy Tester),64,64,80
0x995281 (Cocomelon),64,64,80
0x0F0B02 (Degen30),63,63,79
0xe779E8 (hollowlight64),63,63,79
0x08034d (BOT_Saget),63,63,79
0x0b065d (Pikapoo),62,57,80
0x340dC3 (3pac),62,62,78
0x6246e6 (Furioso),60,60,77
0xA3927D (Dr. Drsch),60,56,78
0x634D98 (Savanna),57,57,75
0xeD083C (Peach),56,56,74
0x0Fc0F7 (starl3xx),55,55,74
0xc50B76 (kotak),55,55,74
0xfBBdB9 (TheCompanion),54,54,73
0x0cE8da (DFKBell),52,52,72
0x8F6162 (Chicco),50,50,70
0xC1dc5d (Sluuguu),50,50,70
0x6E5004 (Sir Mihai),49,1,58
0xA08EeD (Bilstin),46,46,67
0xa472ec (mambastic),46,46,67
0x76C6Dd (Meta478345209),45,45,67
0xE96445 (PlanetBoB),41,13,64
0x407f02 (Lokkar),39,39,62
0x87dd92 (Xee),38,38,61
0x78c5C9 (elfiz),38,37,61
0xcA9238 (Eternal_Oblivion),35,35,59
0x39A49a (Golfanatic),32,32,56
0xb6C07d (Gamer Ga),32,32,56
0x6Bd8eE (Puckle),32,24,56
0x87cf77 (Draz Al Ghul),32,0,32
0x78987B (mkg),31,0,31
0x1e465b (osmenazri),31,31,55
0x3e7D67 (Exypnos),31,31,55
0x165f86 (Sir Lil B),30,30,54
0x8E181C (CryptoVegan),29,29,53
0x2D2E63 (x7shadows),29,29,53
0xb85775,29,29,53
0x660710 (Fredtheadct),28,23,52
0x879583 (FleakFrag),27,27,51
0x8f6876 (TheJTrain),27,27,51
0x20E6b3 (Black Scare),26,26,50
0xF07254 (k1ng),26,26,50
0x1450D4 (Alpha Gaming DAO),26,26,50
0x7c48FD (CONE420),26,25,51
0x60C568 (Hiarbas),26,26,50
0x98E589 (Skorpy),25,25,50
0x412F8D (MattLikesGaming),24,24,48
0x5cFa4A (Jon_Crypto),24,24,48
0x54EDAC (Cato),24,5,41
0x06F643 (woofmaster),22,22,46
0x588399 (Dogbelly),21,21,45
0x1Ce6A5 (uberbox),21,21,45
0x9A9D9C (RandomMeLoL),20,20,44
0x4697F1 (Sir Beckett),20,20,44
0x3BdB13 (Bezal),19,19,43
0x2fCa36 (CubanitoLopez),19,19,43
0x562493 (Pasquale),18,18,42
0x1A5d9e (BW-Mule),17,9,38
0xA88360 (DaPlaymaker),17,17,41
0xE5C0A5 (Mad Professor),17,17,41
0xD77a19 (Hussein),17,17,41
0x5eA811 (VaisFalecer),17,17,41
0x38Ee68 (LaHaine),17,17,41
0x7a3f85 (Daracus),17,17,41
0x34001D (Bene),16,16,40
0xf56C85 (Cthom93),15,15,38
0xA78a6B (MATT ),14,14,37
0xD1555E (Rens),14,14,37
0x1A435d (Randolf the Wise),14,0,14
0x730488 (BugsMoney),13,10,34
0xaA8637 (chichi93),12,12,34
0xb63Df2 (baji),11,15,38
0x4D7a99 (IBuyShtCoins),11,7,30
0xe43ED6 (kenny),11,11,33
0x4D1F3a (Viiespax),11,11,33
0x798b4C (Icekin),10,10,31
0xe5Ddc4 (LikeMiike),10,10,31
0x652F3E (Recon),10,10,31
0x7410f9 (Orbital),10,10,31
0x848aDe (Foglet),10,10,31
0x21Ed37 (VeniMoo),10,10,31
0x279AB6 (RockDog),9,9,30
0x211b87 (Mochi_),9,9,30
0xbbB4cC (HeadShotHero117),8,8,28
0x7deCF9 (Sithis),8,8,28
0xd1D563 (Duvad),8,8,28
0x5d28b4 (Mc.Greggar),8,8,28
0x6Ab3d7 (Skyrifter),7,7,26
0x9E4F9e (MRGZ),7,7,26
0x39085d (noped),6,6,24
0xAa2665 (AkizukiRei),6,6,24
0x839414 (JahRasta),6,6,24
0x2E45E5 (Domwaut),6,6,24
0xcfEcd2 (Lazlo),6,4,22
0x4A8735 (DoubleChips),6,6,24
0xac0f24 (Zappa),6,6,24
0x8ae42b (Lord Marcus),6,6,24
0x65c2B6 (Gods Army),6,6,24
0x5cF256 (The Bridgooor),6,6,24
0x8c78bF (Janti_L),5,5,22
0xe47153 (2ezy),5,5,22
0xF153F6 (limau),5,5,22
0x886B87 (Jelle),5,5,22
0x97b215 (Zimbo),5,5,22
0x4c52A5 (kukuem),5,5,22
0x17A4e4 (Breddren$),4,4,20
0x35208a (kietawp),4,4,20
0x67174D (Earn Devo),3,6,24
0x692555 (Jayville),3,3,17
0x838285 (Mystique),3,3,17
0xCA1c8b (Nirac),3,3,17
0xF43c53 (256bitA),3,3,17
0x914e17 (AlphaWxlf),3,3,17
0x8E459D (lee002),3,3,17
0x365013,3,3,17
0xa9cEC6 (pscoin),3,3,17
0x60FFAe (xxD0P3yxx),3,3,17
0x22C6B8,3,3,17
0xCAFE72 (Passo),3,3,17
0x704c8c (Rangid),2,2,14
0x9A3276 (Djibouti Bandit),2,2,14
0x17D189 (Oliverxll),2,2,14
0x376240 (SlayerSparty),2,2,14
0x4340C6 (Mister Masalam),2,2,14
0xE9Df3D (Jonitan),1,1,10
0xe2f5B9 (Driver),1,0,1
0xb97174 (itwaswk),1,1,10
0x3eFa8C (PTG),1,0,1
0x331004 (Nubz),1,1,10
0x97f7bC (Sentius Nox),1,1,10
0x54EDAC (btcle),1,1,10
0x07c912 (Letsgo),1,1,10
0x2EA83C (Jiemind),1,1,10
0x76Ca47 (Sir Edo of Jerry),1,1,10
0x7bE368 (KoenPeters_PAC),1,1,10
0xdd6199 (Kung),1,1,10
0xc35c69 (Aidonir),1,1,10
0x2BD1Ae (Lillbunny),1,1,10
0x8490c5,1,1,10
0xB7ecaD (Lunar Chickadee),1,1,10
0xF838A2,1,1,10
0xd5A06A (Hektor),1,1,10
0x7C7AF4 (btb),0,50,70
0xE48C04 (∈),0,2,14
0xE48C04,0,28,52
0xAc33d3 (Coubain),0,49,70
0xB68108 (Russ Jacobsen ),0,1,10
0x60A001 (Drazoc),0,19,43
0x87E6f8 (dumpling),0,5,22
0xd9Cc04,0,2,14"""


def raffle(user_with_weight: list):
    """
    :param user_with_weight: [["0xDeff(Jeff)", 24], ["0xBeHD(Jackie)", 38], ["0xHijWd(Lnky)", 40]]
    :return:
    """
    l = []
    for uw in user_with_weight:
        l.extend([uw[0] for i in range(int(uw[-1]))])
    bronze = random.choice(l)
    for i in range(l.count(bronze)): l.remove(bronze)
    silver = random.choice(l)
    for i in range(l.count(silver)): l.remove(silver)
    gold = random.choice(l)
    for i in range(l.count(gold)): l.remove(gold)
    return {"Bronze": bronze, "Silver": silver, "Gold": gold}


if __name__ == "__main__":
    import pprint
    pprint.pprint(raffle([u.split(",") for u in snapshot_example.split("\n")]))
