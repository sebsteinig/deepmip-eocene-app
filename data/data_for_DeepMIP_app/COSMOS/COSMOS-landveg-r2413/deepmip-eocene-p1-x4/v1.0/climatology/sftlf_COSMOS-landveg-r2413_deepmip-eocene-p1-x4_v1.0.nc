CDF       
      lat    0   lon    `         CDI       <Climate Data Interface version ?? (http://mpimet.mpg.de/cdi)   Conventions       CF-1.8     history      Wed Nov 22 12:18:49 2023: ncatted -a standard_name,sftlf,o,c,land_area_fraction -a long_name,sftlf,o,c,Percentage of the Grid Cell Occupied by Land -a units,sftlf,o,c,% -a Conventions,global,o,c,CF-1.8 -a institution,global,o,c,Alfred Wegener Institute, Helmholtz Centre for Polar and Marine Research, Bremerhaven, Germany -a source,global,o,c,COSMOS-landveg-r2413 -a project,global,o,c,DeepMIP-Eocene Phase 1 -a experiment,global,o,c,deepmip-eocene-p1-x4 -a version,global,o,c,v1.0 -a reference,global,o,c,https://www.deepmip.org -a title,global,o,c,COSMOS-landveg-r2413 output processed for the DeepMIP-Eocene model database version 1.0 /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg-r2413/deepmip-eocene-p1-x4/v1.0/climatology/sftlf_COSMOS-landveg-r2413_deepmip-eocene-p1-x4_v1.0.nc
Wed Nov 22 12:18:49 2023: ncap2 -O -s sftlf=sftlf*100 /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg-r2413/deepmip-eocene-p1-x4/v1.0/climatology/sftlf_COSMOS-landveg-r2413_deepmip-eocene-p1-x4_v1.0.nc /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg-r2413/deepmip-eocene-p1-x4/v1.0/climatology/sftlf_COSMOS-landveg-r2413_deepmip-eocene-p1-x4_v1.0.nc
Wed Nov 22 10:43:20 2023: ncks -O -v sftlf /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg_r2413/deepmip_sens_4xCO2/v1.0/COSMOS-landveg_r2413-deepmip_sens_4xCO2-sftlf-v1.0.nc /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg_r2413/deepmip_sens_4xCO2/v1.0/COSMOS-landveg_r2413-deepmip_sens_4xCO2-sftlf-v1.0.nc
Wed Nov 22 10:43:20 2023: ncwa -O -a time /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg_r2413/deepmip_sens_4xCO2/v1.0/COSMOS-landveg_r2413-deepmip_sens_4xCO2-sftlf-v1.0.nc /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg_r2413/deepmip_sens_4xCO2/v1.0/COSMOS-landveg_r2413-deepmip_sens_4xCO2-sftlf-v1.0.nc
Wed Nov 22 10:43:20 2023: ncatted -O -a long_name,sftlf,m,c,Land-sea mask (on atmospheric grid) /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg_r2413/deepmip_sens_4xCO2/v1.0/COSMOS-landveg_r2413-deepmip_sens_4xCO2-sftlf-v1.0.nc /Volumes/external_Samsung-SSD/deepmip_database/deepmip-eocene-p1/COSMOS/COSMOS-landveg_r2413/deepmip_sens_4xCO2/v1.0/COSMOS-landveg_r2413-deepmip_sens_4xCO2-sftlf-v1.0.nc
Sun Mar 22 17:00:39 2020: cdo chname,SLM,sftlf -selvar,SLM Eocene_topo.nc COSMOS-landveg_r2413-deepmip_sens_all-sftlf.nc
Tue Mar 17 17:14:03 2020: cdo selvar,OROMEA,SLM T31GR30_jan_surf.nc Eocene_topo.nc
Tue Aug 20 14:01:55 2019: cdo merge -chname,DEPTO,SLM ../lsm/Eocene_atm_lsm.nc vegetation.nc ../orography/Eocene_orography_all.nc T31GR30_jan_surf.nc
Wed Aug 14 11:15:53 2019: cdo setmisstoc,1 tmp.nc Eocene_atm_lsm.nc
Wed Aug 14 11:15:18 2019: cdo remapcon,t31grid Eocene_bathym_122x101_bin.nc tmp.nc
Wed Aug 14 11:08:03 2019: cdo setrtoc,-100000,-0.0000001,0 -setrtoc,0,0,1 -mulc,-1 GR30_topo_jj_modified.nc GR30_topo_jj_modified_miss.nc
Fri Mar 22 16:05:51 2013: cdo setrtomiss,-100000,100000 GR30_topo_jj_modified.nc GR30_topo_jj_template.nc
Fri Mar 22 15:05:00 2013: cdo -f nc -t mpiom1 -selvar,DEPTO -setgrid,GR30s.nc -selindexbox,2,121,1,101 -setgrid,r122x101 fort.72 topo.nc     institution       ^Alfred Wegener Institute, Helmholtz Centre for Polar and Marine Research, Bremerhaven, Germany     CDO       ?Climate Data Operators version 1.9.3 (http://mpimet.mpg.de/cdo)    NCO       `netCDF Operators version 5.1.0 (Homepage = http://nco.sf.net, Code = http://github.com/nco/nco)    source        COSMOS-landveg-r2413   project       DeepMIP-Eocene Phase 1     
experiment        deepmip-eocene-p1-x4   version       v1.0   	reference         https://www.deepmip.org    title         WCOSMOS-landveg-r2413 output processed for the DeepMIP-Eocene model database version 1.0          sftlf                      
_FillValue        ����   cell_methods      
time: mean     code         T   	long_name         ,Percentage of the Grid Cell Occupied by Land   missing_value         ����   table            �   units         %      standard_name         land_area_fraction       H   �   lat                 standard_name         latitude   	long_name         latitude   units         degrees_north      axis      Y        �  Z�   lon                standard_name         	longitude      	long_name         	longitude      units         degrees_east   axis      X           \@                                                                                                                                                                                                                                                                                                                                                                                                                                                            ?���A�a�B/5�B! DA�(�Ac�kA7�A�2*A��<?St                                                                                                                                                                                                                                                                                                                                                        @��rBZ��B�X�B�  B�  B�  B�  B�  B�  B�:B�9�BD@Ժ<A϶B~�B��B���B��FB��B��BAI�@��@���@�==A�^B6^�B,&�B�=B
�>A��A�]�BW��BI��B'/�A�.Bp�BR#�BL�A�;A��OB/�Bw�cB��3B���B�4B�мBP�	A��dB�Ag��A^��                            >���;��5    A�"�B�\LB�/BY;�B4q�Aه�A���A*�IA� A�M�BRIBD��BK2�Bb�UBO2�BQ�BI�@�xT        B�R�B�(BtNYAv�H                    >�&�A�>gB�=�B���B���A�    A���B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�&�B�^B��B��|BC��B\1B �?B39�B�7iB�s B�MBB�7QB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��oB�=cB�[B��B�  B�  B��
Al+    ?m�B/�vB�2�B_̉B�L�B�  B�  BǒlB���AO2�    A�BB�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��SB�cIB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�)�B�  B�  B�  B�  B�  B�  B��A�IBݵBf>GBy�aB���B�  B�  B�  B�  B�  B�  B��0B�P?B���A��?�u�Bq�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��B��A�8vA��N?�?�B	�1B���B�;�B�  B�  B�  B�  B�  B�  B�  B�eZB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B���B���B�  B�  B�  B�  B�  B���A��+B��]B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�+�?e�    A��LB��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B���B�j�BT�OB �@�5&>��f                ?�\�B/%B�+�B��VB�  B�  B� ,B�X�B-&�@���A���A��B��2B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�NBR B��B�  B�  B�  B�  B�  B�  B2B�lpB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�ߠB%B        A0\9B��<B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B���B9�A�@�                                                ?	j�A��B ��@�s;                ?��UB3�B�@B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�SBwδB;��BU)�Bo��B���B��B�Q�B���A�9�Bi��B�  B�  B�  B�  B�  B�  B�[GAжB�9B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�A�}@t�AS��    BJ�"B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�A]A���A�@*                                                                                            @3�B��'B��6B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��AaA�@�t�B��EB�  B�  B���A���>���B��MB�  B�  B�  B�  B�  B�  Bt6NB	�B�D�B�  B�  B�  B�  B�  B�  B�  B�  B�  B���B��'B�  B��A���B���B��B��B��}B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B:X�                                                                                                                A��HB�fFB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��VB�.B�  B�  B�  B�  B���A��Bj6.B�+�B�  B�CB�CB��B��BeR�Ahj'A�_OBB�B�f�B�:B�  B�  B�:dB��BÄWB�nB0UA&A�B�p�B�  B�xAȕ�BǴDB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B>�5AP}k                                                                                                                <���B��wB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B���A%��?Zv�A��A&r�Bl�B�lB���B��B��B�j�B�vB��A䤺BL�vB"�A+B�=�!�@��v            B%�-B�  BA��    B��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��A��v                                                                                                                    @�	B��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�F�A�F            B3�B���B�  B��kB���B��B�  B��GBO��A��B"e�AJY�        <�Ʀ        ?�HBq�GB�    AǛ�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  AK�
                                                                                                                        A�tB�:-B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B���B�  B�Z�@}sX                A�WYA��*Bz�bB�  B�('BFwA��`B��B�  B�  B�L�B�ĂBw�B�q�A��B|��A�\@
W�A�_3A�Ep>���B� �B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  AF~�                                                                                                                            AT�wB���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��%B���B �UA�W!A0IgA��YA�"�?�er                Bc<�B�C�B�  B�  BE'"        A�zB��[B�  B�  B�  B�  B�A�:�B��zB�V�B���B�  B�J�    A���B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  A��@-��                                                                                                                                B--vB���B�  B�  B�  B�  B�  B�  B�  B�  B�  B���A�e<���                                    @�8�B�D�B�  B�  Adp�>�k            A�FcB���B���Bag]A�&,@���AIcB��B�  B�  B�  B�vG=���>�a�B,��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  A���A	�N?5�                                                                                                                                        B��B�  B�  B�  B�  B�*UB7kB�ZB�˞B4
�A��                                                B�{B[��B'B���A�$?��:@�|�        >�My                    ?��B1��B���B�  B!��    B��NB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�f(A+�                                                                                                                                                A��B�ȥB�  B�  B���A�    <�/�@�t                                                        A;M�B��BT\^BZ�A�'EB��EBS��                                        @���B1��A|N�    B|`B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��7AGO.                                                                                                                                                        B,|�B�  B�  B��]A���                                                                @4AVB�@�B�  B�  Ba��B��B�؈B���                @�SA`��                                A��B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  A��?                                                                                                                                                            A���B�(zB�  B�  B���A$��                                                        A(�A�(PB��B�  B�  B�  B�  B�  B�4Bt�`B��Ac�%B��
B�B�0�>&M                                BrLB�B�B�J�B�  B�  B�  B�  B�  B�  B�  B�  B�  A�_                                                                                                                                                                Bf{{B�  B�  B�  BF        As�)                                            B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B���Bǹ�B�  B�  B���                        ?E�AF5>0�'    A�~qA��B�n�B�fMB�  B�  B�  B�  B�  B�  A��4                                                                                                                                                                A��B���B�  B�3&@��g    >��B�m�                                            Bi,+B�  B�  B�PPB��EB�"B�  B�  B�  B�  B�  B�  B�  B�  B�  B���A�                ?���Bn�B�  B>Z;v�l        ?�Z�B�C+B©�B�  B�  B�  B�  B�  B��Bqx�Br�@u                                                                                                                                                        AH�<A��B'%�A��    @	A�[AA��lA[ĳA81A-9\@c��                    @�i*B�M|B�  B�  B�9�A�\�Blo�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  A�/�                BϖB�  B�  B�  @�w                BH��Bó�B�  B�  B�  B�  B�  B�  B�  Ai                                                                                                                                                                    BL�    AC�B�  B�  B�  B�  B�  B|F�>p�                @�BƅB�  B�  B���Bh+8B,�6B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B<9;                B��DB�  B�  B�  B��A�s6                B�B5��B�  B�  B�  B�  B�  BD�?�{�                                                                                                                                                                        Agz]A���B�  B�  B�  B�  B�  B�  B�]�B)D�?�9�            BNP�BǶ�B�  B�  B��XAݘ<B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�D                B�)�B�  B�  B�  B�  B��e                    @=�@A��*A �Bh˹B�  B��@�{                                                                                                                                                                            B �_A�5�B�  B�  B�  B�  B�  B�  B�  B�  B>V�            ?c�A�,BZ�B$~UA�M�AJR�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�;$                Bf��B�  B�  B�  B�  Bon�?OP                            ?Ũ\@D��?`K                                                                                                                                                                                =0�tA�gJB�  B�  B�  B�  B�  B�  B�  B�  B��}B��B=��A��                    ?k}�B���B�  B�  B�  B�  B�  B�  B�  B��5B2G�>��                B4wVB�  B�  B��B_MA"k                                                                                                                                                                                                                            @em�B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�/jB�>                    B�c�B�  B�  B�  B�  B�  B�  B�  B�PV                        B�vB�  BLx�A�c�                                                                                                                                                                                                                                    @,��B}wEB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�;XA�tw                    B��B�  B�  B�  B�  B�  B�  B�  B���@X�                    A���B�  B \-                                                                                                                                                                                                                                            B
G�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��|                    @��tB�?�B�  B�  B�  B�  B�  B�  B�  B�Y@A*8                    A�SB���A� *                                                                                                                                                                                                                                            A�b�B��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��                    A(>�B�  B�  B�  B�  B�  B�  B�  B�  B_#    B�=�B0�                                                                                                                                                                                                                                                                        A�CB�/oB�  B�  B�  B�  B�  B�  B�  B�  B���A��                    >�+MB��EB�  B�  B�  B�  B�  B�  B�{�A��YBN�B�(Bx��                                                                                            @Nc;=�v�                                                                                                                                                                        B�8bB�  B�  B�  B�  B�  B�  B�  B��ZA��                            B�ގB�  B�  B�  B�  B�  B�  B�~    B-J�B�  B}W                                                                            A;��BN&B3�kB�B�NB�U�                                                                                                                                                                        B���B�  B�  B�  B�  B�  B�  B��
Aӎ                                A��cB�W|B�  B�  B�  B�  B�ǋAN�z    A�p)B�  Aj8                                                                    A�NWA�B���B�  B�  B�  B�  B�AÐ�                                                                                                                                                                    B���B�  B�  B�  B�  B�  B�  B�m                                        B���B�  B�  B�  B�  A��        @t�rAK��?̚                                                            @��6B1nXB���B�  B�  B�  B�  B�  B�  B�  B�p�Bo6�BF¹?�T                                                                                                                                                    A��(B�H�B�  B�  B�  B�  B�  B�<2A8^2                                        BV�uB�  B�+�B��qB^�p@cw'                                                                        ?��RB]}B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��B^@>.�                                                                                                                                                B!"�B�  B�  B�  B�/�B��CA���A"�9                                            @s_fB3�BH                                                                                    A]JB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B/�?                        @�W6@���                                                                                                            A��B���B�  B�  B�5�B�/                                                                                                                                                        A�B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B
��                        Bq(�B�F�@ݝ�                                                                                                        @b15B�q�B�  B�  B�1�@��V=���?�H|                                                                                                                                                A��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�s,                        B@�B�®B�!B�B5�                                                                                                    B���B�  B�  B�  A�eB�ffBn}                                                                                                                                                BB�KB��%B��GB�7jB��B_	3B�B*M;Bs�\B�� B�  B�  B�  B�  B�  B�  B@�                        A� �B�  B�  B��BHe�                                                                                                    B�znB�  B�  B�ֳA�}tBw<?��                                                                                                                                                @���A5q{                            @|}A{qMB�f.B�R�B�WIB�  B��A%�B                        B :�B�.�B3A AU�T                                                                                                        A{U�B�fzB�B��>�ò                                                                                        >'�!A�T�B/�WB��;B�?*By	�A�A@�3    B�BXWBI��B9B���B��bB�r�B��&B���B�a�B��UBGKB\��B� �B���B�=4B���B_֩B�B^B�GDB�]�B��                                                                                                                                        A�d�B&ͺB+�Ax�='/�                                                        >���A�_B��B-?�A���A�d�B ��B!��B�kB�}�B�y�B�H]B�  B�  B�  B�  B�  B�  B�~�B�wkB���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B��B��B���B_�A�z^?���                                                                                                                @��4A�U�B�~�BƯBB�  B�  B!}�                                                            B�bzB�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�	?B�O�B��B:��                                        >��zA��B�:B�XA(�[?^8�=]��    A,�TA�yKA�$RA���B4�B��B)�tB���B�)B�  B�  B�  B�  B�  B���@��                            >$.(@ԙXA�ѐBS$�B��B��B��B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�bBW�AB8bHBV�B �zAЎ[A�p�B"�B�1qB�p�B���B��qB�  B�  B�  B�  B�  BǞ�B�xVB��[B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�UiBkA�*�B�B2��BV�	B}�!B�v�B�q?B���B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  @U�.���@Tަ���@S���f@S~�V�@R$$���@Q)�����@P<H�,�@N��0���@L¯�ٔ@J�9�F@I�� �@G1�E��l@EV�̏s�@C{��Q#]@A���M�V@?�e��ț@;�\��W�@8R8KD�@4iF�+@0�:��g�@)�\� _<@"�B���@DP��Xm?��k���̿��k�����DP��Xm�"�B����)�\� _<�0�:��g��4iF�+�8R8KD��;�\��W��?�e��ț�A���M�V�C{��Q#]�EV�̏s��G1�E��l�I�� ��J�9�F�L¯�ٔ�N��0����P<H�,��Q)������R$$����S~�V��S���f�Tަ����U�.���        @      @      @&�     @.      @2�     @6�     @:@     @>      @@�     @B�     @D�     @F�     @H`     @J@     @L      @N      @O�     @P�     @Q�     @R�     @S�     @T�     @U�     @V�     @Wp     @X`     @YP     @Z@     @[0     @\      @]     @^      @^�     @_�     @`h     @`�     @aX     @a�     @bH     @b�     @c8     @c�     @d(     @d�     @e     @e�     @f     @f�     @f�     @gp     @g�     @h`     @h�     @iP     @i�     @j@     @j�     @k0     @k�     @l      @l�     @m     @m�     @n      @nx     @n�     @oh     @o�     @p,     @ph     @p�     @p�     @q     @qX     @q�     @q�     @r     @rH     @r�     @r�     @r�     @s8     @st     @s�     @s�     @t(     @td     @t�     @t�     @u     @uT     @u�     @u�     @v     @vD     