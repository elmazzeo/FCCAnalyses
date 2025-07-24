import os 

#Input directory where the files produced at the pre-selection level are
inputDir= os.environ.get('ttH_yy_DIR') + '/ntuples/'

#Input directory where the files produced at the pre-selection level are
outputDir  = os.environ.get('ttH_yy_DIR') + '/final/'

processList = {
    #Signal
    #'mgp8_pp_tth01j_5f_haa':{}, #output file from analysis_stage1.py
    #'mgp8_pp_tth01j_5f_84TeV_haaexcl':{}, #output file from analysis_stage1.py
    #Backgrounds
    #'mgp8_pp_ttaa_semilep_5f_100TeV':{} #output file from analysis_stage1.py
    #'mgp8_pp_ttaa01j_5f_84TeV':{}, #output file from analysis_stage1.py
    #'mgp8_pp_Vaajj_HF_5f_84TeV' : {}, #output file from analysis_stage1.py
    # ttZ(ee) signal
    #"mgp8_pp_ttz01j_5f_84TeV_zee" : {'chunks': 100}, # ttZ->ee at 84 TeV
    # Backgrounds
    #"mgp8_pp_WZjj_HF_5f_84TeV_zeewlep" : {'chunks': 100}, # W(->lep)Z(->ee)+jets at 84 TeV
    #"mgp8_pp_ZZjj_HF_5f_84TeV_zzlep" : {'chunks': 100}, # Z(->lep)Z(->ee)+jets at 84 TeV
    #"mgp8_pp_tZj_5f_84TeV_zeewlep" : {'chunks': 100}, # t(->lep)Z(->ee)+jets at 84 TeV
    #"mgp8_pp_tWZj_5f_84TeV_zee" : {'chunks': 100}, # tWZ(->ee)+jets at 84 TeV
    # Q-binned pT ttH(yy) signal
    "mgp8_pp_tth_5f_Q_0_1000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
    "mgp8_pp_tth_5f_Q_1000_3000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
    "mgp8_pp_tth_5f_Q_3000_10000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
    "mgp8_pp_tth_5f_Q_10000_84000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
    # Q-binned ttyy background
    "mgp8_pp_ttaa_Q_0_500_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
    "mgp8_pp_ttaa_Q_500_1000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
    "mgp8_pp_ttaa_Q_1000_2000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
    "mgp8_pp_ttaa_Q_2000_5000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
    "mgp8_pp_ttaa_Q_5000_84000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
    # Q-binned V+yy+bb/cc background
###    "mgp8_pp_vaa_Q_0_500_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
###    "mgp8_pp_vaa_Q_500_1000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
###    "mgp8_pp_vaa_Q_1000_2000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
###    "mgp8_pp_vaa_Q_2000_5000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
###    "mgp8_pp_vaa_Q_5000_84000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
}

#Link to the dictionary that contains all the cross section informations etc...
procDict = "/eos/experiment/fcc/hh/utils/FCCDicts/FCChh_procDict_fcc_v07_II.json"
#Note the numbeOfEvents and sumOfWeights are placeholders that get overwritten with the correct values in the samples

#How to add a process that is not in the official dictionary:
# procDictAdd={"pwp8_pp_hh_5f_hhbbyy": {"numberOfEvents": 4980000, "sumOfWeights": 4980000.0, "crossSection": 0.0029844128399999998, "kfactor": 1.075363, "matchingEfficiency": 1.0}}

# Expected integrated luminosity
intLumi = 30e+06  # pb-1

# Whether to scale to expected integrated luminosity
doScale = True

#Number of CPUs to use
nCPUS = 8

#produces ROOT TTrees, default is False
doTree = True

saveTabular = True

# Optional: Use weighted events
do_weighted = True 

