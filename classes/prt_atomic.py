#!/usr/bin/python
# -*- coding: utf-8 -*-

# definitions from C

MAXRAND = 2147486748.
VERY_BIG = 1e50
TRUE = 1
FALSE = 0
H = 6.6262e-27
HC = 1.98587e-16
HEV = 4.13620e-15
HRYD = 3.04005e-16
C = 2.997925e10
G = 6.670e-8
BOLTZMANN = 1.38062e-16
WIEN = 5.879e10
H_OVER_K = 4.799437e-11
STEFAN_BOLTZMANN = 5.6696e-5
THOMPSON = 0.66524e-24
PI = 3.1415927
MELEC = 9.10956e-28
E = 4.8035e-10
MPROT = 1.672661e-24
MSOL = 1.989e33
PC = 3.08e18
YR = 3.1556925e7
PI_E2_OVER_MC = 0.02655103
PI_E2_OVER_M = 7.96e8
ALPHA = 7.297351e-3
BOHR = 0.529175e-8
CR = 3.288051e15
ANGSTROM = 1.e-8
EV2ERGS = 1.602192e-12
RADIAN = 57.29578
RYD2ERGS = 2.1798741e-11
DENSITY_MIN = 1.e-20
NELEMENTS = 50
NIONS = 500
NLEVELS = 12000
NLTE_LEVELS = 270
NLEVELS_MACRO = 150
NLINES = 200000
NBBJUMPS = 100
NBFJUMPS = 100
MAXJUMPS = 1000000
NAUGER = 2
NCROSS = 1500
NTOP_PHOT = 250
NTRANS = 200
MAX_DR_PARAMS = 9
DRTYPE_BADNELL = 0
DRTYPE_SHULL = 1
T_RR_PARAMS = 6
RRTYPE_BADNELL = 0
RRTYPE_SHULL = 1
BAD_GS_RR_PARAMS = 19
MAX_GAUNT_N_GSQRD = 100


# structures from C as py classes

class elements:

    def __init__(
        self,
        name,
        z,
        firstion,
        nions,
        abun,
        ):
        self.name = name  # type char
        self.z = z  # type int
        self.firstion = firstion  # type int
        self.nions = nions  # type int
        self.abun = abun  # type double


class ions:

    def __init__(
        self,
        z,
        istate,
        ip,
        g,
        nmax,
        n_lte_max,
        firstlevel,
        nlevels,
        first_nlte_level,
        first_levden,
        nlte,
        phot_info,
        macro_info,
        ntop_first,
        ntop_ground,
        ntop,
        nxphot,
        lev_type,
        drflag,
        nxdrecomb,
        cpartflag,
        nxcpart,
        total_rrflag,
        nxtotalrr,
        bad_gs_rr_t_flag,
        bad_gs_rr_r_flag,
        nxbadgsrr,
        ):
        self.z = z  # type int
        self.istate = istate  # type int
        self.ip = ip  # type double
        self.g = g  # type double
        self.nmax = nmax  # type int
        self.n_lte_max = n_lte_max  # type int
        self.firstlevel = firstlevel  # type int
        self.nlevels = nlevels  # type int
        self.first_nlte_level = first_nlte_level  # type int
        self.first_levden = first_levden  # type int
        self.nlte = nlte  # type int
        self.phot_info = phot_info  # type int
        self.macro_info = macro_info  # type int
        self.ntop_first = ntop_first  # type int
        self.ntop_ground = ntop_ground  # type int
        self.ntop = ntop  # type int
        self.nxphot = nxphot  # type int
        self.lev_type = lev_type  # type int
        self.drflag = drflag  # type int
        self.nxdrecomb = nxdrecomb  # type int
        self.cpartflag = cpartflag  # type int
        self.nxcpart = nxcpart  # type int
        self.total_rrflag = total_rrflag  # type int
        self.nxtotalrr = nxtotalrr  # type int
        self.bad_gs_rr_t_flag = bad_gs_rr_t_flag  # type int
        self.bad_gs_rr_r_flag = bad_gs_rr_r_flag  # type int
        self.nxbadgsrr = nxbadgsrr  # type int


class configurations:

    def __init__(
        self,
        z,
        istate,
        nion,
        nden,
        isp,
        ilv,
        macro_info,
        n_bbu_jump,
        n_bbd_jump,
        n_bfu_jump,
        n_bfd_jump,
        g,
        q_num,
        ex,
        rad_rate,
        bbu_jump,
        bbd_jump,
        bfu_jump,
        bfd_jump,
        bbu_indx_first,
        bfu_indx_first,
        bfd_indx_first,
        ):
        self.z = z  # type int
        self.istate = istate  # type int
        self.nion = nion  # type int
        self.nden = nden  # type int
        self.isp = isp  # type int
        self.ilv = ilv  # type int
        self.macro_info = macro_info  # type int
        self.n_bbu_jump = n_bbu_jump  # type int
        self.n_bbd_jump = n_bbd_jump  # type int
        self.n_bfu_jump = n_bfu_jump  # type int
        self.n_bfd_jump = n_bfd_jump  # type int
        self.g = g  # type double
        self.q_num = q_num  # type double
        self.ex = ex  # type double
        self.rad_rate = rad_rate  # type double
        self.bbu_jump = bbu_jump  # type int
        self.bbd_jump = bbd_jump  # type int
        self.bfu_jump = bfu_jump  # type int
        self.bfd_jump = bfd_jump  # type int
        self.bbu_indx_first = bbu_indx_first  # type int
        self.bfu_indx_first = bfu_indx_first  # type int
        self.bfd_indx_first = bfd_indx_first  # type int


