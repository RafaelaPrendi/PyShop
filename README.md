# PyShop
Sistem katalogimi te produkteve
Pershkrim:

Sistem per katalogimin e produkteve te nje dyqani.

Ne qender te sistemit jane Produktet, qe mund te gjehen ne te pakten 1 dyqan, dhe ne cdo dyqan mund te kene cmime
te ndryshme, dhe te gjenden ne sasi te ndryshme.

User-i (i loguar ose jo) ka aftesine per te pare ku mund te gjeje nje produkt, per te pare produktet e nje dyqani,
si dhe inventarin e nje dyqani.
User-i (i loguar) ka aftesine per te blere nje produkt ne nje nga dyqanet qe e kane.

----------------------------------------
Faqet/URL-te:
/produkt/<id> -> GET
*pershkrim i produktit (tip/emer)
*liste me DYQANE
 ku mund ta "ble" kete produkt (si dhe cmimi i ketij produkti ne cdo dyqan)

 /dyqan/<id> -> GET
*pershkrim i dyqanit (emer/adrese)
*liste me PRODUKTe qe mund te "ble" ne kete dyqan (bashke me cmimin qe kane)

 /dyqan/<id>/inventar -> GET
*pershkrim i dyqanit (emer/adrese)
*vlera totale e te gjithe produkteve te ketij dyqani
*vlera totale per cdo TIP produkti te dyqanit.

 /dyqan/bli -> POST
*shton produktin ne listen e produkteve te USER-it.

----------------------------------------
