CDF      
      time       lon    `   lat_2      0         CDI       @Climate Data Interface version 2.1.1 (https://mpimet.mpg.de/cdi)   Conventions       CF-1.0     institution       MPIMET     history      rThu Apr 13 09:40:20 2023: cdo -remapbil,/Volumes/external_Samsung-SSD/DeepMIP_model_database/COSMOS/COSMOS-landveg_r2413/deepmip_stand_3xCO2/v1.0/COSMOS-landveg_r2413-deepmip_stand_3xCO2-orog-v1.0.nc /Volumes/external_Samsung-SSD/DeepMIP_model_database/COSMOS/COSMOS-landveg_r2413/boundary_conditions/COSMOS-landveg_r2413-deepmip_sens_all-sftlf.nc /Volumes/external_Samsung-SSD/DeepMIP_model_database/COSMOS/COSMOS-landveg_r2413/deepmip_stand_3xCO2/v1.0/COSMOS-landveg_r2413-deepmip_stand_3xCO2-sftlf-v1.0.nc
Sun Mar 22 17:00:39 2020: cdo chname,SLM,sftlf -selvar,SLM Eocene_topo.nc COSMOS-landveg_r2413-deepmip_sens_all-sftlf.nc
Tue Mar 17 17:14:03 2020: cdo selvar,OROMEA,SLM T31GR30_jan_surf.nc Eocene_topo.nc
Tue Aug 20 14:01:55 2019: cdo merge -chname,DEPTO,SLM ../lsm/Eocene_atm_lsm.nc vegetation.nc ../orography/Eocene_orography_all.nc T31GR30_jan_surf.nc
Wed Aug 14 11:15:53 2019: cdo setmisstoc,1 tmp.nc Eocene_atm_lsm.nc
Wed Aug 14 11:15:18 2019: cdo remapcon,t31grid Eocene_bathym_122x101_bin.nc tmp.nc
Wed Aug 14 11:08:03 2019: cdo setrtoc,-100000,-0.0000001,0 -setrtoc,0,0,1 -mulc,-1 GR30_topo_jj_modified.nc GR30_topo_jj_modified_miss.nc
Fri Mar 22 16:05:51 2013: cdo setrtomiss,-100000,100000 GR30_topo_jj_modified.nc GR30_topo_jj_template.nc
Fri Mar 22 15:05:00 2013: cdo -f nc -t mpiom1 -selvar,DEPTO -setgrid,GR30s.nc -selindexbox,2,121,1,101 -setgrid,r122x101 fort.72 topo.nc     CDO       @Climate Data Operators version 2.1.1 (https://mpimet.mpg.de/cdo)         time                standard_name         time   units         day as %Y%m%d.%f   calendar      proleptic_gregorian    axis      T               lon                standard_name         	longitude      	long_name         	longitude      units         degrees_east   axis      X          	À   lat_2                  standard_name         latitude   	long_name         latitude   units         degrees_north      axis      Y         À  @   sftlf                         	long_name         depth at pressure points   units         m      code         T   table               CDI_grid_type         gaussian   CDI_grid_num_LPE            
_FillValue        ÷ÝÝü   missing_value         ÷ÝÝü     H       @p  @ð  A4  Ap  A  A´  AÒ  Að  B  B  B%  B4  BC  BR  Ba  Bp  B  B  B B  B B¥  B¬ B´  B» BÃ  BÊ BÒ  BÙ Bá  Bè Bð  B÷ Bÿ  C@ C  C
À C C@ C  CÀ C C!@ C%  C(À C, C0@ C4  C7À C; C?@ CC  CFÀ CJ CN@ CR  CUÀ CY C]@ Ca  CdÀ Ch Cl@ Cp  CsÀ Cw C{@ C  C` C@ C  C  Cà CÀ C  C C` C@ C  C  Cà CÀ C  C C` C¡@ C£  C¥  C¦à C¨À Cª  C¬ C®` C°@ C²  B®QuB¦õ7BÙB#÷B¹!BMÕBâGBtí"BfBW=¸BHe×B9âB*µÞBÝÏB·Aü[/AÞªåAÀúA£J7A×AOÒæAr@²"?í^¿í^À²"ÁrÁOÒæÁ×Á£J7ÁÀúÁÞªåÁü[/Â·ÂÝÏÂ*µÞÂ9âÂHe×ÂW=¸ÂfÂtí"ÂâGÂMÕÂ¹!Â#÷ÂÙÂ¦õ7Â®QuA^ À                                                                                                                                                                                                                                                                                                                                                                                                                                                               <_oQ>h+o>àDô>Î=Ð>Ü¬>¹ô=¶	É>nTÄ>)ÿ;Ëòö4DÓ4 z2Ü7®3×<4ºî4î4Ü4¡þ4¦ÁÀ4ªU3#t2ã2©¼|26Q3ï*Ï4<Ê4264")4Ä3îô®3Ôÿ4_B4Píï4-ô4n4 é÷4Y·4#ß\3ÅöÊ3¯½}46#y4X·4øø4F?4UÚ4á4X!ê3éê43oÈº3fk$                            0ÃI)-    3É4 Ô©4o½4`áè4:Ì	3á0[3¸30ô3!3Ó%4Y°s4K®L4RZ,4jý4V~4X^41C2ã2                                                                    =O!Ù?×}?}á÷?ÿÿ?ÿþ?ÿþ?ÿþ?ÿþ?ÿþ?pî%?7TD>Âæh=%D>ï\?"á4?1öÕ?=?G2C?N0\?Rä)>#bq=5|=Qßt=4ÉB>Üd>éo>ÜZ¶>È\u>±ÂÝ>ºí>oJ?
8?*»>Õÿú> 	µ>Æöà?}.>Ê^>tÆ>YKè>á57?²)?BJ?A:N?# Ã?8i?½>>¨Øv>>>sÁ                            ;qvÅ8/Ñ    >)"?FÜ?>ô?>æ÷Ç>8>cz=ÚËà>5ë>Á
? >ûØ?ê?	+?5?Ä;>²Ið=u÷        ?(ì?'á_?[>Ä    0×3,3þJ3Ë)¶;d9>'ô?/«`?`¾?0=À³    >°?vÛõ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?~é¨?JKÿ?R Ã?M¸ñ>ú¬?ì2>Íê>åhÊ?KÌ?~×?wm!?xº?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿG?nc?@t?0´?  ?ÿÿ?G9£>>4<ý¿< ¬>àñ@?3sä?;;?X´J?  ?  ?s¾?$©>4d!´>V'?]¥?ÿþ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿü?ÿü?j9ÿ?|¨	?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?u÷±?  ?  ?  ?  ?  ?  ?aE5>fkí>¶Þ^?[?´»?n?  ?  ?  ?  ?  ?  ?vö ?}×[?1ß=µ1£<U?G?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿþ?ÿý?n/?lÎ×>tÃ!>H]Ñ<¸>°ß?6ÖÖ?sÕ?ÿþ?  ?  ?  ?ÿÿ?ÿÿ?ÿý?|ª«?ÿü?ÿü?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿþ?Iï.?K@?  ?  ?  ?  ?  ?qT]>cO¨?@¸Ë?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?0Ü<#tN    >?n<?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿþ?ÿü?¾j?7?->£óÖ=;%K;t
¹                <OÓ*>à3?/Ô?l4ã?ÿú?ÿü?d 2?W{ç>Ý¢	=+2>XB>p?mõÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿý?ÿü?ÿý?ÿý?ÿÿ?ÿÿ?ÿÿ?ÿÿ?Hê?fv?Ol?  ?  ?  ?  ?  ?ÿÿ>ªPî?z$a?ÿþ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?Ö>ÓÒ1¨e    =á½Ä?aý¾?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ??§!>ìÜ>O®à4½Df4g4)	á2Àó0ûÏ                1ÖE¡4g
×4µ2;¯èJ>/y*>ÍÇi=^p4Þ+14d(2°^·4
,<G¢F>åB?y©H?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?s?È>ð?ñ?lÈ?b`?UX?UÇ«?Kî?Y]>gø?sË?ÿþ?  ?  ?  ?  ?  ?j²G>=?rí?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿÿ?  ?wº>\w<¨D`>@4¿ø¡?Èk?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?$*³>|>Z:<¦-                                                                                            <©8?2Ç?æ§?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?U°>*=£~3?b[:?  ?  ?0g>7;,Gc?_d8?  ?  ?  ?  ?ÿÿ?ÿþ?K·>¯mý?wbH?ÿü?ÿý?ÿÿ?  ?  ?  ?ÿÿ?  ?ÿþ?j5u?V¡s?ÿÿ?qÇM>({È?NÚ?x`¾?_¡N?áè?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿü>îR                                                                                                                >kJ?vEv?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?j8Á?Xe[?  ?  ?  ?  ?Qo>>.,?å8?sk{?ÿø?}m?{7.?Hþ?'°+?Ä;>¾Ó>	Î>øwÎ?*Á+?lé??ÿÿ?ÿÿ??Wl?zBý?:&j>¼fÒ=ÔÎ÷?n¤?  ?G >_Ì??  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >ô<l>nü                                                                                                                9*ò¶?*ì?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?OLÁ=Óæ<Ñ2=§Mµ=ÕÖ??aW?ýJ?zët>Êìi?=ù(?n:1>É¬>Tó?6>Ïa=Û6´:]K=V¥³.)ZL        >Ôsk?ÿÿ>÷ò±    ?3é?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?RÀ>Be´                                                                                                                    ='?jT/?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?rF=ÃOµ            >Ä?nÓ?ÿþ?p.?[X?Ù­?ÿý?U´Ò?Ýé>~½t>ÏÞ>,4ö$43ñ9]M3	i4ËN<(?Ë>§Ó)3Ò>µ?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >xX                                                                                                                        >e)?D!}?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿû?ÿû?iÉß?ÿû?,S="5T                >ie>Ø? lk?  ?5õó>þ	>0¡Á?,lð?ÿÿ?  ?s6?;ÜÐ?A?c ÷>)
â?!ª9>Sq<±h>io¥>.ma;>®¹?\Rñ?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿþ=þÚ                                                                                                                            >M?dÄä?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?yR?_g>¤º>dF=á¥ >]/Ì>2Ñ<xÓÃ            1ýu1?n?+Û?  ?  >ü[3}Y2¯øP>}z9?FOÑ?  ?  ?ÿÿ?ÿÿ?Zü:>-N?Pz6?|?u8?ÿþ?-,¿/½÷Í>(?<	ô?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >³<Þ©¹                                                                                                                            2ÊW>ÝªÖ?õ{?  ?  ?  ?  ?  ?  ?  ?  ?  ?q>FçÖ9=Î3$ 2ãk2`Í)2Ü[2±lù0÷å            =Yâ?f¾°?ÿÿ?  >3¯;$`/--Ï0µ    >7dV?4wÈ?RÐ?B'>=s,=´ØÑ?lë?  ?  ?  ?7¡¢:M;HÁ>Ýh_?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >0=°';èC                                                                                                                                        ?2ò?  ?  ?  ?  ?eTè>êS¼?fÙ¢?xß>æt0>PN&                                                ?&Û?Ê>´õ?;r>JW7<U[*=7©    1í°L;&Ê3&2ºø
2I°:1Ò1jcâ<y¢w>ã`Ä?pò?  >ÏP.+?OÔ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?c=»}1dÞO/±¬                                                                                                                                        >2?f?  ?  ?\ÖÓ=½ÿ2Ú"9=r2W2ý1                                                =ï¿|>¯J?é2?Y>+·b?Oð?Á        /­*!                    1ç3lg=.Ñ{>ãYT>!z    ?!J{?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?U\o=ÿ¸2B@ß                                                                                                                                                2¸Üå>ÜÈk?  ?  ?k_/>Lmé    .R&1ûÅ³                                                    <æº?IH?ÿÿ?ÿÿ?j¶?Vºø?b\×?Hx@3þ	3yN2ìgé4<¹<õ>Ê/¬-ò                            >9U?,)?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >~F                                                                                                                                                            ><º?t®¯?  ?  ?_Ð~=Ó)ã        2ül                                            =×.>©.?xÒ?  ?  ?  ?  ?  ?{#ø?Ä¹>§45>ãS?C¦t?w0²?f¤û:Ô                         0xC2§/>¨@_?<~?[@Ï?ÿþ?  ?  ?  ?  ?  ?  ?  ?  >Ì-                                                                                                                                                                ?9?ÿÿ?  ?ÿÿ>È¿    /åK,>å>                                            ?5M?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿÿ?h[ô?¦?  ?  ?Yü                        ;¼ñ=ý´:â+N3z¾>aé>Â?Q1à?;D?  ?  ?  ?  ?  ?  >¢V                                                                                                                                                                =Ä?Gw?  ?4¼Y=¢\n    ;.Ê?,¡                                            ?:ý?  ?  ?|Ã?q¦¿?UÅJ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÇ=Ì5ä                <FGÁ?¼9?  >óQ8        <¡×?$-?y+?  ?  ?  ?  ?  ?:Ó7?³?îu=x÷                                                                                                                                                         > ]>é>Õò=®ç    <ºìé>Þ@>2î£>¦Ý=ëÄ=Ýº=ª.ÛÊ                =Rr ?HB?  ?  ?aU>dM«?Q°?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >=a                >­Ö?  ?  ?  =yB        0ì3Ð? d)?zt?  ?  ?  ?  ?  ?  ?  =·                                                                                                                                                         1ÓK¢2x¶2°m?
@    =úE ?ÿÿ?ÿÿ?ÿÿ?ÿÿ?ÿÿ?!u:ÊÍù                <¯Mu?~ó?  ?  ?~§?>Üê?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >ðí                ?ZÔÒ?  ?  ?  ?lÐ7>3Æ«            1P(>»Z>è?  ?  ?  ?  ?  >¹ñÄ<c¾                                                                                                                                                                    1Tsä>%Z>J8=?  ?  ?  ?  ?  ?  ?N¬>Ø©Â<i?        /z?
?¢?  ?  ?_ò\>Ò?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?#»                ?5ø?  ?  ?  ?  ?ríN.$Cð                <ò´Í>?`6>#3¸?ýC?  >¹Ú<º                                                                                                                                                                            >¤ê·>á?  ?  ?  ?  ?  ?  ?  ?  >ó¢z1À
1D·Â0ÓH<TV>e;?ïc>Ò:>Pn>|¢?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?D"¼                ?ö?  ?  ?  ?ÿÿ?<;Ê¢õ                            <} u<ûÇL<k                                                                                                                                                                                9âï>V?  ?  ?  ?  ?  ?  ?  ?  ?zÀ ?låþ>ò«o>w³2´p                <¶Ý?x#Ô?  ?  ?  ?  ?  ?  ?  ?}):>ä2å;wý                >æÿ'?  ?  ?Xõt>Å¶=¼U/ÛT;                            0ëí1Br0;                                                                                                                                                                                =Õ?ÿÛ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?kÁÎ>¬-                    ?Tú?  ?  ?  ?  ?  ?  ?  ?[H0Ýò                    >ªå¶?  ?Ü½>\¨¨                                                                                                                                                                                                                                    <Ý&?"7Ú?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?r7{>ø                    ?/d?  ?  ?  ?  ?  ?  ?  ?{Ý*<¦×ñ                    >dÈî?  >¤M3Mm                                                                                                                                                                                                                                    1 >°ÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?må½3H$ä                =q?<z?  ?  ?  ?  ?  ?  ?  ?j¯®=ÙáN                    =Ì¿%?6|>Ó                                                                                                                                                                                                                                            >eS?ZÃ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >²ÿÉ                    =×ZÁ?  ?  ?  ?  ?  ?  ?  ?  ?ÎÃ3c*?&µu>Çìd                                                                                            1#v.ò{¤                                                                                                                                                                    >O±ó?dÁ?  ?  ?  ?  ?  ?  ?  ?  ?\Õ§>2&                    ;>ï¿?s2D?  ?  ?  ?  ?  ?  ?w¨¹>&S¥?Sç?~ë?2]                                                                            1¨b2ªø²2>2zOr=:iÎ                                                                                                                                                                        ?Pì?  ?  ?  ?  ?  ?  ?  ?nÃ>O                        .û.?KZO?  ?  ?  ?  ?  ?  >Ìoþ1t>ÝÐ?  ?"#E                                                                            =ð3!?êV>æu>Á!_?^Ñ?]ÞC                                                                                                                                                                        ?H[®?  ?  ?  ?  ?  ?  ?j5Ð>e21(s                            >²*?kõ?  ?  ?  ?  ?YQU>wW    >®.?ÿþ>ÓV                                                            1©Ø3bB¸>[E>þÃ?gs0?  ?  ?  ?  ?cçÂ>zR«3ú3}uÐ0ÿ)o                                                                                                                                                    3ÁÐ?<Í¸?  ?  ?  ?  ?  ?  >¥íW                                    3'(g?:ª?  ?  ?  ?  >ô722    =¨>qì<ò                                                            =*;%>ã?lb;?ÿþ?  ?  ?  ?  ?  ?  ?Xâf?Ø>þià<                                                                                                                                                    >R?e{?  ?  ?  ?  ?  ?J~=ëýµ                                        ?	L?  ?uú¯?Mì?§U=        2P3\Á1ÝË                                                    <ms?x?;³?ÿü?ÿÿ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿý?~l?=w:¹Õ«                                                                                                                                                >ÎA+?ÿÿ?  ?  ?yÖÿ?c°ú>q(=ÐdE3G¯                                        =ÂE>´½d>§ÆÆ4°r3ÚzÞ1Þõh                                                                        =²bì?ÿÿ?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ>àÜw                        =¢Ç+=eæ]                                                                                                            =Åç?_¦?  ?  ?xó>³þø4.\ 3nÔ2q                                            1 34E3'$                                                                                    >>ÓF?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  >±qÏ                        ?W?)Pj=Õp                                                                                                        =ÃW?Iå?  ?  ?~÷Ì=MØÊ:$Àõ<É                                                                                                                                                >¡Ð°?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?Oï                        >öõT?±?Oh?3:þ>ç¿Ä                                                                                                24?gg?  ?  ?  >uéq?ixÎ?¢8                                                                                                                                                >øø°?yGÝ?Uª?gõ?#Ö'?¾8>«¤>Ùü|?Ø?Æ?  ?  ?  ?  ?  ?  >öô                        >t¤·?  ?ÿÿ?t? AC                                                                                                    ?;}ÿ?  ?  ?c¢.>r>¶[6<[¸-                                                                                0]`_3µ<¸4h-o4¼»4Ü·~4¤T;4j£3?¤2?5    42IÙ4ÀÁ41è4t,4¸hd4©·ë=\=è?4ÄsC4Ï²¤4ñ]%4_4ÃS4Ýàþ4éAö=!\6> ìk?)x?E ?tê?ÿý?y­Û=Ô"ó                        >¤"?0ß¦>åqä>à2                                                                                                4Ú4\!Ê> Ú·?2n­?y ä?Qð9;Ùc                                                                                        :Ö·/>/È¶>á1?6ÔÂ?Vc?bv>µ=¹½<¹t·    >¬ì?
u-?/ó>ìÓ??2Ûö?$¢?_Km?RË±?>?IrÐ?j>þ×c?`?W3ï?b=B?F´¸?*ú?Aµ>Äzñ>¿0Î?$2E?V:>¦                        4ô¯4!I4I=3p1                                                                                                >Ú>Õ0>Úì>
39Ö6E4¸!H0üT©                                                ;¡¬=¦ò>®¾h>ÝÂ~>x´>oÜâ>¤J>Îö?3[g?'¨?^n?î?ÿý?ÿÿ?ÿÿ?ÿþ?ÿý?ÿû?^¢?Oõ ?},?ÿþ?ÿþ?ÿý?ÿþ?ÿþ?ÿÿ?ÿÿ?ÿÿ?ÿÿ?  ?ÿý?ÿþ?ÿÿ?ÿÿ?ÿÿ?ÿþ?ÿþ?ÿý?ÿý?i·?F@?*,±?
î> 9<2ò                                                                                                                =-¸> Ú?Jß©?~Põ?ÿý?ÿý>ÎµY/{                                                        ?xÏó?ÿû?ÿý?ÿý?ÿü?ÿü?ÿý?ÿý?ÿþ?ÿþ?ÿÿ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?ÿþ?ÿþ?~Ä$?9ÿ?ovk>ï0q                                        ; ï=¿%>¨m>­ÄE=ØQ<8Ð:Ë>    =Üëì>9#>}¢>L>¦ª >²^>Ù]?=C?T¡?ÿü?ÿÿ?  ?  ?  ?Q¿=4Y´                            :Ò&=5>^|Ý?!£?d|D?VV?[ãá?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?ÿÿ?  ?b®?
.à>ìè>ÆÕj>¤¯ö>yÓ>_Hì>Ïk?7I?h>d?[¹?V©?ÿý?ÿþ?ÿþ?ÿý?ÿý?Ê?~
¨?~?ÿþ?ÿþ?ÿþ?ÿþ?ÿþ?ÿþ?ÿÿ?  ?  ?  ?  ?  ?  ?oÉ|>¹©}>c!>¹¦>ä¿j?	j?"i	?<ÀÉ?VS?t,?ÿý?ÿþ?ÿÿ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?  