# Dictionary of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
           # cutflow
           "nocuts":                       "pT_y1 >= 0 || pT_y1 <=0", # all events
           "photons":                      "n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. ", # 2 photons with pT > 25 GeV
           "photons_rel_pt":               "n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25",
           "photons_myy_window":           "n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 && m_yy[0] > 110. && m_yy[0] <= 140.",
           "preselection":                 "n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 && m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1",
           "lep_channel":                  "n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 && m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           # pT(yy) bins
           "pT_yy_bin1": "pT_yy[0] >= 0. && pT_yy[0] < 60.      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin2": "pT_yy[0] >= 60. && pT_yy[0] < 120.    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)", 
           "pT_yy_bin3": "pT_yy[0] >= 120. && pT_yy[0] < 200.   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin4": "pT_yy[0] >= 200. && pT_yy[0] < 300.   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin5": "pT_yy[0] >= 300. && pT_yy[0] < 450.   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin6": "pT_yy[0] >= 450. && pT_yy[0] < 600.   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin7": "pT_yy[0] >= 600. && pT_yy[0] < 1000.  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin8": "pT_yy[0] >= 1000. && pT_yy[0] < 1500. && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin9": "pT_yy[0] >= 1500. && pT_yy[0] < 2000. && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
           "pT_yy_bin10": "pT_yy[0] >= 2000.                    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] > 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # truth bins for the signal
            # pT(H) < 60 GeV
            "TTH_CEN_PTH_0_60_pT_yy_bin1"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)         && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin2"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)       && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin3"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin4"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin5"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin6"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin7"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin8"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin9"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_0_60_pT_yy_bin10"   : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=0 && pT_higgs[0]<60)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 60 < pT(H) < 120 GeV
            "TTH_CEN_PTH_60_120_pT_yy_bin1"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 0. && pT_yy[0] < 60.)         && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin2"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 60. && pT_yy[0] < 120.)       && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin3"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 120. && pT_yy[0] < 200.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin4"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 200. && pT_yy[0] < 300.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin5"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 300. && pT_yy[0] < 450.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin6"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin7"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin8"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin9"  : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_60_120_pT_yy_bin10" : "(abs(rapidity_higgs[0])<4.0 &&  pT_higgs[0]>=60 && pT_higgs[0]<120) && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 120 < pT(H) < 200 GeV
            "TTH_CEN_PTH_120_200_pT_yy_bin1"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin2"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin3"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin4"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin5"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin6"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin7"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin8"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin9"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_120_200_pT_yy_bin10"   : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=120   && pT_higgs[0]<200)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 200 < pT(H) < 300 GeV
            "TTH_CEN_PTH_200_300_pT_yy_bin1"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)         && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin2"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)       && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin3"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin4"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin5"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin6"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin7"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin8"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin9"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_200_300_pT_yy_bin10"   : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=200  && pT_higgs[0]<300)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 300 < pT(H) < 450 GeV
            "TTH_CEN_PTH_300_450_pT_yy_bin1"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)         && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin2"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)       && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin3"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin4"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin5"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin6"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin7"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin8"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin9"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_300_450_pT_yy_bin10"   : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=300 && pT_higgs[0]<450)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 450 < pT(H) < 600 GeV
            "TTH_CEN_PTH_450_600_pT_yy_bin1"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin2"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin3"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin4"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin5"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin6"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin7"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin8"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin9"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_450_600_pT_yy_bin10"   : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=450 && pT_higgs[0]<600)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 600 < pT(H) < 1000 GeV
            "TTH_CEN_PTH_600_1000_pT_yy_bin1"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin2"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin3"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin4"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin5"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin6"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin7"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin8"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin9"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_600_1000_pT_yy_bin10"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=600 && pT_higgs[0]<1000)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 1000 < pT(H) < 1500 GeV
            "TTH_CEN_PTH_1000_1500_pT_yy_bin1"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin2"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin3"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin4"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin5"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin6"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin7"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin8"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin9"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1000_1500_pT_yy_bin10"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1000 && pT_higgs[0]<1500)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 1500 < pT(H) < 2000 GeV
            "TTH_CEN_PTH_1500_2000_pT_yy_bin1"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin2"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin3"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin4"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin5"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin6"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin7"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin8"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin9"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_1500_2000_pT_yy_bin10"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=1500 && pT_higgs[0]<2000)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # 1500 < pT(H) < 2000 GeV
            "TTH_CEN_PTH_2000_inf_pT_yy_bin1"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 0. && pT_yy[0] < 60.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin2"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 60. && pT_yy[0] < 120.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin3"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 120. && pT_yy[0] < 200.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin4"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 200. && pT_yy[0] < 300.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin5"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 300. && pT_yy[0] < 450.)  && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin6"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 450. && pT_yy[0] < 600.  )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin7"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 600. && pT_yy[0] < 1000. )    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin8"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin9"     : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_CEN_PTH_2000_inf_pT_yy_bin10"    : "(abs(rapidity_higgs[0])<4.0 && pT_higgs[0]>=2000)  && (pT_yy[0] >= 2000.)                        && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # Forward Higgs
            "TTH_FWD_pT_yy_bin1"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 0. && pT_yy[0] < 60.)      && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin2"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 60. && pT_yy[0] < 120.)    && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin3"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 120. && pT_yy[0] < 200.)   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin4"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 200. && pT_yy[0] < 300.)   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin5"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 300. && pT_yy[0] < 450.)   && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin6"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 450. && pT_yy[0] < 600.  ) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin7"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 600. && pT_yy[0] < 1000. ) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin8"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 1000. && pT_yy[0] < 1500.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin9"    : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 1500. && pT_yy[0] < 2000.) && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            "TTH_FWD_pT_yy_bin10"   : "(abs(rapidity_higgs[0])>=4.0) && (pT_yy[0] >= 2000.)                     && n_photons > 1 && pT_y1 > 25. && pT_y2 > 25. && rel_pT_y1 > 0.35 && rel_pT_y2 > 0.25 & m_yy[0] >= 110. && m_yy[0] <= 140. && n_bjets > 1 && (n_electrons > 0 || n_muons > 0)",
            # add more cuts here: note you need to && them, they are not sequential!

           # ttZ->ee cutflow
