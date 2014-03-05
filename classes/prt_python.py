#!/usr/bin/python
# -*- coding: utf-8 -*-

# definitions from C

DEBUG = 0
VCHECK = 1.e6
LDEN_MIN = 1e-3
RMIN = 1.e9
RMAX = 3.e10
VWIND = 2.e8
MDOT = 1.e-9 * MSOL / YR
TSTAR = 30000.
BETA = 1.0
KAPPA_CONT = 4.
EPSILON = 1.e-6
NSTAT = 10
VMAX = 1.e9
TAU_MAX = 20.
DANG_LIVE_OR_DIE = 2.0
NWAVE = 10000
MAXSCAT = 50
SPHERICAL = 0
CYLIND = 1
RTHETA = 2
CYLVAR = 3
SPECTYPE_BB = -1
SPECTYPE_UNIFORM = -2
SPECTYPE_POW = -4
SPECTYPE_CL_TAB = -5
SPECTYPE_NONE = -3
NCOMPS = 10
LINELENGTH = 160
NXBANDS = 20
NRINGS = 301
NBLMODEL = 100
NIONIZ = 5
LPDF = 3
W_PART_INTORUS = 3
W_ALL_INTORUS = 2
W_PART_INWIND = 1
W_ALL_INWIND = 0
W_NOT_INWIND = -1
W_IGNORE = -2
PTYPE_STAR = 0
PTYPE_BL = 1
PTYPE_DISK = 2
PTYPE_WIND = 3
PTYPE_AGN = 4
SPEC_MOD_PL = 1
SPEC_MOD_EXP = 2
NSTORE = 10
PTYPE_STAR = 0
PTYPE_BL = 1
PTYPE_DISK = 2
PTYPE_WIND = 3
PTYPE_AGN = 4
P_INWIND = 0
P_SCAT = 1
P_ESCAPE = 2
P_HIT_STAR = 3
P_HIT_DISK = 7
P_ABSORB = 6
P_TOO_MANY_SCATTERS = 4
P_ERROR = 5
P_SEC = 8
P_ADIABATIC = 9
TMAX_FACTOR = 1.5
TMIN = 2000.
TMAX = 5e8
SAHA = 4.82907e15
MAXITERATIONS = 200
FRACTIONAL_ERROR = 0.03
THETAMAX = 1e4
MIN_TEMP = 100.
NDIM_MAX = 500
MAX_PHOT_HIST = 1000
MSPEC = 6
NPDF = 200
NBANDS = 20
NTEMPS = 60
NFB = 10
NCSTAT = 10


# structures from C as py classes

