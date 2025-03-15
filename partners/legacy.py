# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bpartner(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')  # Field name made lowercase.
    bprnum_0 = models.CharField(db_column='BPRNUM_0', unique=True, max_length=15)  # Field name made lowercase.
    enaflg_0 = models.SmallIntegerField(db_column='ENAFLG_0')  # Field name made lowercase.
    brgcod_0 = models.CharField(db_column='BRGCOD_0', max_length=5)  # Field name made lowercase.
    brgobj_0 = models.CharField(db_column='BRGOBJ_0', max_length=3)  # Field name made lowercase.
    bprnam_0 = models.CharField(db_column='BPRNAM_0', max_length=35)  # Field name made lowercase.
    bprnam_1 = models.CharField(db_column='BPRNAM_1', max_length=35)  # Field name made lowercase.
    bprsho_0 = models.CharField(db_column='BPRSHO_0', max_length=10)  # Field name made lowercase.
    eecnum_0 = models.CharField(db_column='EECNUM_0', max_length=20)  # Field name made lowercase.
    betfcy_0 = models.SmallIntegerField(db_column='BETFCY_0')  # Field name made lowercase.
    fcy_0 = models.CharField(db_column='FCY_0', max_length=5)  # Field name made lowercase.
    cry_0 = models.CharField(db_column='CRY_0', max_length=3)  # Field name made lowercase.
    crn_0 = models.CharField(db_column='CRN_0', max_length=20)  # Field name made lowercase.
    naf_0 = models.CharField(db_column='NAF_0', max_length=1)  # Field name made lowercase.
    cur_0 = models.CharField(db_column='CUR_0', max_length=3)  # Field name made lowercase.
    lan_0 = models.CharField(db_column='LAN_0', max_length=3)  # Field name made lowercase.
    bprlog_0 = models.CharField(db_column='BPRLOG_0', max_length=10)  # Field name made lowercase.
    vatnum_0 = models.CharField(db_column='VATNUM_0', max_length=1)  # Field name made lowercase.
    fiscod_0 = models.CharField(db_column='FISCOD_0', max_length=1)  # Field name made lowercase.
    grugpy_0 = models.CharField(db_column='GRUGPY_0', max_length=5)  # Field name made lowercase.
    grucod_0 = models.CharField(db_column='GRUCOD_0', max_length=1)  # Field name made lowercase.
    bpcflg_0 = models.SmallIntegerField(db_column='BPCFLG_0')  # Field name made lowercase.
    bpsflg_0 = models.SmallIntegerField(db_column='BPSFLG_0')  # Field name made lowercase.
    ccnflg_0 = models.SmallIntegerField(db_column='CCNFLG_0')  # Field name made lowercase.
    bptflg_0 = models.SmallIntegerField(db_column='BPTFLG_0')  # Field name made lowercase.
    fctflg_0 = models.SmallIntegerField(db_column='FCTFLG_0')  # Field name made lowercase.
    repflg_0 = models.SmallIntegerField(db_column='REPFLG_0')  # Field name made lowercase.
    bpracc_0 = models.SmallIntegerField(db_column='BPRACC_0')  # Field name made lowercase.
    pptflg_0 = models.SmallIntegerField(db_column='PPTFLG_0')  # Field name made lowercase.
    prvflg_0 = models.SmallIntegerField(db_column='PRVFLG_0')  # Field name made lowercase.
    dooflg_0 = models.SmallIntegerField(db_column='DOOFLG_0')  # Field name made lowercase.
    acccod_0 = models.CharField(db_column='ACCCOD_0', max_length=10)  # Field name made lowercase.
    pthflg_0 = models.SmallIntegerField(db_column='PTHFLG_0')  # Field name made lowercase.
    bprflg_0 = models.SmallIntegerField(db_column='BPRFLG_0')  # Field name made lowercase.
    bprflg_1 = models.SmallIntegerField(db_column='BPRFLG_1')  # Field name made lowercase.
    bprflg_2 = models.SmallIntegerField(db_column='BPRFLG_2')  # Field name made lowercase.
    bprflg_3 = models.SmallIntegerField(db_column='BPRFLG_3')  # Field name made lowercase.
    bpaadd_0 = models.CharField(db_column='BPAADD_0', max_length=5)  # Field name made lowercase.
    cntnam_0 = models.CharField(db_column='CNTNAM_0', max_length=35)  # Field name made lowercase.
    bidnum_0 = models.CharField(db_column='BIDNUM_0', max_length=30)  # Field name made lowercase.
    bidcry_0 = models.CharField(db_column='BIDCRY_0', max_length=3)  # Field name made lowercase.
    acs_0 = models.CharField(db_column='ACS_0', max_length=10)  # Field name made lowercase.
    expnum_0 = models.IntegerField(db_column='EXPNUM_0')  # Field name made lowercase.
    bprgtetyp_0 = models.CharField(db_column='BPRGTETYP_0', max_length=5)  # Field name made lowercase.
    bprfbdmag_0 = models.SmallIntegerField(db_column='BPRFBDMAG_0')  # Field name made lowercase.
    modpam_0 = models.CharField(db_column='MODPAM_0', max_length=20)  # Field name made lowercase.
    accnonrei_0 = models.CharField(db_column='ACCNONREI_0', max_length=5)  # Field name made lowercase.
    legett_0 = models.SmallIntegerField(db_column='LEGETT_0')  # Field name made lowercase.
    cfoexd_0 = models.SmallIntegerField(db_column='CFOEXD_0')  # Field name made lowercase.
    creusr_0 = models.CharField(db_column='CREUSR_0', max_length=5)  # Field name made lowercase.
    credat_0 = models.DateTimeField(db_column='CREDAT_0')  # Field name made lowercase.
    updusr_0 = models.CharField(db_column='UPDUSR_0', max_length=5)  # Field name made lowercase.
    upddat_0 = models.DateTimeField(db_column='UPDDAT_0')  # Field name made lowercase.
    doctyp_0 = models.SmallIntegerField(db_column='DOCTYP_0')  # Field name made lowercase.
    bppflg_0 = models.SmallIntegerField(db_column='BPPFLG_0')  # Field name made lowercase.
    credattim_0 = models.DateTimeField(db_column='CREDATTIM_0')  # Field name made lowercase.
    upddattim_0 = models.DateTimeField(db_column='UPDDATTIM_0')  # Field name made lowercase.
    auuid_0 = models.TextField(db_column='AUUID_0')  # Field name made lowercase. This field type is a guess.
    cpyrel_0 = models.SmallIntegerField(db_column='CPYREL_0')  # Field name made lowercase.
    cslbpr_0 = models.CharField(db_column='CSLBPR_0', max_length=1)  # Field name made lowercase.
    regnum_0 = models.CharField(db_column='REGNUM_0', max_length=1)  # Field name made lowercase.
    vatno_0 = models.CharField(db_column='VATNO_0', max_length=1)  # Field name made lowercase.
    zpagitm_0 = models.SmallIntegerField(db_column='ZPAGITM_0')  # Field name made lowercase.
    eorinum_0 = models.CharField(db_column='EORINUM_0', max_length=35)  # Field name made lowercase.
    intsrvcod_0 = models.CharField(db_column='INTSRVCOD_0', max_length=1)  # Field name made lowercase.
    zeditor_0 = models.SmallIntegerField(db_column='ZEDITOR_0')  # Field name made lowercase.
    rtgcod_0 = models.CharField(db_column='RTGCOD_0', max_length=1)  # Field name made lowercase.
    einvtyp_0 = models.SmallIntegerField(db_column='EINVTYP_0')  # Field name made lowercase.
    zintvsp_0 = models.SmallIntegerField(db_column='ZINTVSP_0')  # Field name made lowercase.
    mapcod_0 = models.CharField(db_column='MAPCOD_0', max_length=1)  # Field name made lowercase.
    zagente_0 = models.SmallIntegerField(db_column='ZAGENTE_0')  # Field name made lowercase.
    zgesflg_0 = models.SmallIntegerField(db_column='ZGESFLG_0')  # Field name made lowercase.
    zanaflg_0 = models.SmallIntegerField(db_column='ZANAFLG_0')  # Field name made lowercase.
    zexpflg_0 = models.SmallIntegerField(db_column='ZEXPFLG_0')  # Field name made lowercase.
    rowid = models.AutoField(db_column='ROWID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPARTNER'
        unique_together = (('betfcy_0', 'fcy_0', 'bprnum_0'),)


class Bpaddress(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')  # Field name made lowercase.
    bpatyp_0 = models.SmallIntegerField(db_column='BPATYP_0')  # Field name made lowercase.
    bpanum_0 = models.CharField(db_column='BPANUM_0', max_length=15)  # Field name made lowercase.
    bpaadd_0 = models.CharField(db_column='BPAADD_0', max_length=5)  # Field name made lowercase.
    bpades_0 = models.CharField(db_column='BPADES_0', max_length=30)  # Field name made lowercase.
    bpabid_0 = models.CharField(db_column='BPABID_0', max_length=30)  # Field name made lowercase.
    bpaaddflg_0 = models.SmallIntegerField(db_column='BPAADDFLG_0')  # Field name made lowercase.
    bpaaddlig_0 = models.CharField(db_column='BPAADDLIG_0', max_length=50)  # Field name made lowercase.
    bpaaddlig_1 = models.CharField(db_column='BPAADDLIG_1', max_length=50)  # Field name made lowercase.
    bpaaddlig_2 = models.CharField(db_column='BPAADDLIG_2', max_length=50)  # Field name made lowercase.
    poscod_0 = models.CharField(db_column='POSCOD_0', max_length=10)  # Field name made lowercase.
    cty_0 = models.CharField(db_column='CTY_0', max_length=40)  # Field name made lowercase.
    codsee_0 = models.CharField(db_column='CODSEE_0', max_length=1)  # Field name made lowercase.
    sat_0 = models.CharField(db_column='SAT_0', max_length=35)  # Field name made lowercase.
    cry_0 = models.CharField(db_column='CRY_0', max_length=3)  # Field name made lowercase.
    crynam_0 = models.CharField(db_column='CRYNAM_0', max_length=40)  # Field name made lowercase.
    tel_0 = models.CharField(db_column='TEL_0', max_length=40)  # Field name made lowercase.
    tel_1 = models.CharField(db_column='TEL_1', max_length=40)  # Field name made lowercase.
    tel_2 = models.CharField(db_column='TEL_2', max_length=40)  # Field name made lowercase.
    tel_3 = models.CharField(db_column='TEL_3', max_length=40)  # Field name made lowercase.
    tel_4 = models.CharField(db_column='TEL_4', max_length=40)  # Field name made lowercase.
    fax_0 = models.CharField(db_column='FAX_0', max_length=40)  # Field name made lowercase.
    mob_0 = models.CharField(db_column='MOB_0', max_length=40)  # Field name made lowercase.
    web_0 = models.CharField(db_column='WEB_0', max_length=80)  # Field name made lowercase.
    web_1 = models.CharField(db_column='WEB_1', max_length=80)  # Field name made lowercase.
    web_2 = models.CharField(db_column='WEB_2', max_length=80)  # Field name made lowercase.
    web_3 = models.CharField(db_column='WEB_3', max_length=80)  # Field name made lowercase.
    web_4 = models.CharField(db_column='WEB_4', max_length=80)  # Field name made lowercase.
    fcyweb_0 = models.CharField(db_column='FCYWEB_0', max_length=250)  # Field name made lowercase.
    extnum_0 = models.CharField(db_column='EXTNUM_0', max_length=30)  # Field name made lowercase.
    expnum_0 = models.IntegerField(db_column='EXPNUM_0')  # Field name made lowercase.
    creusr_0 = models.CharField(db_column='CREUSR_0', max_length=5)  # Field name made lowercase.
    credat_0 = models.DateTimeField(db_column='CREDAT_0')  # Field name made lowercase.
    updusr_0 = models.CharField(db_column='UPDUSR_0', max_length=5)  # Field name made lowercase.
    upddat_0 = models.DateTimeField(db_column='UPDDAT_0')  # Field name made lowercase.
    credattim_0 = models.DateTimeField(db_column='CREDATTIM_0')  # Field name made lowercase.
    upddattim_0 = models.DateTimeField(db_column='UPDDATTIM_0')  # Field name made lowercase.
    auuid_0 = models.TextField(db_column='AUUID_0')  # Field name made lowercase. This field type is a guess.
    adrval_0 = models.SmallIntegerField(db_column='ADRVAL_0')  # Field name made lowercase.
    glncod_0 = models.CharField(db_column='GLNCOD_0', max_length=13)  # Field name made lowercase.
    crn_0 = models.CharField(db_column='CRN_0', max_length=20)  # Field name made lowercase.
    rowid = models.AutoField(db_column='ROWID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPADDRESS'
        unique_together = (('bpatyp_0', 'bpanum_0', 'bpaadd_0'),)


class Bpsupplier(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')  # Field name made lowercase.
    bpsnum_0 = models.CharField(db_column='BPSNUM_0', unique=True, max_length=15)  # Field name made lowercase.
    bpsnam_0 = models.CharField(db_column='BPSNAM_0', max_length=35)  # Field name made lowercase.
    bpssho_0 = models.CharField(db_column='BPSSHO_0', max_length=10)  # Field name made lowercase.
    bpstyp_0 = models.SmallIntegerField(db_column='BPSTYP_0')  # Field name made lowercase.
    bsgcod_0 = models.CharField(db_column='BSGCOD_0', max_length=5)  # Field name made lowercase.
    bprpay_0 = models.CharField(db_column='BPRPAY_0', max_length=15)  # Field name made lowercase.
    bpapay_0 = models.CharField(db_column='BPAPAY_0', max_length=5)  # Field name made lowercase.
    bpsinv_0 = models.CharField(db_column='BPSINV_0', max_length=15)  # Field name made lowercase.
    bpainv_0 = models.CharField(db_column='BPAINV_0', max_length=5)  # Field name made lowercase.
    bpsgru_0 = models.CharField(db_column='BPSGRU_0', max_length=15)  # Field name made lowercase.
    bpsrsk_0 = models.CharField(db_column='BPSRSK_0', max_length=15)  # Field name made lowercase.
    bpcnumbps_0 = models.CharField(db_column='BPCNUMBPS_0', max_length=15)  # Field name made lowercase.
    bptnum_0 = models.CharField(db_column='BPTNUM_0', max_length=15)  # Field name made lowercase.
    cntnam_0 = models.CharField(db_column='CNTNAM_0', max_length=35)  # Field name made lowercase.
    loc_0 = models.CharField(db_column='LOC_0', max_length=10)  # Field name made lowercase.
    abccls_0 = models.SmallIntegerField(db_column='ABCCLS_0')  # Field name made lowercase.
    uvycod_0 = models.CharField(db_column='UVYCOD_0', max_length=5)  # Field name made lowercase.
    cur_0 = models.CharField(db_column='CUR_0', max_length=3)  # Field name made lowercase.
    chgtyp_0 = models.SmallIntegerField(db_column='CHGTYP_0')  # Field name made lowercase.
    pte_0 = models.CharField(db_column='PTE_0', max_length=15)  # Field name made lowercase.
    dep_0 = models.CharField(db_column='DEP_0', max_length=5)  # Field name made lowercase.
    vacbpr_0 = models.CharField(db_column='VACBPR_0', max_length=5)  # Field name made lowercase.
    mdl_0 = models.CharField(db_column='MDL_0', max_length=5)  # Field name made lowercase.
    eecict_0 = models.CharField(db_column='EECICT_0', max_length=5)  # Field name made lowercase.
    eecloc_0 = models.SmallIntegerField(db_column='EECLOC_0')  # Field name made lowercase.
    tsscod_0 = models.CharField(db_column='TSSCOD_0', max_length=20)  # Field name made lowercase.
    tsscod_1 = models.CharField(db_column='TSSCOD_1', max_length=20)  # Field name made lowercase.
    tsscod_2 = models.CharField(db_column='TSSCOD_2', max_length=20)  # Field name made lowercase.
    tsscod_3 = models.CharField(db_column='TSSCOD_3', max_length=20)  # Field name made lowercase.
    tsscod_4 = models.CharField(db_column='TSSCOD_4', max_length=20)  # Field name made lowercase.
    invdtaamt_0 = models.DecimalField(db_column='INVDTAAMT_0', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_1 = models.DecimalField(db_column='INVDTAAMT_1', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_2 = models.DecimalField(db_column='INVDTAAMT_2', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_3 = models.DecimalField(db_column='INVDTAAMT_3', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_4 = models.DecimalField(db_column='INVDTAAMT_4', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_5 = models.DecimalField(db_column='INVDTAAMT_5', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_6 = models.DecimalField(db_column='INVDTAAMT_6', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_7 = models.DecimalField(db_column='INVDTAAMT_7', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_8 = models.DecimalField(db_column='INVDTAAMT_8', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_9 = models.DecimalField(db_column='INVDTAAMT_9', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_10 = models.DecimalField(db_column='INVDTAAMT_10', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_11 = models.DecimalField(db_column='INVDTAAMT_11', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_12 = models.DecimalField(db_column='INVDTAAMT_12', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_13 = models.DecimalField(db_column='INVDTAAMT_13', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_14 = models.DecimalField(db_column='INVDTAAMT_14', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_15 = models.DecimalField(db_column='INVDTAAMT_15', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_16 = models.DecimalField(db_column='INVDTAAMT_16', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_17 = models.DecimalField(db_column='INVDTAAMT_17', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_18 = models.DecimalField(db_column='INVDTAAMT_18', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_19 = models.DecimalField(db_column='INVDTAAMT_19', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_20 = models.DecimalField(db_column='INVDTAAMT_20', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_21 = models.DecimalField(db_column='INVDTAAMT_21', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_22 = models.DecimalField(db_column='INVDTAAMT_22', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_23 = models.DecimalField(db_column='INVDTAAMT_23', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_24 = models.DecimalField(db_column='INVDTAAMT_24', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_25 = models.DecimalField(db_column='INVDTAAMT_25', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_26 = models.DecimalField(db_column='INVDTAAMT_26', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_27 = models.DecimalField(db_column='INVDTAAMT_27', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_28 = models.DecimalField(db_column='INVDTAAMT_28', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_29 = models.DecimalField(db_column='INVDTAAMT_29', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdta_0 = models.SmallIntegerField(db_column='INVDTA_0')  # Field name made lowercase.
    invdta_1 = models.SmallIntegerField(db_column='INVDTA_1')  # Field name made lowercase.
    invdta_2 = models.SmallIntegerField(db_column='INVDTA_2')  # Field name made lowercase.
    invdta_3 = models.SmallIntegerField(db_column='INVDTA_3')  # Field name made lowercase.
    invdta_4 = models.SmallIntegerField(db_column='INVDTA_4')  # Field name made lowercase.
    invdta_5 = models.SmallIntegerField(db_column='INVDTA_5')  # Field name made lowercase.
    invdta_6 = models.SmallIntegerField(db_column='INVDTA_6')  # Field name made lowercase.
    invdta_7 = models.SmallIntegerField(db_column='INVDTA_7')  # Field name made lowercase.
    invdta_8 = models.SmallIntegerField(db_column='INVDTA_8')  # Field name made lowercase.
    invdta_9 = models.SmallIntegerField(db_column='INVDTA_9')  # Field name made lowercase.
    invdta_10 = models.SmallIntegerField(db_column='INVDTA_10')  # Field name made lowercase.
    invdta_11 = models.SmallIntegerField(db_column='INVDTA_11')  # Field name made lowercase.
    invdta_12 = models.SmallIntegerField(db_column='INVDTA_12')  # Field name made lowercase.
    invdta_13 = models.SmallIntegerField(db_column='INVDTA_13')  # Field name made lowercase.
    invdta_14 = models.SmallIntegerField(db_column='INVDTA_14')  # Field name made lowercase.
    invdta_15 = models.SmallIntegerField(db_column='INVDTA_15')  # Field name made lowercase.
    invdta_16 = models.SmallIntegerField(db_column='INVDTA_16')  # Field name made lowercase.
    invdta_17 = models.SmallIntegerField(db_column='INVDTA_17')  # Field name made lowercase.
    invdta_18 = models.SmallIntegerField(db_column='INVDTA_18')  # Field name made lowercase.
    invdta_19 = models.SmallIntegerField(db_column='INVDTA_19')  # Field name made lowercase.
    invdta_20 = models.SmallIntegerField(db_column='INVDTA_20')  # Field name made lowercase.
    invdta_21 = models.SmallIntegerField(db_column='INVDTA_21')  # Field name made lowercase.
    invdta_22 = models.SmallIntegerField(db_column='INVDTA_22')  # Field name made lowercase.
    invdta_23 = models.SmallIntegerField(db_column='INVDTA_23')  # Field name made lowercase.
    invdta_24 = models.SmallIntegerField(db_column='INVDTA_24')  # Field name made lowercase.
    invdta_25 = models.SmallIntegerField(db_column='INVDTA_25')  # Field name made lowercase.
    invdta_26 = models.SmallIntegerField(db_column='INVDTA_26')  # Field name made lowercase.
    invdta_27 = models.SmallIntegerField(db_column='INVDTA_27')  # Field name made lowercase.
    invdta_28 = models.SmallIntegerField(db_column='INVDTA_28')  # Field name made lowercase.
    invdta_29 = models.SmallIntegerField(db_column='INVDTA_29')  # Field name made lowercase.
    amtcod_0 = models.SmallIntegerField(db_column='AMTCOD_0')  # Field name made lowercase.
    amtcod_1 = models.SmallIntegerField(db_column='AMTCOD_1')  # Field name made lowercase.
    amtcod_2 = models.SmallIntegerField(db_column='AMTCOD_2')  # Field name made lowercase.
    amtcod_3 = models.SmallIntegerField(db_column='AMTCOD_3')  # Field name made lowercase.
    amtcod_4 = models.SmallIntegerField(db_column='AMTCOD_4')  # Field name made lowercase.
    amtcod_5 = models.SmallIntegerField(db_column='AMTCOD_5')  # Field name made lowercase.
    amtcod_6 = models.SmallIntegerField(db_column='AMTCOD_6')  # Field name made lowercase.
    amtcod_7 = models.SmallIntegerField(db_column='AMTCOD_7')  # Field name made lowercase.
    amtcod_8 = models.SmallIntegerField(db_column='AMTCOD_8')  # Field name made lowercase.
    amtcod_9 = models.SmallIntegerField(db_column='AMTCOD_9')  # Field name made lowercase.
    amtcod_10 = models.SmallIntegerField(db_column='AMTCOD_10')  # Field name made lowercase.
    amtcod_11 = models.SmallIntegerField(db_column='AMTCOD_11')  # Field name made lowercase.
    amtcod_12 = models.SmallIntegerField(db_column='AMTCOD_12')  # Field name made lowercase.
    amtcod_13 = models.SmallIntegerField(db_column='AMTCOD_13')  # Field name made lowercase.
    amtcod_14 = models.SmallIntegerField(db_column='AMTCOD_14')  # Field name made lowercase.
    amtcod_15 = models.SmallIntegerField(db_column='AMTCOD_15')  # Field name made lowercase.
    amtcod_16 = models.SmallIntegerField(db_column='AMTCOD_16')  # Field name made lowercase.
    amtcod_17 = models.SmallIntegerField(db_column='AMTCOD_17')  # Field name made lowercase.
    amtcod_18 = models.SmallIntegerField(db_column='AMTCOD_18')  # Field name made lowercase.
    amtcod_19 = models.SmallIntegerField(db_column='AMTCOD_19')  # Field name made lowercase.
    amtcod_20 = models.SmallIntegerField(db_column='AMTCOD_20')  # Field name made lowercase.
    amtcod_21 = models.SmallIntegerField(db_column='AMTCOD_21')  # Field name made lowercase.
    amtcod_22 = models.SmallIntegerField(db_column='AMTCOD_22')  # Field name made lowercase.
    amtcod_23 = models.SmallIntegerField(db_column='AMTCOD_23')  # Field name made lowercase.
    amtcod_24 = models.SmallIntegerField(db_column='AMTCOD_24')  # Field name made lowercase.
    amtcod_25 = models.SmallIntegerField(db_column='AMTCOD_25')  # Field name made lowercase.
    amtcod_26 = models.SmallIntegerField(db_column='AMTCOD_26')  # Field name made lowercase.
    amtcod_27 = models.SmallIntegerField(db_column='AMTCOD_27')  # Field name made lowercase.
    amtcod_28 = models.SmallIntegerField(db_column='AMTCOD_28')  # Field name made lowercase.
    amtcod_29 = models.SmallIntegerField(db_column='AMTCOD_29')  # Field name made lowercase.
    plistc_0 = models.CharField(db_column='PLISTC_0', max_length=10)  # Field name made lowercase.
    payban_0 = models.CharField(db_column='PAYBAN_0', max_length=5)  # Field name made lowercase.
    acccod_0 = models.CharField(db_column='ACCCOD_0', max_length=10)  # Field name made lowercase.
    die_0 = models.CharField(db_column='DIE_0', max_length=3)  # Field name made lowercase.
    die_1 = models.CharField(db_column='DIE_1', max_length=3)  # Field name made lowercase.
    die_2 = models.CharField(db_column='DIE_2', max_length=3)  # Field name made lowercase.
    die_3 = models.CharField(db_column='DIE_3', max_length=3)  # Field name made lowercase.
    die_4 = models.CharField(db_column='DIE_4', max_length=3)  # Field name made lowercase.
    die_5 = models.CharField(db_column='DIE_5', max_length=3)  # Field name made lowercase.
    die_6 = models.CharField(db_column='DIE_6', max_length=3)  # Field name made lowercase.
    die_7 = models.CharField(db_column='DIE_7', max_length=3)  # Field name made lowercase.
    die_8 = models.CharField(db_column='DIE_8', max_length=3)  # Field name made lowercase.
    die_9 = models.CharField(db_column='DIE_9', max_length=3)  # Field name made lowercase.
    die_10 = models.CharField(db_column='DIE_10', max_length=3)  # Field name made lowercase.
    die_11 = models.CharField(db_column='DIE_11', max_length=3)  # Field name made lowercase.
    die_12 = models.CharField(db_column='DIE_12', max_length=3)  # Field name made lowercase.
    die_13 = models.CharField(db_column='DIE_13', max_length=3)  # Field name made lowercase.
    die_14 = models.CharField(db_column='DIE_14', max_length=3)  # Field name made lowercase.
    die_15 = models.CharField(db_column='DIE_15', max_length=3)  # Field name made lowercase.
    die_16 = models.CharField(db_column='DIE_16', max_length=3)  # Field name made lowercase.
    die_17 = models.CharField(db_column='DIE_17', max_length=3)  # Field name made lowercase.
    die_18 = models.CharField(db_column='DIE_18', max_length=3)  # Field name made lowercase.
    die_19 = models.CharField(db_column='DIE_19', max_length=3)  # Field name made lowercase.
    cce_0 = models.CharField(db_column='CCE_0', max_length=15)  # Field name made lowercase.
    cce_1 = models.CharField(db_column='CCE_1', max_length=15)  # Field name made lowercase.
    cce_2 = models.CharField(db_column='CCE_2', max_length=15)  # Field name made lowercase.
    cce_3 = models.CharField(db_column='CCE_3', max_length=15)  # Field name made lowercase.
    cce_4 = models.CharField(db_column='CCE_4', max_length=15)  # Field name made lowercase.
    cce_5 = models.CharField(db_column='CCE_5', max_length=15)  # Field name made lowercase.
    cce_6 = models.CharField(db_column='CCE_6', max_length=15)  # Field name made lowercase.
    cce_7 = models.CharField(db_column='CCE_7', max_length=15)  # Field name made lowercase.
    cce_8 = models.CharField(db_column='CCE_8', max_length=15)  # Field name made lowercase.
    cce_9 = models.CharField(db_column='CCE_9', max_length=15)  # Field name made lowercase.
    cce_10 = models.CharField(db_column='CCE_10', max_length=15)  # Field name made lowercase.
    cce_11 = models.CharField(db_column='CCE_11', max_length=15)  # Field name made lowercase.
    cce_12 = models.CharField(db_column='CCE_12', max_length=15)  # Field name made lowercase.
    cce_13 = models.CharField(db_column='CCE_13', max_length=15)  # Field name made lowercase.
    cce_14 = models.CharField(db_column='CCE_14', max_length=15)  # Field name made lowercase.
    cce_15 = models.CharField(db_column='CCE_15', max_length=15)  # Field name made lowercase.
    cce_16 = models.CharField(db_column='CCE_16', max_length=15)  # Field name made lowercase.
    cce_17 = models.CharField(db_column='CCE_17', max_length=15)  # Field name made lowercase.
    cce_18 = models.CharField(db_column='CCE_18', max_length=15)  # Field name made lowercase.
    cce_19 = models.CharField(db_column='CCE_19', max_length=15)  # Field name made lowercase.
    bpaadd_0 = models.CharField(db_column='BPAADD_0', max_length=5)  # Field name made lowercase.
    sevlin_0 = models.SmallIntegerField(db_column='SEVLIN_0')  # Field name made lowercase.
    ordtex_0 = models.CharField(db_column='ORDTEX_0', max_length=17)  # Field name made lowercase.
    rtntex_0 = models.CharField(db_column='RTNTEX_0', max_length=17)  # Field name made lowercase.
    ltimrkcoe_0 = models.DecimalField(db_column='LTIMRKCOE_0', max_digits=18, decimal_places=7)  # Field name made lowercase.
    primrkcoe_0 = models.DecimalField(db_column='PRIMRKCOE_0', max_digits=18, decimal_places=7)  # Field name made lowercase.
    qlymrkcoe_0 = models.DecimalField(db_column='QLYMRKCOE_0', max_digits=18, decimal_places=7)  # Field name made lowercase.
    qtymrkcoe_0 = models.DecimalField(db_column='QTYMRKCOE_0', max_digits=18, decimal_places=7)  # Field name made lowercase.
    rskmrkcoe_0 = models.DecimalField(db_column='RSKMRKCOE_0', max_digits=18, decimal_places=7)  # Field name made lowercase.
    ltimrk_0 = models.DecimalField(db_column='LTIMRK_0', max_digits=7, decimal_places=3)  # Field name made lowercase.
    primrk_0 = models.DecimalField(db_column='PRIMRK_0', max_digits=7, decimal_places=3)  # Field name made lowercase.
    qlymrk_0 = models.DecimalField(db_column='QLYMRK_0', max_digits=7, decimal_places=3)  # Field name made lowercase.
    qtymrk_0 = models.DecimalField(db_column='QTYMRK_0', max_digits=7, decimal_places=3)  # Field name made lowercase.
    rskmrk_0 = models.DecimalField(db_column='RSKMRK_0', max_digits=7, decimal_places=3)  # Field name made lowercase.
    genmrk_0 = models.DecimalField(db_column='GENMRK_0', max_digits=8, decimal_places=3)  # Field name made lowercase.
    ordminamt_0 = models.DecimalField(db_column='ORDMINAMT_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    ostctl_0 = models.SmallIntegerField(db_column='OSTCTL_0')  # Field name made lowercase.
    ostauzamt_0 = models.DecimalField(db_column='OSTAUZAMT_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    eecincrat_0 = models.DecimalField(db_column='EECINCRAT_0', max_digits=8, decimal_places=3)  # Field name made lowercase.
    bpsrem_0 = models.CharField(db_column='BPSREM_0', max_length=250)  # Field name made lowercase.
    dudclc_0 = models.SmallIntegerField(db_column='DUDCLC_0')  # Field name made lowercase.
    curclc_0 = models.SmallIntegerField(db_column='CURCLC_0')  # Field name made lowercase.
    fupflg_0 = models.SmallIntegerField(db_column='FUPFLG_0')  # Field name made lowercase.
    ocnflg_0 = models.SmallIntegerField(db_column='OCNFLG_0')  # Field name made lowercase.
    dadflg_0 = models.SmallIntegerField(db_column='DADFLG_0')  # Field name made lowercase.
    prvnum_0 = models.CharField(db_column='PRVNUM_0', max_length=1)  # Field name made lowercase.
    douflg_0 = models.SmallIntegerField(db_column='DOUFLG_0')  # Field name made lowercase.
    enaflg_0 = models.SmallIntegerField(db_column='ENAFLG_0')  # Field name made lowercase.
    paylokflg_0 = models.SmallIntegerField(db_column='PAYLOKFLG_0')  # Field name made lowercase.
    norprnflg_0 = models.SmallIntegerField(db_column='NORPRNFLG_0')  # Field name made lowercase.
    nreprnflg_0 = models.SmallIntegerField(db_column='NREPRNFLG_0')  # Field name made lowercase.
    nrtprnflg_0 = models.SmallIntegerField(db_column='NRTPRNFLG_0')  # Field name made lowercase.
    ritcod_0 = models.CharField(db_column='RITCOD_0', max_length=1)  # Field name made lowercase.
    ritnbr_0 = models.SmallIntegerField(db_column='RITNBR_0')  # Field name made lowercase.
    ritrat_0 = models.DecimalField(db_column='RITRAT_0', max_digits=28, decimal_places=8)  # Field name made lowercase.
    ritparnbr_0 = models.SmallIntegerField(db_column='RITPARNBR_0')  # Field name made lowercase.
    ritparnam_0 = models.CharField(db_column='RITPARNAM_0', max_length=1)  # Field name made lowercase.
    ritparcoe_0 = models.DecimalField(db_column='RITPARCOE_0', max_digits=28, decimal_places=8)  # Field name made lowercase.
    cai_0 = models.CharField(db_column='CAI_0', max_length=1)  # Field name made lowercase.
    datvlycai_0 = models.DateTimeField(db_column='DATVLYCAI_0')  # Field name made lowercase.
    agtpcp_0 = models.SmallIntegerField(db_column='AGTPCP_0')  # Field name made lowercase.
    agtsattax_0 = models.SmallIntegerField(db_column='AGTSATTAX_0')  # Field name made lowercase.
    sattax_0 = models.CharField(db_column='SATTAX_0', max_length=1)  # Field name made lowercase.
    flgsattax_0 = models.SmallIntegerField(db_column='FLGSATTAX_0')  # Field name made lowercase.
    bpcnum_0 = models.CharField(db_column='BPCNUM_0', max_length=1)  # Field name made lowercase.
    tpmcod_0 = models.CharField(db_column='TPMCOD_0', max_length=5)  # Field name made lowercase.
    dia_0 = models.CharField(db_column='DIA_0', max_length=10)  # Field name made lowercase.
    iptexs_0 = models.CharField(db_column='IPTEXS_0', max_length=20)  # Field name made lowercase.
    expnum_0 = models.IntegerField(db_column='EXPNUM_0')  # Field name made lowercase.
    creusr_0 = models.CharField(db_column='CREUSR_0', max_length=5)  # Field name made lowercase.
    credat_0 = models.DateTimeField(db_column='CREDAT_0')  # Field name made lowercase.
    updusr_0 = models.CharField(db_column='UPDUSR_0', max_length=5)  # Field name made lowercase.
    upddat_0 = models.DateTimeField(db_column='UPDDAT_0')  # Field name made lowercase.
    mattol_0 = models.CharField(db_column='MATTOL_0', max_length=5)  # Field name made lowercase.
    frm1099_0 = models.SmallIntegerField(db_column='FRM1099_0')  # Field name made lowercase.
    box1099_0 = models.CharField(db_column='BOX1099_0', max_length=1)  # Field name made lowercase.
    credattim_0 = models.DateTimeField(db_column='CREDATTIM_0')  # Field name made lowercase.
    upddattim_0 = models.DateTimeField(db_column='UPDDATTIM_0')  # Field name made lowercase.
    auuid_0 = models.TextField(db_column='AUUID_0')  # Field name made lowercase. This field type is a guess.
    flg281_0 = models.SmallIntegerField(db_column='FLG281_0')  # Field name made lowercase.
    purprityp_0 = models.SmallIntegerField(db_column='PURPRITYP_0')  # Field name made lowercase.
    cshvat_0 = models.SmallIntegerField(db_column='CSHVAT_0')  # Field name made lowercase.
    cshdat_0 = models.DateTimeField(db_column='CSHDAT_0')  # Field name made lowercase.
    autinvcod_0 = models.CharField(db_column='AUTINVCOD_0', max_length=5)  # Field name made lowercase.
    ordfrefrt_0 = models.DecimalField(db_column='ORDFREFRT_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    bprdsp_0 = models.CharField(db_column='BPRDSP_0', max_length=10)  # Field name made lowercase.
    rexnum_0 = models.CharField(db_column='REXNUM_0', max_length=30)  # Field name made lowercase.
    wlflg_0 = models.SmallIntegerField(db_column='WLFLG_0')  # Field name made lowercase.
    zeditor_0 = models.SmallIntegerField(db_column='ZEDITOR_0')  # Field name made lowercase.
    invorimod_0 = models.SmallIntegerField(db_column='INVORIMOD_0')  # Field name made lowercase.
    zarrlqd_0 = models.DateTimeField(db_column='ZARRLQD_0')  # Field name made lowercase.
    rowid = models.AutoField(db_column='ROWID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPSUPPLIER'


class Bpcustomer(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')  # Field name made lowercase.
    bpcnum_0 = models.CharField(db_column='BPCNUM_0', unique=True, max_length=15)  # Field name made lowercase.
    bpcnam_0 = models.CharField(db_column='BPCNAM_0', max_length=35)  # Field name made lowercase.
    bpcsho_0 = models.CharField(db_column='BPCSHO_0', max_length=10)  # Field name made lowercase.
    bcgcod_0 = models.CharField(db_column='BCGCOD_0', max_length=5)  # Field name made lowercase.
    grp_0 = models.CharField(db_column='GRP_0', max_length=5)  # Field name made lowercase.
    bpctyp_0 = models.SmallIntegerField(db_column='BPCTYP_0')  # Field name made lowercase.
    bpcinv_0 = models.CharField(db_column='BPCINV_0', max_length=15)  # Field name made lowercase.
    bpainv_0 = models.CharField(db_column='BPAINV_0', max_length=5)  # Field name made lowercase.
    bpcpyr_0 = models.CharField(db_column='BPCPYR_0', max_length=15)  # Field name made lowercase.
    bpapyr_0 = models.CharField(db_column='BPAPYR_0', max_length=5)  # Field name made lowercase.
    bpcgru_0 = models.CharField(db_column='BPCGRU_0', max_length=15)  # Field name made lowercase.
    bpcrsk_0 = models.CharField(db_column='BPCRSK_0', max_length=15)  # Field name made lowercase.
    bpaadd_0 = models.CharField(db_column='BPAADD_0', max_length=5)  # Field name made lowercase.
    bpdadd_0 = models.CharField(db_column='BPDADD_0', max_length=5)  # Field name made lowercase.
    cntnam_0 = models.CharField(db_column='CNTNAM_0', max_length=35)  # Field name made lowercase.
    bpcsta_0 = models.SmallIntegerField(db_column='BPCSTA_0')  # Field name made lowercase.
    pptflg_0 = models.SmallIntegerField(db_column='PPTFLG_0')  # Field name made lowercase.
    bpcbpsnum_0 = models.CharField(db_column='BPCBPSNUM_0', max_length=15)  # Field name made lowercase.
    fctnum_0 = models.CharField(db_column='FCTNUM_0', max_length=15)  # Field name made lowercase.
    cur_0 = models.CharField(db_column='CUR_0', max_length=3)  # Field name made lowercase.
    chgtyp_0 = models.SmallIntegerField(db_column='CHGTYP_0')  # Field name made lowercase.
    comcat_0 = models.SmallIntegerField(db_column='COMCAT_0')  # Field name made lowercase.
    rep_0 = models.CharField(db_column='REP_0', max_length=15)  # Field name made lowercase.
    rep_1 = models.CharField(db_column='REP_1', max_length=15)  # Field name made lowercase.
    vacbpr_0 = models.CharField(db_column='VACBPR_0', max_length=5)  # Field name made lowercase.
    vatexn_0 = models.CharField(db_column='VATEXN_0', max_length=15)  # Field name made lowercase.
    pte_0 = models.CharField(db_column='PTE_0', max_length=15)  # Field name made lowercase.
    freinv_0 = models.SmallIntegerField(db_column='FREINV_0')  # Field name made lowercase.
    dep_0 = models.CharField(db_column='DEP_0', max_length=5)  # Field name made lowercase.
    invdtaamt_0 = models.DecimalField(db_column='INVDTAAMT_0', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_1 = models.DecimalField(db_column='INVDTAAMT_1', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_2 = models.DecimalField(db_column='INVDTAAMT_2', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_3 = models.DecimalField(db_column='INVDTAAMT_3', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_4 = models.DecimalField(db_column='INVDTAAMT_4', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_5 = models.DecimalField(db_column='INVDTAAMT_5', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_6 = models.DecimalField(db_column='INVDTAAMT_6', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_7 = models.DecimalField(db_column='INVDTAAMT_7', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_8 = models.DecimalField(db_column='INVDTAAMT_8', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_9 = models.DecimalField(db_column='INVDTAAMT_9', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_10 = models.DecimalField(db_column='INVDTAAMT_10', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_11 = models.DecimalField(db_column='INVDTAAMT_11', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_12 = models.DecimalField(db_column='INVDTAAMT_12', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_13 = models.DecimalField(db_column='INVDTAAMT_13', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_14 = models.DecimalField(db_column='INVDTAAMT_14', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_15 = models.DecimalField(db_column='INVDTAAMT_15', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_16 = models.DecimalField(db_column='INVDTAAMT_16', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_17 = models.DecimalField(db_column='INVDTAAMT_17', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_18 = models.DecimalField(db_column='INVDTAAMT_18', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_19 = models.DecimalField(db_column='INVDTAAMT_19', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_20 = models.DecimalField(db_column='INVDTAAMT_20', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_21 = models.DecimalField(db_column='INVDTAAMT_21', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_22 = models.DecimalField(db_column='INVDTAAMT_22', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_23 = models.DecimalField(db_column='INVDTAAMT_23', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_24 = models.DecimalField(db_column='INVDTAAMT_24', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_25 = models.DecimalField(db_column='INVDTAAMT_25', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_26 = models.DecimalField(db_column='INVDTAAMT_26', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_27 = models.DecimalField(db_column='INVDTAAMT_27', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_28 = models.DecimalField(db_column='INVDTAAMT_28', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_29 = models.DecimalField(db_column='INVDTAAMT_29', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdta_0 = models.SmallIntegerField(db_column='INVDTA_0')  # Field name made lowercase.
    invdta_1 = models.SmallIntegerField(db_column='INVDTA_1')  # Field name made lowercase.
    invdta_2 = models.SmallIntegerField(db_column='INVDTA_2')  # Field name made lowercase.
    invdta_3 = models.SmallIntegerField(db_column='INVDTA_3')  # Field name made lowercase.
    invdta_4 = models.SmallIntegerField(db_column='INVDTA_4')  # Field name made lowercase.
    invdta_5 = models.SmallIntegerField(db_column='INVDTA_5')  # Field name made lowercase.
    invdta_6 = models.SmallIntegerField(db_column='INVDTA_6')  # Field name made lowercase.
    invdta_7 = models.SmallIntegerField(db_column='INVDTA_7')  # Field name made lowercase.
    invdta_8 = models.SmallIntegerField(db_column='INVDTA_8')  # Field name made lowercase.
    invdta_9 = models.SmallIntegerField(db_column='INVDTA_9')  # Field name made lowercase.
    invdta_10 = models.SmallIntegerField(db_column='INVDTA_10')  # Field name made lowercase.
    invdta_11 = models.SmallIntegerField(db_column='INVDTA_11')  # Field name made lowercase.
    invdta_12 = models.SmallIntegerField(db_column='INVDTA_12')  # Field name made lowercase.
    invdta_13 = models.SmallIntegerField(db_column='INVDTA_13')  # Field name made lowercase.
    invdta_14 = models.SmallIntegerField(db_column='INVDTA_14')  # Field name made lowercase.
    invdta_15 = models.SmallIntegerField(db_column='INVDTA_15')  # Field name made lowercase.
    invdta_16 = models.SmallIntegerField(db_column='INVDTA_16')  # Field name made lowercase.
    invdta_17 = models.SmallIntegerField(db_column='INVDTA_17')  # Field name made lowercase.
    invdta_18 = models.SmallIntegerField(db_column='INVDTA_18')  # Field name made lowercase.
    invdta_19 = models.SmallIntegerField(db_column='INVDTA_19')  # Field name made lowercase.
    invdta_20 = models.SmallIntegerField(db_column='INVDTA_20')  # Field name made lowercase.
    invdta_21 = models.SmallIntegerField(db_column='INVDTA_21')  # Field name made lowercase.
    invdta_22 = models.SmallIntegerField(db_column='INVDTA_22')  # Field name made lowercase.
    invdta_23 = models.SmallIntegerField(db_column='INVDTA_23')  # Field name made lowercase.
    invdta_24 = models.SmallIntegerField(db_column='INVDTA_24')  # Field name made lowercase.
    invdta_25 = models.SmallIntegerField(db_column='INVDTA_25')  # Field name made lowercase.
    invdta_26 = models.SmallIntegerField(db_column='INVDTA_26')  # Field name made lowercase.
    invdta_27 = models.SmallIntegerField(db_column='INVDTA_27')  # Field name made lowercase.
    invdta_28 = models.SmallIntegerField(db_column='INVDTA_28')  # Field name made lowercase.
    invdta_29 = models.SmallIntegerField(db_column='INVDTA_29')  # Field name made lowercase.
    tsccod_0 = models.CharField(db_column='TSCCOD_0', max_length=20)  # Field name made lowercase.
    tsccod_1 = models.CharField(db_column='TSCCOD_1', max_length=20)  # Field name made lowercase.
    tsccod_2 = models.CharField(db_column='TSCCOD_2', max_length=20)  # Field name made lowercase.
    tsccod_3 = models.CharField(db_column='TSCCOD_3', max_length=20)  # Field name made lowercase.
    tsccod_4 = models.CharField(db_column='TSCCOD_4', max_length=20)  # Field name made lowercase.
    prityp_0 = models.SmallIntegerField(db_column='PRITYP_0')  # Field name made lowercase.
    bpcrem_0 = models.CharField(db_column='BPCREM_0', max_length=250)  # Field name made lowercase.
    ostctl_0 = models.SmallIntegerField(db_column='OSTCTL_0')  # Field name made lowercase.
    ostauz_0 = models.DecimalField(db_column='OSTAUZ_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    ordminamt_0 = models.DecimalField(db_column='ORDMINAMT_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    cdtisr_0 = models.DecimalField(db_column='CDTISR_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    cdtisrdat_0 = models.DateTimeField(db_column='CDTISRDAT_0')  # Field name made lowercase.
    bpccdtisr_0 = models.CharField(db_column='BPCCDTISR_0', max_length=15)  # Field name made lowercase.
    fuptyp_0 = models.SmallIntegerField(db_column='FUPTYP_0')  # Field name made lowercase.
    fupminamt_0 = models.DecimalField(db_column='FUPMINAMT_0', max_digits=27, decimal_places=13)  # Field name made lowercase.
    soiper_0 = models.SmallIntegerField(db_column='SOIPER_0')  # Field name made lowercase.
    payban_0 = models.CharField(db_column='PAYBAN_0', max_length=5)  # Field name made lowercase.
    acccod_0 = models.CharField(db_column='ACCCOD_0', max_length=10)  # Field name made lowercase.
    die_0 = models.CharField(db_column='DIE_0', max_length=3)  # Field name made lowercase.
    die_1 = models.CharField(db_column='DIE_1', max_length=3)  # Field name made lowercase.
    die_2 = models.CharField(db_column='DIE_2', max_length=3)  # Field name made lowercase.
    die_3 = models.CharField(db_column='DIE_3', max_length=3)  # Field name made lowercase.
    die_4 = models.CharField(db_column='DIE_4', max_length=3)  # Field name made lowercase.
    die_5 = models.CharField(db_column='DIE_5', max_length=3)  # Field name made lowercase.
    die_6 = models.CharField(db_column='DIE_6', max_length=3)  # Field name made lowercase.
    die_7 = models.CharField(db_column='DIE_7', max_length=3)  # Field name made lowercase.
    die_8 = models.CharField(db_column='DIE_8', max_length=3)  # Field name made lowercase.
    die_9 = models.CharField(db_column='DIE_9', max_length=3)  # Field name made lowercase.
    die_10 = models.CharField(db_column='DIE_10', max_length=3)  # Field name made lowercase.
    die_11 = models.CharField(db_column='DIE_11', max_length=3)  # Field name made lowercase.
    die_12 = models.CharField(db_column='DIE_12', max_length=3)  # Field name made lowercase.
    die_13 = models.CharField(db_column='DIE_13', max_length=3)  # Field name made lowercase.
    die_14 = models.CharField(db_column='DIE_14', max_length=3)  # Field name made lowercase.
    die_15 = models.CharField(db_column='DIE_15', max_length=3)  # Field name made lowercase.
    die_16 = models.CharField(db_column='DIE_16', max_length=3)  # Field name made lowercase.
    die_17 = models.CharField(db_column='DIE_17', max_length=3)  # Field name made lowercase.
    die_18 = models.CharField(db_column='DIE_18', max_length=3)  # Field name made lowercase.
    die_19 = models.CharField(db_column='DIE_19', max_length=3)  # Field name made lowercase.
    cce_0 = models.CharField(db_column='CCE_0', max_length=15)  # Field name made lowercase.
    cce_1 = models.CharField(db_column='CCE_1', max_length=15)  # Field name made lowercase.
    cce_2 = models.CharField(db_column='CCE_2', max_length=15)  # Field name made lowercase.
    cce_3 = models.CharField(db_column='CCE_3', max_length=15)  # Field name made lowercase.
    cce_4 = models.CharField(db_column='CCE_4', max_length=15)  # Field name made lowercase.
    cce_5 = models.CharField(db_column='CCE_5', max_length=15)  # Field name made lowercase.
    cce_6 = models.CharField(db_column='CCE_6', max_length=15)  # Field name made lowercase.
    cce_7 = models.CharField(db_column='CCE_7', max_length=15)  # Field name made lowercase.
    cce_8 = models.CharField(db_column='CCE_8', max_length=15)  # Field name made lowercase.
    cce_9 = models.CharField(db_column='CCE_9', max_length=15)  # Field name made lowercase.
    cce_10 = models.CharField(db_column='CCE_10', max_length=15)  # Field name made lowercase.
    cce_11 = models.CharField(db_column='CCE_11', max_length=15)  # Field name made lowercase.
    cce_12 = models.CharField(db_column='CCE_12', max_length=15)  # Field name made lowercase.
    cce_13 = models.CharField(db_column='CCE_13', max_length=15)  # Field name made lowercase.
    cce_14 = models.CharField(db_column='CCE_14', max_length=15)  # Field name made lowercase.
    cce_15 = models.CharField(db_column='CCE_15', max_length=15)  # Field name made lowercase.
    cce_16 = models.CharField(db_column='CCE_16', max_length=15)  # Field name made lowercase.
    cce_17 = models.CharField(db_column='CCE_17', max_length=15)  # Field name made lowercase.
    cce_18 = models.CharField(db_column='CCE_18', max_length=15)  # Field name made lowercase.
    cce_19 = models.CharField(db_column='CCE_19', max_length=15)  # Field name made lowercase.
    mtcflg_0 = models.SmallIntegerField(db_column='MTCFLG_0')  # Field name made lowercase.
    ordtex_0 = models.CharField(db_column='ORDTEX_0', max_length=17)  # Field name made lowercase.
    invtex_0 = models.CharField(db_column='INVTEX_0', max_length=17)  # Field name made lowercase.
    lndauz_0 = models.SmallIntegerField(db_column='LNDAUZ_0')  # Field name made lowercase.
    ocnflg_0 = models.SmallIntegerField(db_column='OCNFLG_0')  # Field name made lowercase.
    invper_0 = models.SmallIntegerField(db_column='INVPER_0')  # Field name made lowercase.
    dudclc_0 = models.SmallIntegerField(db_column='DUDCLC_0')  # Field name made lowercase.
    ordcle_0 = models.SmallIntegerField(db_column='ORDCLE_0')  # Field name made lowercase.
    odl_0 = models.SmallIntegerField(db_column='ODL_0')  # Field name made lowercase.
    dme_0 = models.SmallIntegerField(db_column='DME_0')  # Field name made lowercase.
    ime_0 = models.SmallIntegerField(db_column='IME_0')  # Field name made lowercase.
    bus_0 = models.CharField(db_column='BUS_0', max_length=20)  # Field name made lowercase.
    orippt_0 = models.CharField(db_column='ORIPPT_0', max_length=20)  # Field name made lowercase.
    pitcdt_0 = models.IntegerField(db_column='PITCDT_0')  # Field name made lowercase.
    pitcpt_0 = models.IntegerField(db_column='PITCPT_0')  # Field name made lowercase.
    totpit_0 = models.IntegerField(db_column='TOTPIT_0')  # Field name made lowercase.
    cotchx_0 = models.CharField(db_column='COTCHX_0', max_length=20)  # Field name made lowercase.
    cotpitrqd_0 = models.IntegerField(db_column='COTPITRQD_0')  # Field name made lowercase.
    cntfirdat_0 = models.DateTimeField(db_column='CNTFIRDAT_0')  # Field name made lowercase.
    ordfirdat_0 = models.DateTimeField(db_column='ORDFIRDAT_0')  # Field name made lowercase.
    quolasdat_0 = models.DateTimeField(db_column='QUOLASDAT_0')  # Field name made lowercase.
    cntlasdat_0 = models.DateTimeField(db_column='CNTLASDAT_0')  # Field name made lowercase.
    cntnexdat_0 = models.DateTimeField(db_column='CNTNEXDAT_0')  # Field name made lowercase.
    cntlastyp_0 = models.SmallIntegerField(db_column='CNTLASTYP_0')  # Field name made lowercase.
    cntnextyp_0 = models.SmallIntegerField(db_column='CNTNEXTYP_0')  # Field name made lowercase.
    abccls_0 = models.SmallIntegerField(db_column='ABCCLS_0')  # Field name made lowercase.
    agtpcp_0 = models.SmallIntegerField(db_column='AGTPCP_0')  # Field name made lowercase.
    agtsattax_0 = models.SmallIntegerField(db_column='AGTSATTAX_0')  # Field name made lowercase.
    sattax_0 = models.CharField(db_column='SATTAX_0', max_length=1)  # Field name made lowercase.
    flgsattax_0 = models.SmallIntegerField(db_column='FLGSATTAX_0')  # Field name made lowercase.
    tpmcod_0 = models.CharField(db_column='TPMCOD_0', max_length=5)  # Field name made lowercase.
    dia_0 = models.CharField(db_column='DIA_0', max_length=10)  # Field name made lowercase.
    bpcsncdat_0 = models.DateTimeField(db_column='BPCSNCDAT_0')  # Field name made lowercase.
    expnum_0 = models.IntegerField(db_column='EXPNUM_0')  # Field name made lowercase.
    creusr_0 = models.CharField(db_column='CREUSR_0', max_length=5)  # Field name made lowercase.
    credat_0 = models.DateTimeField(db_column='CREDAT_0')  # Field name made lowercase.
    updusr_0 = models.CharField(db_column='UPDUSR_0', max_length=5)  # Field name made lowercase.
    upddat_0 = models.DateTimeField(db_column='UPDDAT_0')  # Field name made lowercase.
    credattim_0 = models.DateTimeField(db_column='CREDATTIM_0')  # Field name made lowercase.
    upddattim_0 = models.DateTimeField(db_column='UPDDATTIM_0')  # Field name made lowercase.
    auuid_0 = models.TextField(db_column='AUUID_0')  # Field name made lowercase. This field type is a guess.
    daymon_0 = models.SmallIntegerField(db_column='DAYMON_0')  # Field name made lowercase.
    daymon_1 = models.SmallIntegerField(db_column='DAYMON_1')  # Field name made lowercase.
    daymon_2 = models.SmallIntegerField(db_column='DAYMON_2')  # Field name made lowercase.
    daymon_3 = models.SmallIntegerField(db_column='DAYMON_3')  # Field name made lowercase.
    daymon_4 = models.SmallIntegerField(db_column='DAYMON_4')  # Field name made lowercase.
    daymon_5 = models.SmallIntegerField(db_column='DAYMON_5')  # Field name made lowercase.
    uvycod2_0 = models.CharField(db_column='UVYCOD2_0', max_length=5)  # Field name made lowercase.
    cshvatrgm_0 = models.SmallIntegerField(db_column='CSHVATRGM_0')  # Field name made lowercase.
    cshvatrgm_1 = models.SmallIntegerField(db_column='CSHVATRGM_1')  # Field name made lowercase.
    cshvatrgm_2 = models.SmallIntegerField(db_column='CSHVATRGM_2')  # Field name made lowercase.
    cshvatrgm_3 = models.SmallIntegerField(db_column='CSHVATRGM_3')  # Field name made lowercase.
    cshvatrgm_4 = models.SmallIntegerField(db_column='CSHVATRGM_4')  # Field name made lowercase.
    cshvatrgm_5 = models.SmallIntegerField(db_column='CSHVATRGM_5')  # Field name made lowercase.
    cshvatrgm_6 = models.SmallIntegerField(db_column='CSHVATRGM_6')  # Field name made lowercase.
    cshvatrgm_7 = models.SmallIntegerField(db_column='CSHVATRGM_7')  # Field name made lowercase.
    cshvatrgm_8 = models.SmallIntegerField(db_column='CSHVATRGM_8')  # Field name made lowercase.
    vatstrdat_0 = models.DateTimeField(db_column='VATSTRDAT_0')  # Field name made lowercase.
    vatstrdat_1 = models.DateTimeField(db_column='VATSTRDAT_1')  # Field name made lowercase.
    vatstrdat_2 = models.DateTimeField(db_column='VATSTRDAT_2')  # Field name made lowercase.
    vatstrdat_3 = models.DateTimeField(db_column='VATSTRDAT_3')  # Field name made lowercase.
    vatstrdat_4 = models.DateTimeField(db_column='VATSTRDAT_4')  # Field name made lowercase.
    vatstrdat_5 = models.DateTimeField(db_column='VATSTRDAT_5')  # Field name made lowercase.
    vatstrdat_6 = models.DateTimeField(db_column='VATSTRDAT_6')  # Field name made lowercase.
    vatstrdat_7 = models.DateTimeField(db_column='VATSTRDAT_7')  # Field name made lowercase.
    vatstrdat_8 = models.DateTimeField(db_column='VATSTRDAT_8')  # Field name made lowercase.
    vatenddat_0 = models.DateTimeField(db_column='VATENDDAT_0')  # Field name made lowercase.
    vatenddat_1 = models.DateTimeField(db_column='VATENDDAT_1')  # Field name made lowercase.
    vatenddat_2 = models.DateTimeField(db_column='VATENDDAT_2')  # Field name made lowercase.
    vatenddat_3 = models.DateTimeField(db_column='VATENDDAT_3')  # Field name made lowercase.
    vatenddat_4 = models.DateTimeField(db_column='VATENDDAT_4')  # Field name made lowercase.
    vatenddat_5 = models.DateTimeField(db_column='VATENDDAT_5')  # Field name made lowercase.
    vatenddat_6 = models.DateTimeField(db_column='VATENDDAT_6')  # Field name made lowercase.
    vatenddat_7 = models.DateTimeField(db_column='VATENDDAT_7')  # Field name made lowercase.
    vatenddat_8 = models.DateTimeField(db_column='VATENDDAT_8')  # Field name made lowercase.
    belvatsub_0 = models.SmallIntegerField(db_column='BELVATSUB_0')  # Field name made lowercase.
    invcnd_0 = models.CharField(db_column='INVCND_0', max_length=20)  # Field name made lowercase.
    electinv_0 = models.SmallIntegerField(db_column='ELECTINV_0')  # Field name made lowercase.
    cntefat_0 = models.CharField(db_column='CNTEFAT_0', max_length=15)  # Field name made lowercase.
    strdatefat_0 = models.DateTimeField(db_column='STRDATEFAT_0')  # Field name made lowercase.
    aeiflg_0 = models.SmallIntegerField(db_column='AEIFLG_0')  # Field name made lowercase.
    zeditor_0 = models.SmallIntegerField(db_column='ZEDITOR_0')  # Field name made lowercase.
    zagente_0 = models.SmallIntegerField(db_column='ZAGENTE_0')  # Field name made lowercase.
    zintvsp_0 = models.SmallIntegerField(db_column='ZINTVSP_0')  # Field name made lowercase.
    zdiscrgval_0 = models.DecimalField(db_column='ZDISCRGVAL_0', max_digits=10, decimal_places=3)  # Field name made lowercase.
    zexpflg_0 = models.SmallIntegerField(db_column='ZEXPFLG_0')  # Field name made lowercase.
    zcrynam_0 = models.CharField(db_column='ZCRYNAM_0', max_length=40)  # Field name made lowercase.
    rowid = models.AutoField(db_column='ROWID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCUSTOMER'
        unique_together = (('zcrynam_0', 'bpcnam_0', 'bpcnum_0'),)