#            "nocuts"                :  "(n_electrons >=0)",
##            "electrons"             : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0",
##            "electrons_charge"      : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0 && (charge_e1*charge_e2 < 0)",
##            "electrons_mee_window"  : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0 && (abs(m_ee[0] - 91.1876) <= 10.) && (charge_e1*charge_e2 < 0)",
##            "preselection"          : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0 && (abs(m_ee[0] - 91.1876) <= 10.) && (charge_e1*charge_e2 < 0) && n_bjets >= 2",
##            "trilep_channel"        : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0 && (abs(m_ee[0] - 91.1876) <= 10.) && (charge_e1*charge_e2 < 0) && n_bjets >= 2 && n_leptons == 3 && n_jets >= 4",
##            "tetralep_channel"      : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0 && (abs(m_ee[0] - 91.1876) <= 10.) && (charge_e1*charge_e2 < 0) && n_bjets >= 2 && n_leptons == 4 && (charge_e1+charge_e2+charge_l3+charge_l4 == 0)",
##            "lep_channel"           : "n_electrons >=2 && pT_e1 > 27. && pT_e2 > 15. && abs(eta_e1) < 6.0 && abs(eta_e2) < 6.0 && (abs(m_ee[0] - 91.1876) <= 10.) && (charge_e1*charge_e2 < 0) && n_bjets >= 2 && ((n_leptons == 3 && n_jets >= 4) || (n_leptons == 4 && (charge_e1+charge_e2+charge_l3+charge_l4 == 0)))",
            }

# Dictionary for the output variable/histograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    # object multiplicity
    "n_photons":{"name":"n_photons","title":"Number of photons","bin":15,"xmin":-0.5,"xmax":14.5},
    "n_bjets":{"name":"n_bjets","title":"Number of b-jets","bin":10,"xmin":-0.5,"xmax":9.5},
    #"n_jets":{"name":"n_jets","title":"Number of jets","bin":20,"xmin":-0.5,"xmax":19.5},
    #"n_light_jets":{"name":"n_light_jets","title":"Number of light jets","bin":20,"xmin":-0.5,"xmax":19.5},
    "n_electrons":{"name":"n_electrons","title":"Number of electrons","bin":10,"xmin":-0.5,"xmax":9.5},
    "n_muons":{"name":"n_muons","title":"Number of muons","bin":10,"xmin":-0.5,"xmax":9.5},
  #  "n_leptons":{"name":"n_leptons","title":"Number of leptons","bin":10,"xmin":-0.5,"xmax":9.5},
    #"n_higgs":{"name":"n_higgs","title":"Number of Higgs bosons","bin":5,"xmin":-0.5,"xmax":4.5},
    # final discriminant
    "m_yy":{"name":"m_yy","title":"m_{#gamma#gamma} [GeV]","bin":55,"xmin":110.,"xmax":140., "latex":"$m_{\gamma\gamma}$ [GeV]"},
    # add more variables here