class geometry:

    def __init__(
        self,
        wcycle,
        pcycle,
        wcycles,
        pcycles,
        coord_type,
        ndim,
        mdim,
        nplasma,
        nmacro,
        rmax,
        rmax_sq,
        mstar,
        rstar,
        rstar_sq,
        tstar,
        gstar,
        twind,
        tmax,
        system_type,
        disk_type,
        disk_illum,
        disk_tprofile,
        disk_mdot,
        diskrad,
        diskrad_sq,
        disk_z0,
        disk_z1,
        wind_type,
        log_linear,
        xlog_scale,
        zlog_scale,
        star_radiation,
        disk_radiation,
        bl_radiation,
        wind_radiation,
        agn_radiation,
        matom_radiation,
        ioniz_mode,
        macro_ioniz_mode,
        ioniz_or_extract,
        macro_simple,
        partition_mode,
        line_mode,
        scatter_mode,
        rt_mode,
        nxfreq,
        xfreq,
        star_ion_spectype,
        star_spectype,
        disk_ion_spectype,
        disk_spectype,
        bl_ion_spectype,
        bl_spectype,
        agn_ion_spectype,
        agn_spectype,
        model_list,
        wind_mdot,
        stellar_wind_mdot,
        wind_rmin,
        wind_rmax,
        wind_rho_min,
        wind_rho_max,
        wind_thetamin,
        wind_thetamax,
        mdot_norm,
        adiabatic,
        auger_ionization,
        sv_lambda,
        sv_rmin,
        sv_rmax,
        sv_thetamin,
        sv_thetamax,
        sv_gamma,
        sv_v_zero,
        sv_r_scale,
        sv_alpha,
        sv_v_infinity,
        elvis_offset,
        kn_dratio,
        kn_lambda,
        kn_r_scale,
        kn_alpha,
        kn_v_infinity,
        kn_v_zero,
        cl_v_zero,
        cl_v_infinity,
        cl_beta,
        cl_rmin,
        cl_rmax,
        shell_vmin,
        shell_vmax,
        shell_beta,
        shell_rmin,
        shell_rmax,
        corona_rmin,
        corona_rmax,
        corona_base_density,
        corona_scale_height,
        corona_vel_frac,
        pl_vol,
        pl_vmax,
        pl_t_r,
        pl_t_e,
        pl_w,
        pl_nh,
        lum_tot,
        lum_star,
        lum_disk,
        lum_bl,
        lum_wind,
        lum_agn,
        agn_cltab_low,
        agn_cltab_hi,
        agn_cltab_low_alpha,
        agn_cltab_hi_alpha,
        lum_ff,
        lum_fb,
        lum_lines,
        lum_comp,
        lum_dr,
        lum_adiabatic,
        heat_adiabatic,
        f_tot,
        f_star,
        f_disk,
        f_bl,
        f_agn,
        f_wind,
        lum_ff_ioniz,
        lum_fb_ioniz,
        lum_lines_ioniz,
        lum_comp_ioniz,
        lum_dr_ioniz,
        lum_adiabatic_ioniz,
        lum_wind_ioniz,
        lum_star_ioniz,
        lum_disk_ioniz,
        lum_bl_ioniz,
        lum_tot_ioniz,
        f_matom,
        f_kpkt,
        m_sec,
        q,
        period,
        a,
        l1,
        l2,
        phi,
        l1_from_m2,
        r2_far,
        r2_width,
        t_bl,
        weight,
        alpha_agn,
        const_agn,
        r_agn,
        d_agn,
        compton_torus,
        compton_torus_rmin,
        compton_torus_rmax,
        compton_torus_zheight,
        compton_torus_tau,
        compton_torus_te,
        n_ioniz,
        lum_ioniz,
        atomic_filename,
        fixed_con_file,
        ):
        self.wcycle = wcycle  # type int
        self.pcycle = pcycle  # type int
        self.wcycles = wcycles  # type int
        self.pcycles = pcycles  # type int
        self.coord_type = coord_type  # type int
        self.ndim = ndim  # type int
        self.mdim = mdim  # type int
        self.nplasma = nplasma  # type int
        self.nmacro = nmacro  # type int
        self.rmax = rmax  # type double
        self.rmax_sq = rmax_sq  # type double
        self.mstar = mstar  # type double
        self.rstar = rstar  # type double
        self.rstar_sq = rstar_sq  # type double
        self.tstar = tstar  # type double
        self.gstar = gstar  # type double
        self.twind = twind  # type double
        self.tmax = tmax  # type double
        self.system_type = system_type  # type int
        self.disk_type = disk_type  # type int
        self.disk_illum = disk_illum  # type int
        self.disk_tprofile = disk_tprofile  # type int
        self.disk_mdot = disk_mdot  # type double
        self.diskrad = diskrad  # type double
        self.diskrad_sq = diskrad_sq  # type double
        self.disk_z0 = disk_z0  # type double
        self.disk_z1 = disk_z1  # type double
        self.wind_type = wind_type  # type int
        self.log_linear = log_linear  # type int
        self.xlog_scale = xlog_scale  # type double
        self.zlog_scale = zlog_scale  # type double
        self.star_radiation = star_radiation  # type int
        self.disk_radiation = disk_radiation  # type int
        self.bl_radiation = bl_radiation  # type int
        self.wind_radiation = wind_radiation  # type int
        self.agn_radiation = agn_radiation  # type int
        self.matom_radiation = matom_radiation  # type int
        self.ioniz_mode = ioniz_mode  # type int
        self.macro_ioniz_mode = macro_ioniz_mode  # type int
        self.ioniz_or_extract = ioniz_or_extract  # type int
        self.macro_simple = macro_simple  # type int
        self.partition_mode = partition_mode  # type int
        self.line_mode = line_mode  # type int
        self.scatter_mode = scatter_mode  # type int
        self.rt_mode = rt_mode  # type int
        self.nxfreq = nxfreq  # type int
        self.xfreq = xfreq  # type double
        self.star_ion_spectype = star_ion_spectype  # type int
        self.star_spectype = star_spectype  # type int
        self.disk_ion_spectype = disk_ion_spectype  # type int
        self.disk_spectype = disk_spectype  # type int
        self.bl_ion_spectype = bl_ion_spectype  # type int
        self.bl_spectype = bl_spectype  # type int
        self.agn_ion_spectype = agn_ion_spectype  # type int
        self.agn_spectype = agn_spectype  # type int
        self.model_list = model_list  # type char
        self.wind_mdot = wind_mdot  # type double
        self.stellar_wind_mdot = stellar_wind_mdot  # type double
        self.wind_rmin = wind_rmin  # type double
        self.wind_rmax = wind_rmax  # type double
        self.wind_rho_min = wind_rho_min  # type double
        self.wind_rho_max = wind_rho_max  # type double
        self.wind_thetamin = wind_thetamin  # type double
        self.wind_thetamax = wind_thetamax  # type double
        self.mdot_norm = mdot_norm  # type double
        self.adiabatic = adiabatic  # type int
        self.auger_ionization = auger_ionization  # type int
        self.sv_lambda = sv_lambda  # type double
        self.sv_rmin = sv_rmin  # type double
        self.sv_rmax = sv_rmax  # type double
        self.sv_thetamin = sv_thetamin  # type double
        self.sv_thetamax = sv_thetamax  # type double
        self.sv_gamma = sv_gamma  # type double
        self.sv_v_zero = sv_v_zero  # type double
        self.sv_r_scale = sv_r_scale  # type double
        self.sv_alpha = sv_alpha  # type double
        self.sv_v_infinity = sv_v_infinity  # type double
        self.elvis_offset = elvis_offset  # type double
        self.kn_dratio = kn_dratio  # type double
        self.kn_lambda = kn_lambda  # type double
        self.kn_r_scale = kn_r_scale  # type double
        self.kn_alpha = kn_alpha  # type double
        self.kn_v_infinity = kn_v_infinity  # type double
        self.kn_v_zero = kn_v_zero  # type double
        self.cl_v_zero = cl_v_zero  # type double
        self.cl_v_infinity = cl_v_infinity  # type double
        self.cl_beta = cl_beta  # type double
        self.cl_rmin = cl_rmin  # type double
        self.cl_rmax = cl_rmax  # type double
        self.shell_vmin = shell_vmin  # type double
        self.shell_vmax = shell_vmax  # type double
        self.shell_beta = shell_beta  # type double
        self.shell_rmin = shell_rmin  # type double
        self.shell_rmax = shell_rmax  # type double
        self.corona_rmin = corona_rmin  # type double
        self.corona_rmax = corona_rmax  # type double
        self.corona_base_density = corona_base_density  # type double
        self.corona_scale_height = corona_scale_height  # type double
        self.corona_vel_frac = corona_vel_frac  # type double
        self.pl_vol = pl_vol  # type double
        self.pl_vmax = pl_vmax  # type double
        self.pl_t_r = pl_t_r  # type double
        self.pl_t_e = pl_t_e  # type double
        self.pl_w = pl_w  # type double
        self.pl_nh = pl_nh  # type double
        self.lum_tot = lum_tot  # type double
        self.lum_star = lum_star  # type double
        self.lum_disk = lum_disk  # type double
        self.lum_bl = lum_bl  # type double
        self.lum_wind = lum_wind  # type double
        self.lum_agn = lum_agn  # type double
        self.agn_cltab_low = agn_cltab_low  # type double
        self.agn_cltab_hi = agn_cltab_hi  # type double
        self.agn_cltab_low_alpha = agn_cltab_low_alpha  # type double
        self.agn_cltab_hi_alpha = agn_cltab_hi_alpha  # type double
        self.lum_ff = lum_ff  # type double
        self.lum_fb = lum_fb  # type double
        self.lum_lines = lum_lines  # type double
        self.lum_comp = lum_comp  # type double
        self.lum_dr = lum_dr  # type double
        self.lum_adiabatic = lum_adiabatic  # type double
        self.heat_adiabatic = heat_adiabatic  # type double
        self.f_tot = f_tot  # type double
        self.f_star = f_star  # type double
        self.f_disk = f_disk  # type double
        self.f_bl = f_bl  # type double
        self.f_agn = f_agn  # type double
        self.f_wind = f_wind  # type double
        self.lum_ff_ioniz = lum_ff_ioniz  # type double
        self.lum_fb_ioniz = lum_fb_ioniz  # type double
        self.lum_lines_ioniz = lum_lines_ioniz  # type double
        self.lum_comp_ioniz = lum_comp_ioniz  # type double
        self.lum_dr_ioniz = lum_dr_ioniz  # type double
        self.lum_adiabatic_ioniz = lum_adiabatic_ioniz  # type double
        self.lum_wind_ioniz = lum_wind_ioniz  # type double
        self.lum_star_ioniz = lum_star_ioniz  # type double
        self.lum_disk_ioniz = lum_disk_ioniz  # type double
        self.lum_bl_ioniz = lum_bl_ioniz  # type double
        self.lum_tot_ioniz = lum_tot_ioniz  # type double
        self.f_matom = f_matom  # type double
        self.f_kpkt = f_kpkt  # type double
        self.m_sec = m_sec  # type double
        self.q = q  # type double
        self.period = period  # type double
        self.a = a  # type double
        self.l1 = l1  # type double
        self.l2 = l2  # type double
        self.phi = phi  # type double
        self.l1_from_m2 = l1_from_m2  # type double
        self.r2_far = r2_far  # type double
        self.r2_width = r2_width  # type double
        self.t_bl = t_bl  # type double
        self.weight = weight  # type double
        self.alpha_agn = alpha_agn  # type double
        self.const_agn = const_agn  # type double
        self.r_agn = r_agn  # type double
        self.d_agn = d_agn  # type double
        self.compton_torus = compton_torus  # type int
        self.compton_torus_rmin = compton_torus_rmin  # type double
        self.compton_torus_rmax = compton_torus_rmax  # type double
        self.compton_torus_zheight = compton_torus_zheight  # type double
        self.compton_torus_tau = compton_torus_tau  # type double
        self.compton_torus_te = compton_torus_te  # type double
        self.n_ioniz = n_ioniz  # type double
        self.lum_ioniz = lum_ioniz  # type double
        self.atomic_filename = atomic_filename  # type char
        self.fixed_con_file = fixed_con_file  # type char