class lines:

    def __init__(
        self,
        nion,
        z,
        istate,
        gl,
        gu,
        nconfigl,
        nconfigu,
        levl,
        levu,
        macro_info,
        freq,
        f,
        el,
        eu,
        pow,
        where_in_list,
        down_index,
        up_index,
        ):
        self.nion = nion  # type int
        self.z = z  # type int
        self.istate = istate  # type int
        self.gl = gl  # type double
        self.gu = gu  # type double
        self.nconfigl = nconfigl  # type int
        self.nconfigu = nconfigu  # type int
        self.levl = levl  # type int
        self.levu = levu  # type int
        self.macro_info = macro_info  # type int
        self.freq = freq  # type double
        self.f = f  # type double
        self.el = el  # type double
        self.eu = eu  # type double
        self.pow = pow  # type double
        self.where_in_list = where_in_list  # type int
        self.down_index = down_index  # type int
        self.up_index = up_index  # type int


class photoionization:

    def __init__(
        self,
        nion,
        z,
        istate,
        freq_t,
        freq_max,
        freq0,
        sigma,
        ya,
        p,
        yw,
        y0,
        y1,
        f_last,
        sigma_last,
        ):
        self.nion = nion  # type int
        self.z = z  # type int
        self.istate = istate  # type int
        self.freq_t = freq_t  # type double
        self.freq_max = freq_max  # type double
        self.freq0 = freq0  # type double
        self.sigma = sigma  # type double
        self.ya = ya  # type double
        self.p = p  # type double
        self.yw = yw  # type double
        self.y0 = y0  # type double
        self.y1 = y1  # type double
        self.f_last = f_last  # type double
        self.sigma_last = sigma_last  # type double


class topbase_phot:

    def __init__(
        self,
        nlev,
        uplev,
        nion,
        z,
        istate,
        np,
        nlast,
        macro_info,
        down_index,
        up_index,
        freq,
        x,
        f,
        sigma,
        ):
        self.nlev = nlev  # type int
        self.uplev = uplev  # type int
        self.nion = nion  # type int
        self.z = z  # type int
        self.istate = istate  # type int
        self.np = np  # type int
        self.nlast = nlast  # type int
        self.macro_info = macro_info  # type int
        self.down_index = down_index  # type int
        self.up_index = up_index  # type int
        self.freq = freq  # type double
        self.x = x  # type double
        self.f = f  # type double
        self.sigma = sigma  # type double


class innershell:

    def __init__(
        self,
        nion,
        nion_target,
        z,
        istate,
        n,
        l,
        freq_t,
        Sigma,
        ya,
        P,
        yw,
        E_0,
        _yield,
        arad,
        etarad,
        adi,
        bdi,
        t0di,
        t1di,
        ):
        self.nion = nion  # type int
        self.nion_target = nion_target  # type int
        self.z = z  # type int
        self.istate = istate  # type int
        self.n = n  # type int
        self.l = l  # type int
        self.freq_t = freq_t  # type double
        self.Sigma = Sigma  # type double
        self.ya = ya  # type double
        self.P = P  # type double
        self.yw = yw  # type double
        self.E_0 = E_0  # type double
        self._yield = _yield  # type double
        self.arad = arad  # type double
        self.etarad = etarad  # type double
        self.adi = adi  # type double
        self.bdi = bdi  # type double
        self.t0di = t0di  # type double
        self.t1di = t1di  # type double


class ground_fracs:

    def __init__(
        self,
        z,
        istate,
        frac,
        ):
        self.z = z  # type int
        self.istate = istate  # type int
        self.frac = frac  # type double


class collision_strength:

    def __init__(
        self,
        nion,
        z,
        istate,
        freq,
        ex,
        alpha,
        beta,
        tm,
        pow,
        ):
        self.nion = nion  # type int
        self.z = z  # type int
        self.istate = istate  # type int
        self.freq = freq  # type double
        self.ex = ex  # type double
        self.alpha = alpha  # type double
        self.beta = beta  # type double
        self.tm = tm  # type double
        self.pow = pow  # type double


class dielectronic_recombination:

    def __init__(
        self,
        nion,
        nparam,
        c,
        e,
        shull,
        type,
        ):
        self.nion = nion  # type int
        self.nparam = nparam  # type int
        self.c = c  # type double
        self.e = e  # type double
        self.shull = shull  # type double
        self.type = type  # type int


class cardona_partition:

    def __init__(
        self,
        nion,
        part_eps,
        part_G,
        part_m,
        ):
        self.nion = nion  # type int
        self.part_eps = part_eps  # type double
        self.part_G = part_G  # type int
        self.part_m = part_m  # type int


class total_rr:

    def __init__(
        self,
        nion,
        params,
        type,
        ):
        self.nion = nion  # type int
        self.params = params  # type double
        self.type = type  # type int


class badnell_gs_rr:

    def __init__(
        self,
        nion,
        temps,
        rates,
        ):
        self.nion = nion  # type int
        self.temps = temps  # type double
        self.rates = rates  # type double


class gaunt_total:

    def __init__(
        self,
        log_gsqrd,
        gff,
        s1,
        s2,
        s3,
        ):
        self.log_gsqrd = log_gsqrd  # type float
        self.gff = gff  # type float
        self.s1 = s1  # type float
        self.s2 = s2  # type float
        self.s3 = s3  # type float