#    # photon variables
#    "E_y1"  :{"name":"E_y1","title":"Leading photon energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
    "pT_y1" :{"name":"pT_y1","title":"Leading photon p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400.,"latex":"Leading photon $p_{T}$ [GeV]"},
#    "eta_y1":{"name":"eta_y1","title":"Leading photon #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Leading photon $\eta$"},
#    "phi_y1":{"name":"phi_y1","title":"Leading photon #phi",  "bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Leading photon $\phi$"},
#    "rel_pT_y1":{"name":"rel_pT_y1","title":"Leading photon p_{T} / m_{#gamma#gamma}","bin":50,"xmin":0.,"xmax":3.,"latex":"Leading photon $p_{T}/m_{\gamma\gamma}$"},
#    #"iso_y1":{"name":"iso_y1","title":"Leading photon iso variable","bin":50,"xmin":0.,"xmax":0.5,"latex":"Leading photon iso variable"},
#    "E_y2"  :{"name":"E_y2","title":"Subleading photon energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
    "pT_y2" :{"name":"pT_y2","title":"Subleading photon p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400.,"latex":"Subleading photon $p_{T}$ [GeV]"},
#    "eta_y2":{"name":"eta_y2","title":"Subleading photon #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Subleading photon $\eta$"},
#    "phi_y2":{"name":"phi_y2","title":"Subleading photon #phi","bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Subleading photon $\phi$"},
#    "rel_pT_y2":{"name":"rel_pT_y2","title":"Subleading photon p_{T} / m_{#gamma#gamma}","bin":50,"xmin":0.,"xmax":3.,"latex":"Subleading photon $p_{T}/m_{\gamma\gamma}$"},
    #"iso_y2":{"name":"iso_y2","title":"Subleading photon iso variable","bin":50,"xmin":0.,"xmax":0.5,"latex":"Subleading photon iso variable"},
    "pT_yy" :{"name":"pT_yy","title":"p_{T}^{#gamma#gamma} [GeV]","bin":60,"xmin":0.,"xmax":600.,"latex":"$p_{T}^{\gamma\gamma}$ [GeV]"},
    # Truth photons from Higgs
    ## "HtoYY_n_truth_photons" : {"name":"HtoYY_n_truth_photons","title":"Number of truth photons from Higgs","bin":3,"xmin":-0.5,"xmax":2.5},
    ## "HtoYY_truth_m_yy" :{"name":"HtoYY_truth_m_yy","title":"Truth m_{#gamma#gamma} from Higgs [GeV]","bin":50,"xmin":105.,"xmax":160., "latex":"Truth $m_{\gamma\gamma}$ [GeV]"},
    ## "HtoYY_truth_E_y1" :{"name":"HtoYY_truth_E_y1","title":"Leading truth photon from Higgs energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
    ## "HtoYY_truth_pT_y1":{"name":"HtoYY_truth_pT_y1","title":"Leading truth photon from Higgs p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400.,"latex":"Leading truth photon from Higgs $p_{T}$ [GeV]"},
    ## "HtoYY_truth_eta_y1":{"name":"HtoYY_truth_eta_y1","title":"Leading truth photon from Higgs #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Leading truth photon from Higgs $\eta$"},
    ## "HtoYY_truth_phi_y1":{"name":"HtoYY_truth_phi_y1","title":"Leading truth photon from Higgs #phi",  "bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Leading truth photon from Higgs $\phi$"},
    ## "HtoYY_truth_E_y2" :{"name":"HtoYY_truth_E_y2","title":"Subleading truth photon from Higgs energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
    ## "HtoYY_truth_pT_y2":{"name":"HtoYY_truth_pT_y2","title":"Subleading truth photon from Higgs p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400.,"latex":"Subleading truth photon from Higgs $p_{T}$ [GeV]"},
    ## "HtoYY_truth_eta_y2":{"name":"HtoYY_truth_eta_y2","title":"Subleading truth photon from Higgs #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Subleading truth photon from Higgs $\eta$"},
    ## "HtoYY_truth_phi_y2":{"name":"HtoYY_truth_phi_y2","title":"Subleading truth photon from Higgs #phi","bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Subleading truth photon from Higgs $\phi$"},
##    # b-jet variables
##    "E_b1"  :{"name":"E_b1","title":"Leading b-jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_b1" :{"name":"pT_b1","title":"Leading b-jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Leading b-jet $p_{T}$ [GeV]"},
##    "eta_b1":{"name":"eta_b1","title":"Leading b-jet #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Leading b-jet $\eta$"},
##    "phi_b1":{"name":"phi_b1","title":"Leading b-jet #phi",  "bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Leading b-jet $\phi$"},
##    "btag_score_b1":{"name":"btag_score_b1","title":"Leading b-jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "E_b2"  :{"name":"E_b2","title":"Subleading b-jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_b2" :{"name":"pT_b2","title":"Subleading b-jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Subleading b-jet $p_{T}$ [GeV]"},
##    "eta_b2":{"name":"eta_b2","title":"Subleading b-jet #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Subleading b-jet $\eta$"},
##    "phi_b2":{"name":"phi_b2","title":"Subleading b-jet #phi","bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Subleading b-jet $\phi$"},
##    "btag_score_b2":{"name":"btag_score_b2","title":"Subleading b-jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "m_bb" :{"name":"m_bb","title":"m_{bb} [GeV]","bin":40,"xmin":0.,"xmax":800., "latex":"$m_{bb}$ [GeV]"},
##    "pT_bb" :{"name":"pT_bb","title":"p_{T}^{bb} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$p_{T}^{bb}$ [GeV]"},
##    # jet variables
##    "E_j1"  :{"name":"E_j1","title":"Leading jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_j1" :{"name":"pT_j1","title":"Leading jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Leading jet $p_{T}$ [GeV]"},
##    "eta_j1":{"name":"eta_j1","title":"Leading jet #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Leading jet $\eta$"},
##    "phi_j1":{"name":"phi_j1","title":"Leading jet #phi",  "bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Leading jet $\phi$"},
##    "btag_score_j1":{"name":"btag_score_j1","title":"Leading jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "E_j2"  :{"name":"E_j2","title":"Subleading jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_j2" :{"name":"pT_j2","title":"Subleading jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Subleading jet $p_{T}$ [GeV]"},
##    "eta_j2":{"name":"eta_j2","title":"Subleading jet #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Subleading jet $\eta$"},
##    "phi_j2":{"name":"phi_j2","title":"Subleading jet #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Subleading jet $\phi$"},
##    "btag_score_j2":{"name":"btag_score_j2","title":"Subleading jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "E_j3"  :{"name":"E_j3","title":"Third jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_j3" :{"name":"pT_j3","title":"Third jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Third jet $p_{T}$ [GeV]"},
##    "eta_j3":{"name":"eta_j3","title":"Third jet #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Third jet $\eta$"},
##    "phi_j3":{"name":"phi_j3","title":"Third jet #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Third jet $\phi$"},
##    "btag_score_j3":{"name":"btag_score_j3","title":"Third jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "E_j4"  :{"name":"E_j4","title":"Fourth jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_j4" :{"name":"pT_j4","title":"Fourth jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Fourth jet $p_{T}$ [GeV]"},
##    "eta_j4":{"name":"eta_j4","title":"Fourth jet #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Fourth jet $\eta$"},
##    "phi_j4":{"name":"phi_j4","title":"Fourth jet #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Fourth jet $\phi$"},
##    "btag_score_j4":{"name":"btag_score_j4","title":"Fourth jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "E_j5"  :{"name":"E_j5","title":"Fifth jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_j5" :{"name":"pT_j5","title":"Fifth jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Fifth jet $p_{T}$ [GeV]"},
##    "eta_j5":{"name":"eta_j5","title":"Fifth jet #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Fifth jet $\eta$"},
##    "phi_j5":{"name":"phi_j5","title":"Fifth jet #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Fifth jet $\phi$"},
##    "btag_score_j5":{"name":"btag_score_j5","title":"Fifth jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    "E_j6"  :{"name":"E_j6","title":"Sixth jet energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "pT_j6" :{"name":"pT_j6","title":"Sixth jet p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Sixth jet $p_{T}$ [GeV]"},
##    "eta_j6":{"name":"eta_j6","title":"Sixth jet #eta","bin":50,"xmin":-6.0,"xmax":6.0, "latex":"Sixth jet $\eta$"},
##    "phi_j6":{"name":"phi_j6","title":"Sixth jet #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Sixth jet $\phi$"},
##    "btag_score_j6":{"name":"btag_score_j6","title":"Sixth jet b-tagging score","bin":4,"xmin":-0.5,"xmax":3.5},
##    # high-level jet variables
##    "HT" :{"name":"HT","title":"H_{T} [GeV]","bin":60,"xmin":0.,"xmax":1200., "latex":"$H_{T}$ [GeV]"},
##    "topness" :{"name":"topness","title":"Topness","bin":30,"xmin":0.,"xmax":3.},
##    "MET" :{"name":"MET","title":"E_{T}^{miss} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$E_{T}^{miss}$ [GeV]"},
##    "MET_phi" :{"name":"MET_phi","title":"#phi(E_{T}^{miss})","bin":100,"xmin":-3.6,"xmax":3.6,"latex":"$\phi(E_{T}^{miss})$"},
##    # lepton variables
##    "E_e1"  :{"name":"E_e1","title":"Leading electron energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_e1" :{"name":"pT_e1","title":"Leading electron p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200.,"latex":"Leading electron $p_{T}$ [GeV]"},
##    "eta_e1":{"name":"eta_e1","title":"Leading electron #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Leading electron $\eta$"},
##    "phi_e1":{"name":"phi_e1","title":"Leading electron #phi",  "bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Leading electron $\phi$"},
##    "charge_e1":{"name":"charge_e1","title":"Leading electron charge",  "bin":3,"xmin":-1.5,"xmax":1.5,"latex":"Leading electron charge"},
##    "E_e2"  :{"name":"E_e2","title":"Subleading electron energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_e2" :{"name":"pT_e2","title":"Subleading electron p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Subleading electron $p_{T}$ [GeV]"},
##    "eta_e2":{"name":"eta_e2","title":"Subleading electron #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Subleading electron $\eta$"},
##    "phi_e2":{"name":"phi_e2","title":"Subleading electron #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Subleading electron $\phi$"},
##    "charge_e2" :{"name":"charge_e2","title":"Subleading electron charge",  "bin":3,"xmin":-1.5,"xmax":1.5,"latex":"Subleading electron charge"},
##    "m_ee" :{"name":"m_ee","title":"m_{ee} [GeV]","bin":40,"xmin":80.,"xmax":100., "latex":"$m_{ee}$ [GeV]"},
##    "pT_ee" :{"name":"pT_ee","title":"p_{T}^{ee} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$p_{T}^{ee}$ [GeV]"},
##    "DR_e_e" :{"name":"DR_e_e","title":"#Delta R(e,e)","bin":50,"xmin":0.,"xmax":5.,"latex":"$\Delta R(e,e)$"},
##    "E_mu1"  :{"name":"E_mu1","title":"Leading muon energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_mu1" :{"name":"pT_mu1","title":"Leading muon p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Leading muon $p_{T}$ [GeV]"},
##    "eta_mu1":{"name":"eta_mu1","title":"Leading muon #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Leading muon $\eta$"},
##    "phi_mu1":{"name":"phi_mu1","title":"Leading muon #phi",  "bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Leading muon $\phi$"},
##    "E_mu2"  :{"name":"E_mu2","title":"Subleading muon energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_mu2" :{"name":"pT_mu2","title":"Subleading muon p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Subleading muon $p_{T}$ [GeV]"},
##    "eta_mu2":{"name":"eta_mu2","title":"Subleading muon #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Subleading muon $\eta$"},
##    "phi_mu2":{"name":"phi_mu2","title":"Subleading muon #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Subleading muon $\phi$"},
##    "E_l1"  :{"name":"E_l1","title":"Leading lepton energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_l1" :{"name":"pT_l1","title":"Leading lepton p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Leading lepton $p_{T}$ [GeV]"},
##    "eta_l1":{"name":"eta_l1","title":"Leading lepton #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Leading lepton $\eta$"},
##    "phi_l1":{"name":"phi_l1","title":"Leading lepton #phi",  "bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Leading lepton $\phi$"},
##    "charge_l1":{"name":"charge_l1","title":"Leading lepton charge",  "bin":3,"xmin":-1.5,"xmax":1.5,"latex":"Leading lepton charge"},
##    "pdgID_l1":{"name":"pdgID_l1","title":"Leading lepton PDG ID","bin":27,"xmin":-13.5,"xmax":13.5,"latex":"Leading lepton PDG ID"},
##    "E_l2"  :{"name":"E_l2","title":"Subleading lepton energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_l2" :{"name":"pT_l2","title":"Subleading lepton p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Subleading lepton $p_{T}$ [GeV]"},
##    "eta_l2":{"name":"eta_l2","title":"Subleading lepton #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Subleading lepton $\eta$"},
##    "phi_l2":{"name":"phi_l2","title":"Subleading lepton #phi","bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Subleading lepton $\phi$"},
##    "charge_l2":{"name":"charge_l2","title":"Subleading lepton charge",  "bin":3,"xmin":-1.5,"xmax":1.5,"latex":"Subleading lepton charge"},
##    "pdgID_l2":{"name":"pdgID_l2","title":"Subleading lepton PDG ID","bin":27,"xmin":-13.5,"xmax":13.5,"latex":"Subleading lepton PDG ID"},
##    "E_l3"  :{"name":"E_l3","title":"Third lepton energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_l3" :{"name":"pT_l3","title":"Third lepton p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Third lepton $p_{T}$ [GeV]"},
##    "eta_l3":{"name":"eta_l3","title":"Third lepton #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Third lepton $\eta$"},
##    "phi_l3":{"name":"phi_l3","title":"Third lepton #phi",  "bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Third lepton $\phi$"},
##    "charge_l3":{"name":"charge_l3","title":"Third lepton charge",  "bin":3,"xmin":-1.5,"xmax":1.5,"latex":"Third lepton charge"},
##    "pdgID_l3":{"name":"pdgID_l3","title":"Third lepton PDG ID","bin":27,"xmin":-13.5,"xmax":13.5,"latex":"Third lepton PDG ID"},
##    "E_l4"  :{"name":"E_l4","title":"Fourth lepton energy [GeV]","bin":40,"xmin":0.,"xmax":400.},
##    "pT_l4" :{"name":"pT_l4","title":"Fourth lepton p_{T} [GeV]","bin":40,"xmin":0.,"xmax":200., "latex":"Fourth lepton $p_{T}$ [GeV]"},
##    "eta_l4":{"name":"eta_l4","title":"Fourth lepton #eta","bin":60,"xmin":-6.0,"xmax":6.0,"latex":"Fourth lepton $\eta$"},
##    "phi_l4":{"name":"phi_l4","title":"Fourth lepton #phi",  "bin":40,"xmin":-3.6,"xmax":3.6,"latex":"Fourth lepton $\phi$"},
##    "charge_l4":{"name":"charge_l4","title":"Fourth lepton charge",  "bin":3,"xmin":-1.5,"xmax":1.5,"latex":"Fourth lepton charge"},
##    "pdgID_l4":{"name":"pdgID_l4","title":"Fourth lepton PDG ID","bin":27,"xmin":-13.5,"xmax":13.5,"latex":"Fourth lepton PDG ID"},
##    "m_ll_non_Z" :{"name":"m_ll_non_Z","title":"m_{ll}^{non-Z} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$m_{ll}^{non-Z}$ [GeV]"},
##    "pT_ll_non_Z" :{"name":"pT_ll_non_Z","title":"p_{T}^{ll^{non-Z}} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$p_{T}^{ll^{non-Z}}$ [GeV]"},
##    "DR_l_l_non_Z" :{"name":"DR_l_l_non_Z","title":"#Delta R(l,l)^{non-Z}","bin":50,"xmin":0.,"xmax":5.,"latex":"$\Delta R(l,l)^{non-Z}$"},
##    "true_E_y1" : {"name":"true_E_y1","title":"Leading photon true energy [GeV]","bin":50,"xmin":0.,"xmax":500.},
##    "true_E_y2" : {"name":"true_E_y2","title":"Subleading photon true energy [GeV]","bin":50,"xmin":0.,"xmax":500},
##    "true_pT_y1" : {"name":"true_pT_y1","title":"Leading photon true p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Leading lepton $p_T$ [GeV]"},
##    "true_pT_y2" : {"name":"true_pT_y2","title":"Subleading photon true p_{T} [GeV]","bin":40,"xmin":0.,"xmax":400., "latex":"Subleading lepton $p_T$ [GeV]"},
##    "true_eta_y1" : {"name":"true_eta_y1","title":"Leading photon true #eta","bin":40,"xmin":-6.0,"xmax":6.0, "latex":"Leading photon $\eta$"},
##    "true_eta_y2" : {"name":"true_eta_y2","title":"Subleading photon true #eta","bin":40,"xmin":-6.0,"xmax":6.0, "latex":"Subleading photon $\eta$"},
##    "true_phi_y1" : {"name":"true_phi_y1","title":"Leading photon true #phi","bin":50,"xmin":-3.6,"xmax":3.6, "latex":"Leading photon $\phi$"},
##    "true_phi_y2" : {"name":"true_phi_y2","title":"Subleading photon true #phi","bin":50,"xmin":-3.6,"xmax":3.6, "latex":"Subleading photon $\phi$"},
##    "true_m_yy" : {"name":"true_m_yy","title":"True m_{#gamma#gamma} [GeV]","bin":60,"xmin":0.,"xmax":600., "latex":"True $m_{\gamma\gamma}$ [GeV]"},
##    "pT_top_had_jet2" : {"name":"pT_top_had_jet2","title":"Leading light jet p_{T} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"Leading light jet $p_T$ [GeV]"},
##    "E_top_had_jet2" : {"name":"E_top_had_jet2","title":"Leading light jet energy [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"Leading light jet $E$ [GeV]"},
##    "eta_top_had_jet2" : {"name":"eta_top_had_jet2","title":"Leading light jet #eta","bin":50,"xmin":-6.0,"xmax":6.0, "latex":"Leading light jet $\eta$"},
##    "phi_top_had_jet2" : {"name":"phi_top_had_jet2","title":"Leading light jet #phi","bin":50,"xmin":-3.6,"xmax":3.6, "latex":"Leading light jet $\phi$"},
##    "pT_top_had_jet3" : {"name":"pT_top_had_jet3","title":"Subleading light jet p_{T} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"Subleading light jet $p_T$ [GeV]"},
##    "E_top_had_jet3" : {"name":"E_top_had_jet3","title":"Subleading light jet energy [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"Subleading light jet $E$ [GeV]"},
##    "eta_top_had_jet3" : {"name":"eta_top_had_jet3","title":"Subleading light jet #eta","bin":50,"xmin":-6.0,"xmax":6.0, "latex":"Subleading light jet $\eta$"},
##    "phi_top_had_jet3" : {"name":"phi_top_had_jet3","title":"Subleading light jet #phi","bin":50,"xmin":-3.6,"xmax":3.6, "latex":"Subleading light jet $\phi$"},
##    "m_w_had" : {"name":"m_w_had","title":"m_{W}^{had} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$m_{W}^{had}$ [GeV]"},
##    "pT_w_had" : {"name":"pT_w_had","title":"p_{T}^{W^{had}} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$p_{T}^{W^{had}}$ [GeV]"},
##    "E_w_had" : {"name":"E_w_had","title":"E_{W}^{had} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":"$E_{W}^{had}$ [GeV]"},
##    "eta_w_had" : {"name":"eta_w_had","title":"#eta(W^{had})","bin":50,"xmin":-6.0,"xmax":6.0, "latex":"$\eta(W^{had})$"},
##    "phi_w_had" : {"name":"phi_w_had","title":"#phi(W^{had})","bin":50,"xmin":-3.6,"xmax":3.6, "latex":"$\phi(W^{had})$"},
##    "m_b1l" : {"name":"m_b1l","title":"m_{b_1 #ell} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":r"$m_{b_1\ell}$ [GeV]"},
##    "m_b2l" : {"name":"m_b2l","title":"m_{b_2 #ell} [GeV]","bin":50,"xmin":0.,"xmax":500., "latex":r"$m_{b_2\ell}$ [GeV]"},
##    #'E_higgs' : {"name":"E_higgs","title":"Higgs energy [GeV]","bin":50,"xmin":0.,"xmax":5000.},
##    #'pT_higgs' : {"name":"pT_higgs","title":"Higgs p_{T} [GeV]","bin":40,"xmin":0.,"xmax":1000., "latex":"Higgs $p_{T}$ [GeV]"},
##    #'eta_higgs' : {"name":"eta_higgs","title":"Higgs #eta","bin":40,"xmin":-6.0,"xmax":6.0,"latex":"Higgs $\eta$"},
##    #'phi_higgs' : {"name":"phi_higgs","title":"Higgs #phi","bin":50,"xmin":-3.6,"xmax":3.6,"latex":"Higgs $\phi$"},
##    #'rapidity_higgs' : {"name":"phi_higgs","title":"Higgs rapidity","bin":50,"xmin":-10,"xmax":10,"latex":"Higgs rapidity"},
##    # add more variables here
}