class plane:

    def __init__(self, x, lmn):
        self.x = x  # type double
        self.lmn = lmn  # type double


class cone:

    def __init__(self, z, dzdr):
        self.z = z  # type double
        self.dzdr = dzdr  # type double


class xdisk:

    def __init__(
        self,
        r,
        t,
        g,
        v,
        heat,
        ave_freq,
        w,
        t_hit,
        nphot,
        nhit,
        ):
        self.r = r  # type double
        self.t = t  # type double
        self.g = g  # type double
        self.v = v  # type double
        self.heat = heat  # type double
        self.ave_freq = ave_freq  # type double
        self.w = w  # type double
        self.t_hit = t_hit  # type double
        self.nphot = nphot  # type int
        self.nhit = nhit  # type int


class blmodel:

    def __init__(
        self,
        n_blpts,
        r,
        t,
        ):
        self.n_blpts = n_blpts  # type int
        self.r = r  # type float
        self.t = t  # type float


class wind:

    def __init__(
        self,
        nwind,
        nplasma,
        x,
        xcen,
        r,
        rcen,
        theta,
        thetacen,
        v,
        v_grad,
        div_v,
        dvds_ave,
        dvds_max,
        lmn,
        vol,
        inwind,
        ):
        self.nwind = nwind  # type int
        self.nplasma = nplasma  # type int
        self.x = x  # type double
        self.xcen = xcen  # type double
        self.r = r  # type double
        self.rcen = rcen  # type double
        self.theta = theta  # type double
        self.thetacen = thetacen  # type double
        self.v = v  # type double
        self.v_grad = v_grad  # type double
        self.div_v = div_v  # type double
        self.dvds_ave = dvds_ave  # type double
        self.dvds_max = dvds_max  # type double
        self.lmn = lmn  # type double
        self.vol = vol  # type double
        self.inwind = inwind  # type int


class plasma:

    def __init__(
        self,
        nwind,
        nplasma,
        ne,
        rho,
        vol,
        density,
        partition,
        levden,
        PWdenom,
        PWdtemp,
        PWnumer,
        PWntemp,
        kappa_ff_factor,
        nscat_es,
        nscat_res,
        recomb_simple,
        kpkt_emiss,
        kpkt_abs,
        kbf_use,
        kbf_nuse,
        t_r,
        t_r_old,
        t_e,
        t_e_old,
        dt_e,
        dt_e_old,
        heat_tot,
        heat_tot_old,
        heat_lines,
        heat_ff,
        heat_comp,
        heat_ind_comp,
        heat_lines_macro,
        heat_photo_macro,
        heat_photo,
        heat_z,
        w,
        ntot,
        ntot_star,
        ntot_bl,
        ntot_disk,
        ntot_wind,
        ntot_agn,
        mean_ds,
        n_ds,
        nrad,
        nioniz,
        ioniz,
        recomb,
        scatters,
        xscatters,
        heat_ion,
        lum_ion,
        j,
        ave_freq,
        lum,
        xj,
        xave_freq,
        fmin,
        fmax,
        fmin_mod,
        fmax_mod,
        j_direct,
        j_scatt,
        ip_direct,
        ip_scatt,
        xsd_freq,
        nxtot,
        max_freq,
        lum_lines,
        lum_ff,
        lum_adiabatic,
        lum_comp,
        lum_dr,
        lum_fb,
        lum_z,
        lum_rad,
        lum_rad_old,
        lum_ioniz,
        lum_lines_ioniz,
        lum_ff_ioniz,
        lum_adiabatic_ioniz,
        lum_comp_ioniz,
        lum_dr_ioniz,
        lum_fb_ioniz,
        lum_z_ioniz,
        lum_rad_ioniz,
        dmo_dt,
        npdf,
        pdf_x,
        pdf_y,
        gain,
        converge_t_r,
        converge_t_e,
        converge_hc,
        trcheck,
        techeck,
        hccheck,
        converge_whole,
        converging,
        gamma_inshl,
        spec_mod_type,
        pl_alpha,
        pl_log_w,
        exp_temp,
        exp_w,
        sim_ip,
        ferland_ip,
        ip,
        ):
        self.nwind = nwind  # type int
        self.nplasma = nplasma  # type int
        self.ne = ne  # type double
        self.rho = rho  # type double
        self.vol = vol  # type double
        self.density = density  # type double
        self.partition = partition  # type double
        self.levden = levden  # type double
        self.PWdenom = PWdenom  # type double
        self.PWdtemp = PWdtemp  # type double
        self.PWnumer = PWnumer  # type double
        self.PWntemp = PWntemp  # type double
        self.kappa_ff_factor = kappa_ff_factor  # type double
        self.nscat_es = nscat_es  # type int
        self.nscat_res = nscat_res  # type int
        self.recomb_simple = recomb_simple  # type double
        self.kpkt_emiss = kpkt_emiss  # type double
        self.kpkt_abs = kpkt_abs  # type double
        self.kbf_use = kbf_use  # type int
        self.kbf_nuse = kbf_nuse  # type int
        self.t_r = t_r  # type double
        self.t_r_old = t_r_old  # type double
        self.t_e = t_e  # type double
        self.t_e_old = t_e_old  # type double
        self.dt_e = dt_e  # type double
        self.dt_e_old = dt_e_old  # type double
        self.heat_tot = heat_tot  # type double
        self.heat_tot_old = heat_tot_old  # type double
        self.heat_lines = heat_lines  # type double
        self.heat_ff = heat_ff  # type double
        self.heat_comp = heat_comp  # type double
        self.heat_ind_comp = heat_ind_comp  # type double
        self.heat_lines_macro = heat_lines_macro  # type double
        self.heat_photo_macro = heat_photo_macro  # type double
        self.heat_photo = heat_photo  # type double
        self.heat_z = heat_z  # type double
        self.w = w  # type double
        self.ntot = ntot  # type int
        self.ntot_star = ntot_star  # type int
        self.ntot_bl = ntot_bl  # type int
        self.ntot_disk = ntot_disk  # type int
        self.ntot_wind = ntot_wind  # type int
        self.ntot_agn = ntot_agn  # type int
        self.mean_ds = mean_ds  # type double
        self.n_ds = n_ds  # type int
        self.nrad = nrad  # type int
        self.nioniz = nioniz  # type int
        self.ioniz = ioniz  # type double
        self.recomb = recomb  # type double
        self.scatters = scatters  # type int
        self.xscatters = xscatters  # type double
        self.heat_ion = heat_ion  # type double
        self.lum_ion = lum_ion  # type double
        self.j = j  # type double
        self.ave_freq = ave_freq  # type double
        self.lum = lum  # type double
        self.xj = xj  # type double
        self.xave_freq = xave_freq  # type double
        self.fmin = fmin  # type double
        self.fmax = fmax  # type double
        self.fmin_mod = fmin_mod  # type double
        self.fmax_mod = fmax_mod  # type double
        self.j_direct = j_direct  # type double
        self.j_scatt = j_scatt  # type double
        self.ip_direct = ip_direct  # type double
        self.ip_scatt = ip_scatt  # type double
        self.xsd_freq = xsd_freq  # type double
        self.nxtot = nxtot  # type int
        self.max_freq = max_freq  # type double
        self.lum_lines = lum_lines  # type double
        self.lum_ff = lum_ff  # type double
        self.lum_adiabatic = lum_adiabatic  # type double
        self.lum_comp = lum_comp  # type double
        self.lum_dr = lum_dr  # type double
        self.lum_fb = lum_fb  # type double
        self.lum_z = lum_z  # type double
        self.lum_rad = lum_rad  # type double
        self.lum_rad_old = lum_rad_old  # type double
        self.lum_ioniz = lum_ioniz  # type double
        self.lum_lines_ioniz = lum_lines_ioniz  # type double
        self.lum_ff_ioniz = lum_ff_ioniz  # type double
        self.lum_adiabatic_ioniz = lum_adiabatic_ioniz  # type double
        self.lum_comp_ioniz = lum_comp_ioniz  # type double
        self.lum_dr_ioniz = lum_dr_ioniz  # type double
        self.lum_fb_ioniz = lum_fb_ioniz  # type double
        self.lum_z_ioniz = lum_z_ioniz  # type double
        self.lum_rad_ioniz = lum_rad_ioniz  # type double
        self.dmo_dt = dmo_dt  # type double
        self.npdf = npdf  # type int
        self.pdf_x = pdf_x  # type int
        self.pdf_y = pdf_y  # type double
        self.gain = gain  # type double
        self.converge_t_r = converge_t_r  # type double
        self.converge_t_e = converge_t_e  # type double
        self.converge_hc = converge_hc  # type double
        self.trcheck = trcheck  # type int
        self.techeck = techeck  # type int
        self.hccheck = hccheck  # type int
        self.converge_whole = converge_whole  # type int
        self.converging = converging  # type int
        self.gamma_inshl = gamma_inshl  # type double
        self.spec_mod_type = spec_mod_type  # type int
        self.pl_alpha = pl_alpha  # type double
        self.pl_log_w = pl_log_w  # type double
        self.exp_temp = exp_temp  # type double
        self.exp_w = exp_w  # type double
        self.sim_ip = sim_ip  # type double
        self.ferland_ip = ferland_ip  # type double
        self.ip = ip  # type double


class photon_store:

    def __init__(
        self,
        n,
        t,
        f1,
        f2,
        freq,
        ):
        self.n = n  # type int
        self.t = t  # type double
        self.f1 = f1  # type double
        self.f2 = f2  # type double
        self.freq = freq  # type double


class macro:

    def __init__(
        self,
        jbar,
        jbar_old,
        gamma,
        gamma_old,
        gamma_e,
        gamma_e_old,
        alpha_st,
        alpha_st_old,
        alpha_st_e,
        alpha_st_e_old,
        recomb_sp,
        recomb_sp_e,
        matom_emiss,
        matom_abs,
        kpkt_rates_known,
        cooling_bf,
        cooling_bf_col,
        cooling_bb,
        cooling_normalisation,
        cooling_bbtot,
        cooling_bftot,
        cooling_bf_coltot,
        cooling_ff,
        cooling_adiabatic,
        ):
        self.jbar = jbar  # type pointer, double
        self.jbar_old = jbar_old  # type pointer, double
        self.gamma = gamma  # type pointer, double
        self.gamma_old = gamma_old  # type pointer, double
        self.gamma_e = gamma_e  # type pointer, double
        self.gamma_e_old = gamma_e_old  # type pointer, double
        self.alpha_st = alpha_st  # type pointer, double
        self.alpha_st_old = alpha_st_old  # type pointer, double
        self.alpha_st_e = alpha_st_e  # type pointer, double
        self.alpha_st_e_old = alpha_st_e_old  # type pointer, double
        self.recomb_sp = recomb_sp  # type pointer, double
        self.recomb_sp_e = recomb_sp_e  # type pointer, double
        self.matom_emiss = matom_emiss  # type pointer, double
        self.matom_abs = matom_abs  # type pointer, double
        self.kpkt_rates_known = kpkt_rates_known  # type int
        self.cooling_bf = cooling_bf  # type pointer, double
        self.cooling_bf_col = cooling_bf_col  # type pointer, double
        self.cooling_bb = cooling_bb  # type pointer, double
        self.cooling_normalisation = cooling_normalisation  # type double
        self.cooling_bbtot = cooling_bbtot  # type double
        self.cooling_bftot = cooling_bftot  # type double
        self.cooling_bf_coltot = cooling_bf_coltot  # type double
        self.cooling_ff = cooling_ff  # type double
        self.cooling_adiabatic = cooling_adiabatic  # type double


class photon:

    def __init__(
        self,
        x,
        lmn,
        freq,
        w,
        tau,
        istat,
        nscat,
        nres,
        nnscat,
        nrscat,
        grid,
        origin,
        np,
        ):
        self.x = x  # type double
        self.lmn = lmn  # type double
        self.freq = freq  # type double
        self.w = w  # type double
        self.tau = tau  # type double
        self.istat = istat  # type int
        self.nscat = nscat  # type int
        self.nres = nres  # type int
        self.nnscat = nnscat  # type int
        self.nrscat = nrscat  # type int
        self.grid = grid  # type int
        self.origin = origin  # type int
        self.np = np  # type int


class basis:

    def __init__(self, a):
        self.a = a  # type double


class spectrum:

    def __init__(
        self,
        name,
        freqmin,
        freqmax,
        dfreq,
        lfreqmin,
        lfreqmax,
        ldfreq,
        lmn,
        mmax,
        mmin,
        renorm,
        nphot,
        nscat,
        top_bot,
        x,
        r,
        f,
        lf,
        lfreq,
        ):
        self.name = name  # type char
        self.freqmin = freqmin  # type float
        self.freqmax = freqmax  # type float
        self.dfreq = dfreq  # type float
        self.lfreqmin = lfreqmin  # type float
        self.lfreqmax = lfreqmax  # type float
        self.ldfreq = ldfreq  # type float
        self.lmn = lmn  # type double
        self.mmax = mmax  # type double
        self.mmin = mmin  # type double
        self.renorm = renorm  # type double
        self.nphot = nphot  # type int
        self.nscat = nscat  # type int
        self.top_bot = top_bot  # type int
        self.x = x  # type double
        self.r = r  # type double
        self.f = f  # type double
        self.lf = lf  # type double
        self.lfreq = lfreq  # type double


class Pdf:

    def __init__(
        self,
        x,
        y,
        d,
        limit1,
        limit2,
        x1,
        x2,
        norm,
        ):
        self.x = x  # type double
        self.y = y  # type double
        self.d = d  # type double
        self.limit1 = limit1  # type double
        self.limit2 = limit2  # type double
        self.x1 = x1  # type double
        self.x2 = x2  # type double
        self.norm = norm  # type double


class xbands:

    def __init__(
        self,
        f1,
        f2,
        alpha,
        pl_const,
        min_fraction,
        nat_fraction,
        used_fraction,
        flux,
        weight,
        nphot,
        nbands,
        ):
        self.f1 = f1  # type double
        self.f2 = f2  # type double
        self.alpha = alpha  # type double
        self.pl_const = pl_const  # type double
        self.min_fraction = min_fraction  # type double
        self.nat_fraction = nat_fraction  # type double
        self.used_fraction = used_fraction  # type double
        self.flux = flux  # type double
        self.weight = weight  # type double
        self.nphot = nphot  # type int
        self.nbands = nbands  # type int


class fbstruc:

    def __init__(
        self,
        f1,
        f2,
        emiss,
        ):
        self.f1 = f1  # type double
        self.f2 = f2  # type double
        self.emiss = emiss  # type double


class emiss_range:

    def __init__(self, fmin, fmax):
        self.fmin = fmin  # type double
        self.fmax = fmax  # type double


